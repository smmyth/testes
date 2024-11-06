import requests
from requests.auth import HTTPBasicAuth

# URL base do sistema da Target
url_base = "https://facilit.plataformatarget.com.br/html/swagger/targetApi.html#/"

# Autenticação
auth = HTTPBasicAuth("turma3@facilit.com.br", "xxx")

# Dados para inserir
dados_financeiros = {
    "financeiros": [
        {
            "ano": 2023,
            "entidade": "Secretaria de Saúde",
            "receita": 5000000,
            "despesa": 4200000,
            "investimentos": 300000,
            "categoria_receita": "Impostos",
            "categoria_despesa": "Salários e Infraestrutura"
        },
        {
            "ano": 2023,
            "entidade": "Secretaria de Educação",
            "receita": 6000000,
            "despesa": 5500000,
            "investimentos": 500000,
            "categoria_receita": "Subsídios Governamentais",
            "categoria_despesa": "Infraestrutura e Projetos Educacionais"
        }
    ]
}

dados_projetos = {
    "projetos": [
        {
            "id": 1,
            "nome": "Reforma das Escolas Públicas",
            "objetivo": "Melhorar a infraestrutura de 50 escolas públicas",
            "orçamento_total": 2000000,
            "data_inicio": "2023-01-15",
            "data_termino": "2024-01-15",
            "status": "Em andamento",
            "responsavel": "Ana Souza",
            "fases": [
                {"fase": "Planejamento", "status": "Concluído", "percentual_concluido": 100},
                {"fase": "Execução", "status": "Em andamento", "percentual_concluido": 40}
            ]
        }
    ]
}

# Função para enviar dados
def enviar_dados(endpoint, dados):
    url = f"{url_base}/{endpoint}"
    resposta = requests.post(url, json=dados, auth=auth)
    
    if resposta.status_code == 201:
        print(f"Dados enviados com sucesso para {endpoint}!")
    else:
        print(f"Erro ao enviar dados para {endpoint}: {resposta.status_code} - {resposta.text}")

# Enviar os dados financeiros e de projetos
enviar_dados("financeiros", dados_financeiros)
enviar_dados("projetos", dados_projetos)
