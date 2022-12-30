import json

wintun = {
    "name":"Win Tun Hlaing",
    "age":35,
    "cloudCertified":["AWS SAA","AZ-104"],
    "Address":[
        {"Home":"No.Home,DEF Road"},
        {"Address":"No.Office,DEF Road"}
    ],
    "isMarried":False
}
# single item by key
getSingleItem=wintun.get("name")
# get items from dictionary
getItems=wintun.items()
#get dictionary key
getKeys = wintun.keys()
#get dictionary valuse
getValues = wintun.values()
#copy dictionary
secondDict = wintun.copy()
#Update dictionary
wintun.update({"Belove Liquor":"Wisaki"})
updateDict=wintun
#convert dictionary to Json
jsonDict=json.dumps(updateDict)
print(jsonDict)

