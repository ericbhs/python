class MyTest(object):

    def __init__(self, *list):
        print("type of list is", type(list))
        for i in list:
            print(i)
            
o = MyTest("str", 4.56, [1,2,3])

input("Press enter to end the program")