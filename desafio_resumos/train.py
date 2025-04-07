import os
import time
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import csv

# Carrega as variáveis do arquivo .env
load_dotenv()
deepseek_api = os.getenv("DEEPSEEK_API_KEY")
if not deepseek_api:
    raise ValueError("Chave da API DEEPSEEK_API_KEY não encontrada no arquivo .env.")

client = OpenAI(api_key=deepseek_api, base_url="https://api.deepseek.com")

def avaliar_resumo_com_prompt(prompt_text, summary_text):
    """
    Combina o texto do prompt com o resumo e envia um prompt à API para avaliar o resumo.
    O prompt orienta a IA a retornar um JSON com as chaves "content" e "wording".
    """
    full_prompt = (
        "Considere o seguinte prompt que foi dado aos alunos:\n"
        f"{prompt_text}\n\n"
        "Agora, considere o seguinte resumo escrito pelo aluno:\n"
        f"{summary_text}\n\n"
        "Por favor, avalie o resumo com base na tarefa definida no prompt, e retorne uma resposta em JSON com as chaves 'content' e 'wording'.\n"
        "A nota para 'content' deve refletir a qualidade de representação da ideia principal e dos detalhes, e a nota para 'wording' deve refletir a clareza, precisão e fluência do texto.\n\n"
        "Resposta no formato: {\"content\": <nota>, \"wording\": <nota>}"
    )
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # Modelo a ser utilizado; verifique se é compatível
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0,
            max_tokens=50
        )
        resposta_texto = response.choices[0].message.content.strip()
        
        # Remover formatação de bloco de código, se presente.
        if resposta_texto.startswith("```"):
            # Remove as linhas de abertura e fechamento do bloco de código
            linhas = resposta_texto.splitlines()
            # Se a primeira linha for algo como "```json", remove-a
            if linhas[0].startswith("```"):
                linhas = linhas[1:]
            # Se a última linha for "```", remove-a
            if linhas and linhas[-1].strip() == "```":
                linhas = linhas[:-1]
            resposta_texto = "\n".join(linhas).strip()
        
        try:
            notas = json.loads(resposta_texto)
        except json.JSONDecodeError as e:
            print("Erro ao decodificar JSON:", e)
            print("Resposta recebida:", resposta_texto)
            return None, None
        return notas.get("content"), notas.get("wording")
    except Exception as e:
        print("Erro ao avaliar o resumo:", e)
        return None, None

# Ler os arquivos de teste
prompts_test_df = pd.read_csv("prompts_test.csv", engine="python")
summaries_test_df = pd.read_csv("summaries_test.csv", engine="python", quoting=csv.QUOTE_MINIMAL)

# Fazer merge dos dados de resumos e prompts com base em "prompt_id"
merged_test_df = summaries_test_df.merge(prompts_test_df, on="prompt_id", how="left")

# Seleciona os primeiros 10 registros para teste
merged_sample = merged_test_df.head(10)

content_scores = []
wording_scores = []

print("Avaliando 10 registros do conjunto de teste (prompt + resumo):")
for index, row in merged_sample.iterrows():
    prompt_text = row.get("prompt_text", "")
    summary_text = row.get("text", "")
    content, wording = avaliar_resumo_com_prompt(prompt_text, summary_text)
    print(f"Student {row['student_id']} - Content: {content}, Wording: {wording}")
    content_scores.append(content)
    wording_scores.append(wording)
    time.sleep(1)  # Delay para evitar rate limit

# Gerar o arquivo de submissão
submission = pd.DataFrame({
    'student_id': merged_sample['student_id'],
    'prompt_id': merged_sample['prompt_id'],
    'content': content_scores,
    'wording': wording_scores
})

submission.to_csv("submission_test.csv", index=False)
print("\nArquivo submission_test.csv gerado com sucesso!")
