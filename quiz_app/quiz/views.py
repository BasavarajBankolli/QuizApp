# import requests
# from django.shortcuts import render


# def home(request):
#     # Just render the home page with domains
#     return render(request, "quiz/index.html")

# API_URL = "https://quizapi.io/api/v1/questions"
# API_KEY = "Hgpab1trKBwi6Bvy8FTMEwVBEc4pIfUSQ4MOTPWG" 

# def quiz_view(request):
#     if request.method == "POST":
#         # Calculate Score
#         score = 0
#         questions = request.session.get("questions", [])
#         for i, q in enumerate(questions):
#             user_answer = request.POST.get(f"q{i+1}")
#             if user_answer and q["correct_answers"].get(f"{user_answer}_correct") == "true":
#                 score += 1

#         return render(request, "quiz/result.html", {
#             "score": score,
#             "total": len(questions)
#         })

#     else:
#         # Fetch questions from API (Programming → category 7)
#         response = requests.get(
#             API_URL,
#             headers={"X-Api-Key": API_KEY},
#             params = {
#                 "limit": 10,        # number of questions
#                 "category": "code",
#                 "difficulty": "easy"  # valid category name (API expects 'Code' instead of 'Programming')
#             }
#         )

#         questions = response.json() if response.status_code == 200 else []

#         # Store in session for checking later
#         request.session["questions"] = questions

#         return render(request, "quiz/quiz.html", {"questions": questions})


# def domain_view(request, id):
#     # Here, 'id' comes from the URL (e.g., /domain/1/)
#     print("Selected Domain ID:", id)  # for debugging
#     quiz_view(id)
#     return render(request, 'quiz/quiz.html', {"domain_id": id})    


# def quiz_view(request):
#     """
#     Handles quiz submission and scoring.
#     """
#     if request.method == "POST":
#         questions = request.session.get("questions", [])
#         score = 0

#         for i, q in enumerate(questions):
#             user_answer = request.POST.get(f"q{i+1}")
#             if user_answer and q["correct_answers"].get(f"{user_answer}_correct") == "true":
#                 score += 1

#         return render(request, "quiz/result.html", {
#             "score": score,
#             "total": len(questions),
#         })

#     # If someone accesses quiz_view directly → redirect home




# / # def fetch_questions(id, limit=10, difficulty="easy"):
    
#     # web : Nodejs, React, Next.js, HTML
#     # programming : Code
#     # devops : Devops, Docker
#     # sql: SQL

#     if id == 1:
#         limit = 3
    
#     elif id == 3:
#         limit = 5
    
#     domains = {1:['Nodejs', 'React', 'Next.js', 'HTML'], 2:['code'], 3:['devops', 'Docker'], 4: ['SQL']}
#     domain = domains[id]

#     questions = []    
#     i = 0
#     while i < len(domain):
#         diff = requests.get(
#             API_URL,
#             headers={"X-Api-Key": API_KEY},
#             params= {
#                 "limit": limit,
#                 "category": domain[i],
#                 # "difficulty": difficulty,
#             }
#         )

#         i += 1
#         if diff.status_code != 200:
#             limit += 3
#             continue

#         print(diff)
#         questions.extend(diff)
#         print(i)
#     questions = questions[:10]
#     random.shuffle(questions)
#     print(questions)
#     print()
#     return questions if questions else []


# def domain_view(request, id):
#     """
#     Handles domain selection. 
#     Example: /domain/1/ → fetches questions for that domain.
#     """

#     questions = fetch_questions(id)
#     return render(request, "quiz/quiz.html", {"questions":questions}) \





    

