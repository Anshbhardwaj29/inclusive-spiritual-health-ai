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

### 🔄 System Workflow Diagram

```mermaid
graph TD
    A[User Speech Input] -->|Audio Capture| B[OpenAI Whisper STT]
    B -->|Transcribed Text| C[Llama 3 / Mistral via Ollama]
    C -->|Spiritual / Cognitive Response| D{Language Check}
    
    D -->|If English| E[Direct Voice Output]
    D -->|If Regional Language| F[IndicTrans2 Translation Engine]
    
    F -->|Translated Text| G[gTTS / Neural TTS]
    E --> G
    G -->|Empathetic Audio Feedback| H[User Listening]

    %% Styling
    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style C fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    style F fill:#efebe9,stroke:#3e2723,stroke-width:2px
    style H fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
