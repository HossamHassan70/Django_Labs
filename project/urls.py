"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from company.views import EmployeeView, EmployeeView2
from myapi.views import EmployeeAPIView, TeamAPIView, TeamViewSet

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="team")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", EmployeeView, name="employee"),
    path("emp", EmployeeView2, name="employee2"),
    path("api-auth/", include("rest_framework.urls")),
    path("employee/", EmployeeAPIView.as_view(), name="employee-list-create"),
    path("employee/<int:pk>/", EmployeeAPIView.as_view(), name="employee-update"),
    path("employee/<int:pk>/", EmployeeAPIView.as_view(), name="employee-delete"),
    path("teams/", include(router.urls)),
    path("team/", TeamAPIView.as_view(), name="team-list-create"),
    path("team/<str:pk>/", TeamAPIView.as_view(), name="team-update-delete"),
]
