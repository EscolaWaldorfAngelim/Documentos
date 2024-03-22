import os

# Define o diretório raiz onde as pastas serão criadas
diretorio_raiz = "Escola"

# Lista de pastas a serem criadas com breve explicação do conteúdo
pastas = {
    "Documentos Administrativos": "Este diretório contém documentos administrativos importantes, como contratos, políticas, relatórios financeiros, etc.",
    "Recursos Humanos": "Este diretório contém documentos relacionados aos recursos humanos da escola, incluindo contratos de trabalho, avaliações de desempenho, etc.",
    "Academico": "Este diretório contém materiais acadêmicos, como currículos, planos de aula, material didático, etc.",
    "Alunos": "Este diretório contém registros e documentos relacionados aos alunos da escola, incluindo inscrições, registros de notas, etc.",
    "Comunicacoes e Marketing": "Este diretório contém material de comunicação e marketing da escola, como folhetos, comunicados, etc.",
    "Tecnologia da Informacao": "Este diretório contém documentos relacionados à tecnologia da informação, como políticas de segurança, documentação de sistemas, etc.",
    "Eventos e Atividades Extracurriculares": "Este diretório contém informações sobre eventos e atividades extracurriculares da escola.",
    "Facilidades e Manutencao": "Este diretório contém documentos relacionados às instalações e manutenção da escola, como contratos de fornecedores, registros de manutenção, etc.",
    "Projetos e Desenvolvimento": "Este diretório contém informações sobre projetos e desenvolvimento escolar, como planos estratégicos, relatórios de pesquisa, etc.",
    "Registros Historicos": "Este diretório contém registros históricos da escola, incluindo documentos antigos, arquivos de ex-alunos, etc."
}

# Função para criar as pastas
def criar_pastas_com_readme(diretorio_raiz, pastas):
    # Verifica se o diretório raiz já existe
    if not os.path.exists(diretorio_raiz):
        os.makedirs(diretorio_raiz)
        print(f"Diretório raiz '{diretorio_raiz}' criado.")
    else:
        print(f"Diretório raiz '{diretorio_raiz}' já existe.")
    
    # Cria as subpastas dentro do diretório raiz e cria o arquivo README.md em cada pasta
    for pasta, explicacao in pastas.items():
        nova_pasta = os.path.join(diretorio_raiz, pasta)
        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)
            print(f"Pasta '{pasta}' criada.")
        else:
            print(f"Pasta '{pasta}' já existe.")
        
        # Cria o arquivo README.md em cada pasta
        with open(os.path.join(nova_pasta, "README.md"), "w") as arquivo_readme:
            arquivo_readme.write(explicacao)
            print(f"Arquivo README.md criado em '{pasta}'.")

# Chamada da função para criar as pastas com o arquivo README.md
criar_pastas_com_readme(diretorio_raiz, pastas)
