user = {
    "name":"Win Tun",
    "age":35,
    "married":False    
}
# print(user)
name,age,married =user.values() # like javascript destructure const {name,age,marriged} = user
# print(name,age,married)
# print(user)

update_user = {**user,"occupation": "dev-op backend"} #like javascript operator const updateUser = {...user,occupation: "dev-op backend"}
print(update_user)



