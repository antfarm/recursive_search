def suche(num, vorwahl):
    if len(num) == 1:
        if num[0][:len(vorwahl)] == vorwahl: # wenn Liste num nur aus einem Element besteht, ebesteht aus Stirng,
            return nummernliste              # es wird geprüft ob der Slice "num[0][:len(vorwahl)]", also der vordre Teilstring,
        else:                                # der in der Länge der vorgegebenen Vorwahl entspricht, gleich der Vorwahl ist.
            return []
    else:
        index = int(len(num)/2)
        return suche(num[:index], vorwahl)+\
               suche(num[index:], vorwahl)   # im Fall, das die Namensliste "num" mehr als ein Element enthält,
                                             # wird die Liste in der Mitte aufgeteilt. Das hei?t, es werden zwei Slices gebildet.
                                             # Die Grenze ist der Index len(num)/2. Die Funktion suche()wird rekursiv auf beide Teile angewendet.

nummernliste = ["0223 788834", "0201 657543", "0435 287784", "4348 394947", "0201 658843"]

x = input("Suche:")
f = suche(nummernliste, x)
print(f)
