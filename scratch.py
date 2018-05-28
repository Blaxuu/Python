def list_print() -> None:
    """Wypisz poniższą listę w formacie:
        0  ->  red
        1  ->  green
        2  ->  blue
    Skorzystaj z funkcji enumerate().
    """

    colors = ['red', 'green', 'blue']
    for c, k in enumerate(colors, 0):
        print(str(c) + " -> " + str(k))

def remove_duplicates(elements):
    return (list(set(elements)))
    """Usuń duplikaty z listy (bez zachowania kolejności).
     Skorzystaj z funkcji list() i set().


     Przykład: [1, 1, 2, 2] -> [2, 1]

     Parametry:
     elements -- lista elementów, z której należy usunąć duplikaty
     """

list_print()
lista = [1,1,1,2,2,2,3,3,2,3,4,32,7]
print(remove_duplicates(lista))


for i in range(5,1, -1):
    print(i)

print("====================")
k = 3

while(k != 5):
    print(k)
    k+=1


print("====================\n")


class lol:
    id: int
    name : str

name = "LoL"
summoner = "smoking111"

print("The {0} ppp {1}".format(name, summoner))