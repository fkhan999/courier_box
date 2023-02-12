import requests

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '6BILwfXFVuBqMnE78zZipwz3K68KZ76qLPctXMayGQ4auKjFuiZ0MBrJrCVrGPAN',
}

for x in range(1):
    json_data = {
        'dataSource': 'Database',
        'database': 'Data',
        'collection': 'Boxes',
        'filter': {"_id":0},
        'update':{'$set':{'box1':1}}
    }
    response = requests.post('https://data.mongodb-api.com/app/data-byhgw/endpoint/data/v1/action/updateOne', headers=headers, json=json_data)
    print(response)
    print(response.content)