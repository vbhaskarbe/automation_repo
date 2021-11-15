import sys
import os
import json

print(sys.prefix)
print("HOME" in os.environ)
print(os.environ.get('MGMT_URL','https://173.36.208.191'))

#for a in os.environ:
#    print('Var: ', a, 'Value: ', os.getenv(a))
#print("all done")

#for param in os.environ.keys():
#    print("%s: %s " % (param, os.environ[param]))

#for item, value in os.environ.items():
#    print('{}: {}'.format(item, value))

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

print(json.dumps(data, sort_keys=True, indent=4))

## Writing JSON data to a file
with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)

## Reading JSON data from a file
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')


try:  
   os.environ["FOO"]
except KeyError: 
   print("Please set the environment variable FOO")
   sys.exit(1)

