from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentUser
from .serializers import StudentUserSerializer


# Register a New User
@api_view(["POST"])
def register(request):
    try:
        user = StudentUser(username=request.data["username"])
        user.set_password(request.data["password"])  # This hashes the password.
        user.save()
        return Response({"success": "successfully registered"})
    except Exception as e:
        return Response({"error": "error check credentials"})


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