'''

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

import random

# Quiz API info
API_URL = "https://quizapi.io/api/v1/questions"
API_KEY = "--"   


def home(request):
    """Home page with domain selection"""
    
    return render(request, "quiz/index.html")



def fetch_questions(id, limit=10, difficulty="easy"):
    domains = {
        1: ["Node.js", "React", "Next.js", "HTML"],
        2: ["Code"],
        3: ["DevOps", "Docker"],
        4: ["SQL"],
    }
    domain = domains[id]

    questions = [{'id': 10102, 'question': 'A team needs to implement Terraform for ephemeral development environments. Which approach would be most efficient?', 'description': 'Implementing ephemeral environments with Terraform.', 'answers': {'answer_a': 'Create permanent environments for all developers', 'answer_b': 'Implement environment modules with state isolation and cleanup automation', 'answer_c': 'Share a single development environment among all developers', 'answer_d': 'Give developers cloud console access to create resources', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'true', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': 'Environment modules with state isolation and cleanup automation provide the most efficient ephemeral environment approach. Environment modules deploy consistent developer environments. State isolation prevents interference between environments. Cleanup automation destroys unused environments to control costs. This approach provides developers with dedicated environments without interference, ensures consistent environment configuration across the team, automatically manages the lifecycle of temporary resources, eliminates manual cleanup effort, and creates an efficient system for managing development environments at scale.', 'tip': None, 'tags': [{'name': 'Terraform'}], 'category': 'DevOps', 'difficulty': 'Medium'}, {'id': 10129, 'question': 'Your team needs to implement logging for a containerized application deployed across multiple hosts. Which approach would be most effective?', 'description': 'Implementing effective logging for containerized applications.', 'answers': {'answer_a': 'Write all logs to local files inside each container', 'answer_b': 'Implement a centralized logging architecture with container-aware drivers', 'answer_c': 'Use volumes to store logs on the host', 'answer_d': 'Disable logging to improve performance', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'true', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': 'A centralized logging architecture with container-aware drivers provides the most effective logging solution. Container-aware logging drivers (like fluentd, syslog, or json-file with a collector) capture logs from stdout/stderr across all containers. Centralization in systems like Elasticsearch, Splunk, or Loki enables cross-container correlation, searching, and alerting. This approach preserves logs when containers are removed, scales across multiple hosts, maintains consistent logging structure across services, enables comprehensive filtering and searching, and creates a complete observability solution without sacrificing container portability.', 'tip': None, 'tags': [{'name': 'Docker'}], 'category': 'DevOps', 'difficulty': 'Medium'}, {'id': 1150, 'question': 'Which OpenShift component allows network communication between pods across different nodes?', 'description': None, 'answers': {'answer_a': 'Cluster Network', 'answer_b': 'Service', 'answer_c': 'Route Manager', 'answer_d': 'Ingress Controller', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'true', 'answer_b_correct': 'false', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': 'answer_a', 'explanation': None, 'tip': None, 'tags': [{'name': 'Openshift'}], 'category': 'DevOps', 'difficulty': 'Medium'}, {'id': 10146, 'question': 'A containerized application needs to access sensitive host resources. Which approach would provide the necessary access while minimizing security risks?', 'description': 'Securely accessing host resources from containers.', 'answers': {'answer_a': 'Run all containers with the --privileged flag', 'answer_b': 'Implement selective capability granting with minimal bind mounts', 'answer_c': 'Use host networking mode for all containers', 'answer_d': 'Allow all containers to access all host resources', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'true', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': 'Selective capability granting with minimal bind mounts follows the principle of least privilege for host access. Selective capabilities (using --cap-add for specific capabilities rather than --privileged) provide only the exact permissions needed. Minimal bind mounts with narrow scopes limit filesystem access to only required directories. This targeted approach gives containers necessary access without excessive permissions, maintains container isolation where possible, follows security best practices for container deployment, minimizes the damage if containers are compromised, and creates a secure foundation even when host resource access is required.', 'tip': None, 'tags': [{'name': 'Docker'}], 'category': 'DevOps', 'difficulty': 'Hard'}, {'id': 1364, 'question': 'How does `openshift-kube-apiserver` handle API request limits to prevent overload?', 'description': 'API request limits help protect the server from being overwhelmed by too many requests.', 'answers': {'answer_a': 'It limits requests per user', 'answer_b': 'It uses token-based quotas', 'answer_c': 'It applies request rate limiting', 'answer_d': 'It scales up automatically', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'false', 'answer_c_correct': 'true', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': '`openshift-kube-apiserver` applies request rate limiting to manage API request load and prevent overload.', 'tip': None, 'tags': [{'name': 'Openshift'}], 'category': 'DevOps', 'difficulty': 'Hard'}, {'id': 897, 'question': 'Replication Controllers and Deployment Controllers are part of', 'description': None, 'answers': {'answer_a': 'API Controller Manager', 'answer_b': 'Etcd manager', 'answer_c': 'Master Controller Manager', 'answer_d': 'Kubeadm', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'false', 'answer_c_correct': 'true', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': None, 'tip': None, 'tags': [{'name': 'Kubernetes'}], 'category': 'DevOps', 'difficulty': 'Easy'}, {'id': 10120, 'question': 'A team needs to improve the quality and consistency of their Terraform code. Which development approach would be most effective?', 'description': 'Implementing quality control for Terraform code.', 'answers': {'answer_a': 'Let each developer use their preferred style', 'answer_b': 'Implement automated linting with pre-commit hooks and style guides', 'answer_c': 'Perform visual reviews of code formatting', 'answer_d': 'Focus only on functional correctness', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'true', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': 'Automated linting with pre-commit hooks and style guides provides the most effective quality control. Linting tools automatically enforce style and best practices. Pre-commit hooks catch issues before they enter version control. Style guides establish team standards. This approach ensures consistent code formatting and structure across the team, catches common errors and anti-patterns automatically, provides immediate feedback during development, reduces code review overhead by automating style checks, and creates higher quality infrastructure code that follows established best practices.', 'tip': None, 'tags': [{'name': 'Terraform'}], 'category': 'DevOps', 'difficulty': 'Medium'}, {'id': 1019, 'question': 'Is Kubernetes open-source?', 'description': None, 'answers': {'answer_a': 'True', 'answer_b': 'False', 'answer_c': None, 'answer_d': None, 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'true', 'answer_b_correct': 'false', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': None, 'tip': None, 'tags': [{'name': 'Kubernetes'}], 'category': 'DevOps', 'difficulty': 'Easy'}, {'id': 10175, 'question': 'Your team is struggling with inconsistent Docker behavior across different environments due to version mismatches. Which approach would most effectively address this issue?', 'description': 'Managing Docker version consistency across environments.', 'answers': {'answer_a': 'Allow each environment to use different Docker versions', 'answer_b': 'Implement version pinning with compatibility testing and controlled upgrades', 'answer_c': 'Always use the latest Docker version everywhere', 'answer_d': "Write applications that don't depend on Docker features", 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'true', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': "Version pinning with compatibility testing and controlled upgrades provides the most effective version management. Version pinning ensures the same Docker version across environments. Compatibility testing verifies application behavior before upgrading. Controlled upgrades roll out version changes systematically across environments. This disciplined approach prevents unexpected behavior due to version differences, catches compatibility issues before they reach production, provides a consistent foundation across development and production, enables proper testing of Docker upgrades, and creates a stable and predictable container platform despite Docker's rapid evolution.", 'tip': None, 'tags': [{'name': 'Docker'}], 'category': 'DevOps', 'difficulty': 'Medium'}, {'id': 1427, 'question': 'How can you remove an unused Docker image from your system?', 'description': 'Removing unused images frees up space on the local machine.', 'answers': {'answer_a': 'docker rm <image_id>', 'answer_b': 'docker rmi <image_id>', 'answer_c': 'docker delete <image_id>', 'answer_d': 'docker remove <image_id>', 'answer_e': None, 'answer_f': None}, 'multiple_correct_answers': 'false', 'correct_answers': {'answer_a_correct': 'false', 'answer_b_correct': 'true', 'answer_c_correct': 'false', 'answer_d_correct': 'false', 'answer_e_correct': 'false', 'answer_f_correct': 'false'}, 'correct_answer': None, 'explanation': 'The `docker rmi <image_id>` command removes a Docker image from the local machine.', 'tip': None, 'tags': [{'name': 'Docker'}], 'category': 'DevOps', 'difficulty': 'Medium'}]
    
    for cat in domain:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"limit": limit, "category": cat},
        )

        if response.status_code == 200:
            data = response.json()
            questions.extend(data)

    questions = questions[:2]   
    random.shuffle(questions)
    
    return questions


def results_view(request):
    questions = request.session.get("questions", [])
    user_answers = request.session.get("user_answers", {})

    score = 0
    results = []

    for q in questions:
        qid = q["id"]
        correct_key = None
        for k, v in q["correct_answers"].items():
            if v == "true":
                correct_key = k.replace("_correct", "")
                break

        # store qid in str form
        user_choice = user_answers.get(str(qid))

        is_correct = user_choice == correct_key
        if is_correct:
            score += 1

        results.append({
            "question": q["question"],
            "user_answer": q["answers"].get(user_choice),
            "correct_answer": q["answers"].get(correct_key),
            "is_correct": is_correct
        })

    return render(
        request,
        "quiz/result.html",
        {"result": results, "score": score, "total": len(questions)}
    )


def domain_view(request, id):
    user_answers = {}
    if request.method == "POST":
        # Get the stored questions from session
        questions = request.session.get("questions", [])
        user_answers = {}

        for q in questions:
            selected = request.POST.get(f"q{q['id']}")
            user_answers[q["id"]] = selected

        
        request.session["user_answers"] = user_answers

        return redirect("result")   

    # fetch_questions
    questions = fetch_questions(id)
    request.session["questions"] = questions




    return render(request, "quiz/quiz.html", {"questions": questions})
'''

