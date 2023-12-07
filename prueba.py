from sys import stdin, stdout
import itertools


def es_clique(grafo, conjunto):
    for i in conjunto:
        for j in conjunto:
            if i != j and not grafo[i][j]:
                return False
    return True


def encontrar_cliques(grafo, valores):
    todos_cliques = []
    valores_cliques = []

    for i in range(1, 2 ** len(grafo)):
        conjunto_actual = {j for j in range(len(grafo)) if (i & (1 << j))}
        if es_clique(grafo, conjunto_actual):
            todos_cliques.append(conjunto_actual)
            valores_cliques.append(
                sum(valores[nodo] for nodo in conjunto_actual))

    return todos_cliques, valores_cliques


def encontrar_todas_cliques(grafo, valores):
    cliques, valores_cliques = encontrar_cliques(grafo, valores)
    if not cliques:
        return [], 0

    max_valor_clique = max(valores_cliques)
    max_clique_index = valores_cliques.index(max_valor_clique)

    return cliques[max_clique_index], max_valor_clique


def crear_grafo(grafo, vertices, personas):
    for a in range(personas):
        for b in vertices[a]:
            grafo[a][b - 1] = 1
    return grafo


def main():
    N = int(stdin.readline())
    for i in range(N):
        pagoPersonas = stdin.readline().split(" ")
        pagoPersonas = list(map(str.strip, pagoPersonas))
        pagoPersonas = list(map(int, pagoPersonas))
        personas = len(pagoPersonas)
        vertices = []
        for i in range(personas):
            line = stdin.readline().strip()
            if line:
                vertices.append(list(map(int, line.split(" "))))
        grafo = [[0] * personas for z in range(personas)]
        grafo = crear_grafo(grafo, vertices, personas)
        nodos = [i for i in range(personas)]
        max_clique, max_valor = encontrar_todas_cliques(grafo, pagoPersonas)
        print("Clique with max total value:",
              max_clique, "with total value:", max_valor)


main()
