import json

json_list=[]

with open('data.json' , 'r') as fp:
    json_data = json.load(fp)

userData = {}
parsData = []

for data in json_data['users']:
    userData['userId'] = data['userId']
    userData['firstName'] = data['firstName']
    userData['lastName'] = data['lastName']
    userData['phoneNumber'] = data['phoneNumber']
    userData['emailAddress'] = data['emailAddress']
    
    parsData.append(userData)

print(parsData)
        
     