from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from lab1.forms import Dataform, Studentform
from lab1.models import Student
from lab1.models import Data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render (request ,'lab1/home.html')

def viewstd(request):
    if request.session.get('username'):
        students = Data.objects.all()
        context = {'students': students}
        return render(request ,'lab1/viewstd.html', context)
    else:
        return redirect("signin")


def deletestd(request,id):
    Data.objects.get(id=id).delete()
    return redirect (viewstd)

def updatestd(request,id):
    student = Data.objects.get(id=id)
    if request.method == 'POST':
        student.track = request.POST['track']
        student.branch = request.POST['branch']
        student.save() 
        return redirect('viewstd')
    context = {'student': student}
    return render(request, 'lab1/updatestd.html', context)
    
def signup(request):  
    if request.method == 'GET':
        myform=Studentform()
        return render(request,'lab1/signup.html',{'form':myform})
    if request.method == 'POST':
        myform=Studentform(request.POST)
        print(myform)
        if myform.is_valid():

            Student.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            return render(request,'lab1/signin.html',{'form':myform})
            
    
        
def signin(request):
    if request.method == 'GET':
        return render(request,'lab1/signin.html')
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        data=Student.objects.filter(username=username)
        
        if data:
            auth=authenticate(username=data[0].username,password=password)
            
            if auth:
                login(request,auth)
                request.session["username"]=username
                return redirect ("viewstd")
            else:
                return render (request,'lab1/signin.html')   

        else:
            return render(request,'lab1/signin.html')    

def createstd(request):
    myform = Dataform()
    if request.method == 'POST':
        myform = Dataform(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('viewstd')
    return render(request, 'lab1/createstd.html', {'form': myform})


def signout(request):
    logout(request)
    return redirect('signin')