person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}


print(person)
#prints person dictionary (everything in the dictionary)

print(type(person['children']))
#returns us a LIST, use type function to tell us what class

print(person['children'][1])
#takes value that is in index location 1

print(person['pets']['cat'])
#pets is the key value, index value is cat, thus returning the name who has a cat

for i in person['pets']:
#whereas i represents the key in the list (1,2,3) - (Ralph, Betty, Joey)
    #print(i) - prints the order in the dictionary
    print(person['pets'][i])
    #prints name with each key
