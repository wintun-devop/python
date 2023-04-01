import json

from pydantic import Json

event_list = [
    {
    "id":"1",
    "name":"Event-1",
    "Date":"03-25-2020",
    "memory":{"id":1,"comments":[]},
    "details":[]
    },    
    {
    "id":"2",
    "name":"Event-A",
    "Date":"04-25-2021",
    "details":[]
    },
    {
    "id":"3",
    "name":"Event-B",
    "Date":"05-25-2021",
    "memory":{"id":1,"comments":[]},
    "details":[]
    },
    {
    "id":"4",
    "name":"Event-D",
    "Date":"06-25-2021",
    "details":[]
    },
    {
    "id":"5",
    "name":"Event-E",
    "Date":"07-25-2021",
    "details":[]
    },
    {
    "id":"6",
    "name":"Event-F",
    "Date":"08-25-2021",
    "memory":{"id":1,"comments":[]},
    "details":[{"id":1},{"id":2}]
    },    
]

# convert Janson
list_to_json = json.dumps(event_list)


#get a modified list with a collection of dictionary in specific key
def get_filter_dict(list,filter_key):
    try:
        update_list=[x for x  in list if (filter_key in x)
        ]
        return update_list
    except:
        return f"Input parameter is missing."

a = get_filter_dict(event_list,"ujf")
print(a)






