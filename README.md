```markdown
# Jeevan Voice Assistant

Jeevan is a desktop voice assistant built in Python that can perform various tasks through voice commands. It utilizes several libraries, including speech recognition, text-to-speech, and Dialogflow for conversational AI.

## Features

- **Voice Commands:** Control the assistant using voice commands.
- **Time and Date:** Get the current time and date.
- **Screenshot Capture:** Take screenshots and save them in the user's Pictures folder.
- **Wikipedia Search:** Search for information on Wikipedia and read summaries aloud.
- **YouTube Search:** Open YouTube and search for videos based on user queries.
- **Music Playback:** Play music from the user's local music directory.
- **Dialogflow Integration:** Ask questions to Dialogflow and get AI-generated responses.
- **Animated GIF Display:** Display an animated GIF as a visual companion to the assistant.

## Requirements

- Python 3.x
- Libraries:
  - `openai`
  - `pyttsx3`
  - `datetime`
  - `speech_recognition`
  - `wikipedia`
  - `webbrowser`
  - `os`
  - `random`
  - `pyautogui`
  - `PIL`
  - `google-cloud-dialogflow`
  
You can install the required libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia webbrowser pyautogui Pillow google-cloud-dialogflow
```

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Set up Google Cloud credentials for Dialogflow. Create a service account key in the Google Cloud Console, download the JSON file, and place it in the project directory. Update the path in the script accordingly:

   ```python
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_file.json"
   ```

3. Customize the GIF path if necessary. Ensure the GIF file is placed in a folder named `GIF` in the project directory.

## Usage

Run the assistant by executing the Python script:

```bash
python jeevan_assistant.py
```

Speak commands to the assistant, such as:

- "What time is it?"
- "Open YouTube"
- "Play music"
- "Ask GPT about [your question]"

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

- **Mugesh Kumar**
```

### Notes
- Replace `<repository_url>` and `<repository_directory>` with the actual URL of your repository and the directory name.
- You may also want to add a section for contributions or a list of known issues, depending on your project's needs. Let me know if you’d like any changes or additional information!
