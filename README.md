# AI-Driven Multilingual Spiritual Counselor for Inclusive Healthcare

An offline, privacy-first, voice-to-voice assistive technology system designed to provide emotional and cognitive support using ancient spiritual wisdom (Bhagwat Geeta) mixed with modern AI. 

This system is specifically optimized as an **Assistive Tool** for the disabled community (visually impaired, motor-disabled), the elderly, and rural populations who face language barriers and accessibility constraints in standard healthcare platforms.

---

## 🌟 Key Features
- **Voice-First Interface:** Complete hands-free, screen-free interaction designed for visually impaired and motor-disabled individuals.
- **Multilingual Support:** Translates complex spiritual and cognitive advice into 22+ regional Indian languages using state-of-the-art translation pipelines.
- **Privacy by Design (100% Offline):** Runs completely on local hardware to ensure absolute data sovereignty and compliance with strict mental health privacy standards.
- **Crisis Intervention:** Built-in `CrisisHandler` that detects high-risk keywords (self-harm, trauma) and instantly routes users to emergency resources instead of automated dialog.
- **Edge AI Optimization:** Finetuned to deliver real-time, low-latency conversational feedback on consumer-grade hardware (NVIDIA RTX 3050).

---

## 🛠️ Technical Stack & Architecture
| Pipeline Stage | Technology Used | Description |
| :--- | :--- | :--- |
| **1. Perception (STT)** | OpenAI Whisper | High-accuracy speech-to-text handling diverse Indian accents. |
| **2. Cognition (LLM)** | Llama 3 / Mistral (via Ollama) | Local intelligence engine driven by spiritual framework prompting. |
| **3. Translation (NMT)** | IndicTrans2 (AI4Bharat) | SOTA neural translation specifically optimized for Indic scripts. |
| **4. Synthesis (TTS)** | gTTS & Playsound | Emits calm, natural audio feedback back to the user. |

---

## 🚀 Installation & Setup
```bash
git clone [https://github.com/Anshbhardwaj29/inclusive-spiritual-health-ai.git](https://github.com/Anshbhardwaj29/inclusive-spiritual-health-ai.git)
cd inclusive-spiritual-health-ai
python -m venv whisper_env
.\whisper_env\Scripts\activate
pip install -r requirements.txt
python main.py