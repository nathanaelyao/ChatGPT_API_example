# Documentation for `example.py`

### example
Here are the docstrings for the given module and function:

```python
"""
Module: create_l3vpn_workflow

This module contains the implementation of the CreateL3VPNWorkflow class which is a subclass
of the AbstractWorkflow class. This class implements the workflow for creating a Layer 3 VPN.

This module also imports the following classes and modules: json, RequestCallbackInfo, L3vpnPayload,
Northbound, AbstractAsyncAction, BaseVPNAction, AbstractWorkflow, Events, RequestInfo, ServiceInfo,
RequestType, and logger.

To use this module, import the CreateL3VPNWorkflow class as follows:

    from create_l3vpn_workflow import CreateL3VPNWorkflow

Example usage of the module:

    workflow = CreateL3VPNWorkflow()

"""

"""
Class: CreateL3VPNWorkflow

This class implements the workflow for creating a Layer 3 VPN. The workflow consists of the
following actions: Start, CreateL3VPN, and RevertStart.

These actions are implemented as inner classes of the CreateL3VPNWorkflow class.

Class Methods:
    - __init__(self, *args, **kwargs): Initializes a new instance of the CreateL3VPNWorkflow class.

Attributes:
    - start: an instance of the Start inner class.
    - create_evpn: an instance of the CreateL3VPN inner class.
    - timeout_start: an instance of the RevertStart inner class.

Inner Classes:
    - Start: an abstract class that represents the starting point of the workflow. This class implements
            the on_start, on_success, and on_failure methods.
    - RevertStart: an abstract class that reverts the state of the workflow to the previous state when an
                    error occurs. This class implements the on_start method.
    - CreateL3VPN: an abstract class that represents the main action of the workflow. This class implements
                    the on_start, on_success, and on_failure methods.
"""
```



```python
"""
Module: create_l3vpn_workflow

This module contains the implementation of the CreateL3VPNWorkflow class which is a subclass
of the AbstractWorkflow class. This class implements the workflow for creating a Layer 3 VPN.

This module also imports the following classes and modules: json, RequestCallbackInfo, L3vpnPayload,
Northbound, AbstractAsyncAction, BaseVPNAction, AbstractWorkflow, Events, RequestInfo, ServiceInfo,
RequestType, and logger.

To use this module, import the CreateL3VPNWorkflow class as follows:

    from create_l3vpn_workflow import CreateL3VPNWorkflow

Example usage of the module:

    workflow = CreateL3VPNWorkflow()

"""

"""
Class: CreateL3VPNWorkflow

This class implements the workflow for creating a Layer 3 VPN. The workflow consists of the
following actions: Start, CreateL3VPN, and RevertStart.

These actions are implemented as inner classes of the CreateL3VPNWorkflow class.

Class Methods:
    - __init__(self, *args, **kwargs): Initializes a new instance of the CreateL3VPNWorkflow class.

Attributes:
    - start: an instance of the Start inner class.
    - create_evpn: an instance of the CreateL3VPN inner class.
    - timeout_start: an instance of the RevertStart inner class.

Inner Classes:
    - Start: an abstract class that represents the starting point of the workflow. This class implements
            the on_start, on_success, and on_failure methods.
    - RevertStart: an abstract class that reverts the state of the workflow to the previous state when an
                    error occurs. This class implements the on_start method.
    - CreateL3VPN: an abstract class that represents the main action of the workflow. This class implements
                    the on_start, on_success, and on_failure methods.
"""

"""
Class: CreateL3VPNWorkflow.Start

This is an inner abstract class of the CreateL3VPNWorkflow class that represents the starting point
of the workflow. This class implements the on_start, on_success, and on_failure methods.

Class Methods:
    - on_start(self, nb_request_payload, audit=False): This method is called when the workflow is started.
                It accepts the following parameters:
                    - nb_request_payload: the Northbound payload
                    - audit: a boolean value that determines if the workflow is being audited

    - on_success(self, callback_info: RequestCallbackInfo): This method is called when the workflow
                completes successfully. It accepts the following parameter:
                    - callback_info: the RequestCallbackInfo object containing information about
                                    the completed request

    - on_failure(self, callback_info: RequestCallbackInfo): This method is called when the workflow
                fails to complete successfully. It accepts the following parameter:
                    - callback_info: the RequestCallbackInfo object containing information about
                                    the failed request
"""

"""
Class: CreateL3VPNWorkflow.CreateL3VPN

This is an inner abstract class of the CreateL3VPNWorkflow class that represents the main action of
the workflow. This class implements the on_start, on_success, and on_failure methods.

Class Methods:
    - on_start(self, payload): This method is called when the workflow is started. It accepts the
                following parameters:
                    - payload: the payload sent to the workflow

    - on_success(self, callback_info: RequestCallbackInfo): This method is called when the workflow
                completes successfully. It accepts the following parameter:
                    - callback_info: the RequestCallbackInfo object containing information about
                                    the completed request

    - on_failure(self, callback_info: RequestCallbackInfo): This method is called when the workflow
                fails to complete successfully. It accepts the following parameter:
                    - callback_info: the RequestCallbackInfo object containing information about
                                    the failed request
"""

"""
Class: CreateL3VPNWorkflow.RevertStart

This is an inner abstract class of the CreateL3VPNWorkflow class that reverts the state of the workflow
to the previous state when an error occurs. This class implements the on_start method.

Class Methods:
    - on_start(self, payload): This method is called when the workflow is started. It accepts the
                following parameters:
                    - payload: the payload sent to the workflow
"""
```


