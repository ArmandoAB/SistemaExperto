# %% [markdown]
# ## Analizador Lexico
# Un analizador lexico transforma una entrada en tokens

# %%
entrada = "si es de dia entonces mañana no es de noche"

# %%
tokens = entrada.lower().split()
tokens

# %%
from enum import Enum

class TipoToken(Enum):
    O = 1
    Y = 2
    S = 3
    N = 4
    E = 5
    P = 6

# %%
lexemas = []
for token in tokens:
    if token == 'o':
        lexemas.append({"valor" : token , "tipo": TipoToken.O })
    elif token == 'y':
        lexemas.append({"valor" : token , "tipo": TipoToken.Y})
    elif token == 'si':
        lexemas.append({"valor" : token , "tipo": TipoToken.S})
    elif token == 'entonces':
        lexemas.append({"valor" : token , "tipo": TipoToken.E})
    elif token == 'no':
        lexemas.append({"valor" : token , "tipo": TipoToken.N})
    else :
        lexemas.append({"valor" :token , "tipo": TipoToken.P })
        
lexemas

# %% [markdown]
# ## Analizador Sintactico

# %%
class EstadosAnalizador(Enum):
    INICIO = 1
    PRECEDENTE = 2
    NEGACION = 3
    CONSECUENTE = 4
    DISYUNCION = 5
    CONJUNCION = 6
    ATOMO = 7
    ERROR1 = 8  #se esperaba un 'si', 'no' o un atomo
    ERROR2 = 9  #se esperaba un 'no' o un atomo
    ERROR3 = 10 #se esperaba un 'y', 'o', 'entonces' o un atomo
    ERROR4 = 11 #se esperaba un atomo
    FIN = 12

# %%
EstadoActual = EstadosAnalizador.INICIO

regla = ""
pila = ""
prec = 0
pila = []
prop = ""

for lexema in lexemas:
    if EstadoActual == EstadosAnalizador.INICIO:
        if lexema['valor'] == "si":
            EstadoActual = EstadosAnalizador.PRECEDENTE
            prec = 1
        elif lexema['valor'] == "no":
            EstadoActual = EstadosAnalizador.NEGACION
        elif lexema['tipo'] == TipoToken.P:
            EstadoActual == EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        else:
            EstadoActual = EstadosAnalizador.ERROR1

    elif EstadoActual == EstadosAnalizador.PRECEDENTE:
        if lexema['valor'] == "no":
            EstadoActual = EstadosAnalizador.NEGACION
        elif lexema['tipo'] == TipoToken.P:
            EstadoActual = EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        else:
            EstadoActual = EstadosAnalizador.ERROR2

    elif EstadoActual == EstadosAnalizador.NEGACION:
        if lexema['tipo'] == TipoToken.P:
            EstadoActual = EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        else:
            EstadoActual = EstadosAnalizador.ERROR3

    elif EstadoActual == EstadosAnalizador.CONSECUENTE:
        if lexema['tipo'] == TipoToken.P:
            EstadoActual = EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        elif lexema['valor'] == "no":
            EstadoActual = EstadosAnalizador.NEGACION
        else:
            EstadoActual = EstadosAnalizador.ERROR2

    elif EstadoActual == EstadosAnalizador.ATOMO:
        if lexema['valor'] == "entonces":
            EstadoActual = EstadosAnalizador.CONSECUENTE
            prop = " ".join(pila)
        elif lexema['valor'] == "y":
            EstadoActual = EstadosAnalizador.CONJUNCION
            prop = " ".join(pila)
        elif lexema['valor'] == "o":
            EstadoActual = EstadosAnalizador.DISYUNCION
            prop = " ".join(pila)
        elif lexema['tipo'] == TipoToken.P:
            EstadoActual = EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        else:
            EstadoActual = EstadosAnalizador.ERROR3

    elif EstadoActual == EstadosAnalizador.CONJUNCION:
        if lexema['tipo'] == TipoToken.P:
            EstadoActual = EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        elif lexema['valor'] == "no":
            EstadoActual = EstadosAnalizador.NEGACION
        else:
            EstadoActual = EstadosAnalizador.ERROR2

    elif EstadoActual == EstadosAnalizador.DISYUNCION:
        if lexema['tipo'] == TipoToken.P:
            EstadoActual = EstadosAnalizador.ATOMO
            pila.append(lexema['valor'])
        elif lexema['valor'] == "no":
            EstadoActual == EstadosAnalizador.NEGACION
        else:
            EstadoActual = EstadosAnalizador.ERROR4

    elif EstadoActual == EstadosAnalizador.ERROR1:
        print("se esperaba un 'si', 'no' o un atomo")
        break
    elif EstadoActual == EstadosAnalizador.ERROR2:
        print("se esperaba un 'no' o un atomo")
        break
    elif EstadoActual == EstadosAnalizador.ERROR3:
        print("se esperaba un 'y', 'o', 'entonces' o un atomo")
        break
    elif EstadoActual == EstadosAnalizador.ERROR4:
        print("se esperaba un atomo")
        break
    elif EstadoActual == EstadosAnalizador.FIN:
        break
    else:
        EstadoActual == EstadosAnalizador.FIN
    print(EstadoActual)
    print(pila)
    print(prop)

# %%
print(EstadoActual)


