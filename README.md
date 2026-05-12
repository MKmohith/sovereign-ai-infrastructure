# Sovereign AI Infrastructure: Secure Access Control with Personalized Voice Synthesis

A secure, privacy-preserving edge AI environment featuring local LLM execution, strict Role-Based Access Control (RBAC), and offline multimodal interaction (Text, Image, and Voice), optimized for resource-constrained hardware.

## 🚀 Project Overview
Traditional cloud AI systems inherently compromise data privacy and lack granular user-level governance. This project demonstrates an **Edge-Native Sovereign AI** architecture. By combining Role-Based Access Control (RBAC) with hardware-optimized inference, this system ensures organizations (like healthcare or educational institutions) maintain absolute control over their private data and the behavioral outputs of the AI, without requiring expensive enterprise servers.

## ✨ Core Features
* **100% Data Sovereignty:** Executes generative models entirely offline (0 external API calls) to guarantee zero-trust data privacy.
* **RBAC Security Gateway:** A custom FastAPI middleware layer that intercepts queries and restricts model access based on user authorization tokens.
* **Behavioral Constraint via Prompt Injection:** Custom Modelfiles utilize strict output templating to force LLMs into a "Socratic Tutoring" mode, mathematically blocking unauthorized Python code generation for students.
* **Multimodal Capabilities:** Supports text inference, Stable Diffusion image generation (via VRAM swapping), and Wyoming-Satellite Voice Integration (Piper TTS).
* **Hardware Democratization:** Utilizes 4-bit tensor quantization and dynamic memory-slicing to run 3-Billion parameter LLMs and Vision models on a standard 4GB VRAM GPU (GTX 1650).

## 🏗️ System Architecture
* **Hardware Engine:** NVIDIA GTX 1650 (4GB VRAM)
* **Text Inference:** Ollama (Qwen 2.5 Coder: 3B) 
* **Vision Inference:** Stable Diffusion WebUI (`--lowvram` optimized)
* **Voice Pipeline:** Wyoming Satellite + Piper TTS Wake-Word Engine
* **User Interface:** Open WebUI

## 📂 Repository Contents
This repository contains the core Infrastructure-as-Code (IaC) and security routing logic that orchestrates the Sovereign AI node:

1. `rbac_api_gateway.py`: The core Access Control List (ACL) middleware that intercepts user queries and routes them to authorized models based on institutional roles.
2. `rbac_terminal_demo.py`: A telemetry script to simulate and verify privilege escalation blocking in the terminal.
3. `Modelfile`: The custom tensor configuration that applies strict output templating and dynamic prompt injection to create the restricted `Sovereign-Tutor`.
4. `vram_swap.sh`: The memory management scripts used to safely transition the GPU between LLM inference and Stable Diffusion image synthesis.

---
*Developed as a B.Tech Final Year Project by Mohith Kkumar RA, Abinaya S, and Malathi M.*
