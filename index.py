import moviepy.editor as mp
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import whisper
from deep_translator import GoogleTranslator


video_path = "/content/Instructor.mp4"
audio_path = "/content/audio.wav"
srt_en_path = "/content/transcript_en.srt"
srt_tamil_path = "/content/transcript_ta.srt"


video = mp.VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)


ckpt = "openai/whisper-small.en"
tokenizer = WhisperProcessor.from_pretrained(ckpt)
model = WhisperForConditionalGeneration.from_pretrained(ckpt)

new_tokens = ["payil demo", "payil", "payil.app", "technogamesinc.com", "payil demo"]
new_tokens = set(new_tokens) - set(tokenizer.tokenizer.get_vocab().keys())
if new_tokens:
    tokenizer.tokenizer.add_tokens(list(new_tokens))
    model.resize_token_embeddings(len(tokenizer.tokenizer))

result = whisper.load_model("medium").transcribe(audio_path, initial_prompt=", ".join(new_tokens))


with open(srt_en_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]

        f.write(f"{i+1}\n")
        f.write(f"{start:.2f} --> {end:.2f}\n")
        f.write(f"{text}\n\n")


translator = GoogleTranslator(source="en", target="ta")
with open(srt_en_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

translated_lines = []
for line in lines:
    if "-->" not in line and not line.strip().isdigit():
        try:
            translated_text = translator.translate(line.strip())
            translated_lines.append(translated_text + "\n") if translated_text else translated_lines.append(line)
        except Exception as e:
            print(f"Error translating line: {line.strip()} - {e}")
            translated_lines.append(line)
    else:
        translated_lines.append(line)

translator = GoogleTranslator(source="en", target="ta")
with open(srt_en_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

translated_lines = []
for line in lines:
    if "-->" not in line and not line.strip().isdigit():
        try:
            translated_text = translator.translate(line.strip())
            translated_lines.append(translated_text + "\n") if translated_text else translated_lines.append(line)
        except Exception as e:
            print(f"Error translating line: {line.strip()} - {e}")
            translated_lines.append(line)
    else:
        translated_lines.append(line)


with open(srt_tamil_path, "w", encoding="utf-8") as f:
    f.writelines(translated_lines)

files.download(srt_en_path)
files.download(srt_tamil_path)