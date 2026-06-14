---
name: youtube-clipper
description: "AI-powered YouTube video clipper for downloading, clipping segments, and subtitle translation."
---

# youtube-clipper

This skill uses a Python script (`clipper.py`) to download YouTube videos, extract segments, translate subtitles using the Gemini API, and hard-burn the translated subtitles into the video.

## How to use this skill

1. Ensure the Python environment is set up. You should create and use a virtual environment within this skill's directory if one doesn't exist, and install `requirements.txt`.
2. The user must provide a YouTube URL, a start time, an end time, and a target language.
3. You must have `ffmpeg` installed on the system and available in the PATH.
4. Run the script from the skill directory.

**Command usage:**
```bash
python clipper.py --url "<youtube_url>" --start <start_time> --end <end_time> --lang "<target_language>"
```

Example:
```bash
python clipper.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --start 00:00:10 --end 00:00:20 --lang "Indonesian"
```

**Note:** The script relies on the `GEMINI_API_KEY` environment variable. If it is not set in the environment, the script will prompt the user or fail. As an agent, ensure the key is passed or the user is asked for it if it's missing.
