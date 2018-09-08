import requests
import getopt
import sys


def get_api_key():
    argv = getopt.getopt(sys.argv[1:], "")
    return argv[1]


api_key = get_api_key()
my_api_key = api_key[0]

file=open("output.csv", "w+")

for p in range(1, 16):
    res = requests.get("https://api.themoviedb.org/3/discover/movie?api_key="+my_api_key+"&language=en-US&sort_by=popularity.desc&page="+str(p)+"&primary_release_date.gte=2000&with_genres=35")
    print("HTTP status: " + str(res.status_code))
    print(res.json())
    json_text = res.json()
    print(json_text, file=open("output.csv", "a+"))

