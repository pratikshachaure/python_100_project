# clear method :- Removes all the elements from the dictionay.

car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1979
}

car.clear()
print("clear dictionary :- ",car)


# Returns a copy of the dictionary..


obj={
    "name":"pratiksha",
    "lname":"chaure",
    "age":20
}
copied=obj.copy() 
print("The copied object :- ",copied)



# fromkeys() method returns a dictionary with the specified keys and the specified value..


keys={'a','e','i','o','i'}
value='vowel'
vowels=dict.fromkeys(keys,value)
print("Vowels ",vowels)


# get() Returns the value of the specified key..

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print("Key is :- ",x)


# items():- Returns a list containing a tuple for each key value pair..


obj={

    "first":"second",
    "third":"fourth",
    "fifth":"sixth",
    "seven":"eight"
}

x=obj.items()
print("items in object :- ",x)


# Returns a list containing the dictionary's keys
obj={

    "first":"second",
    "third":"fourth",
    "fifth":"sixth",
    "seven":"eight"
}


find_keys=obj.keys()
print("The keys are :- ",find_keys)


# pop :- Removes the element with the specified key
pop_obj={

    "roll_no":10,
    "name":"Pratikha",
    "lname":"Chaure",
    "age":20
}

pop_obj.pop("lname")
print("Poped array :- ",pop_obj)



# popitem() method removes the last inserted key-value pair..


pop_obj={

    "roll_no":10,
    "name":"Pratikha",
    "lname":"Chaure",
    "age":20
}



pop_obj.popitem()
print("Popitem array :- ",pop_obj)



# setdefault Returns the value of the specified key. If the key does not exist: insert the key, with the specified value


 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("modell", "Bronco")

print(x)


# update():- Update the dictionary with the specified key-value pair.


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"model": "White"}) 
print("Updated car :- ",car)


# values() Returns a list of all the values in the dictionary..


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print("Value in Object :- ",x)