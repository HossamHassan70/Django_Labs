from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from company.forms import EmployeeForm, EmployeeForm2
from django.views.decorators.http import require_http_methods
from company.models import Employee, Team


# Create your views here.
def EmployeeView(request):
    if request.method == "GET":
        myform = EmployeeForm()
        return render(request, "company/create_employee.html", {"form": myform})

    if request.method == "POST":
        myform = EmployeeForm(request.POST)
        if myform.is_valid():
            team_id = request.POST["team"]
            team = Team.objects.get(pk=team_id)
            Employee.objects.create(
                name=request.POST["name"],
                salary=request.POST["salary"],
                title=request.POST["title"],
                team=team,
            )
            return render(request, "company/create_employee.html", {"form": myform})
    return HttpResponse("Helooo")


@require_http_methods(["GET", "POST"])
def EmployeeView2(request):
    if request.method == "GET":
        myform = EmployeeForm2()
        return render(request, "company/create_employee.html", {"form": myform})

    if request.method == "POST":
        myform = EmployeeForm2(request.POST)
        if myform.is_valid():
            myform.save()
            return render(request, "company/create_employee.html", {"form": myform})
    return HttpResponse("Helooo")


class TeamClassView(View):
    def get(self, request):
        return render(request, "company/create_team.html")

    def post(self, request):
        name = request.POST.get("name")
        manager_name = request.POST.get("manager")
        if name and manager_name:
            try:
                manager = Employee.objects.get(name=manager_name)
                Team.objects.create(name=name, manager=manager)
                return HttpResponse("Team created successfully!")
            except Employee.DoesNotExist:
                return HttpResponse("Manager not found!", status=400)
        else:
            return HttpResponse("Invalid request!", status=400)
