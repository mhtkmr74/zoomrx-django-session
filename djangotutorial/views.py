from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from . models import Person
from django.shortcuts import render

# Create your views here.


def person_details(request):
    person_result = list(Person.objects.all().values())
    template = loader.get_template('result.html')
    html_message = template.render({'result': person_result})
    print(html_message)
    return HttpResponse(html_message)
