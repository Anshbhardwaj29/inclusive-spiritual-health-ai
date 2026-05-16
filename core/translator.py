# import torch
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# from huggingface_hub import login

# # 1. HuggingFace Login (Token yahan dalein)
# # Settings -> Access Tokens par jao website pe aur token copy karo
# login(token="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")

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Device check
device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "ai4bharat/indictrans2-en-indic-dist-200M"

# Model loading
print("Loading Translator...")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True).to(device)

INDIC_CODES = {
    'hi': 'hin_Devn', 'mr': 'mar_Devn', 'ta': 'tam_Taml',
    'te': 'tel_Telu', 'gu': 'guj_Gujr', 'kn': 'kan_Knda',
    'pa': 'pan_Guru', 'bn': 'ben_Beng', 'ml': 'mal_Mlym'
}

def get_misty_response(english_text, whisper_lang_code):
    if whisper_lang_code == 'en':
        return english_text

    target_lang = INDIC_CODES.get(whisper_lang_code)
    if not target_lang:
        return english_text

    # --- THE FIX: Manually setting the internal state of the tokenizer ---
    # Kuch versions mein ye attributes hote hain, kuch mein methods. 
    # Hum dono try karenge safe rehne ke liye.
    try:
        tokenizer.src_lang = "eng_Latn"
        tokenizer.tgt_lang = target_lang
    except:
        pass

    # IndicTrans2 tokenizer call with specific formatting
    inputs = tokenizer(
        english_text, 
        src_lang="eng_Latn", 
        tgt_lang=target_lang, 
        return_tensors="pt", 
        padding=True
    ).to(device)
    
    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs, 
            forced_bos_token_id=tokenizer.lang_code_to_id[target_lang],
            max_length=256
        )
    
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]