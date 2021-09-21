import  requests 
from ss import *


api_address='https://newsapi.org/v2/everything?q=Apple&from=2021-09-21&sortBy=popularity&apiKey='+key

json_data = requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("Number "+ str(i+1)+" , "+json_data["articles"][i]["title"]+".")

    return ar


