import os
import subprocess
import whisper

def download_audio(youtube_link, temp_audio_path="temp_audio.mp3"):
    try:
        subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", temp_audio_path, youtube_link], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
        return False

def transcribe_audio(audio_path, output_path, model_size="medium", language=""):
    try:
        model = whisper.load_model(model_size)
        print(f"Model with {model_size} size loaded. Transcribing now...")

        options = {"language": language} if language else {}
        result = model.transcribe(audio_path, **options)
        with open(output_path, "w") as f:
            f.write(result["text"])
        print("Transcription completed successfully!")
        return True
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return False

def main():
    youtube_link = input("Enter the YouTube link: ")
    output_filename = input("Enter output filename/path: ")
    model = input("Enter model (leave empty for default 'medium'): ") or "medium"
    language = input("Enter language (leave empty for auto-detect): ")

    temp_audio_path = "temp_audio.mp3"
    if download_audio(youtube_link, temp_audio_path):
        if transcribe_audio(temp_audio_path, output_filename, model, language):
            print("Transcription successful!")
        else:
            print("Transcription failed.")
    else:
        print("Failed to download audio.")

    # Clean up the temporary audio file
    try:
        os.remove(temp_audio_path)
    except OSError as e:
        print(f"Error removing temporary audio file: {e}")

if __name__ == "__main__":
    main()
