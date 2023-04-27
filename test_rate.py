import requests

url = "http://127.0.0.1:5000/post"

data = {
	"msg":"Hi"
}

reponse_status_list=[]
response_json=[]

for i in range(0,100):
    response = requests.post(url, json=data)
    reponse_status_list.append(response.status_code)
    response_json.append(response.json())
    # print("Status Code", response.status_code)
    # print("JSON Response ", response.json())

# print(reponse_status_list)
print(response_json)