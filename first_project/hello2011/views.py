from django.shortcuts import render, redirect
from .models import Company, Product
from django.http import HttpResponseRedirect, HttpResponseNotFound


# получение данных из бд
def index2(request):
    products = Product.objects.all()
    return render(request, "hello2011/index.html", {"products": products})


# добавление данных из бд
def create(request):
    create_companies()  # добавляем начальные данные для компаний

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return redirect('index2')
    # передаем данные в шаблон
    companies = Company.objects.all()
    return render(request, "hello2011/create.html", {"companies": companies})


# изменение данных в бд
def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.company_id = request.POST.get("company")
            product.save()
            return redirect('index2')
        else:
            companies = Company.objects.all()
            return render(request, "hello2011/edit.html", {"product": product, "companies": companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('index2')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


# добавление начальных данных в таблицу компаний
def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name="Apple")
        Company.objects.create(name="Asus")
        Company.objects.create(name="MSI")
