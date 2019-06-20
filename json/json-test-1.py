import json

 

# A dictionary of roll numbers vs student names

studentDict = {1:"John Napier",

               2:"Leonhard Euler",

               3:"Scarlett O'Hara",

               4:"Henry Ford"}

 

jsonString  = json.dumps(studentDict)

 

# A python dictionary as a JSON string

print(jsonString)

 

# A list as JSON

repDigits = [11,22,33,44]

jsonString  = json.dumps(repDigits)

 

# A python list as a JSON string

print(jsonString)

 

# Print None as JSON

reference1 = None

jsonString  = json.dumps(reference1)

print(jsonString)

 

# Print True as JSON

alive = True

jsonString  = json.dumps(alive)

print(jsonString)