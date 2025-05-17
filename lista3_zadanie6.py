# -*- coding: utf-8 -*-
"""
Created on Fri May  9 16:13:11 2025

@author: Natalia Kurczyna
"""

def komplement (kodujaca: list[str]) -> list[str]:
    """
    Funkcja tworzy nić matrycową, która jest komplementarna do nici kodującej, gdy podane zostaną zasady mogące budować DNA.

    Args
    ----------
    kodujaca : list[str]
     Lista kodująca zbudowana z zasad A,C,G,T.   

    Raises
    ------
    ValueError
        Wyrzuca błąd kiedy podano nieprawidłową zasadę, czyli taką, która nie może budować DNA.


    Returns
    -------
    list[str]
        Lista matrycowa komplementarna do nici kodującej.
        
    Skorzystano z chatGPT, który pokazał metodę na odrwacanie listy[str], której użyto oraz poprawił nieprawidłowo działający kod.
    Wykorzystano logikę oraz kod z zadania utworzonego w ramach listy 1     

    """
    matrycowa = []
    for zasada in kodujaca:
        if zasada == "A":
             matrycowa.append("T")
        elif zasada == "T" :     
            matrycowa.append("A")
        elif zasada == "C":    
            matrycowa.append("G")
        elif zasada == "G":    
            matrycowa.append("C")
        else:
            raise ValueError ("Podano nieprawidlowa zasade, ktora nie moze budować DNA")
            
    return matrycowa

def transkrybuj (matrycowa: list[str]) -> list[str]:
    """
    Funkcja tworzy nić RNA na podstawie nici matrycowej, gdzie zamiast tyminy pojawia się uracyl, tylko jesli pojawią
    się zasady mogące budować RNA.

    Args
    ----------
    matrycowa : list[str]
        Lista matrycowa zbudowana z zasad A,G,C,T.

    Raises
    ------
    ValueError
        Wyrzuca błąd, gdy podano nieprawidłową zasadę, która nie może budować RNA.

    Returns
    -------
    list[str]
        Zwraca nić RNA, która jest tworzona na podstawie nici matrycowej.
        
    Skorzystano z logiki oraz kodu z zadania wykonanego w ramach listy 1. 
    Skorzystano z chatGPT, który poprawił nieprawidłowo zaimplementowane fragmenty kodu oraz pokazał jak odwrócić listę[str].    

    """
    nicRNA = []
    for zasada in matrycowa[::-1]:
        if zasada == "A":
            nicRNA.append("U")
        elif zasada == "T":
            nicRNA.append("A")
        elif zasada == "C":
            nicRNA.append("G")
        elif zasada == "G":
            nicRNA.append("C")
        else:
            raise ValueError ("Podana nieprawidlowa zasade, ktora nie moze budowac RNA")
    return nicRNA     
    
    
if __name__ == "__main__":
    kodujaca = ["A", "C", "C", "T", "A"]  
    print(f"Nic kodujaca od 5' do 3': {kodujaca}")
    matrycowa = komplement(kodujaca)
    print(f"Nic matrycowa od 5' do 3': {matrycowa[::-1]}")
    if matrycowa[::-1] == ['T', 'A', 'G', 'G', 'T']:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    nicRNA = transkrybuj(matrycowa)
    print(f"Nic RNA: {nicRNA}")
    if nicRNA == ['A', 'U', 'C', 'C', 'A']:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    kodujaca1 = ["C", "C", "A", "A", "T", "T", "G", "G"] 
    print(f"Nic kodujaca: {kodujaca1}")
    matrycowa1 = komplement(kodujaca1)
    print(f"Nic matrycowa: {matrycowa1[::-1]}")
    if matrycowa1[::-1] == ['C', 'C', 'A', 'A', 'T', 'T', 'G', 'G']:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    nicRNA1 = transkrybuj(matrycowa1)
    print(f"Nic RNA: {nicRNA1}")
    if nicRNA1 == ['G', 'G', 'U', 'U', 'A', 'A', 'C', 'C']:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    try:    
        kodujacaZla = ["Z", "H", "K", "O"]
        matrycowa = komplement(kodujacaZla)
        print(f"Test nie przeszedl, bo funkcja zwrocila {matrycowa}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek {e}")
    try:
        matrycowaZla = ["Z", "H", "K", "O"]
        nicRNA = transkrybuj(matrycowaZla)
        print(f"Test nie przeszedl, bo funkcja zwrocila {matrycowaZla}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek {e}")
    kodujaca = ["A"]  
    print(f"Nic kodujaca od 5' do 3': {kodujaca}")
    matrycowa = komplement(kodujaca)
    print(f"Nic matrycowa od 5' do 3': {matrycowa[::-1]}")
    if matrycowa[::-1] == ['T']:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    nicRNA = transkrybuj(matrycowa)
    print(f"Nic RNA: {nicRNA}")
    if nicRNA == ['A']:
        print("Test przeszedl")    
    
    