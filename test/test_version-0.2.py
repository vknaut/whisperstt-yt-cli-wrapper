import subprocess
import re
import os

def transcribe_audio_cli(audio_path, output_path, model_size="medium", language="", include_timestamps=False):
    command = ["whisper", audio_path, "--model", model_size]
    if language:
        command += ["--language", language]

    # Compile a regular expression pattern to match the timestamp lines
    timestamp_pattern = re.compile(r'^\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]')

    try:
        # Start the Whisper process, capturing stdout for transcription progress
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        
        with open(output_path, "w") as output_file:
            for line in process.stdout:
                # Check if the line matches the timestamp pattern
                if timestamp_pattern.match(line):
                    # Display the timestamp part for progress update
                    print("Processing:", line.strip().split(']')[0] + "]")
                    if include_timestamps:
                        output_file.write(line)
                elif include_timestamps:
                    # Write all lines to the output file if timestamps are to be included
                    output_file.write(line)
                else:
                    # Exclude timestamp lines based on user preference
                    if not line.strip().startswith('['):
                        output_file.write(line)
        
        process.wait()
        
        if process.returncode == 0:
            print("Transcription successful!")
            return True
        else:
            print("Transcription failed.")
            return False
    except Exception as e:
        print(f"Error during transcription: {e}")
        return False

def download_audio(youtube_link, temp_audio_path="temp_audio.mp3"):
    try:
        subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", temp_audio_path, youtube_link], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
        return False
    
def main():
    youtube_link = input("Enter the YouTube link: ")
    output_filename = input("Enter output filename/path: ")
    model = input("Enter model (leave empty for default 'medium'): ") or "medium"
    language = input("Enter language (leave empty for auto-detect): ")
    include_timestamps_input = input("Include timestamps in the output file? (y/n): ")
    include_timestamps = include_timestamps_input.strip().lower() == 'y'
    temp_audio_path = "temp_audio.mp3"
    if download_audio(youtube_link, temp_audio_path):
        if transcribe_audio_cli(temp_audio_path, output_filename, model, language, include_timestamps):
            print("Transcription process completed successfully.")
        else:
            print("An error occurred during the transcription process.")
    else:
        print("Failed to download audio from YouTube.")

    # Clean up the temporary audio file
    try:
        os.remove(temp_audio_path)
    except OSError as e:
        print(f"Error removing temporary audio file: {e}")

if __name__ == "__main__":
    main()
