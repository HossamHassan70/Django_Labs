from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from company.models import Employee, Team
from myapi.serializers import EmpSerializer, TeamSerializer


class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmpSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            employees = Employee.objects.all()
            Employees = EmpSerializer(employees, many=True)
            return Response(
                {"employees": Employees.data}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        employee_instance = Employee.objects.get(id=pk)
        serializer = EmpSerializer(employee_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        employee_instance = Employee.objects.get(pk=pk)
        employee_instance.delete()
        return Response(
            {"message": "Employee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class TeamViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                team_instance = Team.objects.get(name=pk)
                serializer = TeamSerializer(team_instance)
                return Response(serializer.data)
            except Team.DoesNotExist:
                return Response(
                    {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            teams = Team.objects.all()
            serializer = TeamSerializer(teams, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            teams = Team.objects.all()
            Teams = TeamSerializer(teams, many=True)
            return Response({"teams": Teams.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        team_instance = Team.objects.get(name=pk)
        serializer = TeamSerializer(team_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            team_instance = Team.objects.get(name=pk)
            team_instance.delete()
            return Response(
                {"message": "Team deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
