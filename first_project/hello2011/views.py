from django.shortcuts import render


def index(request):
    people = Person.objects.all()
    return render(request, "hello2011/index.html", {"people": people})
