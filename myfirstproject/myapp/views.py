from django.shortcuts import render


# Create your views here.
def index(request):
	data = {"red": "красный", "green": "зелёный", "blue": "синий"}
	return render(request, "index.html", context={"data": data})


def about(request):
	return render(request, "about.html")


def contact(request):
	return render(request, "contact.html")