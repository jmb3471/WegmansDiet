import requests

def sendPost(json):
    res = requests.post('http://127.0.0.1:5000/processjson',json=json)
    print ('debug response from server: ' + res.text)

sendPost({'name':'robby','cost':'1'})