# Projeto 2 — Ranking de Jogadores por Score de Impacto
# score = 2 * points + rebounds + assists

partidas = [
    {"player_id": 1, "points": 25, "rebounds": 8, "assists": 6},
    {"player_id": 2, "points": 18, "rebounds": 10, "assists": 4},
    {"player_id": 1, "points": 30, "rebounds": 5, "assists": 7},
    {"player_id": 3, "points": 12, "rebounds": 12, "assists": 3},
    {"player_id": 2, "points": 22, "rebounds": 7, "assists": 9},
    {"player_id": 4, "points": 15, "rebounds": 4, "assists": 11},
    {"player_id": 3, "points": 28, "rebounds": 9, "assists": 2},
    {"player_id": 5, "points": 10, "rebounds": 6, "assists": 5},
    {"player_id": 4, "points": 20, "rebounds": 5, "assists": 8},
    {"player_id": 1, "points": 17, "rebounds": 11, "assists": 4},
]


def score_acumulado(partidas):
    dados = {}

    for partida in partidas:
        player_id = partida["player_id"]
        score = 2 * partida["points"] + partida["rebounds"] + partida["assists"]

        if player_id not in dados:
            dados[player_id] = 0

        dados[player_id] += score

    return dados


def ordenar(scores, k):
    ordenado = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return ordenado[:k]


resultado = score_acumulado(partidas)
ordenado = ordenar(resultado, 3)
print(resultado)
print(ordenado)
