def func():
    return 'Hello World'

# Name: Rongbo He,Justin Jennings, Stefan Ivanov, group Edoardo Mangiarotti
# email: hero@mail.uc.edu, jenninjx@mail.uc.edu, ivanovsw@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is the main module to execute the code for the assignment.
# Citations:
# Anything else that's relevant:
import requests
import json
#Connect to the server
response = requests.get('https://api.si.edu/openaccess/api/v1.0/stats?api_key=a0lubHR3UaSnviEsbukDs1YNQYvS2HYlORKqdfhe')
#Receive the results
json_string = response.content
#Parse it to dictionary
parsed_json = json.loads(json_string)
#print(parsed_json)
#Print the number of total objects for each units
print('Total_Objects:',parsed_json['response']['units'][0]['total_objects'])
#Get the data from the first individual units to 
#the end of all the units, discard the aggregate data
units = parsed_json['response']['units'][1:]
#Iterate through every unit to get their unit names and number of objects
for unit in units:
    print('Unit:', unit['unit'],', ','Total_Objects: ', unit['total_objects'])
