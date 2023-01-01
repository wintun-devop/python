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
    

def get_global_datetimestemps(timezone):
    URL1 = "https://worldtimeapi.org/api/timezone/"+timezone
    #URL2 = "http://worldtimeapi.net/api/timezone/"+timezone
    try:
        response = requests.request("GET",URL1)
        dictionary_data = response.json()
        #json_data = json.dumps(dictionary_data)
        currentDateTime = dictionary_data["datetime"]
        print(currentDateTime)
    except:
        error = {}
        error.update({1:"API call error"})
        print(error[1])



get_global_datetime("Asia/Tokyo")

