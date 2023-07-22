

def args_test(*args):
    for i in args:
        print(i)

# args_test("a","b","c","d")
    

def kwargs_test(**kwargs):
    for i in kwargs:
        print(i,":",kwargs[i])

# kwargs_test(a="love",b="life",c="girlfriend")

def args_kwrgs_test(*args,**kwrgs):
    print(args)
    print(kwrgs)

#args_kwrgs_test("a","b","c","d",a="love",b="life",c="girlfriend")