# YouTube Video Transcription with Whisper
## whisperstt-yt-cli-wrapper
This project enables users to transcribe the audio from YouTube videos using OpenAI's Whisper model, offering an easy-to-use interface for downloading audio, transcribing it, and saving the transcription to a file. It's designed to handle videos of any length, providing accurate transcriptions in a variety of languages.

## Feature Roadmap
- YouTube Audio Download: Downloads the audio track from a specified YouTube video using yt-dlp, a command-line program to download videos from YouTube and other video hosting sites.
- Audio Transcription: Utilizes OpenAI's Whisper, a state-of-the-art speech recognition system, to transcribe the audio to text. Supports multiple languages and dialects with automatic detection or user-specified options.
- Progress Tracking (IN PROGRESS / **NOT IMPLEMENTED YET**): Displays real-time progress of the transcription process, giving users updates on the current processing stage without showing the entire text output.
- Flexible Model Selection: Allows users to choose the Whisper model size that best fits their balance between accuracy and processing time. Supports model sizes from "tiny" to "large".
- Language Selection: Offers automatic language detection by default with the option for users to specify the language for transcription.

## Getting Started
- Clone the Repository: Start by cloning this repository to your local machine.
- Installation: Ensure you have Python installed, then run pip install -r requirements.txt to install the necessary packages, including yt-dlp and openai-whisper.
- Run the Script: Execute the script by running python youtube_transcribe.py from your terminal. Follow the on-screen prompts to enter the YouTube link, output filename/path, model size (optional), and language (optional).
- View the Transcription: Once the transcription process is complete, the transcribed text will be saved to the specified output file. Progress updates during transcription will be displayed in the terminal.

## Prerequisites
* Python 3.7 or newer
* pip for installing Python packages
* Internet connection for downloading YouTube audio and Whisper models'
