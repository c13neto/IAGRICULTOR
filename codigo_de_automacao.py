import json
import requests

# Configurações da API do Ollama
OLLAMA_URL = "http://localhost:11434/api/chat"  # URL padrão da API local do Ollama
MODEL_NAME = "llama3.2:1b"  # Substitua pelo nome do modelo que você está usando no Ollama

# Função para enviar uma mensagem para a API do Ollama
def enviar_para_ollama(model, pergunta):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": pergunta}]
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP
        
        # Coletar e juntar partes da resposta em streaming
        resposta_completa = ""
        for chunk in response.iter_lines(decode_unicode=True):
            if chunk:  # Ignorar linhas vazias
                try:
                    data = json.loads(chunk)
                    if "message" in data and "content" in data["message"]:
                        resposta_completa += data["message"]["content"]
                except json.JSONDecodeError:
                    print(f"Parte da resposta ignorada: {chunk}")
        
        return resposta_completa.strip() or "Resposta vazia."
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do Ollama: {e}")
        return "Erro ao obter resposta (conexão falhou)."

# Carregar o arquivo perguntas_humanas.json
with open("perguntas_humanas.json", "r", encoding="utf-8") as file:
    dados = json.load(file)
    perguntas = [pergunta for bloco in dados.get("perguntas_humanas", []) for pergunta in bloco]  # Desempacotando todos os blocos de perguntas

# Processar as perguntas e obter respostas
conversas = []
for idx, pergunta in enumerate(perguntas, 1):
    print(f"Enviando pergunta {idx}: {pergunta}")
    
    # Garantir que a pergunta está formatada como string válida
    pergunta = str(pergunta).strip()
    
    # Obter resposta da API
    resposta = enviar_para_ollama(MODEL_NAME, pergunta)
    print(f"Resposta recebida: {resposta}")
    
    # Armazenar pergunta e resposta
    conversas.append({"pergunta": pergunta, "resposta": resposta})

# Salvar as perguntas e respostas no arquivo conversa.json
with open("conversa.json", "w", encoding="utf-8") as file:
    json.dump(conversas, file, ensure_ascii=False, indent=4)

print("Processo concluído! Respostas salvas no arquivo conversa.json.")

# Modo interativo contínuo
print("\nEntrando no modo interativo. Envie sua mensagem ou pressione Ctrl+C para sair.")
try:
    while True:
        entrada_usuario = input("Você: ").strip()
        if entrada_usuario:
            resposta = enviar_para_ollama(MODEL_NAME, entrada_usuario)
            print(f"Ollama: {resposta}")
except KeyboardInterrupt:
    print("\nSessão encerrada. Até a próxima!")
