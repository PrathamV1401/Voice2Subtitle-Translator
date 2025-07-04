@echo off
setlocal enabledelayedexpansion
set SE_PATH="C:\SubtitleEdit\SubtitleEdit.exe"
set INPUT_DIR=chinese_subs
set OUTPUT_DIR=english_subs
mkdir %OUTPUT_DIR%

for %%f in (%INPUT_DIR%\*.srt) do (
    echo Translating %%f...
    %SE_PATH% /translate /input:"%%f" /output:"%OUTPUT_DIR%\%%~nf_EN.srt" /from:zh /to:en /api:Google /apikey:YOUR_GOOGLE_API_KEY
)
echo Done!
pause