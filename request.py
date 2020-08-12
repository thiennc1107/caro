import json
import requests
from ast import literal_eval
def get_matrix():
    jsonstring=requests.post("https://tryit.dangchiviet.com/caro/send.php",data={"API_KEY":"c12c51a23b8a5d0d9a917a78631f48a48b7ed799b8ee10aa3e3afa695f46aa66","action":"getposition","gameid":32})
    raw_response=jsonstring.content
    str_response=raw_response.decode('utf-8')
    response=[]
    for i in range(29,len(str_response)-1,7):
        response.append(str_response[i])
    return response

   
    

get_matrix()
    
    

