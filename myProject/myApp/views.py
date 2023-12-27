from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.models import Person
from django.contrib import messages

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
        messages.success(request, "Submit Success")

        # change direction
        return redirect("/")
    else:
        return render(request, "form.html")
    
def edit(request, personID):
    if request.method == "POST":
        person = Person.objects.get(id=personID) # check person id
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()

        # change direction
        return redirect("/")

    else:
        # get data
        person = Person.objects.get(id=personID)


        return render(request, "edit.html",{"person":person})
    
def delete(request, personID):
    person = Person.objects.get(id=personID)
    person.delete()

    messages.success(request, "Deleted Success")

    # change direction
    return redirect("/")