import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question
import json


@api_view(["POST"])
def add_question(request):
    try:
        data = request.data  # DRF automatically parses the request body as JSON

        if isinstance(data, list):  # Handle batch question creation
            questions = []
            for item in data:
                description = item.get("description")
                difficulty = item.get("difficulty")
                result = item.get("result")

                if description and difficulty and result:
                    question = Question.objects.create(
                        description=description, difficulty=difficulty, result=result
                    )
                    questions.append(
                        {
                            "id": question.id,
                            "description": question.description,
                            "difficulty": question.difficulty,
                            "result": question.result,
                            "message": "Question added successfully!",
                        }
                    )
                else:
                    return Response(
                        {"error": "All fields are required for each question."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response({"questions": questions}, status=status.HTTP_201_CREATED)

        elif isinstance(data, dict):  # Handle single question creation
            description = data.get("description")
            difficulty = data.get("difficulty")
            result = data.get("result")

            if description and difficulty and result:
                question = Question.objects.create(
                    description=description, difficulty=difficulty, result=result
                )
                return Response(
                    {
                        "id": question.id,
                        "description": question.description,
                        "difficulty": question.difficulty,
                        "result": question.result,
                        "message": "Question added successfully!",
                    },
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"error": "All fields are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"error": "Invalid input format."}, status=status.HTTP_400_BAD_REQUEST
        )

    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_question(request):
    questions = Question.objects.filter(difficulty=request.data["difficulty"])
    question_list = [
        {
            "id": q.id,
            "description": q.description,
            "difficulty": q.difficulty,
            "result": q.result,
        }
        for q in questions
    ]
    randomized_questions = random.shuffle(question_list)

    return Response(randomized_questions, status=status.HTTP_200_OK)
