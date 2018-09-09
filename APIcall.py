import requests
import getopt
import sys
import json


def get_api_key():
    argv = getopt.getopt(sys.argv[1:], "")
    return argv[1]


payload = {}
api_key = get_api_key()
my_api_key = api_key[0]

file = open("movie_ID_name.csv", "w+")

for p in range(1, 16):
    res = requests.post("https://api.themoviedb.org/3/discover/movie?api_key="+my_api_key+"&language=en-US&sort_by=popularity.desc&page="+str(p)+"&primary_release_date.gte=2000&with_genres=35", data = {'key':'value'})
    j = res.json()
    s1 = json.dumps(j)
    json_parsed = json.loads(s1)
    keys = j.keys()

    for key in j.keys():
        if key == 'results':
            results = j[key]
            for i in range(0, len(results)):
                for key1 in results[i].keys():
                    if key1 == 'id':
                        movie_id = results[i][key1]
                        movie_title = results[i]['title']
                        print(str(movie_id)+","+movie_title, file=open("movie_ID_name.csv", "a+"))
