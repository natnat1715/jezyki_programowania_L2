# -*- coding: utf-8 -*-
"""
Created on Thu May  8 19:49:02 2025

@author: Natalia Kurczyna

"""
import math

def heron (a, b, c): 
    """
Funkcja oblicza pole trojkata za pomoca wzoru Herona.
Funkcja zaklada, ze z podanych trzech dlugosci bokow mozna utworzyc trojkat i wszytskie sa liczbami dodatnimi.
Jesli podane wartosci nie spelniaja warunkow i sa nieporawne, funkcja zglasza odpowiedni wyjatek.

Args:
    a (float): Dlugosc pierwszego boku trojkata.
    b (float): Dlugosc drugiego boku trojkata.
    c (float): Dlugosc trzeciego boku trojkata.
    
Returns:
    float: Pole powierzchni trojkata.

Raises:
    ValueError : Jesli jakikolwiek bok ma wartosc ujemna lub rowna 0.
    ValueError: Jesli z podanych bokow nie mozna utworzyc trojkata. 
    
    
Do wzoru Herona i tresci wyswietlanych komunikatów skorzystano z: https://pl.wikipedia.org/wiki/Wz%C3%B3r_Herona
Korzystano z biblioteki Phytona do wyrzucania wyjatkow (ValueError) oraz try-except
Do dokumentacji korzystano z:https://www.geeksforgeeks.org/python-docstrings/
Skorzystano z logiki własnego kodu wykonanego na liscie 1.
Skorzystano z chatGPT, który pomógł w znalezieniu błędów,pomógł w tworzeniu komentarzy dokumentacyjnych, poprawił nieprawidłową implementację kodu i testów, które miałyby wyrzucać wyjątki
i zaproponował rozwiązania w implementacji, z których skorzystano.
Do utworzenia komentarzy dokumentacyjnych używano także: https://www.geeksforgeeks.org/python-docstrings/
"""    
    if a<= 0 or b<= 0 or c<=0 :
        raise ValueError ("Podano nieprawidlowa wartosc boku rowna 0 lub liczbie ujemnej")
        
    if a + b <= c or b + c <= a or a + c <= b:
         raise ValueError ("Odcinkami o podanych dlugosciach nie mozna polaczyc trzech punktow tej samej plaszczyzny, wiec wartosc pola nie nalezy do liczb rzeczywistych")
            
    p = ((a + b + c)/ 2)
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return pole
            
if __name__== "__main__":
    pole = heron(3.0, 4.0, 5.0)
    print(f"Pole: {pole}")

try:
    pole = heron(3.0, 4.0, 5.0)
    print (f"Pole: {pole}")
except ValueError as e:
    print(f"Pole: {e}")   

if pole != 6.0:
    print("Test nie przeszedl")
else:
    print("Test przeszedl")    
    
try:
    pole = heron(5.0, 3.1, 0.1)
    print(f"Test nie przeszedl, bo funkcja zwrocila {pole}, a powinna wyrzucic wyjatek")
except ValueError as e:
    print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}") 
    
try:
    pole = heron(-1.1, 4.0, 5.1)
    print(f"Test nie przeszedl, bo funkcja zwrocila {pole}, a powinna wyrzucic wyjatek")
except ValueError as e:
    print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}") 
    
try:
    pole = heron(4.0, 5.0, 9.0)
    print(f"Test nie przeszedl, bo funkcja zwrocila {pole}, a powinna wyrzucic wyjatek")
except ValueError as e:
    print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}") 
    
try:
    pole = heron(0.0, 0.0, 0.0)
    print(f"Test nie przeszedl, bo funkcja zwrocila {pole}, a powinna wyrzucic wyjatek")
except ValueError as e:
    print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}") 
    
try:
    pole = heron(-3.0, -4.0, -5.0)
    print(f"Test nie przeszedl, bo funkcja zwrocila {pole}, a powinna wyrzucic wyjatek")
except ValueError as e:
    print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}") 
        
        
        
        
    
    