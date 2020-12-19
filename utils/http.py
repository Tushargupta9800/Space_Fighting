import requests

def getall():
    geturl = "http://localhost:3000/getScore"
    PARAMS = {'kuch-bhi':'kuch-bhi'}
    response = requests.get(url = geturl, params = PARAMS)
    data = response.json()
    return data
    #for i in range(10):
        #print(i)
        #print(data[i]["name"])
        #print(data[i]["score"])


def sendScore(name, score):
    sendurl = "http://localhost:3000/addScore/"+str(name)+"/"+str(score)
    print(sendurl)
    PARAMS = {
        'name': name,
        'score': score}
    requests.get(url = sendurl)

def checkInternet():
    url = "http://www.google.com"
    timeout = 5
    try:
            request = requests.get(url, timeout=timeout)
            return 1
    except (requests.ConnectionError, requests.Timeout) as exception:
            return 0
