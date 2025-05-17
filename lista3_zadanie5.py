# -*- coding: utf-8 -*-
"""
Created on Thu May  8 23:16:53 2025

@author: Natalia Kurczyna
"""
def problem (c: int) -> list[int]:
   """
    Funkcja zwraca ciąg liczb przed wpadnięciem w cykl 4,2,1,4,2,1 itd., czyli jest to tzw. problem Collatza. Funkcja tworzy nową listę, do której dodawane będą kolejne elementy ciągu.
    Następnie wykonuje odpowiednie działanie w przypadku liczby parzystej i nieparzystej i działa aż do momentu osiągnięcia wartosci 1. Przewidziano również obsługę przypadku brzegowego,
    kiedy w przypadku podania liczby równej 1 zostanie dopisana ona do listy, a funkcja zakończy działanie.
    
    Args:
    ----------
    c : int
        Podana liczba rozpoczynajaca ciag. Musi byc ona dodatnią liczbą naturalną, czyli różną od 0. 

    Returns
    -------
    list[int]
        Lista z kolejnymi elementami ciągu przed wpsadnięciem w ciąg 4,2,1,4,2,1 itd.

    Raises
    -------
    Funkcja wyrzuca błąd, gdy podana liczba nie jest liczbą całkowitą, dodatnią lub różną od 0.
    
    Do opracowania kodu użyto logiki i kodu napisanego w ramach zadania z listy 1 oraz https://pl.wikipedia.org/wiki/Problem_Collatza
    Skorzystano z chatGPT, który poprawił błędnie zaimplementowane fragmenty kodu, pokazał jak użyć if not isinstance, z którego skorzystano

    
 """    
   if not isinstance(c, int) or c<= 0:
        raise ValueError("Podano nieprawidlowa liczbe. Liczba musi byc dodatnia, calkowita i rozna od 0.")
    
   ciag_nowy : list[int] = []

   podana_liczba = c 
   ciag_nowy.append(podana_liczba) 
   if podana_liczba == 1:
        return ciag_nowy
   while podana_liczba != 1:
        if podana_liczba % 2 == 0:
            podana_liczba = podana_liczba // 2
        else:
            podana_liczba = 3 * podana_liczba + 1
        ciag_nowy.append(podana_liczba)
   return ciag_nowy  

if __name__ == "__main__":
    c = 37
    ciag_nowy = problem(c)
    print(f"Nowy ciag: {ciag_nowy}") 
    if ciag_nowy ==[37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    c = 10
    ciag_nowy = problem(c)
    print(f"Nowy ciag: {ciag_nowy}")
    if ciag_nowy == [10, 5, 16, 8, 4, 2, 1]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    c = 1
    ciag_nowy = problem(c)
    print(f"Nowy ciag: {ciag_nowy}")
    if ciag_nowy == [1]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")   
        
    c = 2
    ciag_nowy = problem(c)
    print(f"Nowy ciag: {ciag_nowy}")  
    if ciag_nowy == [2, 1]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    try:
        c = 0
        ciag_nowy = problem(c)
        print(f"Test nie przeszedl, bo funkcja zwrocila {ciag_nowy}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        
    try:
        c = -4
        ciag_nowy = problem(c)
        print(f"Test nie przeszedl, bo funkcja zwrocila {ciag_nowy}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        
    try:
        c = 2.8
        ciag_nowy = problem(c)
        print(f"Test nie przeszedl, bo funkcja zwrocila {ciag_nowy}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        