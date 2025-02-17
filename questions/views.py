from rest_framework.response import Response
from rest_framework.decorators import api_view
import sys
import io
import json
import random
from rest_framework import status
from .models import Question


@api_view(["POST"])
def list_question(request):
    """Fetches random questions based on difficulty"""
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
    random.shuffle(question_list)

    return Response(question_list, status=status.HTTP_200_OK)


@api_view(["POST"])
def submit_code(request):
    """Evaluates user-submitted code and ensures a function exists before execution"""
    try:
        data = request.data
        question_id = data.get("question_id")
        user_code = data.get("code")

        # Retrieve the question from the database
        question = Question.objects.get(id=question_id)
        expected_output = question.result.strip()

        # Dynamically extract function name from the question description
        function_name = None
        words = question.description.split(" ")
        for i, word in enumerate(words):
            if word.startswith("") and word.endswith(""):
                function_name = word.strip("`")
                break

        if not function_name:
            return Response(
                {"error": "Function name not found in question description."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 🚨 *Ensure the function is defined*
        if f"def {function_name}(" not in user_code:
            return Response(
                {
                    "result": f"❌ Your code must define {function_name}() using def {function_name}()"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Safe execution environment
        exec_globals = {}

        # Redirect stdout to capture print() output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        try:
            # Execute the user code
            exec(user_code, exec_globals)

            # Check if function is defined
            if function_name not in exec_globals or not callable(
                exec_globals[function_name]
            ):
                return Response(
                    {"result": f"❌ Function {function_name} is not defined properly."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Get the user's function
            user_function = exec_globals[function_name]

            # Create a dynamic test input based on the function name
            test_input = ["Alice"] if "name" in function_name else [2]

            # Run the function with test input
            user_return_value = user_function(*test_input)

            # Capture printed output
            user_print_output = sys.stdout.getvalue().strip()

            # Determine final output (either return value or print output)
            user_output = (
                user_print_output if user_print_output else str(user_return_value)
            )

            # Compare user function's output with expected output
            is_correct = user_output.strip() == expected_output.strip()
            result = (
                "✅ Correct!"
                if is_correct
                else f"❌ Incorrect! Expected: '{expected_output}', Got: '{user_output}'"
            )

        except Exception as e:
            result = f"⚠️ Error in function execution: {str(e)}"

        # Reset stdout
        sys.stdout = old_stdout

        return Response({"result": result}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {"error": f"⚠️ Server Error: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def generate_questions(request):
    """API endpoint to create 30 coding questions"""

    questions = [
        # Beginner Questions
        {
            "description": "Create a function called hello_world that prints 'Hello, World!'.",
            "difficulty": "beginner",
            "result": "Hello, World!",
        },
        {
            "description": "Define a function add_numbers(a, b) that returns the sum of a and b.",
            "difficulty": "beginner",
            "result": "8",
        },
        {
            "description": "Write a function square(n) that returns the square of n.",
            "difficulty": "beginner",
            "result": "25",
        },
        {
            "description": "Create a function greet(name) that prints 'Hello, {name}!' with the given name.",
            "difficulty": "beginner",
            "result": "Hello, Alice!",
        },
        {
            "description": "Write a function is_even(n) that returns 'True' if n is even, otherwise 'False'.",
            "difficulty": "beginner",
            "result": "True",
        },
        # Intermediate Questions
        {
            "description": "Define a function factorial(n) that returns the factorial of n.",
            "difficulty": "intermediate",
            "result": "120",
        },
        {
            "description": "Create a function reverse_string(s) that returns the reversed version of s.",
            "difficulty": "intermediate",
            "result": "olleh",
        },
        {
            "description": "Write a function count_vowels(s) that counts the vowels (a, e, i, o, u) in s.",
            "difficulty": "intermediate",
            "result": "4",
        },
        {
            "description": "Create a function is_palindrome(s) that returns 'True' if s is a palindrome.",
            "difficulty": "intermediate",
            "result": "True",
        },
        {
            "description": "Write a function find_max(lst) that returns the largest number in lst.",
            "difficulty": "intermediate",
            "result": "99",
        },
        # Professional Questions
        {
            "description": "Define a function fibonacci(n) that returns the `n`th Fibonacci number.",
            "difficulty": "professional",
            "result": "13",
        },
        {
            "description": "Write a function merge_sorted_lists(lst1, lst2) that merges two sorted lists into one sorted list.",
            "difficulty": "professional",
            "result": "[1,2,3,4,5,6,7,8]",
        },
        {
            "description": "Write a function is_anagram(s1, s2) that returns 'True' if s1 and s2 are anagrams.",
            "difficulty": "professional",
            "result": "True",
        },
        {
            "description": "Create a function find_duplicates(lst) that returns a list of duplicate numbers in lst.",
            "difficulty": "professional",
            "result": "[2, 3]",
        },
        {
            "description": "Write a function binary_search(lst, target) that returns the index of target in lst using binary search.",
            "difficulty": "professional",
            "result": "3",
        },
    ]

    # Insert the questions into the database
    created_count = 0
    for q in questions:
        # Prevent duplicate entries
        if not Question.objects.filter(description=q["description"]).exists():
            Question.objects.create(
                description=q["description"],
                difficulty=q["difficulty"],
                result=q["result"],
            )
            created_count += 1

    return Response(
        {"message": f"✅ {created_count} questions added successfully!"},
        status=status.HTTP_201_CREATED,
    )
