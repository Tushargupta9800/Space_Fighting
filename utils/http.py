import requests
#connecting backend with frontend using requests

#get all the highscore list
def getall():
    geturl = "https://spacefightingbackend.herokuapp.com/getScore"
    PARAMS = {'kuch-bhi':'kuch-bhi'}
    response = requests.get(url = geturl, params = PARAMS)
    data = response.json()
    return data
    #for i in range(10):
        #print(i)
        #print(data[i]["name"])
        #print(data[i]["score"])

#sending the high scores to the backend
def sendScore(name, score):
    sendurl = "https://spacefightingbackend.herokuapp.com/addScore/"+str(name)+"/"+str(score)
    print(sendurl)
    PARAMS = {
        'name': name,
        'score': score}
    requests.get(url = sendurl)

#checking if the user is connected to the INTERNET or not
def checkInternet():
    url = "http://www.google.com"
    timeout = 5
    try:
            request = requests.get(url, timeout=timeout)
            return 1
    except (requests.ConnectionError, requests.Timeout) as exception:
            return 0
