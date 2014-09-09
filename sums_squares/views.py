import json
import datetime

from django.http import HttpResponse
from django.core.cache import cache

def sumofsquares_squareofsum_difference(n):
    sum_of_squares = sum(i ** 2 for i in range(n+1))
    square_of_sum = sum(range(n+1)) ** 2
    difference = square_of_sum - sum_of_squares
    return difference

def difference(request):
    number = int(request.GET.get('number'))
    cached_item = cache.get(number)
    if cached_item:
        difference, count = cached_item
        count += 1
    else:
        difference = sumofsquares_squareofsum_difference(number)
        count = 1
    cache.set(number, (difference, count))
    response_data = {}
    response_data['number'] = number
    response_data['value'] = difference
    response_data['occurrences'] = count
    response_data['datetime'] = str(datetime.datetime.now())
    return HttpResponse(json.dumps(response_data), content_type="application/json")


    
