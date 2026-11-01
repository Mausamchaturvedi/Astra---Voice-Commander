# 🔊 Python Voice Assistant – Time & Date Announcer

A simple Python-based Voice Assistant that automatically greets the user according to the current time of the day and announces the current date and time using Text-to-Speech (TTS).

The project uses Python's `pyttsx3` library to convert text into speech, providing a basic voice interaction experience without requiring an internet connection.

## ✨ Features

- **Automatic Greeting:** Greets the user with Good Morning, Good Afternoon, or Good Evening.
- **Real-Time Clock:** Fetches and displays the current system time.
- **Date Announcement:** Announces the current day, date, month, and year.
- **Text-to-Speech:** Converts text messages into natural computer-generated speech using `pyttsx3`.
- **Voice Configuration:** Automatically selects the first available system voice.
- **Speech Rate Control:** Sets the speech rate to 170 words per minute (engine-dependent).
- **Fallback Mechanism:** Includes a dummy TTS engine if the speech library fails to initialize.
- **Offline Functionality:** Works without an internet connection when the TTS engine is properly configured.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pyttsx3 | Text-to-Speech conversion |
| datetime | Fetching current date and time |
| time | Adding execution delay |

## 📁 Project Structure

```text
Python-Voice-Assistant/
│
├── main.py          # Main Python program
├── README.md        # Project documentation
└── requirements.txt # Project dependencies
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Python-Voice-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd Python-Voice-Assistant
```

### 3. Install Required Library

```bash
pip install pyttsx3
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
pyttsx3
```

**Note:** On some systems, additional speech-engine dependencies may be required. For example, Windows uses the SAPI5 speech engine.

## 🖥️ Sample Output

```text
Today is Sunday, 01 November 2026
The time is 09:30 AM

Speaking: Good Morning, and welcome back sir!
I hope you have a wonderful day.
Today is Sunday, 01 November 2026.
The time is 09:30 AM.
```

The voice assistant will speak the complete greeting, date, and time through your computer's speakers.

*The displayed date and time are examples; actual output depends on your system clock.*

## 🔄 How It Works

1. Imports the required Python libraries.
2. Initializes the Text-to-Speech engine.
3. Selects an available system voice.
4. Checks the current hour using the `datetime` module.
5. Generates an appropriate greeting:
   - Before 12:00 PM – Good Morning
   - Before 5:00 PM – Good Afternoon
   - After 5:00 PM – Good Evening
6. Retrieves the current date and time.
7. Displays the information in the terminal.
8. Converts the complete greeting into speech.
9. Waits for 0.5 seconds before completing execution.

## 🎯 Learning Outcomes

Through this project, I learned:

- Python functions and modular programming.
- Exception handling using `try-except`.
- Working with Python date and time modules.
- Using external Python libraries.
- Implementing Text-to-Speech functionality.
- Handling library initialization failures.
- Creating a simple voice-based application.

## 🚀 Future Enhancements

- Add speech recognition for voice commands.
- Integrate weather updates.
- Add reminders and alarms.
- Implement news announcements.
- Add multiple voice and language options.
- Develop a graphical user interface (GUI).
- Create a smart personal desktop assistant.

## 👨‍💻 Author

**Mausam Chaturvedi**

Python Developer | MCA Student

## 📜 License

This project is open-source and available for educational and learning purposes.

---

⭐ If you find this project useful, consider giving this repository a star!
