import requests

def get_omdb(id, key):
    id_base = 't'
    if id[0:2] == 'tt':
        id_base = 'i'

    r = requests.session() 
    response = r.get('http://www.omdbapi.com', 
        params={'apikey':key,
            id_base:id
        })
    #print (response.url)
    movie= response.json()
    return movie

def extact(dic):
    try:
        title =  dic['Title']
    except:
        title = ""
    try:
        bo =  dic['BoxOffice']
    except:
        bo = ""
    
    return [title, bo]
    
apikey = "91a21490"
x01 = get_omdb("Frozen", apikey)
x02 = get_omdb("tt3896198",apikey)

print(extact(x01))
print(extact(x02))