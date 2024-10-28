from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст : {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "hello/index.html", {"form": userform})


# def index(request):
#     return render(request, 'hello/index.html')


# def postuser(request):
#     # получаем из данных запроса POST отправленные через форму данные
#     name = request.POST.get("name", "Undefined")
#     age = request.POST.get("age", 1)
#     langs = request.POST.getlist("languages", ["python"])
#
#     return HttpResponse(f"""
#                 <div>Name : {name}<br>  Age : {age}</div><br>
#                 <div>Languages : {langs}</div>
#             """)
