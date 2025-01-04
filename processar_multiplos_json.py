import json
import os

# Passo 1: Caminho para a pasta com os arquivos JSON
caminho_pasta = "/Users/macair/Downloads/Archive"

# Passo 2: Caminho para o arquivo de saída
caminho_saida = "/Users/macair/Downloads/Archive/textos_extraidos.txt"

# Abrir o arquivo de saída
with open(caminho_saida, "w", encoding="utf-8") as arquivo_saida:
    # Passo 3: Percorrer todos os arquivos da pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.endswith(".json"):  # Verificar se é um arquivo JSON
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
            try:
                # Carregar o JSON
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                    print(f"Processando: {nome_arquivo}")
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Erro ao processar {nome_arquivo}: {e}")
                continue
            
            # Processar os textos do JSON
            for item in dados:
                text = item.get("text", "Texto não encontrado")
                user = item.get("user", "Usuário desconhecido")
                timestamp = item.get("ts", "Timestamp não encontrado")
                
                # Salvar no arquivo de saída
                arquivo_saida.write(f"Arquivo: {nome_arquivo} - Usuário: {user} - Texto: {text} - Timestamp: {timestamp}\n")

print(f"Textos extraídos e salvos em: {caminho_saida}")
