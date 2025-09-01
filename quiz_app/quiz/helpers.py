def calculate_score(questions, post_data):
    score = 0
    for i, q in enumerate(questions):
        user_answer = post_data.get(f"q{i+1}")
        if user_answer and q["correct_answers"].get(f"{user_answer}_correct") == "true":
            score += 1
    return score
