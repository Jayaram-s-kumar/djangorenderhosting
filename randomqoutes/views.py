from django.shortcuts import render
import requests,json

# Create your views here.

def home(request):
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url,headers={'x-api-key':'wEuJMF5D4ghd4bs8fRbpig==oT6NhiuxotmhleMi'})
    if response.status_code == 200:

        print(response.text)
        print(type(response.text),'\n')

        jsondata = json.loads(response.text)
        print(jsondata)
        print(type(jsondata),'\n')

        firstelement = jsondata[0]
        print(firstelement)
        print(type(firstelement),'\n')

        quote = firstelement['quote']
        print(quote,'\n')
        print(type(quote))

        author = json.loads(response.text)[0]['author']



      
        return render(request,'quotes.html',{'quote':quote,'author':author})
    else:
        print("Error",response.status_code , response.text)
