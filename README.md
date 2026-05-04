# Clínica Virtual - Assistente de Triagem Médica com IA

Um assistente virtual inteligente para triagem médica inicial, construído com **Ollama** e modelos de IA local. O sistema realiza perguntas complementares e orienta sobre a necessidade de atendimento médico.

## 🎯 Objetivo

Criar um chatbot de triagem médica que:
- Escuta a queixa inicial do paciente
- Realiza perguntas complementares pertinentes
- Identifica situações de emergência
- Encaminha para atendimento apropriado
- **Nunca fornece diagnóstico**

## 🛠️ Tecnologias

- **Ollama**: Servidor local de IA
- **Modelos**: phi3, llama3.2:1b
- **Linguagem**: Python
- **Ambiente**: Jupyter Notebook

## 📋 Requisitos

- Python 3.8+
- Ollama instalado ([ollama.com](https://ollama.com))
- ~2GB de RAM disponível
- ~1GB de espaço em disco (para os modelos)

## 📁 Estrutura do Projeto

```
.
├── README.md                 # Este arquivo
├── modelfile                 # Definição do modelo customizado
├── dataset/
│   └── dados.json           # Dataset com perguntas/respostas de exemplo
├── notebook/
│   └── customizacao.ipynb   # Notebook para treinar e testar o modelo
├── resultados/
│   └── testes-1_a_5/        # Resultados dos testes realizados
└── asssets/
    └── Prints/              # Screenshots/documentação visual
```

## 🚀 Como Usar

### 1. Instalação

```bash
# Instalar Ollama (se ainda não tiver)
# Visite https://ollama.com

# Instalar dependências Python
pip install ollama
```

### 2. Executar o Notebook

```bash
jupyter notebook notebook/customizacao.ipynb
```

O notebook executará:
1. ✅ Instalação do Ollama
2. ✅ Download do modelo base (phi3)
3. ✅ Criação do Modelfile customizado
4. ✅ Treino do modelo `clinica-triagem`
5. ✅ Execução de testes

### 3. Usar o Modelo

```python
import ollama

response = ollama.chat(
    model='clinica-triagem',
    messages=[{
        'role': 'user',
        'content': 'Estou com febre e dor de cabeça'
    }]
)

print(response['message']['content'])
```

## 📊 Dataset

O arquivo `dataset/dados.json` contém exemplos de:
- Febre
- Dor no peito (emergência)
- Tosse
- Dor abdominal
- Tontura
- Falta de ar (emergência)
- Renovação de receita
- Check-up
- Dor de cabeça
- Vômitos

## ⚙️ Configuração do Modelo

No **Modelfile**:
- `FROM phi3`: Modelo base utilizado
- `PARAMETER temperature 0.3`: Respostas mais determinísticas e médicas
- `SYSTEM`: Prompt do sistema com regras de comportamento

## 🧪 Testes

Os testes são executados no notebook e os resultados salvos em `resultados/testes-1_a_5/`.

## ⚠️ Aviso Importante

Este é um **projeto educacional** de triagem médica inicial. **Não substitui atendimento médico profissional**. Em emergências, procure atendimento médico imediatamente.

## 📝 Licença

Projeto desenvolvido para fins educacionais.