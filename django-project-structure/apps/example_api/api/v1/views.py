import requests
from django.shortcuts import render

from apps.example_api.models import Category


def index(request):
    latest_question_list = []
    context = {'latest_question_list': latest_question_list}
    # cmc = CoinMarketCapAPI('e9beb68a-4459-4ec7-9bb0-a48f45a2922a')
    #
    # rep = cmc.tools_priceconversion(amount=1, symbol='BTC').data
    url = 'https://api.coinmarketcap.com/data-api/v3/tools/price-conversion?amount=1&convert_id=2781&id=1'
    data = requests.get(url)

    return render(request, 'index.html', context)


def all_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'index.html', context)
