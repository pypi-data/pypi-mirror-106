import sys
import os
import re

allow_commands = ['generate', 'g']
allow_types = ['model']
command = ''
type = ''
project_name = ''
if sys.argv[1]:
    command = sys.argv[1]
if sys.argv[2]:
    type = sys.argv[2]
if sys.argv[3]:
    project_name = sys.argv[3]

directory = ""

def create_project(projectName):
    create_folder(projectName)
    create_pipeline_file(projectName, 'preprocessor')
    create_pipeline_file(projectName, 'postprocessor')
    create_pipeline_file(projectName, 'labelizer')

def create_folder(projectName):
    global directory
    directory = projectName + '_pipeline'
    if not os.path.exists(directory):
        os.mkdir(directory)

def create_pipeline_file(projectName, pipelineType):
    with open('cli/' + pipelineType + '_template.py', 'r') as file:
        data = file.read()
        projectNameNoUnderscore = ''.join(elem.capitalize() for elem in projectName.split('_'))
        className = projectNameNoUnderscore + pipelineType.capitalize()
        classNameFotBaseObject = projectNameNoUnderscore + '_' + pipelineType
        data = data.replace('generatedClassName', classNameFotBaseObject)
        data = data.replace('generatedClass',className)
        current_dir = directory + '/' + pipelineType
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)
        new_file = current_dir + "/" + pipelineType + ".py"
        new_init_file = current_dir + "/__init__.py"
        new_init_export = "from " + directory + "." + pipelineType + "." + pipelineType + " import " + className
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()
        create_pipeline_init_file(new_init_file, new_init_export)

def create_pipeline_init_file(init_path, init_export):
    if not os.path.exists(init_path):
        f = open(init_path, "w")
        f.write(init_export)
        f.close()

def init():
    # print('command', command)
    # print('type', type)
    # print('project_name', project_name)
    if command not in allow_commands:
        print('command not allowed')
        return
    if type not in allow_types:
        print('type not allowed')
        return
    create_project(project_name)


init()


# how to use
# cli.py generate model sig_extractor
