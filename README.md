# Automation of Todo List using Pure Python

This project is an automation of a To-Do list using pure Python. It integrates text-to-speech functionality with task management features to help you keep track of your tasks efficiently. The program uses `pyttsx3` for speech synthesis, and various Python modules to manage tasks and record task timelines.

## Features

- **Task Management**: Add, start, and end tasks.
- **Text-to-Speech**: Provides audio feedback using `pyttsx3`.
- **Task Timeline**: Records start and end times of tasks.
- **Task Sorting**: Sorts tasks based on the time taken to complete.
- **User Interaction**: Prompts the user for inputs to manage tasks.

## Requirements

- Python 3.x
- `pyttsx3` library

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Sivabalan10/Automation-of-Todo-List.git
    ```
2. **Navigate to the Project Directory**:
    ```sh
    cd your-repo-name
    ```
3. **Install the Required Libraries**:
    ```sh
    pip install pyttsx3
    ```

## Usage

1. **Prepare the Input Files**:
    - `user_task.txt`: Contains a comma-separated list of tasks.
    - `newupd.txt`: Contains the index of the current task to start.
    - `timeline.txt`: Used to record the start and end times of tasks.
    - `logicse.txt`: Used to track whether a task is in progress.
    - `current_task.txt`: Keeps a record of the current task.
    - `time_taken.txt`: Records the time taken for each task.
    - `Learned_data.txt`: Stores sorted tasks based on the time taken.

2. **Run the Script**:
    ```sh
    python your-script-name.py
    ```
3. **Follow the Prompts**:
    - The script will prompt you to start or end tasks, and provide audio feedback.

## Code Explanation

### Initialization

```python
import datetime
import pyttsx3
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
