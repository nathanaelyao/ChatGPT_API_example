import re

def find_toplevel_funcs(lines):
    functions = []
    function_head = ""
    function_content = ""
    function_body_indent_level = 0

    for line in lines:
        curr_indent_level = len(line) - len(line.lstrip())
        function_found = re.search('^def(\s+)(.*)\(.*\)(\s*):(\s*)$', line.strip(), re.MULTILINE)

        if len(function_head.strip()) > 0 and (curr_indent_level <= function_body_indent_level):
            functions.append({
                "head": function_head.strip(),
                "content": function_content
            })
            function_head = ""
            function_content = ""

        if function_found and len(function_head) == 0:
            function_head = re.search("^def(\s+)(.*)\(.*\)(\s*):(\s*)$", line.strip()).group(2).strip()
            function_content = line
            function_body_indent_level = curr_indent_level + 1

        elif not function_found and len(function_head.strip()) > 0 and curr_indent_level >= function_body_indent_level:
            function_content += line

    if len(function_head.strip()) > 0:
        functions.append({
            "head": function_head.strip(),
            "content": function_content
        })

    return functions
