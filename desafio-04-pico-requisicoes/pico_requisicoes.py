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
W = 5


def PicoGlobal(eventos):
    max_bolinhas = 0
    melhor_start = None
    for e_start in eventos:
        start = e_start['timestamp']
        bolinhas = 0
        for e in eventos:
            t = e['timestamp']
            if start <= t < start + W:
                bolinhas += 1
        if bolinhas > max_bolinhas:
            max_bolinhas = bolinhas
            melhor_start = start
    return max_bolinhas, melhor_start


def PicoGlobalUsuarios(eventos, melhor_start):
    usuarios = {}
    for e in eventos:
        t = e['timestamp']
        client_id = e['client_id']
        if melhor_start <= t < melhor_start + W:
            usuarios[client_id] = usuarios.get(client_id, 0) + 1
    return usuarios


def intervalos(eventos):
    # assume que eventos já estão ordenados por timestamp
    deltas = []
    for i in range(1, len(eventos)):
        t_atual = eventos[i]['timestamp']
        t_anterior = eventos[i - 1]['timestamp']
        delta = t_atual - t_anterior
        if delta not in deltas:
            deltas.append(delta)
    return deltas


max_bolinhas, melhor_start = PicoGlobal(eventos)
u = PicoGlobalUsuarios(eventos, melhor_start)
d = intervalos(eventos)

print(f'Numero Maximo Requisicoes: {max_bolinhas}')
print(f'Melhor Start: {melhor_start}')
print(f'Usuarios na janela do pico: {u}')
print(f'Deltas entre eventos: {d}')
