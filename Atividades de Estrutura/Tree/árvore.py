class NodoArvore:
    def __init__(self, chave=None, esquerdo=None, direito=None):
        self.chave = chave
        self.esquerdo = esquerdo
        self.direito = direito
 
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerdo and self.esquerdo.chave,
                                   self.chave,
                                   self.direito and self.direito.chave)
       
 
def em_ordem(raiz):
  if not raiz:
    return
 
  # Visita filho da esquerda
  em_ordem(raiz.esquerdo)
 
  # Visita nodo corrente
  print(raiz.chave)
 
  # Visita filho da esquerda
  em_ordem(raiz.direito)
 
def contar(raiz):
    if raiz is None:
        return 0
    return contar(raiz.esquerdo) + contar(raiz.direito) + 1

def impar(raiz, esquerdo , direito, nimpar):
    if (raiz.esquerdo%2 != 0):
    nimpar = raiz.esquerdo

    if (raiz.direito%2 != 0):
    nimpar = raiz.direito




raiz = NodoArvore(40)
 
raiz.esquerdo = NodoArvore(20)
raiz.direito = NodoArvore(60)
 
raiz.direito.esquerdo = NodoArvore(50)
raiz.direito.direito = NodoArvore(70)
raiz.esquerdo.esquerdo = NodoArvore(10)
raiz.esquerdo.direito = NodoArvore(30)
 
em_ordem(raiz)
print("O número de nós é: ", contar(raiz))