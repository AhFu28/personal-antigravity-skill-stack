import argparse
import subprocess
import os
import sys
from google import genai

def download_video_and_subs(url, start, end, out_dir):
    # We download the video and best available subs
    # Using yt-dlp's --download-sections
    video_path = os.path.join(out_dir, "raw_video.mp4")
    
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "-f", "bestvideo[ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/mp4",
        "--write-auto-subs",
        "--write-subs",
        "--sub-langs", "en.*", 
        "--download-sections", f"{start}-{end}",
        "-o", os.path.join(out_dir, "raw_video.%(ext)s"),
        url
    ]
    
    print(f"Running yt-dlp: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    
    # Find the downloaded sub file (yt-dlp names it raw_video.en.vtt or similar)
    downloaded_sub = None
    for f in os.listdir(out_dir):
        if f.startswith("raw_video.") and f.endswith(".vtt"):
            downloaded_sub = os.path.join(out_dir, f)
            break
            
    if not downloaded_sub:
        print("Warning: No subtitles found for this section. Proceeding without subtitles.")
        
    return video_path, downloaded_sub

def translate_subs(sub_path, target_lang):
    if not sub_path or not os.path.exists(sub_path):
        return None
        
    client = genai.Client()
    
    with open(sub_path, "r", encoding="utf-8") as f:
        vtt_content = f.read()
        
    prompt = f"""
You are a professional translator. Translate the text in this WebVTT subtitle file to {target_lang}.
CRITICAL INSTRUCTIONS:
- Preserve the exact WebVTT format.
- DO NOT alter any timestamps (e.g., 00:00:10.000 --> 00:00:15.000).
- DO NOT add extra commentary, markdown formatting, or notes.
- Output ONLY the valid WebVTT content.

Original VTT:
{vtt_content}
"""

    print(f"Translating subtitles to {target_lang}...")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    translated_content = response.text.strip()
    if translated_content.startswith("```"):
        lines = translated_content.split("\n")
        if lines[0].startswith("```"): lines = lines[1:]
        if lines[-1].startswith("```"): lines = lines[:-1]
        translated_content = "\n".join(lines).strip()
        
    out_sub = os.path.join(os.path.dirname(sub_path), "translated.vtt")
    with open(out_sub, "w", encoding="utf-8") as f:
        f.write(translated_content)
        
    print(f"Saved translated subtitles to {out_sub}")
    return out_sub

def burn_subtitles(video_path, sub_path, out_dir):
    out_video = os.path.join(out_dir, "final_clip.mp4")
    
    if not sub_path:
        print("No subtitles to burn. Just renaming video.")
        os.rename(video_path, out_video)
        return out_video
        
    # Relative path trick for FFmpeg on Windows to avoid drive letter colon escaping
    sub_name = os.path.basename(sub_path)
    
    cmd = [
        "ffmpeg",
        "-y",
        "-i", os.path.basename(video_path),
        "-vf", f"subtitles={sub_name}",
        "-c:a", "copy",
        os.path.basename(out_video)
    ]
    
    print(f"Running FFmpeg: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=out_dir, check=True)
    return out_video

def main():
    parser = argparse.ArgumentParser(description="YouTube Clipper & Translator")
    parser.add_argument("--url", required=True)
    parser.add_argument("--start", required=True, help="Start time (e.g. 00:00:10)")
    parser.add_argument("--end", required=True, help="End time (e.g. 00:00:20)")
    parser.add_argument("--lang", required=True, help="Target language")
    
    args = parser.parse_args()
    
    if "GEMINI_API_KEY" not in os.environ:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)
        
    out_dir = os.path.join(os.getcwd(), "output_clip")
    os.makedirs(out_dir, exist_ok=True)
    
    video_path, sub_path = download_video_and_subs(args.url, args.start, args.end, out_dir)
    translated_sub_path = translate_subs(sub_path, args.lang)
    final_video = burn_subtitles(video_path, translated_sub_path, out_dir)
    
    print(f"\nSuccess! Final clipped and translated video saved to: {final_video}")

if __name__ == "__main__":
    main()
