from sys import stdin, stdout
import itertools
import queue

def es_clique_l(grafo : list, vecinos: list):
    base=vecinos.copy()
    # Use a single loop to iterate over pairs of nodes
    for i in range(len(vecinos)):
        actual= vecinos.pop()

        graf= grafo[actual]
        for vecino in base: 
            if vecino != actual: 
             if vecino not in graf :
                return False  
    return True

def total_valor_clique(valores, conjunto):
    return sum(valores[nodo] for nodo in conjunto)

def main2():
    N = int(stdin.readline())
    for i in range(N):
        # print(i)
        pagoPersonas = stdin.readline().split(" ")
        pagoPersonas = list(map(str.strip, pagoPersonas))
        pagoPersonas = list(map(int, pagoPersonas))
        personas = len(pagoPersonas)
        grafo = []
        grados=[]
        cola= queue.PriorityQueue(personas)
        for i in range(personas):
            line = stdin.readline().strip()
            if line:
                vecinos= list(map(int, line.split(" ")))
                vecinos=[n-1 for n in vecinos]
                grado= len(vecinos)
                grados.append(grado)
                cola.put((grado,i))
                grafo.append(vecinos)
        n=[]
        for i in range(cola.qsize()):
           grad,nodo=cola.get()
           n.append(nodo) 

        sol=back_Track_kindof(n,grafo,[],grados)    
        
        clique=get_max(sol)
        strr= str(total_valor_clique(pagoPersonas,clique)) + " "
        for i in range(len(clique)):
            if i == len(clique)-1:
                strr+= str(clique(i)) + " "
            else:
                strr+= str(clique(i))          
        print(strr)

def get_max(sol:list):
    ret= []
    maxi=0
    for sols in sol:
        if len(sols)> maxi:
           ret= sols 
           maxi= len(sols)
    return ret       

def back_Track_kindof(n:list,grafo:list,sol:list,grados:list):
    while n: 
        actual = n.pop(0)
        vecinos = grafo[actual]
        grado= len(vecinos)
        add=[]
 
        for vecino in vecinos:
            if grados[vecino]>= grado : 
            
              add.append(vecino)
        add.append(actual)     
            
        if es_clique_l(grafo,add.copy()):
         
            sol.append(add)
    return sol       
    
main2()
