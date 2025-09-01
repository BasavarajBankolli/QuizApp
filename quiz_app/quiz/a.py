import requests
import random

url = "https://quizapi.io/api/v1/questions"
headers = {
    "X-Api-Key": "Hgpab1trKBwi6Bvy8FTMEwVBEc4pIfUSQ4MOTPWG"  # replace with your real key
}



categories = ["SQL", "Postgres"]
all_questions = []

for cat in categories:
    params = {
        "limit": 5,             # 5 per category
        "category": cat,
        "difficulty": "medium"
    }
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        all_questions.extend(res.json())
    else:
        print("Error:", res.status_code, res.text)

print(all_questions)
random.shuffle(all_questions)

print(f"Fetched {len(all_questions)} questions (5 from each category):")
for i, q in enumerate(all_questions, start=1):
    print(f"{i}. {q['question']} (Category: {q['category']})")
