from search import search_prompt

def main():
    print("\nBusca semântica - Vestibular UnB\nDigite sua pergunta (ou 'sair' para encerrar):\n")
    while True:
        question = input("Pergunta: ").strip()
        if question.lower() in ("sair", "exit", "quit"): break
        resposta = search_prompt(question)
        print(f"\nResposta: {resposta}\n")

if __name__ == "__main__":
    main()