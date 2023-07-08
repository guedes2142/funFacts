import requests
from django.shortcuts import render

def api_view(request):
    jokes = []

    for _ in range(20):  # Gera 20 novos fatos
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            joke = {
                'setup': data['setup'],
                'punchline': data['punchline']
            }
            jokes.append(joke)
        

    return render(request, 'funfacts/index.html', {'jokes': jokes})


