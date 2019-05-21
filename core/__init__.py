from os import listdir
from os.path import isfile, join

#Vars
controllers = {}

#Methods
def load_config():
    config_file = open("config.txt")
    config_settings = config_file.read()
    config_file.close()
    config_settings = config_settings.split("\n")
    config_settings_array = {}
    for x in range(0,len(config_settings)):
        config_settings_array[config_settings[x].split("=")[0]] = config_settings[x].split("=")[1]
    return config_settings_array

def register_controllers():
    print("Registering Controllers...")
    controllerFiles = [f for f in listdir("app/Controllers/") if isfile(join("app/Controllers/", f))]
    for x in range(0, len(controllerFiles)):
        global controllers
        if "Controller.py" in controllerFiles[x]:
            controllers[controllerFiles[x].replace("Controller.py","").lower()] = {}
            controller_file = open("app/Controllers/"+controllerFiles[x])
            controller_file_content = controller_file.read()
            controller_file.close()
            print(" -", controllerFiles[x].replace("Controller.py",""))
            register_views(controllerFiles[x].replace("Controller.py",""), controller_file_content)

def register_views(controller_name, content):
    content = content.split("\n")
    for x in range(0, len(content)):
        if content[x][:3] == "def":
            method_name = content[x].replace("def ","")
            method_action_name = method_name.split("(")[0]
            method_params = list(filter(None,find_between(method_name,"(",")").replace(" ","").split(",")))
            print("     -", method_action_name)
            global controllers
            controllers[controller_name.lower()][method_action_name.lower()] = []
            for y in range(0, len(method_params)):
                controllers[controller_name.lower()][method_action_name.lower()].append(method_params[y].lower())
                print("         >", method_params[y])
        


#Helpers

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
