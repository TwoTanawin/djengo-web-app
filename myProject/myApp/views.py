from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.models import Person

# Create your views here.
def index(request):
    # name = 'admin'
    # age = 23

    # return render(request, 
    #               "index.html", 
    #               {"name":name, "age":age})
    allPerson = Person.objects.all()

    # allPerson = Person.objects.filter(age=24)
    return render(request, "index.html", {"allPerson":allPerson})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        #recieve
        name = request.POST["name"]
        age = request.POST["age"]

        #save
        person = Person.objects.create(
            name = name,
            age=age
        )

        person.save()
        # print(name, age)

        # change direction
        return redirect("/")
    else:
        return render(request, "form.html")