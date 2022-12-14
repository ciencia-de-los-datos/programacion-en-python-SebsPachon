"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
with open("data.csv", "r") as file:
    data= file.readlines()

data1 = [row.replace("\t", ";") for row in data]
data1 = [row.replace("\n", "") for row in data1]
data1 = [row.split(";") for row in data1]


def pregunta_01():
    row_2=[int(data1[i][1]) for i in range(len(data1))]
    return(sum(row_2))

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras=tuple([data1[i][0] for i in range(len(data1))])
    l=[(i,letras.count(i)) for i in (set(letras))]
    return(sorted(l))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    values = tuple(map(lambda x:x[0:2],data1))
    l=[]
    for x in sorted(set(map(lambda x:x[0],data1))): 
        z=[values[i][:] for i in range(len(data1)) if values[i][0]==x]
        w=(x,sum(int(z[i][1]) for i in range(len(z))))
        l.append(w)

    return (l)
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    l=[]
    fechas=list([data1[i][2] for i in range(len(data1))])
    values= [fechas.split("-") for fechas in fechas]
    months=tuple(map(lambda x:x[1],values))
    key=sorted(set(months))
    for i in range (len(key)):
        w=(key[i],months.count(key[i]))
        l.append(w)
    return(l)

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    values = tuple(map(lambda x:x[0:2],data1))
    l=[]
    for x in sorted(set(map(lambda x:x[0],data1))): 
        z=[values[i][:] for i in range(len(data1)) if values[i][0]==x]
        w=(x,max(int(z[i][1]) for i in range(len(z))),min(int(z[i][1]) for i in range(len(z))))
        l.append(w)
    return (l)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
           ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    values = list(map(lambda x:(x[4]),data1))
    items=list(map(lambda x:(x.split(',')),values))
    items_join=[inner for outer in items for inner in outer]
    splited=tuple(map(lambda x: list(x.split(':')),items_join))
    l=[]
    for x in sorted(set(map(lambda x:x[0],splited))): 
        z=[splited[i][:] for i in range(len(splited)) if splited[i][0]==x]
        w=(x,min(int(z[i][1]) for i in range(len(z))),max(int(z[i][1]) for i in range(len(z))))
        l.append(w)
    return(l)

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    values =tuple(map(lambda x:tuple(x[0:2]),data1))
    l=[]
    for x in sorted(set(map(lambda x:x[1],values))):
        z=[values[i][:] for i in range(len(values)) if values[i][1]==x]
        w=(int(z[0][1]),list(map(lambda x:x[0],z)))
        l.append(w)
    return(l)


    

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    values =tuple(map(lambda x:tuple(x[0:2]),data1))
    l=[]
    for x in sorted(set(map(lambda x:x[1],values))):
        z=[values[i][:] for i in range(len(values)) if values[i][1]==x]
        w=(int(z[0][1]),sorted(set(map(lambda x:x[0],z))))
        l.append(w)
    return(l)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    values = list(map(lambda x:(x[4]),data1))

    items=list(map(lambda x:(x.split(',')),values))
    items_join=[inner for outer in items for inner in outer]
    splited=tuple(map(lambda x: tuple(x.split(':')),items_join))
    l=[]
    for x in sorted(set(map(lambda x:x[0],splited))):
        z=[splited[i][:] for i in range(len(splited)) if splited[i][0]==x]
        w=(z[0][0],len(list(map(lambda x:(x[1]),z))))
        l.append(w)
    return(dict(l))

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    words = tuple(map(lambda x:x[0],data1))
    element_4=tuple(map(lambda x:len(x[3].split(',')),data1))
    element_5=tuple(map(lambda x:len(x[4].split(',')),data1))
    l=[(words[i],element_4[i],element_5[i]) for i in range(len(words))]
    return (l)

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letters=list(map(lambda x:x[3].split(','),data1))
    numbers=list(map(lambda x:int(x[1]),data1))
    values=[(letters[i],numbers[i])for i in range(len(data1))]
    unique=sorted(set(x for l in letters for x in l))
    l=[]
    for x in unique:
        z=[values[i][:] for i in range(len (values)) if x in values[i][0]]
        w=(x,sum((z[i][1]) for i in range(len(z))))
        l.append(w)
    return (dict(l))   



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letters=list(map(lambda x:x[0],data1))
    items=list(map(lambda x:x[4].replace(',',' ').replace(':',' '),data1))
    numbers=[]
    for j in range(len(items)):
        test=items[j]
        w = [int(i) for i in items[j].split(' ') if i.isdigit()]
        numbers.append(sum(w)) 
    final=[(letters[i],numbers[i]) for i in range(len(items))]
    l=[]
    for x in sorted(set(map(lambda x:x[0],letters))):
        z=[final[i][:] for i in range(len(final)) if final[i][0]==x]
        w=(x,(sum(list(map(lambda x:(x[1]),z)))))
        l.append(w)    
    return (dict(l))

