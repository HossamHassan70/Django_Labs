from django.shortcuts import render, redirect

# from django.shortcuts import
# from django.http import HttpResponse
from lab1.forms import Dataform, Studentform
from lab1.models import Student, Data

# from lab1.models import
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "lab1/home.html")


def viewstd(request):
    if request.session.get("username"):
        students = Data.objects.all()
        context = {"students": students}
        return render(request, "lab1/viewstd.html", context)
    else:
        return redirect("signin")


def deletestd(request, id):
    Data.objects.get(id=id).delete()
    return redirect(viewstd)


def updatestd(request, id):
    student = Data.objects.get(id=id)
    if request.method == "POST":
        student.track = request.POST["track"]
        student.branch = request.POST["branch"]
        student.save()
        return redirect("viewstd")
    context = {"student": student}
    return render(request, "lab1/updatestd.html", context)


def signup(request):
    if request.method == "GET":
        myform = Studentform()
        return render(request, "lab1/signup.html", {"form": myform})

    if request.method == "POST":
        myform = Studentform(request.POST)

        if myform.is_valid():
            Student.objects.create(
                username=myform.cleaned_data["username"],
                email=myform.cleaned_data["email"],
                password=myform.cleaned_data["password"],
            )
            return render(request, "lab1/signin.html", {"form": myform})
        else:
            # Form is not valid, render the signup page again with the form and errors
            return render(request, "lab1/signup.html", {"form": myform})


def signin(request):
    if request.method == "GET":
        return render(request, "lab1/signin.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        data = Student.objects.filter(username=username)

        if data:
            auth = authenticate(username=data[0].username, password=password)

            if auth:
                login(request, auth)
                request.session["username"] = username
                return redirect("viewstd")
            else:
                return render(
                    request,
                    "lab1/signin.html",
                    {"error": "Invalid username or password"},
                )
        else:
            return render(request, "lab1/home.html", {"error": "User not found"})


def createstd(request):
    myform = Dataform()
    if request.method == "POST":
        myform = Dataform(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect("viewstd")
    return render(request, "lab1/createstd.html", {"form": myform})


def signout(request):
    logout(request)
    return redirect("signin")
