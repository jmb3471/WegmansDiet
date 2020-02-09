import requests

def sendFood(json):
    res = requests.post('http://127.0.0.1:5000/sendDataToBack',json=json)
    print ('debug response from server: ' + res.text)

#sendFood({'action':'add','object':{'sku':'435178'}})
#sendFood({'action':'remove','object':{'sku':'435178'}})
print(sendFood({'action':'search','name':'banana'}))

