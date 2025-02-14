import requests

rest = requests.get('http://127.0.0.1:8000/testapp/view')

if rest.status_code == 200:
    objects = rest.json()
    school_list = []

    for i in objects:
        school_dict = {
            "schl_id": i["schl_id"],
            "schl_name": i["schl_name"],
            "schl_add": i["schl_add"],
            "schl_fees": i["schl_fees"]
        }
        school_list.append(school_dict)

    print(school_list)
else:
    print("Connection error!")
