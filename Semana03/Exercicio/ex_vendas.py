import os

def ler_arquivo(parq:str)->list:
    """ 
    Recebe um arquivo

    Confirma se ele existe

    Trata e limpa ele antes de devolver uma lista  
    """
    lista_pronta = []
    if os.path.exists(parq):
        with open(parq, 'r', encoding='utf-8') as arquivo:
            for linha_suja in arquivo:
                linha_limpa = linha_suja.strip()
                linha = linha_limpa.split(";")
                lista_pronta.append(linha)
    else:
        print("Arquivo não encontrado")

    return lista_pronta   

def calc_total(plista:list)->float:
    """
    Recebe uma lista para apurar o valor total vendido
    """
    rtotal = 0
    for linha in plista[1:]:
        rtotal = rtotal + float(linha[2])
    return rtotal

caminho = "vendas.txt"

def imprimir_resultado(plista, ptotal):
    """
    Recebe uma lista e um valor total para imprimir o formulario
    """
    cabecalho = plista[0]

    print ("==============RELATÓRIO DE VENDAS====================")
    print(f"{cabecalho[0]:13} {cabecalho[1]:15} {cabecalho[2]:12}")
    print ("-----------------------------------------------------")
    for linha in plista[1:]:    
        valor = float(linha[2])
        print(f"{linha[0]:13} {linha[1]:15} R$ {linha[2]:12}")
    print ("-----------------------------------------------------")

    print(f"TOTAL GERAL                   R$ {ptotal:.2f}")
    print ("=====================================================")


lista_vendas = ler_arquivo(caminho)
valor_total = calc_total(lista_vendas)
imprimir_resultado(lista_vendas, valor_total)




 