Avaliação Automatizada de Resumos Estudantis
Este projeto automatiza a avaliação de resumos estudantis utilizando a API DeepSeek (compatível com a interface OpenAI). Ele combina resumos e prompts de avaliação, envia para a IA e obtém notas de content e wording. Os resultados são consolidados em um arquivo CSV para análise e feedback educacional.

Funcionalidades
Integração de Dados: Une resumos dos alunos e os prompts fornecidos.

Avaliação via IA: Envia um prompt combinado para a API DeepSeek, que retorna as pontuações.

Geração de Submissão: Cria um CSV com os campos student_id, prompt_id, content e wording.

Requisitos
Python 3.x

Bibliotecas:

pandas

python-dotenv

openai

csv (módulo padrão do Python)

Setup
Clone o repositório:

bash
Copiar
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Crie e ative o ambiente virtual:

bash
Copiar
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar
pip install -r requirements.txt
Configure o arquivo .env:

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo (substitua pela sua chave):

ini
Copiar
DEEPSEEK_API_KEY=sua_chave_api_aqui
Coloque os arquivos CSV de teste na raiz:

prompts_test.csv

summaries_test.csv

Uso
Execute o script para avaliar os resumos e gerar o arquivo de submissão:

bash
Copiar
python train.py
O script realizará as seguintes etapas:

Ler os arquivos CSV de prompts e resumos.

Fazer merge dos dados com base no prompt_id.

Enviar cada par (prompt + resumo) para a API DeepSeek e coletar as notas.

Gerar o arquivo submission_test.csv com os resultados.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto é licenciado sob a MIT License.

