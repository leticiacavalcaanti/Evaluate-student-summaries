# Desafio sobre Testes Unitários
[**Unit Test Quality Prediction using LLMs**](https://www.kaggle.com/competitions/python-code-unit-test-assertion-quality-prediction/data?select=test.csv)

## Execução do notebook
Para executar o notebook _test_eval.ipynb_ é necessário ter uma chave de API do DeepSeek. Preferencialmente, em um arquivo _.env_ com o nome de "DEEPSEEK_API_KEY". Também é possível usar uma chave de API da OpenAI, uma vez que o construtor utilizado é o mesmo.

Além disso, é necessário ter a linguagem Python3 e seu instalador de pacotes instalados. Em seguida, execute o seguinte comando no terminal para instalar as dependências:
```bash
pip install pandas numpy openai python-dotenv tqdm aiohttp backoff
```