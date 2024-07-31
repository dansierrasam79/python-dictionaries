#create a dict from object

class createDict():
    def __init__(self,name,age):
        self.n = name
        self.a = age

    def blah_method():
        print("Nothing")

firstObject = createDict("Dan", 36)
final_dict = firstObject.__dict__
print(final_dict)
