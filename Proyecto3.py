from sys import stdin, stdout
import itertools


def es_clique(grafo, conjunto):
    conjunto = list(conjunto)  # Convert the set to a list for indexing

    # Use a single loop to iterate over pairs of nodes
    for i in range(len(conjunto)):
        for j in range(i + 1, len(conjunto)):
            nodo1 = conjunto[i]
            nodo2 = conjunto[j]

            if grafo[nodo1][nodo2] == 0:
                return False

    return True


def total_valor_clique(valores, conjunto):
    return sum(valores[nodo] for nodo in conjunto)


def encontrar_clique_max_valor(grafo, valores, tamano_clique, conjunto_actual, nodos_restantes, max_valor, max_clique):

    if len(conjunto_actual) > tamano_clique:
        valor_actual = total_valor_clique(valores, conjunto_actual)
        if valor_actual > max_valor:
            max_valor = valor_actual
            max_clique = conjunto_actual.copy()

    for nodo in nodos_restantes:
        nuevo_conjunto = conjunto_actual.copy()
        nuevo_conjunto.add(nodo)

        new_remaining = {n for n in nodos_restantes if grafo[nodo][n]}

        if es_clique(grafo, nuevo_conjunto):
            clique_valor = total_valor_clique(valores, nuevo_conjunto)
            if clique_valor > max_valor:
                max_valor = clique_valor
                max_clique = nuevo_conjunto.copy()

            temp_clique, temp_valor = encontrar_clique_max_valor(
                grafo, valores, tamano_clique, nuevo_conjunto, new_remaining, max_valor, max_clique)

            if temp_valor > max_valor:
                max_valor = temp_valor
                max_clique = temp_clique.copy()

    return max_clique, max_valor


def crear_grafo(grafo, vertices, personas):
    for a in range(personas):
        for b in vertices[a]:
            grafo[a][b - 1] = 1
    return grafo


def main():
    N = int(stdin.readline())
    for i in range(N):
        # print(i)
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
        conjunto_vacio = set()
        nodos = [i for i in range(personas)]
        max_valued_clique = encontrar_clique_max_valor(
            grafo, pagoPersonas, 0, conjunto_vacio, nodos, 0, set())
        print("Clique with max total value:", max_valued_clique)


main()
