import sys, os, re, json

def existsFile(file):
    return True #TODO

def get_dict_from_json_file(file):
    json_data = open(file).read()
    return json.loads(json_data)

def create_api_from_specification(api_specification):
    result = list()

    initial_api_statement = "<api name=\"" + api_specification['apiName'] + "\" context=\"" + api_specification['apiContext'] + "\">"
    result.append(initial_api_statement)

    for resource in api_specification['resources']:
        print(resource)
    
    result.append("</api>")

    return result

def generate_result_file(api_result):
    print("File has been created!") #TODO
    print(api_result)

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