#libraries for database, HTTP connection and Json handling

import requests
import json
import pandas as pd


#URl connection for weather API
url = 'http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=f19183c7cecdf1a18c3e84b138490e3e'

'''
#connection for databse
conn = sqlite3.connect('db1.db')
c = conn.cursor()

#creates a databse (if does not already exists) fields - Soil moisture, Temperature, humidity, and water to be poured
c.execute('CREATE TABLE IF NOT EXISTS weatherdata (moisture REAL, temperature REAL, humidity REAL, waterlevel REAL)')
'''


def getweatherdata():
    #getting data from the API
    res = requests.get(url)
    data = res.json()

    #seperation of data
    inter = data["main"]
    temp = inter["temp"]
    hum = inter["humidity"]

    return temp,hum

#get data from web server
#Demo code --- add IP from C++ code
def getmoisinfo():
    mois = requests.get('http://192.168.43.161/Python')
    x = mois.text
    return x
    
# extracting response text
def sendwater(waterlvl):
    API_ENDPOINT = "http://192.168.43.161/Python"
    PARAMS= {'%d' % int(waterlvl):waterlvl}

  
    r = requests.post(url = API_ENDPOINT, params = PARAMS)
# funtion to add data to the database
def adddata(mois,temp,hum,water):
    '''
    c.execute("INSERT INTO weatherdata (moisture, temperature, humidity, waterlevel) VALUES (?,?,?,?)",(mois,temp,hum,water))
    conn.commit()
    '''
    #TODO add important code
    df = pd.read_csv('data_base.csv')
    df_new = pd.DataFrame([mois,temp,hum,water])
    with open('foo.csv', 'a') as f:
             (df_new).to_csv(f, header=False)



def getdbdata():
    #database checking
    # displays all the contents of the data base 
    '''
    c.execute('SELECT * FROM weatherdata')
    x = c.fetchall()
    print(x)
    y = []
    z = []
    for i in x:
        y.append([i[3],i[1],i[2]])
        z.append([i[0]])

    '''
    df = pd.read_csv('data_base.csv')
    #print(df.head())
    return df

