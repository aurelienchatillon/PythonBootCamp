import requests
import json
import os

# partie 1
def getRequest():
    # url = "https://api.github.com/repositories"
    # repo = requests.get(url)
    # data = repo.json()
    path = 'repositories.json' # chemin vers repositories.json ou repositories-stars.json pour la deuxième question
    data = read_from_local_data(path)

    fichier = open('api.txt',"w")
    for dict in data:
        fichier.write(dict['name'] )
    
        if dict['description']:
            fichier.write(' : '+dict['description']+'\n')
        else:
            fichier.write(' \n ')
    fichier.close()

    print("done")

def read_from_local_data(path):
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)
    
def popular_git():
    r = requests.get("https://api.github.com/search/repositories?q=sort=stars&order=desc&pushed:>=2020-01-01&stars:>=500")
    results = r.json()
    f = open("popular_git.txt","a")
    results_aux = results["items"]
    for dict in results_aux :
        f.write("Name : "+dict["name"]+"\n")
        if dict["description"] :
            f.write("Description : "+dict["description"]+"\n")
        f.write("Stars : "+str(dict["stargazers_count"])+"\n")
    f.close()

    print("done")


def read_from_local_data():
    path = './repositories.json' # chemin vers repositories.json ou repositories-stars.json pour la deuxième question
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)

def last_public_git_dict():
    #r = requests.get('https://api.github.com/repositories')
    #results = r.json()
    results = read_from_local_data()
    res = {}
    for dict in results :
        #print(dict["name"])
        if dict["description"] :
            #print(dict["description"])
            res[dict["name"]] = dict["description"]
        else :
            #print("None")
            res[dict["name"]] = "None"
    s = json.dumps(res, indent = 8)
    f = open("data.json","a")
    f.write(s)
    f.close()


popular_git()
getRequest()

# CRON
# * * * * * python3 C:\bootcamp\semaine1\projet.py > C:\bootcamp\semaine1\log.log