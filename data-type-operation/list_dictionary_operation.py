import json

product_list = [
    {"id":"1","name":"Tiger Beer","price":20}, 
    {"id":"2","name":"Myanmar Beer","price":25}, 
    {"id":"3","name":"Hanicle Beer","price":22}, 
    {"id":"4","name":"Leo Beer","price":24}, 
    {"id":"5","name":"Chan Beer","price":24}, 
    {"id":"6","name":"ABC Beer","price":27}, 
]
# convert to json
list_to_json = json.dumps(product_list)

#filter for id ==3
def list_filter(id,input_list):
    try:
        filtered_list_id = [
        x for x in input_list if x["id"] == id
        ]
        return filtered_list_id
    except:
        return f"id is missing"


#filter for price == 24
def list_filter_entity(entity,value,input_list):
    try:
        filter_list_price = [
        x for x in input_list if (x[entity] == value)
        ]
        return filter_list_price
    except:
        return f"Entity and value not found!"

#update name on id == '2'
def list_update_entity(entity,value,input_list):
    try:
        update_product_list=[]
        for x in input_list:
            if (x["id"]=="2"):
                x[entity]=value
            update_product_list.append(x)
        return update_product_list
    except:
        return f"Missing input"

# a = list_update_entity("name","Myanmar Beer Bottle",product_list)

# a = list_filter_entity("price",30,product_list)

a = list_filter("2",product_list)
print(a)

