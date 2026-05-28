# Mission Control AI — APOLO 0

Sistema inteligente de monitoramento de missão espacial experimental, desenvolvido em Python puro como parte da **Global Solution 2026.1 — Pensamento Computacional e Automação com Python (FIAP)**.

---

## Equipe

**PROMETHEUS**

---

## Descrição

O **Mission Control AI** simula o acompanhamento contínuo de uma missão espacial por meio de **ciclos de monitoramento**. A cada ciclo, o sistema analisa cinco sistemas críticos da nave, calcula o nível de risco, classifica a situação da missão e emite recomendações automáticas. Ao final, gera um relatório consolidado com tendência, área mais afetada e classificação geral da missão.

---

## Estrutura do repositório

```
mission-control-ai/
│
├── README.md
└── mission_control.py
```

---

## Como executar

Nenhuma dependência externa é necessária. Basta ter Python 3 instalado.

```bash
python mission_control.py
```

---

## Estrutura dos dados

A missão é representada pela matriz `dados_missao`, onde cada linha é um ciclo e cada coluna é um sistema monitorado:

```python
dados_missao = [
    [temperatura, comunicacao, bateria, oxigenio, estabilidade],
    ...
]
```

| Posição | Sistema | Unidade |
|---|---|---|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

A missão **APOLO 0** simula 6 ciclos: início estável, degradação progressiva dos sistemas, pico crítico no ciclo 5 e tentativa de recuperação no ciclo 6.

---

## Regras de alerta

Cada sistema é classificado como **NORMAL**, **ATENÇÃO** ou **CRÍTICO** conforme os limites abaixo.

| Sistema | NORMAL | ATENÇÃO | CRÍTICO |
|---|---|---|---|
| Temperatura | 18 °C – 30 °C | < 18 °C ou 30 °C – 35 °C | > 35 °C |
| Comunicação | ≥ 60% | 30% – 59% | < 30% |
| Bateria | ≥ 50% | 20% – 49% | < 20% |
| Oxigênio | ≥ 90% | 80% – 89% | < 80% |
| Estabilidade | ≥ 70% | 40% – 69% | < 40% |

---

## Pontuação e classificação por ciclo

Cada classificação gera uma pontuação que, somada, define o status do ciclo:

| Classificação | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

| Pontuação total | Status do ciclo |
|---|---|
| 0 – 2 | MISSÃO ESTÁVEL |
| 3 – 5 | MISSÃO EM ATENÇÃO |
| 6 – 10 | MISSÃO CRÍTICA |

---

## Análise de tendência

O sistema compara a pontuação de risco do **primeiro ciclo** com a do **último ciclo**:

- Risco final **maior** → tendência de **piora**
- Risco final **menor** → tendência de **melhora**
- Risco final **igual** → missão **estável**

---

## Funções do sistema

| Função | Responsabilidade |
|---|---|
| `analisar_sistemas(dados)` | Classifica cada sistema do ciclo e retorna pontos, estados e descrições |
| `classificar_ciclo(pontuacao)` | Retorna o status da missão com base na pontuação total |
| `gerar_recomendacao(classificacao, estados)` | Emite recomendação específica por sistema em risco |
| `analisar_tendencia(inicial, final)` | Compara riscos do primeiro e último ciclo |
| `identificar_area_mais_afetada(acumuladas)` | Retorna a área com maior pontuação acumulada |
| `gerar_conclusao(...)` | Gera o parágrafo de conclusão do relatório final |
| `preview()` | Orquestra toda a execução e exibe o relatório no terminal |

---

## Exemplo de saída

```
============================================================
MISSION CONTROL AI
============================================================
Missao: APOLO 0
Equipe: PROMETHEUS
Quantidade de ciclos analisados: 6
============================================================

CICLO 1
------------------------------------------------------------
Temperatura interna: 24 Graus | NORMAL | Temperatura estavel
Comunicacao com a base: 92% | NORMAL | Comunicacao estavel
Sistema de energia: 88% | NORMAL | Energia estavel
Suporte de oxigenio: 96% | NORMAL | Oxigenio adequado
Estabilidade operacional: 90% | NORMAL | Estabilidade operacional adequada

Pontuacao de risco do ciclo: 0
Classificacao do ciclo: MISSAO ESTAVEL
Recomendacao: Manter operacao normal e continuar monitoramento.

...

============================================================
RELATORIO FINAL DA MISSAO
============================================================
Missao: APOLO 0
Equipe: PROMETHEUS

Ciclo mais critico: Ciclo 5
Maior pontuacao de risco: 10
Area mais afetada: Temperatura interna
Classificacao final da missao: MISSAO EM ATENCAO
============================================================
```

---

## Requisitos atendidos

- [x] Nome da missão e da equipe
- [x] Matriz `dados_missao` com 6 ciclos e 5 sistemas na ordem correta
- [x] Lista `areas_monitoradas` mapeada às colunas
- [x] Mínimo de 5 funções (7 implementadas)
- [x] Estrutura de repetição para percorrer os ciclos
- [x] Estruturas condicionais para geração de alertas
- [x] Cálculo de risco por ciclo
- [x] Classificação de cada ciclo
- [x] Análise de tendência da missão
- [x] Identificação da área mais afetada
- [x] Recomendações automáticas por sistema em risco
- [x] Relatório final exibido no terminal com conclusão