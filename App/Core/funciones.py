
def capitalizar(valor):
    cadena = valor.split()
    retorno = ''
    for x in cadena:
        retorno += x.capitalize()+' '
    return retorno[:-1]