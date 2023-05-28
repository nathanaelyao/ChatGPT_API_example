#import json
#from orchestrator.model.db import requests_db
from orchestrator.model.request_callback_info import RequestCallbackInfo
from orchestrator.payload_utils.l3vpn_payload import L3vpnPayload
from orchestrator.payload_utils.northbound import Northbound
from orchestrator.workflows.abstract.abstract_async_action import AbstractAsyncAction, BaseVPNAction
from orchestrator.workflows.abstract.abstract_workflow import AbstractWorkflow
from orchestrator.workflows.abstract.events import Events


from orchestrator.model.request_info import RequestInfo
from orchestrator.model.service_info import ServiceInfo


from utils.common_util import RequestType as R
from utils.homalogger import logger



class CreateL3VPNWorkflow(AbstractWorkflow):  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start = self.Start(self)
        self.create_evpn = self.CreateL3VPN(self)
        self.timeout_start = self.RevertStart(self)

    class RevertStart(AbstractAsyncAction):
        async def on_start(self, payload):
            factory = self.factory
            request_info = RequestInfo(None, payload, R.create_evpn__TIMEOUT.value)
            
            service_info = ServiceInfo.create_from_request_record(payload)
            vpn_id = service_info.id
            site_id = service_info.site_id

            await factory.l3vpn_entity.services.delete_site(vpn_id, site_id, request_info)
            factory.requests_manager.store_external_request(request_info)


    class Start(BaseVPNAction):
        async def on_start(self, nb_request_payload, audit=False):
            factory = self.factory
            request_info = RequestInfo(None, nb_request_payload, R.create_evpn__SITE.value)
            
            try:
                # translate to ntw 
                # translated_payload = L3vpnPayload(nb_request_payload).transform_to_network()

                # validate
                # ntw_payload = factory.network_validator.validate(translated_payload)

                logger.info("Creating ntw site...")
                # Send to evpn controller
                # await factory.l3vpn_entity.services.create_evpn(ntw_payload, request_info, audit=audit)

            except Exception as e:
                request_info.update_from_exception(e)
                factory.northbound.inform(request_info=request_info)
            
            finally:
                factory.requests_manager.store_external_request(request_info)


        async def on_success(self, callback_info: RequestCallbackInfo):
            factory = self.factory
            factory.requests_manager.update_request_record(callback_info.request_tracker_record["id"], request_state="completed")
            
            callback_info.state = Northbound.COMPLETED
            
            service_info = ServiceInfo.create_from_request_record(callback_info.request_tracker_record)
            if "audit" not in callback_info.response:
                factory.services_manager.add_site(service_info) # store service record


            # inform northbound of success
            northbound_info = factory.northbound.create_response_from_callback(callback_info, service_info)
            factory.northbound.inform(northbound_info=northbound_info)
            factory.requests_manager.update_callback_data(callback_info.request_tracker_record["id"], northbound_info)


        async def on_failure(self, callback_info: RequestCallbackInfo):
            await super().on_failure(callback_info)