import requests
import getopt
import sys
import json
import time
import csv


def get_api_key():
    argv = getopt.getopt(sys.argv[1:], "")
    return argv[1]


payload = {}
api_key_arr = get_api_key()
api_key = api_key_arr[0]

file = open("movie_ID_name.csv", "w+")

for p in range(1, 16):
    res1 = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=" + api_key + "&language=en-US&sort_by=popularity.desc&page=" + str(p) + "&primary_release_date.gte=2000&with_genres=35")
    j = res1.json()
    s1 = json.dumps(j)
    json_parsed = json.loads(s1)
    keys = j.keys()
    time.sleep(1)

# Q1.1b
    for key in j.keys():
        if key == 'results':
            results = j[key]
            for i in range(0, len(results)):
                for key1 in results[i].keys():
                    if key1 == 'id':
                        movie_id = results[i][key1]
                        movie_title = results[i]['title']
                        if not movie_title.find(",") == -1:
                            movie_title = "\"" + movie_title + "\""
                        print(str(movie_id)+","+movie_title, file=open("movie_ID_name.csv", "a+"))


# Q1.1c
file = open("movie_ID_sim_movie_ID.csv", "w+")

with open('movie_ID_name.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    popMoviesIDs = []
    for row in readCSV:
        ID = row[0]
        popMoviesIDs.append(ID)


listBoth = []
for index in range(0, 300):
    print(index)
    res2 = requests.get("https://api.themoviedb.org/3/movie/"+popMoviesIDs[index]+"/similar?api_key=" + api_key + "&language=en-US&page=1")
    sim = res2.json()
    sim_str = json.dumps(sim)
    sim_parsed = json.loads(sim_str)
    for key2 in sim.keys():
        if key2 == 'results':
            sim_results = sim[key2]
            if len(sim_results) > 0:
                for a in range(0, len(sim_results)):  # only need 5 similar movies (ids)
                    # if len(sim_results) <= 5:
                    #     print("+++++++++++++++++++++++"+str(len(sim_results))+" similar movies of" + popMoviesIDs[index])
                    if a == 5:
                        print("-------------"+str(a)+" all similar movies of " + popMoviesIDs[index])
                        break
                    for key3 in sim_results[a].keys():  # 14 items
                        if key3 == 'id':
                            sim_movie_id = sim_results[a][key3]
                            print(popMoviesIDs[index]+","+str(sim_movie_id), file=open("movie_ID_sim_movie_ID.csv", "a+"))
                            listBoth.append([str(popMoviesIDs[index]), str(sim_movie_id)])
            else:
                print(popMoviesIDs[index]+" has no similar movies")


# filling in duplicates to be removed in delDuplicates[]
delDuplicates = []
a = 0
for i in range(0, len(listBoth)):
    j = i + 1
    for j in range(i + 1, len(listBoth)):
        if listBoth[i][0] == listBoth[j][1]:  # print("possible duplicate")
            if listBoth[j][0] == listBoth[i][1]:  # print("duplicate found")
                if listBoth[i][0] < listBoth[j][0]:
                    delDuplicates.append(listBoth[j])
                else:
                    delDuplicates.append(listBoth[i])

print("len(listBoth) before dup rem: " + str(len(listBoth)))
# removing duplicates from listBoth[]
for i in range(len(delDuplicates)):
    for j in range(len(listBoth)):
        if delDuplicates[i] == listBoth[j]:
            del listBoth[j]
            break
# update csv
file = open("movie_ID_sim_movie_ID_wo_duplicates.csv", "w+")
for i in range(len(listBoth)):
    print(str(listBoth[i][0]) + "," + str(listBoth[i][1]), file=open("movie_ID_sim_movie_ID_wo_duplicates.csv", "a+"))

print("len(listBoth) after dup rem: " + str(len(listBoth)))
print("listBoth: " + str(listBoth))
print("len(delDuplicates): " + str(len(delDuplicates)))
print("delDuplicates: " + str(delDuplicates))

