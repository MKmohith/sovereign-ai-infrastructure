#!/bin/bash
# Sovereign AI Infrastructure - VRAM Swap Script
# Safely transitions 4GB VRAM from Text (Ollama) to Vision (Stable Diffusion)

echo "Initiating VRAM Swap Protocol..."
echo "Stopping Ollama to free up 4GB VRAM..."
sudo systemctl stop ollama

echo "Navigating to Stable Diffusion directory..."
cd ~/stable-diffusion-webui || exit

echo "Applying hardware-optimized memory slicing arguments for GTX 1650..."
export COMMANDLINE_ARGS="--lowvram --no-half --precision full --xformers --no-half-vae --skip-torch-cuda-test --api"

echo "Booting Vision Inference Engine..."
./webui.sh