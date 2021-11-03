import re
from django.utils.timezone import datetime
from django.shortcuts import render


def home(request):
    context = {}
    context['date'] = datetime.now()

    return render(request, 'hello/hello_there.html', context)
