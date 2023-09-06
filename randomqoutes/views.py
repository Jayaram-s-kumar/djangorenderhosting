from django.shortcuts import render
import requests,json

# Create your views here.

def home(request):
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url,headers={'x-api-key':'wEuJMF5D4ghd4bs8fRbpig==oT6NhiuxotmhleMi'})
    if response.status_code == 200:
        print(response.text)
        qoute= json.loads(response.text)[0]['quote']
        author= json.loads(response.text)[0]['author']
        print(qoute)
        return render(request,'quotes.html',{'quote':qoute,'author':author})
    else:
        print("Error",response.status_code , response.text)
