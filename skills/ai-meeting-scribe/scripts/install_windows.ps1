$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$venvDir = Join-Path $scriptDir ".venv"

Write-Host "Creating Python virtual environment..."
python -m venv $venvDir

Write-Host "Activating virtual environment..."
$activateScript = Join-Path $venvDir "Scripts\Activate.ps1"
if (-Not (Test-Path $activateScript)) {
    Write-Error "Failed to find activate script. Is Python installed?"
    exit 1
}

. $activateScript

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "Installing PyTorch with CUDA 11.8 support..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

Write-Host "Installing whisperx from git..."
pip install git+https://github.com/m-bain/whisperx.git

Write-Host "Installation complete!"
Write-Host "To run the transcriber:"
Write-Host "1. Set your HuggingFace token: `$env:HF_TOKEN=`"your_token_here`""
Write-Host "2. Run the script: python transcribe.py path\to\audio.mp3"
