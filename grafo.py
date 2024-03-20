class Grafo:
    def __init__(self, arestas):
        self.grafo = {}
        
        for aresta in arestas:
            vertice1, vertice2, peso = aresta
            self.adicionar_vertice(vertice1)
            self.adicionar_vertice(vertice2)
            self.adicionar_aresta(vertice1, vertice2, peso)

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append((vertice2, peso))
            self.grafo[vertice2].append((vertice1, peso))  
            
    def obter_caminhos_possiveis(self, vertice):
        if vertice in self.grafo:
            return self.grafo[vertice]
        else:
            return []