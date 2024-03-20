import math
import dados
from grafo import *

codigo_atual_caminho = 0

def obter_codigo():
    global codigo_atual_caminho
    codigo_atual_caminho += 1
    return codigo_atual_caminho

def construir_caminho(caminho, codigo_pai, custo_atual):
    grafo = custo_atual + caminho[1]
    h = dados.custo_estimado_cidade[caminho[0]]
    f = grafo + h
    
    return {
            "cidade": caminho[0], 
            "codigo": obter_codigo(),
            "codigo_pai": codigo_pai, 
            "f": f, 
            "grafo": grafo, 
            "h": h
        }
    
def imprimir_caminhos(caminhos):
    print("\n "+ "-------------------------------------------------------------------------------------" + "\n")
    
    for caminho in caminhos:
        print(str(caminho))

def obter_caminho_menor(historico_caminhos):
    menor = {"f": math.inf}
    for caminho in historico_caminhos:
        if (caminho["f"] < menor["f"]):
            menor = caminho
            
    return menor

def obter_pai(no, caminhos):
    return next(caminho for caminho in caminhos if caminho["codigo"] == no["codigo_pai"])
    
def obter_percurso(no_atual, primeira_cidade, caminhos):
    percurso = []
    
    while True:
        percurso.append(no_atual)
        
        if no_atual["cidade"] == primeira_cidade:
            break
        
        no_atual = obter_pai(no_atual, caminhos)
        
    return percurso[::-1]

def imprimir_percurso(no_atual, primeira_cidade, caminhos):
    print("\n "+ "-------------------------------------------------------------------------------------" + "\n")
    
    percurso = obter_percurso(no_atual, primeira_cidade, caminhos)
    for index, caminho in enumerate(percurso):
        if index < len(percurso) - 1:
            print(caminho["cidade"], end=" -> ")
        else:
            print(caminho["cidade"], end="\n")
            
    print("Custo: " + str(no_atual["f"]))

# MAIN
grafo = Grafo(dados.arestas)

primeira_cidade = "Arad"
cidade_objetivo = "Bucareste"

no_atual = {
    "cidade": primeira_cidade, 
    "codigo": codigo_atual_caminho,
    "codigo_pai": None, 
    "f": dados.custo_estimado_cidade[primeira_cidade], 
    "grafo": 0, 
    "h": dados.custo_estimado_cidade[primeira_cidade]
}

historico_caminhos = [no_atual]
caminhos_possiveis = [no_atual]
concluido = False

while concluido == False:
    # expandir no atual
    novos_caminhos = grafo.obter_caminhos_possiveis(no_atual["cidade"])
    imprimir_caminhos(caminhos_possiveis)
    caminhos_possiveis.remove(no_atual)
    
    # registrar novos caminhos
    for caminho in novos_caminhos:
        novo_no = construir_caminho(caminho=caminho, codigo_pai=no_atual["codigo"], custo_atual=no_atual["grafo"])
        
        caminhos_possiveis.append(novo_no)
        historico_caminhos.append(novo_no)
    
    # obter caminho menos custoso    
    no_atual = obter_caminho_menor(caminhos_possiveis)
    
    # chegou a cidade objetivo
    if no_atual["cidade"] == cidade_objetivo:
        concluido = True

imprimir_percurso(no_atual=no_atual, primeira_cidade=primeira_cidade, caminhos=historico_caminhos)