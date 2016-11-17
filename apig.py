import sys, os, re, json

def existsFile(file):
    return True #TODO

def get_dict_from_json_file(file):
    json_data = open(file).read()
    return json.loads(json_data)

def get_methods(methods):
    return "GET POST"

def get_string_from_list(list):
    result = ""
    for item in list:
        result += item
    return result

def create_resource_from_specification(resource):
    result = list()
    
    methods_statement = get_methods(resource['methods'])

    initial_resource_statement = "<resource methods=\"" + methods_statement + "\" uri-template=\"" + resource['urlPath'] + "\">"
    result.append(initial_resource_statement)

    resource_content = ""
    if "conf" in resource['endpoint']:
        resource_content = "<inSequence><send><endpoint key=\"" + resource['endpoint'] + "\" /></send></inSequence><outSequence><send /><outSequence><faultSequence/>"
    else:
        resource_content = "<inSequence><send><endpoint uri=\"" + resource['endpoint'] + "\" /></send></inSequence><outSequence><send /><outSequence><faultSequence/>"
    result.append(resource_content)

    result.append("</resource>")

    result_string = get_string_from_list(result)

    return result_string

def create_api_from_specification(api_specification):
    result = list()

    initial_api_statement = "<api name=\"" + api_specification['apiName'] + "\" context=\"" + api_specification['apiContext'] + "\">"
    result.append(initial_api_statement)

    for resource in api_specification['resources']:
        #print(resource) #TODO: Remove this
        resource_result = create_resource_from_specification(resource)
        result.append(resource_result)
        print(resource_result)
    
    result.append("</api>")

    return result

def generate_result_file(api_result):
    print("File has been created!") #TODO
    api_string = get_string_from_list(api_result)
    text_file = open("output.xml", "w")
    text_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
    text_file.write(api_string)
    text_file.close()

if __name__ == '__main__':
    if len(sys.argv)>1:
        file = sys.argv[1]
        if existsFile(file):
            print("Correct File!") #TODO: remove this statements when existsFile method is completed.
            api_specification = get_dict_from_json_file(file)
            api_result = create_api_from_specification(api_specification)
            generate_result_file(api_result)
        else:
            print("File argument is not valid!")











