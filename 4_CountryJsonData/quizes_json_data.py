import requests

url = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"
response = requests.get(url)
content = response.json()


question_id = int(input("Enter the question ID: "))

correct_answer = None
question_found = False

for quiz in content["quizzes"]:
    for question in quiz["questions"]:
        if question["id"] == question_id:
            question_found = True
            for choice, is_correct in question["choices"].items():
                if is_correct:
                    correct_answer = choice


if question_found:
    if correct_answer:
        print(f"The correct answer is: {correct_answer}")
    else:
        print("No correct answer found for the given question ID.")
else:
    print("Question ID not found.")

