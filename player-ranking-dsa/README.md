# Projeto 2 — Ranking de Jogadores por Score de Impacto

## Objetivo

Processar estatísticas de partidas e gerar um ranking de jogadores com base em um **score de impacto**.

```
score = 2 * points + rebounds + assists
```

---

## Estrutura de Dados Escolhida

**Dicionário (`dict`)** para acumular scores por jogador.

- Acesso por chave (`player_id`) em **O(1)** médio.
- Alternativa com lista exigiria varredura linear O(n) a cada consulta.

---

## Análise de Complexidade

| Operação | Complexidade | Motivo |
|---|---|---|
| `score_acumulado` | O(n) tempo, O(p) espaço | n = partidas, p = jogadores únicos |
| `ordenar` (sort completo) | O(p log p) | `sorted()` usa Timsort |
| `ordenar` (heap, alternativa) | O(p log k) | `heapq.nlargest` — melhor quando k << p |

### Quando usar heap?

Quando `k` é muito menor que o total de jogadores `p`.
Ordenar tudo custa `O(p log p)`. Um heap de tamanho `k` custa `O(p log k)`.
Para `k = 3` e `p = 1.000.000`, a heap vence por larga margem.

---

## Exemplo de Entrada

```python
partidas = [
    {"player_id": 1, "points": 25, "rebounds": 8, "assists": 6},
    {"player_id": 2, "points": 18, "rebounds": 10, "assists": 4},
    ...
]
```

## Exemplo de Saída

```python
# score_acumulado
{1: 176, 2: 139, 3: 127, 4: 123, 5: 31}

# top 3
[(1, 176), (2, 139), (3, 127)]
```

---

## Extensões Possíveis

- Atualização incremental com novas partidas chegando em stream
- Desempate por critério secundário (ex: mais rebotes)
- Ranking por janela de tempo (últimas N partidas)
- Comparação direta sort vs heap com benchmark
