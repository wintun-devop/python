import json,requests

def get_global_datetime(timezone):
    URL = "http://worldtimeapi.org/api/timezone/"+timezone
    # sending get request and saving the response as response object
    response = requests.request("GET",URL)
    #response to dictionary format like json
    dictionary_data = response.json()
    #convert python dictionary to json 
    json_data = json.dumps(dictionary_data)
    #convert json to dictionary again
    joson_to_dictionary = json.loads(json_data)
    print(json_data)
    



get_global_datetime("Asia/Tokyo")

