import os
import sys
import torch
import gc
import whisperx
from datetime import timedelta

def format_time(seconds):
    td = timedelta(seconds=int(seconds))
    # format as HH:MM:SS
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file_path>")
        sys.exit(1)
        
    audio_file = sys.argv[1]
    
    if not os.path.exists(audio_file):
        print(f"Error: File '{audio_file}' does not exist.")
        sys.exit(1)
        
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        print("Warning: HF_TOKEN environment variable not set. Diarization may fail if you haven't accepted the user agreement on HuggingFace.")
        
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    # 1. Transcribe with WhisperX
    batch_size = 16 if device == "cuda" else 8
    compute_type = "float16" if device == "cuda" else "int8"
    
    print("Loading whisper large-v2 model...")
    model = whisperx.load_model("large-v2", device, compute_type=compute_type)
    
    print("Loading audio...")
    audio = whisperx.load_audio(audio_file)
    
    print("Transcribing...")
    result = model.transcribe(audio, batch_size=batch_size)
    
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
    
    # 2. Align whisper output
    print("Aligning output...")
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
    
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
        
    # 3. Assign speaker labels
    print("Running diarization...")
    diarize_model = whisperx.DiarizationPipeline(use_auth_token=hf_token, device=device)
    diarize_segments = diarize_model(audio)
    
    result = whisperx.assign_word_speakers(diarize_segments, result)
    
    # 4. Format and save output
    base_name = os.path.splitext(audio_file)[0]
    output_file = f"{base_name}_transcript.txt"
    
    print(f"Saving transcript to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            time_str = format_time(segment['start'])
            speaker = segment.get("speaker", "UNKNOWN_SPEAKER")
            text = segment.get("text", "").strip()
            f.write(f"{speaker} [{time_str}]: {text}\n")
            
    print("Transcription complete.")

if __name__ == "__main__":
    main()
