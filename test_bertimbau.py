import os
import json
from transformers import pipeline

# Caminho da pasta Archive
archive_path = "/Users/macair/Documents/Python-BERTimbau/Archive"

# Inicializando o pipeline para análise de sentimentos
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Função principal
if __name__ == "__main__":
    try:
        # Lista para armazenar os resultados
        all_results = []

        # Processar arquivos JSON
        for file_name in os.listdir(archive_path):
            if file_name.endswith(".json"):
                file_path = os.path.join(archive_path, file_name)
                print(f"Processando arquivo: {file_name}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    if isinstance(data, list):
                        for index, item in enumerate(data):
                            if isinstance(item, dict) and "text" in item:
                                text = item["text"]

                                # Verificar se o texto é vazio ou inválido
                                if not text.strip():
                                    print(f"Texto vazio no índice {index}, ignorando...")
                                    continue

                                print(f"Analisando texto no índice {index}: {text}")

                                # Realizar análise de sentimentos
                                sentiment_result = sentiment_analysis(text)[0]

                                # Adicionar resultados
                                all_results.append({
                                    "file": file_name,
                                    "index": index,
                                    "text": text,
                                    "sentiment": sentiment_result["label"],
                                    "confidence": sentiment_result["score"]
                                })
                except Exception as e:
                    print(f"Erro ao processar {file_name}: {e}")

        # Salvar resultados em JSON
        with open("text_report_with_sentiments.json", "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=4)

        print("\nColeta concluída. Resultados salvos em 'text_report_with_sentiments.json'.")

    except Exception as e:
        print(f"An error occurred: {e}")
