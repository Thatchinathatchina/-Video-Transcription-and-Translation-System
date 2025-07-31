Project Description:
 Video Transcription and Translation System

This project processes a video file by extracting its audio, transcribing spoken content into English, and translating the transcript into Tamil. The system is implemented using Python and relies on Whisper AI for speech recognition and Google Translate API for translation.


Technologies Used :

    1)Python     - scripting.
    2)Whisper AI - speech recognition.
    3)MoviePy    - video/audio processing.
    4)Deep-Translator - Google Translate API - language translation.
    5)Google Colab - execution (if running in a cloud environment).


1)Install Required Libraries:-

   .) Installs moviepy 
   .) whisper 
   .) deep-translator .

2)Import Dependencies:-

   .) Moviepy.editor for handling video/audio files.
   .) whisper for speech-to-text transcription.
   .) GoogleTranslator from deep-translator for translating text.
   .) Time - handling delays and measuring execution tim

3)Extract Audio from Video:-

   .) Loads a video file python.mp4.
   .) Extracts the audio and saves it as python_audio.wav.

4)Generate English Subtitle (SRT) using Whisper:-

   .) Loads the whisper model and transcribes the audio.
   .) Saves the transcript in SRT format transcript_en.srt.

5)Translate the Transcript to Tamil:-

   .) Reads the generated English transcript.
   .) Uses GoogleTranslator to convert English subtitles to Tamil.
   .) Saves the Tamil transcript as transcript_ta.srt.
