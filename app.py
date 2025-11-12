"""
MCQ Application using Chainlit
An interactive multiple-choice quiz application
"""

import chainlit as cl
from questions import QUESTIONS, get_question, get_total_questions


# Store user session data
user_data = {}


@cl.on_chat_start
async def start():
    """Initialize the quiz when chat starts"""
    # Initialize user data
    user_data[cl.user_session.get("id")] = {
        "current_question": 0,
        "score": 0,
        "answers": []
    }
    
    # Welcome message
    await cl.Message(
        content=f"""# 🎯 Welcome to the MCQ Quiz App!

This quiz contains **{get_total_questions()} questions**.

**Instructions:**
- Read each question carefully
- Type the number of your answer (1, 2, 3, or 4)
- You'll get immediate feedback
- At the end, you'll see your final score

Ready to start? Let's begin! 🚀
"""
    ).send()
    
    # Send first question
    await send_question()


async def send_question():
    """Send current question to the user"""
    session_id = cl.user_session.get("id")
    current_q_index = user_data[session_id]["current_question"]
    
    if current_q_index >= get_total_questions():
        await show_results()
        return
    
    question = QUESTIONS[current_q_index]
    
    # Format question with options
    options_text = "\n".join([
        f"**{i+1}.** {option}" 
        for i, option in enumerate(question["options"])
    ])
    
    message = f"""### Question {current_q_index + 1} of {get_total_questions()}

**{question["question"]}**

{options_text}

*Type the number of your answer (1-{len(question["options"])})*
"""
    
    await cl.Message(content=message).send()


@cl.on_message
async def main(message: cl.Message):
    """Handle user's answer"""
    session_id = cl.user_session.get("id")
    
    if session_id not in user_data:
        await cl.Message(content="Please refresh the page to start the quiz.").send()
        return
    
    current_q_index = user_data[session_id]["current_question"]
    
    # Check if quiz is completed
    if current_q_index >= get_total_questions():
        await cl.Message(
            content="Quiz completed! Type 'restart' to take the quiz again."
        ).send()
        
        if message.content.lower() == "restart":
            user_data[session_id] = {
                "current_question": 0,
                "score": 0,
                "answers": []
            }
            await send_question()
        return
    
    question = QUESTIONS[current_q_index]
    
    # Validate user input
    try:
        user_answer = int(message.content.strip()) - 1  # Convert to 0-indexed
        
        if user_answer < 0 or user_answer >= len(question["options"]):
            await cl.Message(
                content=f"⚠️ Please enter a number between 1 and {len(question['options'])}"
            ).send()
            return
            
    except ValueError:
        await cl.Message(
            content="⚠️ Please enter a valid number for your answer."
        ).send()
        return
    
    # Check if answer is correct
    is_correct = user_answer == question["correct_answer"]
    
    if is_correct:
        user_data[session_id]["score"] += 1
        feedback = f"""✅ **Correct!**

{question["explanation"]}
"""
    else:
        correct_option = question["options"][question["correct_answer"]]
        feedback = f"""❌ **Incorrect!**

The correct answer is: **{correct_option}**

{question["explanation"]}
"""
    
    # Store user's answer
    user_data[session_id]["answers"].append({
        "question_id": question["id"],
        "user_answer": user_answer,
        "correct": is_correct
    })
    
    # Send feedback
    await cl.Message(content=feedback).send()
    
    # Move to next question
    user_data[session_id]["current_question"] += 1
    
    # Small delay before next question
    await cl.sleep(1)
    
    # Send next question or show results
    await send_question()


async def show_results():
    """Display final quiz results"""
    session_id = cl.user_session.get("id")
    score = user_data[session_id]["score"]
    total = get_total_questions()
    percentage = (score / total) * 100
    
    # Determine performance level
    if percentage >= 90:
        performance = "Outstanding! 🌟"
        emoji = "🏆"
    elif percentage >= 75:
        performance = "Great job! 👏"
        emoji = "🎉"
    elif percentage >= 50:
        performance = "Good effort! 👍"
        emoji = "😊"
    else:
        performance = "Keep practicing! 💪"
        emoji = "📚"
    
    results = f"""# {emoji} Quiz Complete!

## Your Results:
- **Score:** {score} out of {total}
- **Percentage:** {percentage:.1f}%
- **Performance:** {performance}

---

### Question Summary:
"""
    
    # Add summary of each question
    for i, answer_data in enumerate(user_data[session_id]["answers"]):
        status = "✅" if answer_data["correct"] else "❌"
        results += f"\n{status} Question {i+1}"
    
    results += "\n\n---\n\n*Type 'restart' to take the quiz again!*"
    
    await cl.Message(content=results).send()


if __name__ == "__main__":
    cl.run()
