#Create a class which converts dictionary elements into list like keys are one list and values are another

class DictConverter:
    def lists(dict):
        return list(dict.keys()), list(dict.values())

dict1 = eval(input("Enter a dictionary within {}: "))  
keys, values = DictConverter.lists(dict1)

print("List of Keys:", keys)  
print("List of Values:", values)


