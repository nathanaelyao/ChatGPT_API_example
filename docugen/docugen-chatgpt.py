#!/usr/bin/env python3

import json
import yaml
from yaml import CLoader, CDumper
from revChatGPT.V3 import Chatbot
import os
from sys import argv
import fmtutil
from parse import py
from argparse import ArgumentParser
import openai


argparser = ArgumentParser(
	# prog="docugen",
	description="generate docs with le AI(tm)",
	epilog="https://github.com/turtlebasket/docugen"
)


argparser.add_argument("filename")
argparser.add_argument("-o", dest="output directory",  help="directory to write docs to")
argparser.add_argument("-m", dest="model", help="model to use to generate documentation", choices=["chatgpt"])
argparser.add_argument("-f", dest="format", help="formatting of output documentation", choices=["md"])
args = argparser.parse_args()

file_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{file_path}/config.yaml", "r") as file:
    config = yaml.load(file, Loader=CLoader)

infile = open(args.filename, "r")

openai.api_key = config['OPENAI_API_KEY']
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

functions = py.find_toplevel_funcs(infile)

print(f"Found {len(functions)} functions.")


doc_prompt_head = "Generate commented functions with an explanation on what this function does in one short sentence and the inputs and output of the function. Generate unit tests for the functions:\n"


with open(f"example-doc.md", "w") as outfile:
	outfile.write(f"# Documentation for `{argv[1]}`\n\n")
	for function in functions:
		head_ask = doc_prompt_head + function["content"]
		messages.append(
            {"role": "user", "content": head_ask},
        )
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
		resp = chat.choices[0].message.content
		print(resp)
		print(f'Generated documentation for {function["head"]}.')
		# append results to doc
		output = f"### `{function['head']}`\n" + fmtutil.highlight_multiline_code_md(resp, "python") + "\n\n"
		outfile.write(output)
