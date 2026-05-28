nome_missao = "APOLO 0"
nome_equipe = "PROMETHEUS"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]

def analisar_sistemas(dados):
    pontos = [0, 0, 0, 0, 0]
    estado = ["NORMAL", "NORMAL", "NORMAL", "NORMAL", "NORMAL"]
    descricao = ["", "", "", "", ""]

    # 1. Temperatura
    if dados[0] < 18:
        pontos[0] = 1; estado[0] = "ATENCAO"; descricao[0] = "Temperatura abaixo do ideal"
    elif 18 <= dados[0] <= 30:
        pontos[0] = 0; estado[0] = "NORMAL"; descricao[0] = "Temperatura estavel"
    elif 30 < dados[0] <= 35:
        pontos[0] = 1; estado[0] = "ATENCAO"; descricao[0] = "Temperatura elevada"
    else:
        pontos[0] = 2; estado[0] = "CRITICO"; descricao[0] = "Risco de superaquecimento"

    # 2. Comunicacao
    if dados[1] < 30:
        pontos[1] = 2; estado[1] = "CRITICO"; descricao[1] = "Comunicacao com a base em nivel critico"
    elif 30 <= dados[1] <= 59:
        pontos[1] = 1; estado[1] = "ATENCAO"; descricao[1] = "Comunicacao instavel"
    else:
        pontos[1] = 0; estado[1] = "NORMAL"; descricao[1] = "Comunicacao estavel"

    # 3. Bateria
    if dados[2] < 20:
        pontos[2] = 2; estado[2] = "CRITICO"; descricao[2] = "Bateria em nivel critico"
    elif 20 <= dados[2] <= 49:
        pontos[2] = 1; estado[2] = "ATENCAO"; descricao[2] = "Bateria abaixo do recomendado"
    else:
        pontos[2] = 0; estado[2] = "NORMAL"; descricao[2] = "Energia estavel"

    # 4. Oxigenio
    if dados[3] < 80:
        pontos[3] = 2; estado[3] = "CRITICO"; descricao[3] = "Oxigenio em nivel critico"
    elif 80 <= dados[3] <= 89:
        pontos[3] = 1; estado[3] = "ATENCAO"; descricao[3] = "Oxigenio abaixo do ideal"
    else:
        pontos[3] = 0; estado[3] = "NORMAL"; descricao[3] = "Oxigenio adequado"

    # 5. Estabilidade
    if dados[4] < 40:
        pontos[4] = 2; estado[4] = "CRITICO"; descricao[4] = "Estabilidade operacional critica"
    elif 40 <= dados[4] <= 69:
        pontos[4] = 1; estado[4] = "ATENCAO"; descricao[4] = "Estabilidade operacional reduzida"
    else:
        pontos[4] = 0; estado[4] = "NORMAL"; descricao[4] = "Estabilidade operacional adequada"

    return pontos, estado, descricao

def classificar_ciclo(pontuacao_total):
    if pontuacao_total <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao_total <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def gerar_recomendacao(classificacao, estados):
    if classificacao == "MISSAO CRITICA":
        if estados[0] == "CRITICO": return "Verificar controle termico da missao."
        if estados[1] == "CRITICO": return "Tentar restabelecer contato com a base."
        if estados[2] == "CRITICO": return "Ativar modo de economia de energia."
        if estados[3] == "CRITICO": return "Acionar protocolo de suporte a vida."
        if estados[4] == "CRITICO": return "Reduzir operacoes nao essenciais."
        return "Ativar modo de seguranca e priorizar suporte a vida."
    elif classificacao == "MISSAO EM ATENCAO":
        if estados[0] == "ATENCAO": return "Monitorar temperatura e verificar controle termico."
        if estados[1] == "ATENCAO": return "Monitorar sinal de comunicacao e verificar antenas."
        if estados[2] == "ATENCAO": return "Reduzir consumo de energia e monitorar bateria."
        if estados[3] == "ATENCAO": return "Monitorar nivel de oxigenio e preparar reservas."
        if estados[4] == "ATENCAO": return "Monitorar estabilidade e reduzir operacoes secundarias."
        return "Monitorar sistemas em atencao e preparar plano de contingencia."
    else:
        return "Manter operacao normal e continuar monitoramento."

def analisar_tendencia(risco_inicial, risco_final):
    if risco_final > risco_inicial:
        return "A missao apresentou tendencia de piora."
    elif risco_final < risco_inicial:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."

def identificar_area_mais_afetada(pontuacoes_acumuladas):
    maior_pontuacao = max(pontuacoes_acumuladas)
    indice_maior = pontuacoes_acumuladas.index(maior_pontuacao)
    return areas_monitoradas[indice_maior]

