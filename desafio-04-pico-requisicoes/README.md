# Exercício – Pico de Requisições em Janela de Tempo (Sliding Window)

Este exercício simula um sistema de requisições de clientes (tipo API SaaS)
e treina um padrão clássico de algoritmos: **janela deslizante** (sliding
window) e raciocínio em cima de dados ordenados no tempo.

## Dados de entrada

Você recebe uma lista de eventos. Cada evento tem:

- `timestamp`: momento em segundos em que a requisição aconteceu
- `client_id`: identificador do cliente

Exemplo:

```python
eventos = [
    {"timestamp": 1,  "client_id": "A"},
    {"timestamp": 2,  "client_id": "A"},
    {"timestamp": 3,  "client_id": "B"},
    {"timestamp": 10, "client_id": "A"},
    {"timestamp": 11, "client_id": "B"},
    {"timestamp": 12, "client_id": "B"},
    {"timestamp": 20, "client_id": "A"},
    {"timestamp": 21, "client_id": "A"},
]
W = 5  # tamanho da janela em segundos
```

Importante: `eventos` já vem ordenado por `timestamp` em ordem crescente.

## Objetivos

O programa deve responder três coisas:

1. **Pico global de tráfego**

   Descobrir qual é o **máximo número de requisições** que ocorre dentro de
   qualquer janela contínua de tamanho `W` segundos.

   Saída esperada (para o exemplo): um par `(max_qtd, melhor_start)`, onde:

   - `max_qtd` é o número máximo de requisições em uma janela de tamanho `W`
   - `melhor_start` é o timestamp de início dessa janela que produziu o pico

2. **Pico de tráfego por cliente**

   Para cada `client_id`, descobrir qual foi o máximo de requisições daquele
   cliente dentro de uma janela de tamanho `W` segundos.

3. **Intervalos entre eventos**

   Calcular os `deltas` de tempo entre eventos consecutivos:

   ```python
   deltas[i] = eventos[i+1]['timestamp'] - eventos[i]['timestamp']
   ```

   Saída: `[1, 1, 7, 1, 1, 8, 1]` para a lista acima.

## Versão ingênua (força bruta)

Uma primeira solução natural é:

- Para cada possível `start` (cada evento), percorrer todos os eventos e
  contar quantos caem dentro da janela `[start, start + W)`.
- Guardar o `start` que produz o maior número de eventos.

Isso funciona, mas tem complexidade de tempo **O(N²)** porque temos dois
laços aninhados.

## Ideia da Janela Deslizante (Sliding Window)

Como os eventos já estão ordenados por `timestamp`, dá para melhorar drasticamente:

- Usamos **dois índices** no array: `inicio` e `fim`.
- Mantemos uma janela válida de eventos tal que:

  ```python
  eventos[fim]['timestamp'] - eventos[inicio]['timestamp'] < W
  ```

- Expandimos `fim` enquanto a janela couber em `W` segundos.
- Quando a janela fica grande demais, expulsamos o evento mais antigo (++`inicio`).

A quantidade de eventos na janela é simplesmente:

```python
qtd_na_janela = fim - inicio + 1
```

A complexidade de tempo cai para **O(N)**.

## Regras conceituais da janela

1. `inicio = 0`, `fim = 0`, `max_qtd = 0`, `melhor_start = eventos[0]['timestamp']`
2. Enquanto `fim` ainda está dentro da lista:
   - Se `eventos[fim]['timestamp'] - eventos[inicio]['timestamp'] < W`:
     - Janela válida → calcula `qtd = fim - inicio + 1`
     - Atualiza `max_qtd` e `melhor_start` se necessário
     - `fim += 1`
   - Senão: `inicio += 1`

## Funções do exercício

- `pico_global(eventos, W)` — máximo de eventos em qualquer janela de tamanho `W`
- `pico_por_cliente(eventos, W)` — máximo por `client_id`
- `intervalos(eventos)` — lista de deltas entre eventos consecutivos

## Conceitos treinados

- Raciocínio em cima de listas ordenadas
- Diferença entre O(N²) brute force e O(N) sliding window
- Técnica de **dois ponteiros** para transformar dois laços aninhados em um único laço
- Pensar em "estado que flui" em vez de recomputar tudo do zero a cada passo

## Como executar

```bash
python pico_requisicoes.py
```
