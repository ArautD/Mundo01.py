
class Stack:
    "classe que representa uma pilha"
    def __init__(self):
        "construtor de classe Stack"
        self.elements = []

    def isEmpty(self):
        "retorna verdadeiro caso a pilha esteja vazia"
        return len(self.elements) == 0

    def push(self, Value):
        "Adciona um elemento na pilha"
        self.elements.insert(0,Value)

    def pop(self):
        "retorna o elemento ao topo da pilha"
        return self.elements[0] #o que fazer quando a lista estiver vazia? 
    
    def size(self):
        "retorna o número de elementos da pilha"
        return len(self.elements)

    def clear(self):
        "limpa os elementos da pilha"
        elements=[]
        