import json

def get_mat(): 
        d = {}
        brand = input("Brand : ")
        with open('botbrands.json', 'r') as f:
            a = f.read()
            d = json.loads(a)
            for myKey, myVal in d.items():
                if brand == myKey: 
                    return print(myVal)



get_mat()
