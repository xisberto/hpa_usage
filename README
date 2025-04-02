# Utilização do HPA em Projetos Públicos no GitHub

## Introdução

## Preparar o ambiente

Para trabalhar com estes aqruivos, é necessário um ambiente virtual Python. As dependências do projeto estão listadas no arquivo `requirements.txt`

```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Notebooks

### Notebook [`hpa_usage.ipynb`](hpa_usage.ipynb)

Realiza a pesquisa de código no GitHub com as palavras-chave

> `"kind: HorizontalPodAutoscaler" language:yaml`

Salva os resultados da pesquisa em arquivos CSV no diretório [`partial_results`](partial_results) e os arquivos localizados no diretório [`search_results`](search_results).

Para executar este notebook, é necessário utilizar um [*Fine-grained personal access token*](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) e salvar seu valor em um arquivo `.env` sob a variável `GITHUB_TOKEN`.

```.env
GITHUB_TOKEN=PERSONAL_ACCESS_TOKEN
```

### Notebook [`hpa_classify.ipynb`](hpa_classify.ipynb)

Analisa os resultados da pesquisa gerados pelo `hpa_usage.ipynb`.


