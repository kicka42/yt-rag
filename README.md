# RAG YouTube Transcription and QA

This repository contains a Retrieval-Augmented Generation (RAG) application built using Python, LangChain, and the OpenAI API. The application transcribes YouTube videos and allows users to ask questions based on the transcriptions.

## Features

- **YouTube Video Transcription**: Transcribes the audio from YouTube videos.
- **Question Answering**: Allows users to ask questions based on the transcriptions.
- **Retrieval-Augmented Generation**: Utilizes retrieval techniques to enhance the generation capabilities of the OpenAI API.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kicka42/yt-rag.git
    cd yt-rag
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py YOUTUBE_URL
    ```

2. **Ask Questions Based on Transcription**:
    ```
   Talk with... Andrej Karpathy Tesla AI Self-Driving Optimus Aliens and AGI  - Transcription.txt
   (type 'quit' to exit)
   Question: what is AI?
   Answer: AI stands for artificial intelligence, which refers to the simulation of human intelligence processes by machines, especially computer systems. It involves the development of algorithms and models that enable machines to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, perception, and language understanding.
   Question: what is AGI?
   Answer: AGI stands for Artificial General Intelligence.
   Question: ...
    ```

## Project Structure

- `main.py`: The main entry point for the application.
- `pipeline.py`: Contains the logic for handling the QA pipeline.
- `store.py`: Manages the storage of transcriptions and other data.
- `openai_api.py`: Handles interactions with the OpenAI API.
- `transcription.py`: Contains functions for transcribing YouTube videos.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.