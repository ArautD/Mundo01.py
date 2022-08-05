def movaTorre(passo, Start, auxilio, end):
    if passo >= 1:

        # Estes onde o passo-1 são apenas para mostrar a movimentação
        movaTorre(passo-1, Start, end, auxilio)
        # Aqui é só pra preencher a ordem na função de baixo
        moverDisco(passo, Start, auxilio)
        movaTorre(passo-1, end, auxilio, Start)
        movaTorre(passo-1, auxilio, Start, end)


def moverDisco(pas, fp, tp):
    print("Movendo o disco", pas, "de", fp, "para", tp)


quantia = 5
movaTorre(quantia, "A", "B", "C")
