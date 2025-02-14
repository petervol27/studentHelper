from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentUser
from .serializers import StudentUserSerializer

# Register a New User
@api_view(["POST"])
def register(request):
    serializer = StudentUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the new user to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List All Students and Create a New Student
@api_view(["GET", "POST"])
def student_list_create(request):
    if request.method == "GET":
        students = StudentUser.objects.all()
        serializer = StudentUserSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new student
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Logout (No Action - Simply removed the token on client-side)
@api_view(["POST"])
def logout(request):
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
