import requests
from requests.auth import HTTPBasicAuth

# URL base do sistema da Target
url_base = "https://URL_BASE_DO_SISTEMA/api"

# Autenticação
auth = HTTPBasicAuth("seu_login", "sua_senha")

# Dados simulados para teste
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
        },
        {
            "id": 2,
            "nome": "Programa de Transporte Sustentável",
            "objetivo": "Implementar transporte público ecológico",
            "orçamento_total": 5000000,
            "data_inicio": "2022-06-01",
            "data_termino": "2025-12-31",
            "status": "Em andamento",
            "responsavel": "Carlos Lima",
            "fases": [
                {"fase": "Pesquisa", "status": "Concluído", "percentual_concluido": 100},
                {"fase": "Protótipo", "status": "Em andamento", "percentual_concluido": 30}
            ]
        }
    ]
}

dados_indicadores = {
    "indicadores": [
        {
            "id": 1,
            "nome": "Taxa de Conclusão de Projetos no Prazo",
            "metas": [
                {"ano": 2023, "valor_meta": 85, "valor_realizado": 80, "unidade": "porcentagem"},
                {"ano": 2024, "valor_meta": 90, "valor_realizado": None, "unidade": "porcentagem"}
            ]
        },
        {
            "id": 2,
            "nome": "Cobertura Vacinal Infantil",
            "metas": [
                {"ano": 2023, "valor_meta": 95, "valor_realizado": 92, "unidade": "porcentagem"},
                {"ano": 2024, "valor_meta": 97, "valor_realizado": None, "unidade": "porcentagem"}
            ]
        }
    ]
}

dados_infraestrutura = {
    "infraestrutura": [
        {
            "id": 1,
            "tipo": "Escola Pública",
            "nome": "Escola Estadual José de Alencar",
            "localizacao": {
                "endereco": "Rua das Flores, 123",
                "cidade": "São Paulo",
                "estado": "SP",
                "coordenadas": {"latitude": -23.5505, "longitude": -46.6333}
            },
            "capacidade": 800,
            "ocupacao_atual": 750,
            "necessidades": ["Reforma de banheiros", "Melhoria na acessibilidade"]
        },
        {
            "id": 2,
            "tipo": "Hospital Público",
            "nome": "Hospital Municipal da Criança",
            "localizacao": {
                "endereco": "Av. Central, 456",
                "cidade": "Rio de Janeiro",
                "estado": "RJ",
                "coordenadas": {"latitude": -22.9068, "longitude": -43.1729}
            },
            "capacidade": 500,
            "ocupacao_atual": 400,
            "necessidades": ["Ampliação da ala pediátrica", "Instalação de sistema de ar-condicionado"]
        }
    ]
}

dados_funcionarios = {
    "funcionarios": [
        {
            "id": 1,
            "nome": "Ana Souza",
            "cargo": "Gerente de Projetos",
            "departamento": "Infraestrutura",
            "anos_servico": 5,
            "equipes": [
                {
                    "projeto_id": 1,
                    "nome_projeto": "Reforma das Escolas Públicas",
                    "papel": "Gerente"
                }
            ]
        },
        {
            "id": 2,
            "nome": "Carlos Lima",
            "cargo": "Coordenador de Sustentabilidade",
            "departamento": "Meio Ambiente",
            "anos_servico": 3,
            "equipes": [
                {
                    "projeto_id": 2,
                    "nome_projeto": "Programa de Transporte Sustentável",
                    "papel": "Coordenador"
                }
            ]
        }
    ]
}

dados_feedbacks = {
    "feedbacks": [
        {
            "id": 1,
            "projeto_id": 1,
            "usuario": "João Silva",
            "data": "2023-05-12",
            "comentario": "A reforma nas escolas está indo bem, mas ainda falta a pintura nas salas de aula.",
            "avaliacao": 4
        },
        {
            "id": 2,
            "projeto_id": 2,
            "usuario": "Maria Santos",
            "data": "2023-07-15",
            "comentario": "O transporte sustentável é uma boa ideia, mas precisa de mais pontos de recarga para veículos elétricos.",
            "avaliacao": 3
        }
    ],
    "problemas": [
        {
            "id": 1,
            "projeto_id": 1,
            "descricao": "Falta de materiais de construção",
            "gravidade": "Alta",
            "status": "Em andamento",
            "data_relato": "2023-06-20",
            "prazo_solucao": "2023-07-10"
        },
        {
            "id": 2,
            "projeto_id": 2,
            "descricao": "Ponto de recarga danificado",
            "gravidade": "Média",
            "status": "Pendente",
            "data_relato": "2023-08-01",
            "prazo_solucao": "2023-08-15"
        }
    ]
}

dados_documentos = {
    "documentos": [
        {
            "id": 1,
            "tipo": "Contrato",
            "nome": "Contrato de Reforma Escolar",
            "projeto_id": 1,
            "data_assinatura": "2023-01-10",
            "data_expiracao": "2024-01-15",
            "status": "Vigente",
            "observacoes": "Contrato inclui reforma e pintura de 50 escolas públicas."
        },
        {
            "id": 2,
            "tipo": "Relatório",
            "nome": "Relatório de Progresso do Transporte Sustentável",
            "projeto_id": 2,
            "data_geracao": "2023-06-30",
            "status": "Finalizado",
            "observacoes": "Relatório detalha o andamento e as dificuldades encontradas na implementação."
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

# Enviar todos os conjuntos de dados
enviar_dados("financeiros", dados_financeiros)
enviar_dados("projetos", dados_projetos)
enviar_dados("indicadores", dados_indicadores)
enviar_dados("infraestrutura", dados_infraestrutura)
enviar_dados("funcionarios", dados_funcionarios)
enviar_dados("feedbacks", dados_feedbacks)
enviar_dados("documentos", dados_documentos)