import random
import requests
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest

API_URL = "https://quizapi.io/api/v1/questions"
API_KEY = "Hgpab1trKBwi6Bvy8FTMEwVBEc4pIfUSQ4MOTPWG"

# Session-flag names
FLAG_CAN_ACCESS = "can_access_domain"
FLAG_IN_PROGRESS = "quiz_in_progress"
FLAG_COMPLETED = "quiz_completed"
ACTIVE_DOMAIN_ID = "active_domain_id"

def home(request):
    """
    Render home. IMPORTANT: do NOT set CAN_ACCESS here.
    Instead clear any previous flags so visiting home doesn't grant permission.
    """
    request.session.pop(FLAG_CAN_ACCESS, None)
    request.session.pop(FLAG_IN_PROGRESS, None)
    request.session.pop(FLAG_COMPLETED, None)
    request.session.pop(ACTIVE_DOMAIN_ID, None)
    request.session.pop("questions", None)
    request.session.pop("user_answers", None)
    return render(request, "quiz/index.html")


@require_POST
def start_domain(request, id):
    """
    Called when the user clicks a button on home.
    This sets the one-time permission and redirects to domain_view.
    """
    # optional: validate id against your allowed domain list
    request.session[FLAG_CAN_ACCESS] = True
    request.session[ACTIVE_DOMAIN_ID] = id
    request.session.modified = True
    return redirect("domain_view", id=id)

