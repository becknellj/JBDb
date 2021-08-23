import http.client
import sqlite3
import urllib
import json

conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")
jade_conn = sqlite3.connect ('movie_list.db')
c = jade_conn.cursor() 

c.execute('''
    SELECT title FROM movies bm
''')

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


