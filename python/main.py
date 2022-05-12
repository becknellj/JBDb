import http.client
import urllib
import json
import pyrebase4

config = {
  "apiKey": "S7siXZFd6BgYe4LNOPtYh79Yv4Vd4JYiNHhkR7Bf",
  "authDomain": "jbdb-ce140.firebaseapp.com",
  "databaseURL": "https://jbdb-ce140-default-rtdb.firebaseio.com/",
  "storageBucket": "jbdb-ce140.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "e2e19e0d02mshfbe93db73d9b626p109296jsn8333e16d3d64",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }


for row in c.fetchall():
    temp_data = urllib.parse.urlencode({'s':''.join(row)})

    conn.request("GET", "/?"+temp_data+"&page=1&r=json", headers=headers)
    data = json.loads(conn.getresponse().read())


    print(data['Search'][0]['Title'])





    #data2 is essentially a list of dictionaries
    #need to get thefist dictionary in the list and get the imdb id from that dict
    #use that imdb id to do another request to get the details from the api
    #populate table


