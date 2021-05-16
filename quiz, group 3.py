import requests
import json
import sqlite3


city = 'Tbilisi'
key = 'b06691354e7612207b24cf257a8ddfe9'
payload = {'q': city, 'appid': key, 'units': 'metric'}

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
as_dict = json.loads(r.text)

pretty_json = json.dumps(as_dict, indent=4)

with open('data.json', 'w') as f:
    # json.dump(a, f, indent=4)
    f.write(pretty_json)

# requests functions

# print(r.headers)
# print(r.status_code)
# print(r.content)
# print(r.text)


# additional information
# print(as_dict['main']['temp_max'])  
# print(as_dict["sys"]["id"])  


# add data to DB
main = as_dict['main']
temp = main['temp']
feels_like = main['feels_like']
temp_min = main['temp_min']
temp_max = main['temp_max']

row = [temp, feels_like, temp_min, temp_max]
# create table
conn = sqlite3.connect('weather_basa.sqlite')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS weather(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temp  FLOAT,
                feels_like FLOAT,
                temp_min FLOAT ,
                temp_max FLOAT
                );
''')
conn.commit()

cursor.execute('''
                INSERT INTO weather (temp, feels_like, temp_min, temp_max)
                VALUES(?,?,?,?)
''', row)
conn.commit()

conn.close()
# მონაცემთა ბაზაში ინახება ინფორმაცია ამჟამინდელი ტემპერატურის,
#  ტენიანობის მაქსიმალური და მინიმალური ტემპერატურების შესახებ.





