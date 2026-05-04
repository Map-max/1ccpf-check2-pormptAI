SYSTEM_PROMPT = """
Você é um assistente virtual de triagem médica.

Regras:
- Responda em português
- Seja objetivo
- Faça perguntas complementares
- Oriente emergência quando necessário
- Nunca dê diagnóstico
"""

def gerar_modelfile(modelo_base, system_prompt, exemplos):
    linhas = []

    linhas.append(f"FROM {modelo_base}\n")
    linhas.append("PARAMETER temperature 0.3\n")

    linhas.append(f'SYSTEM """\n{system_prompt}\n"""\n')

    for ex in exemplos:
        linhas.append(f'MESSAGE user "{ex["pergunta"]}"')
        linhas.append(f'MESSAGE assistant "{ex["resposta"]}"\n')

    return "\n".join(linhas)