def fetch_questions(id, limit=10, difficulty="easy"):
    domains = {
        1: ["Node.js", "React", "Next.js", "HTML"],
        2: ["Code"],
        3: ["DevOps", "Docker"],
        4: ["SQL"],
    }
    domain = domains[id]

    questions = []    
    for cat in domain:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"limit": limit, "category": cat},
        )

        if response.status_code == 200:
            data = response.json()
            questions.extend(data)

    questions = questions[:10]   
    random.shuffle(questions)
    
    return questions



@never_cache
def domain_view(request, id):
    # GET: only allow if start_domain set the flag
    if request.method == "GET":
        if not request.session.get(FLAG_CAN_ACCESS, False):
            return redirect("home")

        # consume the permission and mark in-progress
        request.session[FLAG_CAN_ACCESS] = False
        request.session[FLAG_IN_PROGRESS] = True
        request.session[ACTIVE_DOMAIN_ID] = id

        questions = fetch_questions(id)
        if not questions:
            return HttpResponseBadRequest("Invalid domain or no questions available.")

        request.session["questions"] = questions
        request.session.pop("user_answers", None)
        request.session.modified = True

        response = render(request, "quiz/quiz.html", {"questions": questions})
        response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response["Pragma"] = "no-cache"
        return response

    # POST: submit answers
    if request.method == "POST":
        if not request.session.get(FLAG_IN_PROGRESS, False):
            return redirect("home")

        questions = request.session.get("questions", [])
        if not questions:
            return redirect("home")

        user_answers = {}
        for q in questions:
            selected = request.POST.get(f"q{q['id']}")
            user_answers[str(q["id"])] = selected

        request.session["user_answers"] = user_answers
        request.session[FLAG_IN_PROGRESS] = False
        request.session[FLAG_COMPLETED] = True
        request.session.modified = True

        return redirect("result")

    return redirect("home")


@never_cache
def results_view(request):
    if not request.session.get(FLAG_COMPLETED, False):
        return redirect("home")

    questions = request.session.get("questions", [])
    user_answers = request.session.get("user_answers", {})

    if not questions:
        return redirect("home")

    score = 0
    results = []
    for q in questions:
        qid = q["id"]
        correct_key = None
        for k, v in q.get("correct_answers", {}).items():
            if v == "true":
                correct_key = k.replace("_correct", "")
                break

        user_choice = user_answers.get(str(qid))
        is_correct = user_choice == correct_key
        if is_correct:
            score += 1

        results.append({
            "question": q.get("question"),
            "user_answer": (q.get("answers") or {}).get(user_choice),
            "correct_answer": (q.get("answers") or {}).get(correct_key),
            "is_correct": is_correct
        })

    # clear state
    request.session.pop("questions", None)
    request.session.pop("user_answers", None)
    request.session.pop(FLAG_COMPLETED, None)
    request.session.pop(FLAG_IN_PROGRESS, None)
    request.session.pop(ACTIVE_DOMAIN_ID, None)
    request.session.modified = True

    response = render(request, "quiz/result.html", {"result": results, "score": score, "total": len(questions)})
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    return response
