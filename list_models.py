#!/usr/bin/env python3
"""
Lista modelos disponíveis no Google Gemini
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def list_available_models():
    google_key = os.getenv("GOOGLE_API_KEY")
    if not google_key:
        print("❌ GOOGLE_API_KEY não encontrada")
        return
    
    genai.configure(api_key=google_key)
    
    print("🔍 Modelos disponíveis:")
    try:
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                print(f"✅ {model.name}")
        
        # Teste simples
        print("\n🧪 Teste rápido...")
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Diga apenas: Funcionando!")
        print(f"✅ Resposta: {response.text}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    list_available_models()