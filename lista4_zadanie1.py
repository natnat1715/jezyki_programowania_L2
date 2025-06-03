# -*- coding: utf-8 -*-
"""
Created on Mon May 26 09:35:25 2025

@author: Natalia Kurczyna
"""

class Wielomian :
    def __init__ (self,wspolczynniki):
        """
        Tworzy nowy wielomian na podstawie podanych współczynników.

        Parameters
        ----------
        wspolczynniki : list[float]
            Lista współczynników, gdzie indeks jest potęgą x w wielomianie

        Raises
        ------
        ValueError
            Wyrzuca błąd, gdy lista współczynników jest pusta także po usunięciu zer na końcu.

        Returns
        -------
        Nic nie zwraca
        
        Skorzystano z logiki i kodu stworzonego na potrzeby zadania 1 z listy 2. Skorzystano z chatGPT, który
        nakazał użycie self oraz poprawił nieprawidłowo zaimplementowane fragmenty kodu.

        """
        self.wspolczynniki = wspolczynniki
        self.usun_zera_na_koncu(wspolczynniki)
        if not self.wspolczynniki :
            raise ValueError ("Lista nie moze byc pusta")
            
    def usun_zera_na_koncu (self, wspolczynniki: list[float]):
        """
        Funkcja usuwa zera jeli są one na końcu listy, ale tylko jesli lista ma więcej niż jeden element.

        Parameters
        ----------
        wspolczynniki : list[float]
            Lista współczynników, gdzie numer indeksu odpowiada potędze.

        Returns
        -------
        Nie zwraca niczego
        
        Skorzystano z logiki oraz kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self oraz pop(), poprawił nieprawidłowo 
        zaimplementowane fragmenty kodu.

        """
        while len(wspolczynniki) > 1 and wspolczynniki[-1] == 0 :
            wspolczynniki.pop()
            
    def stopien(self) -> int :
        """
        Funkcja zwraca stopień wielomianu, czyli największą potęgę z niezerowym współczynnikiem.
        
        Parameters
        -------
        Nie przyjmuje argumentów.
        
        Returns
        -------
        int
            Zwraca stopień wielomianu.
            
        Raises
        -------
        Nie wyrzuca wyjątków.
        
        Skorzystano z logiki i kodu napisanego w ranach listy 2. Skorzystano z chatGPT, który nakazał użycie self.

        """
        return len(self.wspolczynniki) - 1   

    def __str__(self):
        """
        Funkcja zwraca tekstową reprezentację wielomianu. Jesli wszystkie współczynniki wielomianu są równe 0.0 to zwraca W(x) = 0.0, 
        przed dodatnimi współczynnikami dodaje "+", pomija elementy, gdzie współczynnik jest równy 0.0.

        Parameters
        -------
        Nie przyjmuje argumentów.
        
        Returns
        -------
        String
            Zwraca reprezentację wielomianu w formie tekstowej.
            
        Raises
        -------
        Nie wyrzuca wyjątków.
        
        Skorzystano z logiki i kodu utworzonego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, linijkę z range 
        oraz poprawił nieprawidłowo zaimplementowane fragmenty kodu.

        """
        if all (x == 0 for x in self.wspolczynniki):
            return "W(x) = 0"
        
        wynik = "W(x) = "
        n = len(self.wspolczynniki)
        
        for i in range (n-1, -1, -1):
            if self.wspolczynniki[i] == 0:
                continue
            if i < n - 1 and self.wspolczynniki[i] > 0:
                wynik += "+"
            
            if i == 0:
                wynik += f" {self.wspolczynniki[i]} "
                
            elif i == 1:
                if self.wspolczynniki[i] == 1:
                    wynik += " x "
                
                elif self.wspolczynniki[i] == -1:
                    wynik += " -x "
                    
                else:
                    wynik += f"{self.wspolczynniki[i]}x "
                    
            else: 
                if self.wspolczynniki[i] == 1:
                    wynik += f" x^{i} "
                    
                elif self.wspolczynniki[i] == -1:
                    wynik += f" -x^{i} "
                    
                else: 
                    wynik += f"{self.wspolczynniki[i]}x^{i}"
                    
        return wynik 

    def __call__(self, x: float) -> float:
        """
        Funkcja oblicza wartoć wielomianu dla podanego x.

        Parameters
        ----------
        x : float
            Wartosć, która ma być wstawiona w miejsce x do obliczenia wielomianu.

        Returns
        -------
        float
            Wynik, który jest obliczeniem wartoci wielomianu.
            
        Raises
        -------
        Nie wyrzuca wyjątków i błędów.
        
        Skorzystano z logiki i kodu z zadania wykonanego na potrzebę listy 2. Skorzystano z chatGPT, który 
        nakazał użycie self oraz pokazał jak zapisać podniesienie liczby do potęgi.

        """
        wynik1 = 0.0
        
        for i in range (len(self.wspolczynniki)) :
            wynik1 += self.wspolczynniki[i] * (x ** i)
            
        return wynik1   

    def __add__(self, other):
        """
        Funkcja dodaje dwa wielomiany, lecz jeli jeden z wielomianów nie ma współczynnika
        z daną potęgą, wtedy traktuje (tę potęgę) jako 0.0

        Parameters
        ----------
        other wielomian
            Drugi wielomian, który będzie dodawany do pierwszego wielomianu.

        Returns
        -------
        Zwraca wynik dodawania dwóch wielomianów, jako obiekt klasy wielomian.
        
        Raises
        -------
        Nie wyrzuca wyjątków ani błędów.
        
        Skorzystano z logiki i kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, len
        oraz poprawił nieprawidłowo działające fragmenty kodu.

        """
        max_dlugosc = max(len(self.wspolczynniki), len(other.wspolczynniki)) 
        lista = [0.0] * max_dlugosc

        for i in range(max_dlugosc):
            a = self.wspolczynniki[i] if i < len(self.wspolczynniki) else 0.0
            b = other.wspolczynniki[i] if i < len(other.wspolczynniki) else 0.0
            lista[i] = a + b
        return Wielomian(lista)

    def __sub__(self, other):
        """
        Funkcja odejmuje od jednego wielomianu drugi wielomian. Jesli jeden
        z wielomianów nie ma współczynnika o danej potędze to traktuje ten współczynnik jako 0.0.

        Parameters
        ----------
        other : wielomian
            Funkcja przyjmuje inny wielomian, który będzie odejmowany od pierwszego wielomianu.

        Returns
        -------
        Nowy obiekt klasy Wielomian, który jest wynikiem odejmowania dwóch wielomianów.
        
        Raises
        -------
        Nie wyrzuca wyjątków ani błędów.
        
        Skorzystano z logiki i kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, len
        oraz poprawił nieprawidłowo działające fragmenty kodu.

        """
        max_dlugosc = max(len(self.wspolczynniki), len(other.wspolczynniki))
        lista = [0.0] * max_dlugosc
        
        for i in range(max_dlugosc):
            a = self.wspolczynniki[i] if i < len(self.wspolczynniki) else 0.0
            b = other.wspolczynniki[i] if i < len(other.wspolczynniki) else 0.0
            lista[i] = a - b
        return Wielomian(lista) 
    
    def __mul__(self, other):
        """
        Funkcja wykonuje mnożenie dwóch wielomianów.

        Parameters
        ----------
        other : wielomian
            Funkcja przyjmuje inny wielomian, który będzie mnożony przez pierwszy wielomian.

        Returns
        -------
            Obiekt klasy wielomian, który będzie wynikiem mnożenia dwóch wielomianów.
            
        Raises
        -------
        Nie wyrzuca wyjątków ani błędów.
        
        Skorzystano z logiki i kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, len, range
        oraz poprawił nieprawidłowo działające fragmenty kodu.

        """
        lista = [0.0] * (self.stopien() + other.stopien() + 1)
        
        for i in range(len(self.wspolczynniki)):
            for j in range(len(other.wspolczynniki)):
                lista[i + j] += self.wspolczynniki[i] * other.wspolczynniki[j]
                
        return Wielomian(lista)        
              
    def __iadd__(self,other):
        """
        Funkcja używa operatora złożonego: do pierwszego wielomianu dodaje drugi, czyci listę
        współczynników i dodaje wynik do listy.

        Parameters
        ----------
        other : Wielomian
            Przymuje inny wielomian, który będzie dodawany do pierwszego wielomianu.

        Returns
        -------
        Wielomian
            Zmodyfikowany bieżący obiekt
            
        Raises
        -------
        Nie wyrzuca wyjątków ani błędów.
        
        Skorzystano z logiki i kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, extend
        oraz poprawił nieprawidłowo działające fragmenty kodu.

        """
        nowy = self + other
        self.wspolczynniki.clear()
        self.wspolczynniki.extend(nowy.wspolczynniki)
        return self
    
    def __isub__(self,other):
        """
        Funkcja używa operatora złożonego: od pierwszego wielomianu odejmuje drugi, czyli listę
        współczynników i dodaje wynik do listy.

        Parameters
        ----------
        other : Wielomian
            Przymuje inny wielomian, który będzie odejmowany od pierwszego wielomianu.

        Returns
        -------
        Wielomian
            Zmodyfikowany bieżący obiekt
            
        Raises
        -------
        Nie wyrzuca wyjątków ani błędów.
        
        Skorzystano z logiki i kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, extend
        oraz poprawił nieprawidłowo działające fragmenty kodu.

        """
        nowy = self - other
        self.wspolczynniki.clear()
        self.wspolczynniki.extend(nowy.wspolczynniki)
        return self
    
    def __imul__(self,other):
        """
        Funkcja używa operatora złożonego: mnoży pierwszy i drugi wielomian, czyli listę
        współczynników i dodaje wynik do listy.

        Parameters
        ----------
        other : Wielomian
            Przymuje inny wielomian, który będzie mnożony przez pierwszy wielomian.

        Returns
        -------
        Wielomian
            Zmodyfikowany bieżący obiekt
            
        Raises
        -------
        Nie wyrzuca wyjątków ani błędów.
        
        Skorzystano z logiki i kodu napisanego w ramach listy 2. Skorzystano z chatGPT, który nakazał użycie self, extend
        oraz poprawił nieprawidłowo działające fragmenty kodu.

        """
        nowy = self * other
        self.wspolczynniki.clear()
        self.wspolczynniki.extend(nowy.wspolczynniki)
        return self
    