def gerar_conclusao(classificacao_final, ciclos_criticos, risco_ultimo_ciclo, risco_primeiro_ciclo):
    tendencia = "piora" if risco_ultimo_ciclo > risco_primeiro_ciclo else ("melhora" if risco_ultimo_ciclo < risco_primeiro_ciclo else "estabilidade")
    if classificacao_final == "MISSAO CRITICA":
        return (f"A missao apresentou situacao critica ao longo da operacao com {ciclos_criticos} ciclo(s) critico(s). "
                f"A tendencia de {tendencia} exige ativacao imediata dos protocolos de emergencia.")
    elif classificacao_final == "MISSAO EM ATENCAO":
        return (f"A missao apresentou instabilidade relevante durante a operacao com {ciclos_criticos} ciclo(s) critico(s). "
                f"Apesar da tendencia de {tendencia}, a equipe deve manter o plano de contingencia ativo.")
    else:
        return "A missao transcorreu dentro dos parametros esperados. Continuar monitoramento de rotina."

def preview():
    print("============================================================")
    print("MISSION CONTROL AI")
    print("============================================================")
    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("============================================================")
    print()

    pontuacoes_acumuladas = [0, 0, 0, 0, 0]
    risco_primeiro_ciclo = 0
    risco_ultimo_ciclo = 0
    ciclo_mais_critico = 1
    maior_risco = 0
    soma_riscos = 0
    ciclos_criticos = 0

    soma_medias = [0, 0, 0, 0, 0]

    for i in range(len(dados_missao)):
        dados = dados_missao[i]
        pontos, estados, descricoes = analisar_sistemas(dados)
        pontuacao_total = sum(pontos)
        classificacao = classificar_ciclo(pontuacao_total)
        recomendacao = gerar_recomendacao(classificacao, estados)

        if i == 0: risco_primeiro_ciclo = pontuacao_total
        if i == len(dados_missao) - 1: risco_ultimo_ciclo = pontuacao_total
        
        if pontuacao_total > maior_risco:
            maior_risco = pontuacao_total
            ciclo_mais_critico = i + 1
            
        if classificacao == "MISSAO CRITICA":
            ciclos_criticos += 1

        soma_riscos += pontuacao_total
        for j in range(len(areas_monitoradas)): 
            pontuacoes_acumuladas[j] += pontos[j]
            soma_medias[j] += dados[j]

        print(f"CICLO {i+1}")
        print("------------------------------------------------------------")
        print(f"{areas_monitoradas[0]}: {dados[0]} Graus | {estados[0]} | {descricoes[0]}")
        print(f"{areas_monitoradas[1]}: {dados[1]}% | {estados[1]} | {descricoes[1]}")
        print(f"{areas_monitoradas[2]}: {dados[2]}% | {estados[2]} | {descricoes[2]}")
        print(f"{areas_monitoradas[3]}: {dados[3]}% | {estados[3]} | {descricoes[3]}")
        print(f"{areas_monitoradas[4]}: {dados[4]}% | {estados[4]} | {descricoes[4]}")
        print()
        print(f"Pontuacao de risco do ciclo: {pontuacao_total}")
        print(f"Classificacao do ciclo: {classificacao}")
        print(f"Recomendacao: {recomendacao}")
        print()

    classificacao_final = classificar_ciclo(soma_riscos / len(dados_missao))

    print("============================================================")
    print("RELATORIO FINAL DA MISSAO")
    print("============================================================")
    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print()
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print()
    print(f"Media de temperatura: {soma_medias[0]/len(dados_missao):.2f} Graus")
    print(f"Media de comunicacao: {soma_medias[1]/len(dados_missao):.2f}%")
    print(f"Media de bateria: {soma_medias[2]/len(dados_missao):.2f}%")
    print(f"Media de oxigenio: {soma_medias[3]/len(dados_missao):.2f}%")
    print(f"Media de estabilidade: {soma_medias[4]/len(dados_missao):.2f}%")
    print()
    print(f"Ciclo mais critico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuacao de risco: {maior_risco}")
    print(f"Risco medio da missao: {soma_riscos/len(dados_missao):.2f}")
    print(f"Quantidade de ciclos criticos: {ciclos_criticos}")
    print()
    print("Tendencia da missao:")
    print(analisar_tendencia(risco_primeiro_ciclo, risco_ultimo_ciclo))
    print()
    print("Pontuacao acumulada por area:")
    for k in range(len(areas_monitoradas)): 
        print(f"{areas_monitoradas[k]}: {pontuacoes_acumuladas[k]} pontos")
    print()
    print("Area mais afetada:")
    print(identificar_area_mais_afetada(pontuacoes_acumuladas))
    print()
    print("Classificacao final da missao:")
    print(classificacao_final)
    print()
    print("Conclusao:")
    print(gerar_conclusao(classificacao_final, ciclos_criticos, risco_ultimo_ciclo, risco_primeiro_ciclo))
    print("============================================================")

preview()