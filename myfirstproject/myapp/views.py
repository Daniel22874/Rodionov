from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, "index.html")


def about(request):
	return render(request, "about.html")


def contact(request):
	return render(request, "contact.html")


def lesson2(request):
	return render(request, "lesson2.html")


def products(request, productid):
	category = request.GET.get("cat", "")
	output = f"<h2>Продукт № {productid} Category: {category}</h2>"
	return HttpResponse(output)


def users(request, id, name):
	output = f"<h2>Пользователь</h2><h3>id: {id} имя:{name}</h3>"
	return HttpResponse(output)