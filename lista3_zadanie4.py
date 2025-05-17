# -*- coding: utf-8 -*-
from typing import List

"""
Created on Thu May  8 23:14:59 2025

@author: Natalia Kurczyna
"""
def ciagPetla (n: int) -> list[int]:
    """
    Funkcja za pomocą pętli for liczy ciąg Fibonacciego
    Args
    ----------
    n : int
        Liczba wyrazów ciągu Fibonacciego, która musi być większa od 0 i całkowita.

    Returns
    -------
    list[int]
        Lista int, która jest przedstawieniem kolejnych wyrazów ciągu Fibonacciego.
        
    Raises
    Funkcja wyrzuca błąd jesli podana liczba wyrazów ciągu jest ujemna lub nie jest liczbą całkowitą.
    
    Skorzystano z logiki i kodu napisanego w języku Kotlin na listę 1.
    Wiedza o ciągu Fibonacciego zaczerpnięta z :https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
    Skorzystano z chatGPT, który poprawił błędnie zaimplementowane fragmenty funkcji, podpowiedział użycie not isinstance do warunku n, oraz podpowiedział 
    aby użyć ','.join(map(str,list_)) w testach, z którego skorzystano

    """
    if n < 0 or not isinstance (n, int):
        raise ValueError ("Podano nieprawidłlowa wartosc ciagu: liczba elementow nie moze byc ujemna i musi byc liczba calkowita")
    
    if n < 2:
        return [0 for _ in range(n)]
    
    lista = [0] * n
    lista[0] = 0
    lista[1] = 1
    for i in range(2,n):
        lista[i] = lista[i-1] + lista[i-2]
    return lista     
    

def ciag_rekursja(n:int, d:int=0, e:int=1, list1:List[int] = None) -> List[int]:
    """
    Funkcja liczy ciąg Fibonacciego za pomocą rekurencji.
    Args:
    ----------
    n : int
        Liczba wyrazów ciągu Fibonacciego.
    d : int, domyslnie 0
        Aktualny wyraz ciągu, który zostanie dodany do listy w danym kroku rekurencji. Na początku jest to 0.
    e : int, domyslnie 1
        Następny wyraz ciągu, który będzie dodany do listy jako nowy d w kolejnym kroku rekurencji. Na początku 1 to drugi wyraz ciągu.
    list1 : List[int]
        Lista przechowująca dotychczasowe elementy ciągu. Jesli nie zostanie podana żadna lista, to funkcja stworzy pustą listę.

    Raises
    ------
    ValueError
        Wyrzuca błędy, gdy podana liczba wyrazów ciągu jest mniejsza od 0 lub nie jest liczba calkowita
        

    Returns
    -------
    List[int]
        Listę int, która jest przedstawieniem kolejnych wyrazów ciągu Fibonacciego.
        
    Skorzystano z logiki i kodu napisanego na potrzeby zadania z listy 1.
    Wiedza o ciągu Fibonacciego: https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
    Skorzystano z chatGPT, który poprawił nieprawidłowo zaimplementowane fragmentu kodu,sprawdzenie len oraz zaproponował skorzystanie w testach z ','.join(map(str,list_))
    z którego skorzystano.

    """
    if n < 0 or not isinstance (n, int):
        raise ValueError("Podano nieprawidlowa wartosc ciagu: liczba elementow ciagu nie moze byc ujemna i musi byc liczba calkowita")
    if n ==0:
        return []
    if n == 1:
        return [0]
    if list1 is None:
        list1 = []
    if len(list1) ==n:
        return list1
    
    list1.append(d)
    return ciag_rekursja(n,e,e+d,list1)

if __name__== "__main__":
   n = 5
   list_ = ciagPetla(n)
   print(','.join(map(str,list_)))
   if list_ == [0,1,1,2,3]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl")
   
   list1 = ciag_rekursja(n)
   print(','.join(map(str,list1)))
   if list1 == [0,1,1,2,3]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl")
       
   n = 8
   list_ = ciagPetla(n)
   print(','.join(map(str,list_)))
   if list_ == [0,1,1,2,3,5,8,13]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl")
   
   list1 = ciag_rekursja(n)
   print(','.join(map(str,list1)))
   if list1 == [0,1,1,2,3,5,8,13]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl")
       
   n = 1     
   list_ = ciagPetla(n)
   print(','.join(map(str,list_)))
   if list_ == [0]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl") 
       
   list1 = ciag_rekursja(n)
   print(','.join(map(str,list1)))
   if list1 == [0]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl") 
       
   n = 0
   list_ = ciagPetla(n)
   print(','.join(map(str,list_)))
   if list_ == []:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl") 
    
   list1 = ciag_rekursja(n)
   print(','.join(map(str,list1)))
   if list1 == []:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl") 
       
   try:  
       n = -4
       list_ = ciagPetla(n)
       print("Test nie przeszedl")
   except ValueError as e:
           print(f"Test przeszedl, bo funkcja wyrzucila wyjatek : {e}") 
    
   
   try:  
       n = -4
       list1 = ciag_rekursja(n)
       print("Test nie przeszedl")
   except ValueError as e:
           print(f"Test przeszedl, bo funkcja wyrzucila wyjatek : {e}") 
           
   n = 2
   list_ = ciagPetla(n)
   print(','.join(map(str,list_)))
   if list_ == [0,1]:
       print("Test przeszedl")
   else:
       print("Test nie przeszedl")
    
   list1 = ciag_rekursja(n)
   print(','.join(map(str,list1)))
   if list1 == [0,1]:
       print("Test przeszedl")
   else:
       print("Test przeszedl")
    
   try:    
       n = 4.5
       list_ = ciagPetla(n)
       print("Test nie przeszedl")
   except ValueError as e:
       print(f"Test przeszedl, bo funkcja wyrzuciala wyjatek: {e}")
       
   try:
       n = 4.5
       list1 = ciag_rekursja(n)
       print("Test nie przeszedl")
   except ValueError as e:
       print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
           
            
       


