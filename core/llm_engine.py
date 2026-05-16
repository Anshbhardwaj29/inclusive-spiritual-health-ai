import requests
from core.prompts import SYSTEM_PROMPT

def ask_llm(user_input, history, is_crisis=False):
    url = "http://localhost:11434/api/generate"
    
    # Inject crisis flag if detected
    crisis_modifier = "\n[CRISIS_FLAG]: THE USER IS IN EXTREME DISTRESS OR SUICIDAL. PROVIDE DEEP GEETA-BASED COUNSELING AND APPEND THE HELPLINE." if is_crisis else ""
    
    # Inject hard limit for brevity at the very end of the prompt so the LLM CANNOT ignore it
    strict_rule = "\n[CRITICAL INSTRUCTION: Respond safely in STRICTLY 1 to 3 short sentences. Integrate a Geeta lesson. DO NOT use any Hindi words like 'Arre bhaiya'. Speak only pure English.]"
    
    full_prompt = f"{SYSTEM_PROMPT}\n\nHistory:\n{history}\nUser: {user_input}{crisis_modifier}{strict_rule}\nMisty:"
    
    payload = {
        "model": "mistral",
        "prompt": full_prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    return response.json().get('response', "I am unable to connect to my inner wisdom right now.")