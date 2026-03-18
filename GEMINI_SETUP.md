# 🚀 Google Gemini - Setup Gratuito

## ✅ VANTAGENS DO GEMINI GRATUITO
- 💰 **Completamente grátis** (sem cartão de crédito)
- 🚀 **15 requests/minuto** + 1.500/dia
- ⚡ **Modelo rápido**: gemini-1.5-flash  
- 🌍 **Google AI Studio**: Interface amigável

---

## 🔑 1. OBTER CHAVE API (5 minutos)

### Passo a passo:
1. **Acesse**: https://makersuite.google.com/app/apikey
2. **Faça login** com conta Google (Gmail)
3. **Clique "Create API Key"** 
4. **Selecione** um projeto Google ou crie novo
5. **Copie a chave** (format: `AIza...`)

### ⚠️ Importante: 
- **Gratuito**: Não pede cartão de crédito
- **Restrições**: Apenas uso pessoal/educativo
- **Rate limit**: 15 req/min é suficiente para testes

---

## 🔧 2. CONFIGURAR NO PROJETO

### Editar arquivo `.env`:
```bash
# Substitua pela sua chave real:
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXX
```

### ✅ Verificar instalação:
```bash
# Confirmar que está no ambiente certo:
python --version  # Deve mostrar 3.14

# Testar dependências:
python -c "from langchain_google_genai import ChatGoogleGenerativeAI; print('✅ Gemini OK')"
```

---

## 🎯 3. USAR O SISTEMA

### Testar busca com Gemini:
```bash
python search_gemini.py
```

### Exemplo de uso:
```
🎯 Busca Semântica - Vestibular UnB (Gemini + HuggingFace)
💡 Modelos: HuggingFace (embeddings) + Google Gemini (chat)  
💰 Custo: $0.00 - Completamente gratuito!

Pergunta: Quantos candidatos foram aprovados no vestibular?
🔍 Gerando embedding da pergunta...
📊 Buscando documentos similares... 
📄 Encontrados 3 documentos relevantes
🤖 Gerando resposta com Gemini...

Resposta: Foram aprovados 1.247 candidatos no vestibular da UnB...
```

---

## 🧪 4. SOLUÇÃO DE PROBLEMAS

### Erro "API Key inválida":
- ✓ Verificar se copiou a chave completa
- ✓ Remover aspas extras no .env
- ✓ Reiniciar o script após alterar .env

### Erro "Rate limit exceeded":  
- ✓ Aguardar 1 minuto entre pedidos
- ✓ Verificar se não ultrapassou 1.500/dia

### Erro "Model not found":
- ✓ Usar `gemini-1.5-flash` (gratuito)
- ✓ Evitar `gemini-pro` (pode ser pago)

---

## 💡 5. COMPARAÇÃO DE CUSTOS

| Serviço | Embeddings | Chat LLM | Custo/mês |
|---------|------------|----------|-----------|
| **OpenAI** | $0.02/1M tokens | $0.50/1M tokens | ~$10-50 |  
| **Nossa solução** | HuggingFace (local) | Gemini (gratuito) | **$0.00** |

### 🎉 **Economia**: $120-600 por ano!

---

## ⚡ COMANDOS RÁPIDOS

```bash
# 1. Ativar ambiente  
.\.venv-local\Scripts\Activate.ps1

# 2. Subir banco
docker-compose up -d

# 3. Ingerir PDF (se ainda não fez)
python src\ingest.py docs\vestibular_unb_2026.pdf  

# 4. Chat com Gemini
python search_gemini.py
```

---

> 🎯 **Resultado**: Sistema de busca semântica profissional e gratuito!