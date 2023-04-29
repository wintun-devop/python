import json


my_list = [5,2]
my_list_lenght = len(my_list)


# print(my_list_lenght)
entry_status = "No Data in List" if my_list_lenght==0 else "Data in List"
# multiple ternary
entry_status_detail = "No Data in List" if my_list_lenght==0 else ("Only one in List" if my_list_lenght==1 else "More than one in List")
print(entry_status_detail)