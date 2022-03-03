#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos
#declare a string
a_name="Win Tun Hlaing"
about="He is am IT Professional."

#change all to title case
a_name_capital=a_name.title()
#change all to lower case
a_name_lower=a_name.lower()
#change all to upper case
a_name_upper=a_name.upper()
#rjust a string
a_name_rjust=a_name.rjust(20,'.')
#replace a string
a_name_replace_character=a_name.replace("Hlaing","Lin")
#split a string which going to be a list
a_name_split=a_name.split()
#revert a string
a_name_reverse=reversed(a_name)
#partition a string which going to be a tuple
a_name_partition=a_name.partition(' ')
#count a group of string
x = a_name.count("n")
#format string
a_format_string="My name is {name}.{About}".format(name=a_name,About=about)
#f string
an_fstring=f"My name is {a_name}.{about}"
print(an_fstring)
