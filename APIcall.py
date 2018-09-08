import http.client
import getopt
import sys
import time

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"


def get_api_key():
    argv = getopt.getopt(sys.argv[1:], "")
    return argv[1]


api_key = get_api_key()
my_api_key = api_key[0]

conn.request("GET", "/3/discover/movie?with_runtime.lte=0&with_genres=35&primary_release_date.gte=2000&page=1&sort_by=popularity.desc&language=en-US&api_key="+my_api_key, payload)
res = conn.getresponse()
data = res.read()
a = conn.timeout

print(data, file=open("out_page2.txt", "w+"))
print(a)

