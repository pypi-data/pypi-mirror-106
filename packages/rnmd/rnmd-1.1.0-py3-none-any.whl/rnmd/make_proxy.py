import os
import rnmd.util.extract_document_content as doc_tools
from string import Template
from rnmd.config.mode_printer import print_if

mode_options = None
current_script_dir = os.path.dirname(__file__)
template_file_path = os.path.join(current_script_dir,"templates/proxy-template-py.txt")

with open(template_file_path, "r") as template_file:
    template_string = template_file.read()

#TODO replace by platform independent python script instead
proxy_template = Template(template_string)

def make_proxy(source_path, target_path, backup_path = None, relative = False, update_backup = False, local_instance = False):

    runtime_path = "rnmd"

    if(local_instance is not None and local_instance):
        print("Localinstance")
        runtime_path = "python3 " + os.path.abspath(os.path.join(current_script_dir, "rnmd.py"))

    #Make it possible to create proxies for plain bash scripts
    path_parts = os.path.splitext(os.path.basename(source_path))
    if(path_parts is not None and len(path_parts) > 0):
        if(path_parts[1] == ".sh"):
            runtime_path = "bash"
        elif(path_parts[1] == ".py"):
            runtime_path = "python3"
        elif(path_parts[1] == ".js"):
            runtime_path = "node"
        elif(path_parts[1] == ".ts"):
            runtime_path = "ts-node"


    markdown_doc_path = doc_tools.get_abs_document_location(source_path)
    backup_doc_path = doc_tools.get_abs_document_location(backup_path)

    if(relative):
        #Relative path from proxy file to markdown doc
        markdown_doc_path = doc_tools.get_rel_document_location(markdown_doc_path,target_path)
        backup_doc_path = doc_tools.get_rel_document_location(backup_path,target_path)

    substitution_dict = { 
        'runtime_path': runtime_path, 
        'markdown_doc_path': markdown_doc_path,
        'backup_path': backup_doc_path,
        'update_backup': update_backup,
        'is_rel_path': relative
    }
    proxy_string = proxy_template.substitute(**substitution_dict)

    with open(target_path, "w+") as out_file:
        out_file.write(proxy_string)

    os.system("chmod +x " + target_path)

    print_if("Created proxy at: " + target_path, mode_options)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Compile markdown bash documentation to executable program scripts"
    )

    parser.add_argument('source', help="Path of the documentation file")
    parser.add_argument('target', help="Output path for the resulting executable file")

    # Parse the arguments
    arguments = parser.parse_args()

    source = arguments.source
    target = arguments.target

    make_proxy(source,target)