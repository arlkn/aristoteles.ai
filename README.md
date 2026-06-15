# Aristoteles AI 🤖

Aristoteles is a dynamic and intelligent terminal assistant running locally, developed using the LangGraph and LM Studio infrastructure. It can dynamically learn its own capabilities (`skills`) and tools (`tools`). All interactions are saved in an Obsidian-like daily `.md` format inside the `memory/` directory.

---

## ⚙️ Features

- **Dynamic Skills:** `.md` files added to the `skills/` directory are automatically read and integrated into Aristoteles' personality.
- **Dynamic Tools:** Python (`.py`) files containing LangChain `@tool` functions added to the `tools/` directory are automatically loaded and made available for use.
- **Beautiful Terminal Interface:** A fluid streaming and elegant experience designed using the Rich library.
- **Expandable Memory:** Conversations are archived day by day in markdown format.

---

## 🛠️ Installation Guide

Follow these steps in order to run the project entirely on your local machine safely.

### 1. Python Installation

The application is written in Python. If you do not have Python installed on your computer:

1. Go to the [Python Download Page](https://www.python.org/downloads/).
2. Download the latest version compatible with your operating system.
3. During installation, **make absolutely sure** the **"Add Python to PATH"** option is checked.

### 2. LM Studio Installation (Local AI Server)

Aristoteles draws its intelligence from LM Studio running on your computer.

1. Go to the [LM Studio Download Page](https://lmstudio.ai/) and download the application.
2. Open the program, search for `gemma-4-e4b` (or any supported model) in the search bar, and download it.
3. Click on the **"Local Server"** tab (the double-arrow icon) from the left menu.
4. In the settings section on the right side:
   - Make sure the server port is set to `1234`.
   - Load the downloaded model.
   - Click the **"Start Server"** button.

> **Note:** If the server starts successfully, it means it is listening for requests at `http://localhost:1234/v1`.

### 3. Setting Up the Project

Open your terminal and navigate to the project directory:

```bash
# Clone the repository
git clone [https://github.com/arlkn/aristoteles.ai.git](https://github.com/arlkn/aristoteles.ai.git)
cd aristoteles.ai

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required Python libraries
pip install -r requirements.txt
```
---

### 4. Awaken Aristoteles!
Once everything is ready, run the following command in your terminal:

Bash
python main.py
Aristoteles will display a brief loading screen upon startup, clear the terminal, and greet you with the chat panel.

🧩 Tool and Skill Development
Adding a New Skill
Create a file named my_rule.md inside the skills/ directory and write your instructions in plain text. Aristoteles will immediately adopt it.

Adding a New Tool
Create a file named weather.py inside the tools/ directory as an example:

Python
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Fetches the weather forecast for the specified city."""
    return f"The weather in {city} is currently wonderful!"
When you restart the application, Aristoteles will have acquired the ability to check the weather!

See you around, may the thoughts be with you! 🦉
