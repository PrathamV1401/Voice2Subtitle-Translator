import whisper
import os
from deep_translator import GoogleTranslator
from pathlib import Path
from time import sleep

input_dir = "raw_videos"
output_dir = "english_subs"
os.makedirs(output_dir, exist_ok=True)

model = whisper.load_model("large")  

def transcribe_and_translate(file_path, txt_output_path, srt_output_path=None):
    print(f"\nProcessing: {file_path}")
    result = model.transcribe(file_path, language="zh-CN")

    translated_lines = []
    srt_lines = []

    for i, segment in enumerate(result['segments'], start=1):
        chinese_text = segment['text'].strip()
        if not chinese_text:
            continue

        try:
            english_text = GoogleTranslator(source='zh-CN', target='en').translate(chinese_text)
            translated_lines.append(english_text)

            if srt_output_path:
                start = format_timestamp(segment['start'])
                end = format_timestamp(segment['end'])
                srt_lines.append(f"{i}\n{start} --> {end}\n{english_text}\n\n")
        except Exception as e:
            print(f"Error translating segment:\n{chinese_text}\n{e}")
            translated_lines.append("[Translation failed]")
            continue

        sleep(1)  # Avoid hitting Google Translate rate limits

    # Save TXT
    with open(txt_output_path, 'w', encoding='utf-8') as f:
        for line in translated_lines:
            f.write(line + "\n")

    # Save SRT
    if srt_output_path:
        with open(srt_output_path, 'w', encoding='utf-8') as f:
            f.writelines(srt_lines)

    print(f"Saved TXT: {txt_output_path}")
    if srt_output_path:
        print(f"Saved SRT: {srt_output_path}")

def format_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{ms:03}"

# Process videos
for file in Path(input_dir).glob("*.mp4"):
    print(f"Found file: {file}")
    base_name = file.stem
    txt_path = Path(output_dir) / f"{base_name}_EN.txt"
    srt_path = Path(output_dir) / f"{base_name}_EN.srt"

    transcribe_and_translate(str(file), str(txt_path), str(srt_path))
    
    