if __name__ == "__main__":
    wspolczynniki = [2.0, 0.0, 3.0, 5,0]
    wielomian = Wielomian(wspolczynniki)
    wspolczynniki2 = [3.0, -2.0, 8.0]
    wielomian2 = Wielomian(wspolczynniki2)
    
    print(f"Stopien wielomianu: {wielomian.stopien()}")
    if wielomian.stopien() == 3:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"Wynik: {wielomian(2.0)}")
    if wielomian(2.0) == 54.0:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"Suma: {wielomian + wielomian2}")
    dwa_wielomiany = wielomian + wielomian2
    if str(dwa_wielomiany).strip() =="W(x) = 5.0x^3+11.0x^2-2.0x + 5.0":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"Roznica: {wielomian - wielomian2}")
    dwa_wielomiany = wielomian - wielomian2
    if str(dwa_wielomiany).strip() =="W(x) = 5.0x^3-5.0x^2+2.0x  -1.0" :
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"Mnozenie: {wielomian * wielomian2}")
    dwa_wielomiany = wielomian * wielomian2
    if str(dwa_wielomiany).strip() =="W(x) = 40.0x^5+14.0x^4+9.0x^3+25.0x^2-4.0x + 6.0":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    wielomian += wielomian2    
    print(f"Suma: {wielomian}")
    if str(wielomian).strip() =="W(x) = 5.0x^3+11.0x^2-2.0x + 5.0":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    wielomian -= wielomian2    
    print(f"Roznica: {wielomian}")
    if str(wielomian).strip() =="W(x) = 5.0x^3+3.0x^2+ 2.0":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl") 
        
    wielomian *= wielomian2
    print(f"Mnozenie: {wielomian}")
    if str(wielomian).strip() =="W(x) = 40.0x^5+14.0x^4+9.0x^3+25.0x^2-4.0x + 6.0" :
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    wspolczynniki = [1.0, 0.0, 0.0]
    wielomian3 = Wielomian(wspolczynniki)
    wspolczynniki2 = [-1.0, 2.0, -3.0, 4.0]
    wielomian4 = Wielomian(wspolczynniki2)    
    
    print(f"Stopien: {wielomian3.stopien()}")
    if wielomian3.stopien() == 0:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"Wynik: {wielomian3(2.0)}")
    if wielomian3(2.0) == 1.0:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl") 
        
    print(f"Suma: {wielomian3 + wielomian4}")
    dwa_wielomiany = wielomian3 + wielomian4
    if str(dwa_wielomiany).strip() =="W(x) = 4.0x^3-3.0x^2+2.0x":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl") 
        
    print(f"Roznica: {wielomian3 - wielomian4}")
    dwa_wielomiany = wielomian3 - wielomian4
    if str(dwa_wielomiany).strip() =="W(x) = -4.0x^3+3.0x^2-2.0x + 2.0" :
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"Mnozenie: {wielomian3 * wielomian4}")
    dwa_wielomiany = wielomian3 * wielomian4
    if str(dwa_wielomiany).strip() =="W(x) = 4.0x^3-3.0x^2+2.0x  -1.0":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")  
        
    wielomian3 += wielomian4    
    print(f"Suma: {wielomian3}")
    if str(wielomian3).strip() =="W(x) = 4.0x^3-3.0x^2+2.0x":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
         
    wielomian3 -= wielomian4    
    print(f"Roznica: {wielomian3}")
    if str(wielomian3).strip() =="W(x) =  1.0":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl") 
         
    wielomian3 *= wielomian4
    print(f"Mnozenie: {wielomian3}")
    if str(wielomian3).strip() =="W(x) = 4.0x^3-3.0x^2+2.0x  -1.0" :
        print("Test przeszedl")
    else:
        print("Test nie przeszedl") 
        
    try:
        wspolczynniki = []
        wielomian5 = Wielomian(wspolczynniki)
        print(f"Test nie przeszedl, bo funkcja zwrocila {wielomian5.stopien()}, a powinna wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
    
    wspolczynniki = [0.0]    
    wielomian10 = Wielomian(wspolczynniki)

    print(f"Stopien: {wielomian10.stopien()}")
    if wielomian10.stopien() == 0:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")    
    
             
            
            
        
    