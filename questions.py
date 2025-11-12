"""
MCQ Questions Database
Contains questions with multiple choice options and correct answers
"""

QUESTIONS = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": 2,  # Index of correct option (Paris)
        "explanation": "Paris is the capital and most populous city of France."
    },
    {
        "id": 2,
        "question": "Which programming language is known for its use in web development and has a snake as its logo?",
        "options": ["Java", "Python", "JavaScript", "Ruby"],
        "correct_answer": 1,  # Index of correct option (Python)
        "explanation": "Python is known for its snake logo and is widely used in web development, data science, and automation."
    },
    {
        "id": 3,
        "question": "What is the result of 15 + 27?",
        "options": ["41", "42", "43", "44"],
        "correct_answer": 1,  # Index of correct option (42)
        "explanation": "15 + 27 = 42"
    },
    {
        "id": 4,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": 1,  # Index of correct option (Mars)
        "explanation": "Mars is called the Red Planet due to its reddish appearance caused by iron oxide on its surface."
    },
    {
        "id": 5,
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Tech Modern Language",
            "Home Tool Markup Language",
            "Hyperlinks and Text Markup Language"
        ],
        "correct_answer": 0,  # Index of correct option
        "explanation": "HTML stands for Hyper Text Markup Language, which is the standard markup language for creating web pages."
    },
    {
        "id": 6,
        "question": "Which data structure uses LIFO (Last In First Out) principle?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "correct_answer": 1,  # Index of correct option (Stack)
        "explanation": "A Stack follows the LIFO principle where the last element added is the first one to be removed."
    },
    {
        "id": 7,
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
        "correct_answer": 1,  # Index of correct option (O(log n))
        "explanation": "Binary search has a time complexity of O(log n) as it divides the search space in half with each iteration."
    },
    {
        "id": 8,
        "question": "Which of the following is NOT a Python web framework?",
        "options": ["Django", "Flask", "FastAPI", "React"],
        "correct_answer": 3,  # Index of correct option (React)
        "explanation": "React is a JavaScript library for building user interfaces, not a Python web framework."
    },
    {
        "id": 9,
        "question": "What year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "correct_answer": 2,  # Index of correct option (1945)
        "explanation": "World War II ended in 1945 with the surrender of Germany in May and Japan in August."
    },
    {
        "id": 10,
        "question": "Which of these is a NoSQL database?",
        "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"],
        "correct_answer": 2,  # Index of correct option (MongoDB)
        "explanation": "MongoDB is a popular NoSQL database that stores data in flexible, JSON-like documents."
    }
]


def get_question(question_id):
    """Get a specific question by ID"""
    for q in QUESTIONS:
        if q["id"] == question_id:
            return q
    return None


def get_total_questions():
    """Return total number of questions"""
    return len(QUESTIONS)
