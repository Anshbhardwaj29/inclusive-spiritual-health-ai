from voice.speech_to_text import listen
from voice.text_to_speech import speak
from core.llm_engine import ask_llm
from memory.memory_manager import MemoryManager
from safety.crisis_handler import CrisisHandler

def start_ui():
    print("--- 🕉️ MISTY: ADVANCED GEETA MENTAL HEALTH COUNSELOR ---")
    
    # Initialize components
    memory = MemoryManager()
    crisis_handler = CrisisHandler()
    
    preferred_lang = "en"

    while True:
        print("\n1. Text | 2. Voice | 3. Exit")
        choice = input("Select: ")
        
        user_input = ""
        # The speech-to-text might detect Hindi on its own, but we process based on preferred_lang.
        input_lang_code = "en" 

        if choice == '1':
            user_input = input("You: ")
            input_lang_code = preferred_lang
        elif choice == '2':
            user_input, input_lang_code = listen()
            print(f"-> [YOU] ({input_lang_code}): {user_input}")
        elif choice == '3': break
        else: continue

        if user_input.strip():
            # Check for crisis
            is_crisis = crisis_handler.is_crisis(user_input)
            
            # Fetch history
            history = memory.get_recent_history(limit=4)
            
            # Ask LLM 
            final_response = ask_llm(user_input, history, is_crisis) 
            
            print(f"\n✨ Misty: {final_response}")
            
            # Save to memory 
            memory.save_chat(user_input, final_response)
            
            # Voice Output ONLY if user chose '2. Voice'
            if choice == '2':
                speak(final_response, lang_code=preferred_lang)