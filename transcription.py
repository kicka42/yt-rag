import os
import tempfile
import whisper
from pytube import YouTube
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def transcribe_video(youtube_url):
    youtube = YouTube(youtube_url)
    video_title = youtube.title
    safe_title = "".join(char for char in video_title if char.isalnum() or char in " -_")
    transcription_file = f"{safe_title} - Transcription.txt"

    if not os.path.exists(transcription_file):
        print("Starting transcription...")
        audio = youtube.streams.filter(only_audio=True).first()
        whisper_model = whisper.load_model("base")

        with tempfile.TemporaryDirectory() as tmpdir:
            file = audio.download(output_path=tmpdir)
            transcription = whisper_model.transcribe(file, fp16=False)["text"].strip()

            # Save transcription to file (optional)
            with open(transcription_file, 'w') as f:
                f.write(transcription)
                print("Transcription completed.")
    else:
        with open(transcription_file, 'r') as f:
            transcription = f.read()

    return transcription, transcription_file


def split_transcription(file_path, chunk_size=1000, chunk_overlap=20):
    print("Splitting transcription into chunks...")
    loader = TextLoader(file_path)
    text_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    documents = text_splitter.split_documents(text_documents)

    print("Transcription split into chunks.")

    return documents