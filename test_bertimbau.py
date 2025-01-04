import os
import json

# Caminho da pasta Archive
archive_path = "/Users/macair/Documents/Python-BERTimbau/Archive"

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

                                print(f"Coletando texto no índice {index}: {text}")

                                # Adicionar resultados
                                all_results.append({
                                    "file": file_name,
                                    "index": index,
                                    "text": text
                                })
                except Exception as e:
                    print(f"Erro ao processar {file_name}: {e}")

        # Salvar resultados em JSON
        with open("text_report.json", "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=4)

        print("\nColeta concluída. Resultados salvos em 'text_report.json'.")

    except Exception as e:
        print(f"An error occurred: {e}")
