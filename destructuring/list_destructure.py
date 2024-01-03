a_student_marks = [72,69,76,92,78,82]
[Myanmar,English,*rest] =a_student_marks #like javascrit const [Myanmar,English,...rest]=a_student_marks
print("Myanmar",Myanmar)
print("English",English)
print("Other",rest)

fruits = ["orange","mango","strawberry","grapes"]
vegetables = ["salad","carrot","onions","carrot"]
fruits_and_vegetables = [*fruits,*vegetables] #like javascipt fruits_and_vegetables = [...fruits,...vegetables]
print(fruits_and_vegetables)