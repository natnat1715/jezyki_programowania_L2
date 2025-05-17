# -*- coding: utf-8 -*-
"""
Created on Thu May  8 21:54:25 2025

@author: Natalia Kurczyna
"""
def wspolne (x: list[int], y: list[int]) -> list[int]:
  """
    Funkcja przy pomocy petli porownuje wartosc elementu i z listy x z wartosciami j z kopia listy y.
    Jesli funkcja znajdzie wspolna wartosc to dodaje ja do czesc_wspolna i usuwa ten element z kopii listy y 
    aby nie był on porównywany przy następnym przebiegu pętli.

    Args:
    ----------
    x : list[int]
        Pierwszy multizbior jako lista liczb calkowitych.
    y : list[int]
        Drugi multizbior jako lista liczb calkowitych.

    Returns
    ----------
    list[int]
    Czesc wspolna dla obu multizbiorow. W przypadku braku elementow wspolnych funkcja zwraca pusta liste.
    
    Raises
    ----------
    Funkcja nie wyrzuca wyjątków.
    
    
    Wiedza z multizbiorów zaczerpnięta z zajęć. Skorzystano z logiki własnego kodu wykonanego na liscie 1.
    Skorzystano z chatGPT, który poprawił nieprawidłowo zaimplementowane fragmenty kodu, pomógł prawidłowo zaimplementować testy oraz komentarze dokumentacyjne.
    W tworzeniu komentarzy dokumentacyjnych użyto także: https://www.geeksforgeeks.org/python-docstrings/
    """ 
  y_kopia = y.copy()
  czesc_wspolna = []

  for i in x:
        for j in y_kopia:
            if i == j:
                czesc_wspolna.append(i)
                y_kopia.remove(j)
                break
  return czesc_wspolna 
    
    
    

if __name__ == "__main__":
    x = [2, 2, 3, 5, 6, 6, 7]
    y = [2, 2, 4, 6, 7, 34, 2]
    czesc_wspolna = wspolne(x, y)
    print(f"Elementy wspolne: {czesc_wspolna}") 
    if czesc_wspolna != [2, 2, 6, 7]:
        print("Test nie przeszedl")
    else:
        print("Test przeszedl")
        
    x = [] 
    y= [1, 0]
    czesc_wspolna = wspolne(x, y)
    print(f"Elementy wspolne: {czesc_wspolna}")
    if czesc_wspolna != []:
        print("Test nie przeszedl")
    else:
        print("Test przeszedl")
        
    x = [1, 1, 1, -1]
    y = [1, 0, -1, 5, 1]
    czesc_wspolna = wspolne(x, y)
    print(f"Elementy wspolne: {czesc_wspolna}")
    if czesc_wspolna != [1, 1, -1]:
        print("Test nie przeszedl") 
    else:
        print("Test przeszedl")
        
    x = [0, 0, 0, 0]
    y = [0, 0]
    czesc_wspolna = wspolne(x, y)
    print(f"Elementy wspolne: {czesc_wspolna}")
    if czesc_wspolna != [0, 0]:
        print("Test nie przeszedl") 
    else:
        print("Test przeszedl")   
        
    x = []
    y = []
    czesc_wspolna = wspolne(x, y)
    print(f"Elementy wspolne: {czesc_wspolna}")
    if czesc_wspolna != []:
        print("Test nie przeszedl") 
    else:
        print("Test przeszedl")    
        