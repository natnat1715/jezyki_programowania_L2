# -*- coding: utf-8 -*-
"""
Created on Tue May 13 22:47:12 2025

@author: Natalia Kurczyna
"""
def podzbiory (lista):
  """
    Funkcja za pomocą rekursji/rekurencji zwraca wszystkie możliwe podzbiory danego zbioru (listy).
    Obsługuje przypadek, gdy lista jest pusta. 

    Args
    ----------
    lista : list
        Lista,z której mają zostać wygenerowane wszytskie podzbiory.

    Returns
    -------
    W main zwraca podzbiory listy wejciowej w postaci listy.
 
    Do napisania kodu użytko kodu z odpowiedzi użytkownika lion137 na pytanie "Cześć. Potrzebuje pomocy w kodzie do pythona. Potrzebuje program który będzie 
    wypisywał wszystkie podzbiory ze zbioru. Użytkownik będzie wpisywał jak długi ma być ten zbiór. 
    Mam to zrobić na jednej pętli.": https://4programmers.net/Forum/Python/331501-podzbiory_ze_zbioru_rekurencyjnie
    Skorzystano z chatGPT, który przekształcił kod użytkownika lion137 tak aby obsługiwał także przypadek gdy lista jest pusta
    Skorzystano z chatGPT, który pomógł w przekształceniu niepoprawnie działających fragmentów kodu oraz poprawieniu komentarzy dokumentacyjnych.
    """ 
  if len(lista) == 0:
        yield []
  elif len(lista) ==1:
        yield lista
        yield []
  else:
    for podzbior in podzbiory(lista[1:]):
        yield [lista[0]] + podzbior
        yield podzbior

if __name__ == "__main__":
    print(list(podzbiory(["a","b","c"]))) 
if list(podzbiory(["a","b","c"])) == [['a', 'b', 'c'], ['b', 'c'], ['a', 'c'], ['c'], ['a', 'b'], ['b'], ['a'], []]:
    print("Test przeszedl")
else:
    print("Test nie przeszedl") 
    
print(list(podzbiory(["a"])))
if list(podzbiory(["a"])) == [['a'], []]:
    print("Test przeszedl")
else:
    print("Test nie przeszedl") 
    
print(list(podzbiory([])))
if list(podzbiory([])) == [[]]:
    print("Test przeszedl")
else:
    print("Test nie przeszedl")     
         