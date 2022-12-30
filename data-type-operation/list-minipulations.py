#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos
number_list=[4,8,4.5,10,16,6.8,8.3,6.9,9,11]
character_list=["a","b","c","d"]
#list methods append
character_list.append("k")
#list methods sort
number_list.sort()
#combine the list
combine_list=number_list+character_list
#list separation from combined list
num_list=[ x for x in combine_list if type(x)==int ]
float_list=[ y for y in combine_list if type(y)==float ]
char_list=[ c for c in combine_list if type(c) == str]
fruits=["apple","mango","avogadro","barry","pineapple","pear"]
#zip two list
zip_a_lip=list(zip(fruits,num_list))
print(zip_a_lip)

#filter function
def filter_a_list(i):
    a_list = ["apple","mango","avogadro","barry","pineapple","pear",4,8,4.5,10,16,6.8,8.3,6.9,9,11]
    filter_result = []
    for result in a_list:
        if result == i:
            filter_result.append(result)
    if filter_result == []:
        return False
    else:
        print(filter_result)
        return True



