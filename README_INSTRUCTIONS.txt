=======================
💡 Translator Toolkit Guide (for Windows)
=======================

🟢 Scenario A: You have only videos
1. Put videos in /raw_videos/
2. Install requirements:
   pip install -r requirements.txt
3. Run:
   python translate_whisper.py
4. Output saved in /english_subs/

🟢 Scenario B: You already have Chinese subtitles (.srt)
1. Place them in /chinese_subs/
2. Download Subtitle Edit: https://github.com/SubtitleEdit/subtitleedit/releases
3. Get a Google Translate API key from cloud.google.com
4. Edit translate_all.bat and insert your API key
5. Run:
   translate_all.bat
6. Output will be in /english_subs/

Enjoy automated translation for your series!