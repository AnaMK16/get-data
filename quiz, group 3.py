import requests
import json
import sqlite3
conn = sqlite3.connect('cities1.sqlite3')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE cities1 (Name VARCHAR(50), 
Capital VARCHAR(50),
Language VARCHAR(50), 
 
region VARCHAR(50))''')



resp = requests.get('https://restcountries.eu/rest/v2/lang/es')
print(resp.status_code)
print(resp.url)
print(resp.content)
as_dict = json.loads(resp.text)
with open('data1.json', 'w') as f:
    json.dump(as_dict, f, indent=4)
countries = []
for each in as_dict:
    names = each['name']
    capi = each['capital']
    
    lang = each['languages'][0]['name']
    re = each['region']
    column = (names, capi, lang, re)
    countries.append(column)
cursor.executemany("INSERT INTO cities1 (Name, Capital, Language, region) VALUES (?, ?, ?, ?)", countries) 
conn.commit()  


print(as_dict[0]["topLevelDomain"])
print(as_dict[0]["numericCode"])
        
print(as_dict[0]["population"])
# მონაცემთა ბაზაში ინახება ინფორმაცია იმ ქვეყნების სახელების, დედაქალაქების, ენისა და რეგიონის შესახებ, სადაც ოფიციალური ენაა ესპანური.






