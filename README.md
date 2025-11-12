# MCQ Quiz Application 🎯

An interactive Multiple Choice Questions (MCQ) quiz application built with [Chainlit](https://chainlit.io/) and Python, using UV for dependency management.

## Features ✨

- **Interactive Quiz**: Engaging chat-based interface for taking quizzes
- **10 Sample Questions**: Covers various topics including programming, general knowledge, and more
- **Instant Feedback**: Get immediate feedback after each answer
- **Score Tracking**: Track your performance throughout the quiz
- **Detailed Results**: See your final score, percentage, and question-by-question summary
- **Restart Option**: Take the quiz multiple times to improve your score

## Prerequisites 📋

- Python 3.10 or higher
- [UV](https://github.com/astral-sh/uv) package manager

## Installation 🚀

1. **Clone or navigate to the project directory:**
   ```powershell
   cd MCQ-APP
   ```

2. **Install dependencies using UV** (with corporate proxy if needed):
   ```powershell
   $env:HTTP_PROXY="http://127.0.0.1:9000"; $env:HTTPS_PROXY="http://127.0.0.1:9000"; uv sync --native-tls
   ```

   Or without proxy:
   ```powershell
   uv sync
   ```

## Usage 🎮

### Running the Application

Run the Chainlit app using UV:

**With proxy:**
```powershell
$env:HTTP_PROXY="http://127.0.0.1:9000"; $env:HTTPS_PROXY="http://127.0.0.1:9000"; uv run chainlit run app.py
```

**Without proxy:**
```powershell
uv run chainlit run app.py
```

The application will start and open in your default web browser at `http://localhost:8000`

### Taking the Quiz

1. The app will welcome you with instructions
2. Read each question carefully
3. Type the number corresponding to your answer (1, 2, 3, or 4)
4. Press Enter to submit your answer
5. Receive instant feedback with explanations
6. Continue until all questions are answered
7. View your final score and performance summary
8. Type 'restart' to take the quiz again

## Project Structure 📁

```
MCQ-APP/
├── app.py              # Main Chainlit application
├── questions.py        # MCQ questions database
├── pyproject.toml      # UV project configuration
├── uv.lock            # UV lock file
├── README.md          # This file
└── .venv/             # Virtual environment (created by UV)
```

## Customization 🛠️

### Adding Your Own Questions

Edit the `questions.py` file to add or modify questions:

```python
{
    "id": 11,
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer": 0,  # Index of correct option (0-based)
    "explanation": "Explanation for the correct answer."
}
```

### Configuration

You can customize the Chainlit configuration by creating a `.chainlit/config.toml` file or modifying app settings.

## Technologies Used 💻

- **[Python](https://www.python.org/)**: Programming language
- **[Chainlit](https://chainlit.io/)**: Framework for building conversational AI applications
- **[UV](https://github.com/astral-sh/uv)**: Fast Python package installer and resolver

## Development with UV 🔧

UV is a fast Python package installer and resolver. Here are some useful commands:

```powershell
# Add a new package
uv add package-name

# Remove a package
uv remove package-name

# Update dependencies
uv sync

# Run Python scripts
uv run python script.py

# Run commands in the virtual environment
uv run <command>
```

## Troubleshooting 🔍

### Corporate Proxy Issues

If you're behind a corporate proxy, always prefix UV commands with proxy environment variables:

```powershell
$env:HTTP_PROXY="http://127.0.0.1:9000"; $env:HTTPS_PROXY="http://127.0.0.1:9000"; uv <command>
```

### SSL/TLS Certificate Issues

Use the `--native-tls` flag with UV commands:

```powershell
uv add package-name --native-tls
```

## License 📄

This project is open source and available for educational purposes.

## Contributing 🤝

Feel free to fork this project and add your own questions or features!

---

**Happy Quizzing! 🎉**
