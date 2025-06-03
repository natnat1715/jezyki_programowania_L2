# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:33:57 2025

@author: Natalia Kurczyna
"""

class Sequences :
    """
    Klasa bazowa, po ktorej dziedzicza klasy DNASequence, RNASequence i ProteinSequence, reprezentuje atrybuty i metody,
    ktore wykorzystywane sa przez klasy dziedziczace.
    
    Attributes
    -------
    identifier [str]: identyfikator sekwencji
    data [str] : ciag znakow, ktory reprezentuje sekwencje
    
    Methods
    -------
    length, to_fasta_string, mutate, find_motif : wyjasnione pod kazda funkcja
    
    Do utworzenia komentarzy dokumentacyjnych skorzystano z :https://www.programiz.com/python-programming/docstrings 
    """
    def __init__(self, identifier: str, data: str):
        """
        Do inicjalizacji obiektu sekwencji.

        Parameters
        ----------
        identifier : str
            Identyfikator sekwencji.
        data : str
            Ciąg znakow, ktory reprezentuje sekwencje

        Raises
        ------
        ValueError
            Jesli sekwencja jest pusta lub podano znaki nie znajdujace sie w valid_chars

        Returns
        -------
        Nic nie zwraca.
        
        Skorzystano z logiki i kodu stworzonego na potrzeby zadania wykonanego w ramach listy 2.
        Skorzystano z chatGPT, który powiedzial o konicznosci uzywania self oraz przypisywania go, 
        pokazal o koniecznosci i pomogl w napisaniu sprawdzenia/warunku o koniecznosci podania odpowiednich
        zasad, a takze poprawil nieprawidlowo zaimplementowane fragmenty kodu oraz inicjalizacje sekwencji w postaci bloku init

        """
        if not data:
            raise ValueError("Sekwencja nie moze byc pusta")
            
        if not all(char in self.__class__.valid_chars for char in data):
            raise ValueError(f"Podano nieprawidlowe znaki w sekwencji: {data}")    
            
        self.identifier = identifier
        self.data = data
    
    @property
    def length(self):
        """
        Zwraca dlugosc sekwencji.

        Returns
        -------
        int
            Zwraca dlugosc sekwencji.

        """
        return len(self.data)
    
    def to_fasta_string(self):
        """
        Zwraca sekwencje w formacie FASTA.

        Raises
        ------
        ValueError
            Wyrzuca blad, gdy sekwencja ma niepoprawne/bledne znaki, ktore nie znajduja sie w valid_chars

        Returns
        -------
        str
            Sekwencja w formacie FASTA
            
        Skorzystano z chatGPT, ktory poprawil blednie zaimplementowana petle for
        i poprawil logike sprawdzania obecnosci wpisanych znakow/zasad w valid_chars.
        Skorzystano z logiki i kodu napisanego w ramach listy 2.

        """
        for znak in self.data:
            if znak not in self.valid_chars:
                raise ValueError("Podano nieprawidlowa zasade")
        return f">{self.identifier}\n{self.data}"

    def mutate (self, position: int, value: str) -> str:
        """
        Dokonuje mutacji/zamiany jednego znaku w sekwencji.

        Parameters
        ----------
        position : int
            Indeks znaku, ktory ma zostac zmieniony
        value : str
            Znak na jaki ma zostac zmieniony inny znak, ktorego indeks podano

        Raises
        ------
        IndexError
            Jezeli indeks znaku jest mniejszy lub wiekszy niz indeksy sekwencji bazowej
        ValueError
            Jesli nowy znak do zmiany nie znajduje sie w valid_chars

        Returns
        -------
        str
            Zwraca zmieniona sekwencje
            
        Skorzystano z logiki i kodu wykonanego na potrzeby zadania z listy 2.
        Skorzystano z chatGPT, który poprawil nieprawidlowo zaimplementowane fragmenty kodu i 
        zasugerowal uzycie IndexError 

        """
        if position < 0 or position >= len(self.data):
            raise IndexError("Podano indeks wiekszy niz dostepne")
            
        if value not in self.valid_chars:
            raise ValueError("Podano nieprawidlowa zasade")
            
        self.data = self.data[:position] + value + self.data[position + 1:]
        
        return self.data
    
    def find_motif(self, motif: str) -> list[int]:
        """
        Szuka miejsc/indeksow wystapienia zadanego motywu w sekwencji bazowej.

        Parameters
        ----------
        motif : str
            Motyw, ktory jest wyszukiwany w sekwencji bazowej

        Raises
        ------
        ValueError
            Jesli podano nieprawidlowa zasade w szukanym motywie lub w sekwencji

        Returns
        -------
        list[int]
            Zwraca liste indeksow, na jakich wystepuje szukany motyw
            
        Skorzystano z logiki oraz kodu wykonanego na potrzeby zadania z listy 2.
        Skorzystano z chatGPT, ktory poprawil nieprawidlowo zaimplementowane fragmenty kodu, poprawil i zasugerowal
        zmiany w sprawdzeniu prawidlowosci zasady oraz we fragmencie z while.

        """
        if any(znak not in self.valid_chars for znak in self.data) or any (znak not in self.valid_chars for znak in motif):
            raise ValueError("Podano nieprawidlowa zasade w sekwencji lub w szukanym motywie")
            
        position = []
        indeks = self.data.find(motif)
        while indeks != -1:
            position.append(indeks)
            indeks = self.data.find(motif, indeks + 1)
            
        if not position:
            print(f"Nie znalezniono podanego motywu {motif}")
            
        return position   
    
class DNASequence(Sequences) :
    """
    Reprezentuje sekwencje w nici DNA, dziedziczy po klasie Sequences atrybuty oraz motywy.
    Posiada takze dodatkowe metody complement() oraz trnascribe() objasnione w kazdej funkcji oraz wlasne valid_chars.
    Skorzystano z https://www.programiz.com/python-programming/docstrings do tworzenia
    komentarzy dokumentacyjnych oraz chatGPT, ktory podpowiedzial, zeby kazda klasa miala wlasne valid_chars.
    """
    valid_chars = {"A", "C", "G", "T"}
    
    def complement(self) -> str:
        """
        Tworzy nic komplementarna do sekwencji DNA i zwraca ja odwrocona.

        Raises
        ------
        ValueError
            Jesli podane zostana zasady, ktore nie moga budowac nici DNA.

        Returns
        -------
        str
            Komplementarna sekwencje DNA (odwrocona)
            
        Skorzystano z logiki i kodu napisanego w ramach listy 2.
        Skorzystano z chatGPT, ktory poprawil nieprawidlowo zaimplementowane fragmenty kodu 
        oraz pomogl w poprawie logiki kodu.

        """
        komplementarna = []
        i = 0
        while i < len(self.data):
            znak = self.data[i]
            if znak == 'A':
                komplementarna.append('T')
            elif znak == 'T':
                komplementarna.append('A')
            elif znak == 'C':
                komplementarna.append('G')
            elif znak == 'G':
                komplementarna.append('C')
            else:
                raise ValueError("Podano nieprawidlowa zasade, ktora nie moze budowac DNA")
                
            i += 1 
        return ''.join(reversed(komplementarna))

    def transcribe(self, komplementarna: str) -> str:
        """
        Dokonuje transkrypcji nici DNA na nic RNA.

        Parameters
        ----------
        komplementarna : str
            Komplementarna nic DNA

        Raises
        ------
        ValueError
            Wyrzuca blad jesli w sekwencji podano nieprawidlowe znaki, ktore nie moga budowac RNA.

        Returns
        -------
        str
            Sekwencje RNA po procesie transkrypcji
            
        Skorzystano z logiki i kodu napisanego na potrzeby zadania z listy 2. 
        Skorzystano z chatGPT, ktory poprawil nieprawidlowo zaimplementowane fragmenty kodu.

        """
        nic_RNA = []
        i = 0
        while i < len(komplementarna):
            znak = komplementarna[i]
            if znak == 'A':
                nic_RNA.append('U')
            elif znak == 'T':
                nic_RNA.append('A')
            elif znak == 'C':
                nic_RNA.append('G')
            elif znak == 'G':
                nic_RNA.append('C')
            else:
                raise ValueError("Podano nieprawidlowa zasade, ktora nie moze budowac RNA")
            i += 1    
        
        return ''.join(nic_RNA)

class RNASequence(Sequences):
    """
    Reprezentuje sekwencje w nici RNA, dziedziczy po klasie Sequences atrybuty oraz motywy.
    Posiada takze dodatkowa metode translate() objasniona ponizej oraz wlasne valid_chars i tablice kodonow.
    Skorzystano z https://www.programiz.com/python-programming/docstrings do tworzenia
    komentarzy dokumentacyjnych oraz chatGPT, ktory podpowiedzial, zeby kazda klasa miala wlasne valid_chars.
    """
    valid_chars = {'A', "U", "C", "G"}

    def translate(self) -> 'ProteinSequence' :
        """
        Tlumaczy sekwencje RNA na sekwencje bialek.

        Raises
        ------
        ValueError
            Jezeli nie znaleziono bialka w tablicy kodonow, sekwencji START lub STOP 

        Returns
        -------
        'ProteinSequence'
            Zwraca obiekt klasy ProteinSequence, ktory zawiera przetlumaczona sekwencje RNA na sekwencje bialkowa
            
        Skorzystano z kodu i logiki zadania wykonanego na potrzeby listy 2 i stantad wzieto dane o kodonach i bialkach
        Skorzystano z chatGPT, ktory poprawil nieprawidlowo zaimplementowane fragmenty kodu, użycie self, get, join oraz -1.

        """
        tablica_kodonow = {
            "AUG": "Me",
            "UUU": "Fe", "UUC": "Fe",
            "CUU": "Le", "CUC": "Le", "CUA": "Le", "CUG": "Le",
            "AUU": "Iz", "AUC": "Iz", "AUA": "Iz",
            "GUU": "Wa", "GUC": "Wa", "GUA": "Wa", "GUG": "Wa",
            "UCU": "Sr", "UCC": "Sr", "UCA": "Sr", "UCG": "Sr",
            "CCU": "Pr", "CCC": "Pr", "CCA": "Pr", "CCG": "Pr",
            "ACU": "Te", "ACC": "Te", "ACA": "Te", "ACG": "Te",
            "GCU": "Al", "GCC": "Al", "GCA": "Al", "GCG": "Al",
            "UAU": "Ty", "UAC": "Ty",
            "CAU": "Hi", "CAC": "Hi",
            "CAA": "Gt", "CAG": "Gt",
            "AAU": "As", "AAC": "As",
            "AAA": "Li", "AAG": "Li",
            "GAU": "Ap", "GAC": "Ap",
            "GAA": "Gl", "GAG": "Gl",
            "UGU": "Cy", "UGC": "Cy",
            "UGG": "Tr",
            "CGU": "Ar", "CGC": "Ar", "CGA": "Ar",
            "AGU": "Se", "AGC": "Se",
            "AGA": "Ar", "AGG": "Ar",
            "GGU": "Gi", "GGC": "Gi", "GGA": "Gi", "GGG": "Gi",
            "UAA": "ST", "UAG": "ST", "UGA": "ST"
            }
        
        start_indeks = self.data.find("AUG")
        if start_indeks == -1:
            raise ValueError("Brak kodonu START w podanej sekwencji")
        
        nowa_nic = []
        i = start_indeks
        znaleziony_ST = False
        while(i + 3 <= len(self.data)):
            kodon = self.data[i:i + 3]
            aminokwas = tablica_kodonow.get(kodon)
            if aminokwas is None:
                raise ValueError("Nie znaleziono bialka w tablicy kodonow")
                
            if aminokwas == "ST":
                znaleziony_ST = True
                break
            else:
                nowa_nic.append(aminokwas)
            i += 3   
            
        if not znaleziony_ST:
            raise ValueError("Nie znaleziono kodonu STOP w sekwencji")
            
        if not nowa_nic:
            raise ValueError("Brak bialek przed kodonem STOP")
            
        return ProteinSequence(self.identifier, ''.join(nowa_nic)) 
    
class ProteinSequence(Sequences):
    """
    Klasa reprezentujaca sekwencje bialka. Dziedziczy po klasie Sequences, posiada wlasne valid_chars
    oraz implementuje metody z klasy Sequences na wlasne potrzeby.
    Skorzystano z https://www.programiz.com/python-programming/docstrings do tworzenia
    komentarzy dokumentacyjnych oraz chatGPT, ktory podpowiedzial, zeby kazda klasa miala wlasne valid_chars.
    """
    valid_chars = { 
    "Me", "Fe", "Le", "Iz", "Wa", "Sr", "Pr", "Te", "Al", "Ty", "Hi", "Gt", "As",
    "Li", "Ap", "Gl", "Cy", "Tr", "Ar", "Se", "Gi", "ST"
        }            
        
    def __init__(self, identifier: str, data: str):
        """
        Inicjalizuje sekwencje bialka i sprawdza poprawnosc aminikwasow.
        
        Parameters
        -------
            indentifier [str]: identyfikator sekwencji
            data [str]: sekwencja kodonow aminokwasow, gdzie jeden aminokwas ma dwa znaki
        
        Raises:
        -------
        ValueError
            Jesli dlugosc sekwencji jest nieparzysta lub jesli zawiera aminokwasy nie znajdujace sie w valid_chars
            
        Skorzystano z logiki i kodu napisanego na potrzeby zadania z listy 2 i stamtad wzieto informacje o kodonach i aminokwasach
        Skorzystano z chatGPT, ktory poprawil nieprawidlowo zaimplementowane fragmenty kodu oraz fragment ze sprawdzeniem
        poprawnosci aminokwasow i zasugerowal zmiany, z ktorych skorzystano oraz inicjalizacje sekwencji w postaci bloku init.
        """
        aminokwasy = [data[i:i+2] for i in range(0, len(data), 2)]

        if not aminokwasy or any(am not in self.valid_chars for am in aminokwasy):
            raise ValueError(f"Podano nieprawidlowe aminokwasy: {data}")

        self.identifier = identifier
        self.data = data
        if len(self.data) % 2 != 0:
             raise ValueError("Dlugosc sekwencji bialka powinna byc parzysta")
        
    @property
    def length(self):
        """
        Dlugosc sekwencji bialka, czyli liczba aminokwasow budujacych dane bialko.

        Returns
        -------
        int
            Liczba aminokwasow
            
        Skorzystano z logiki i kodu wykonanego na potzreby zadania z listy 2.   

        """
        return len(self.data) // 2
    
    def to_fasta_string(self):
        """
        Zwraca reprezentacje bialka w formacie FASTA.

        Raises
        ------
        ValueError
            Jesli sekwencja zawiera nieprawidlowe aminokwasy nie znajdujace sie w valid_chars

        Returns
        -------
        str
            Sekwencja bialka w formacie FASTA
            
        Skorzystano z logiki i kodu wykonanego na potrzeby zadania z listy 2.
        Skorzystano z chatGPT, który poprawil nieprawidlowo zaimplementowane fragmenty kodu,
        pomogl w poprawie fragmentu sprawdzajacego poprawnosc znakow, z jakich zbudowane sa aminokwasy.

        """
        aminokwasy = [self.data[i: i + 2] for i in range(0, len(self.data),2)] 
        if all (aminokwas in self.valid_chars for aminokwas in aminokwasy):
            return f">{self.identifier}\n{self.data}"
        else:
            raise ValueError("Podano nieprawidlowy aminokwas")
            
            
    def find_motif(self, motif: str) -> list[int]:
        """
        Wyszukuje motyw czyli dwa znaki znajdujace sie w sekwencji bialkowej i zwraca indeksy ich wystepowania.

        Parameters
        ----------
        motif : str
            Motyw, ktory ma byc znaleziony w sekwencji

        Raises
        ------
        ValueError
            Jesli motyw lub sekwencja zawieraja nieprawidlowe bialko lub jesli szukany motyw ma nieparzysta dlugosc 

        Returns
        -------
        list[int]
            Lista indeksow, gdzie znaleziono motyw
            
        Skorzystano z logiki i kodu wykonanego w ramach zadania z listy 2.
        Skorzytsano z chatGPT, który poprawil nieprawidlowo zaimplementowane fragmenty kodu, poprawil
        fragment doku sluzacy do wyszukiwania pozycji aminokwasu w sekwencji oraz sprawdzanie poprawnosci zakresu motywu.

        """
        if len(motif) % 2 != 0:
            raise ValueError("Podano nieprawidlowy aminokwas- musi byc dwuznakowy")
            
        aminokwasy = [self.data[i: i + 2] for i in range (0, len(self.data), 2)]
        motyw_aminokwasu = [motif[i: i + 2] for i in range(0, len(motif), 2)]
        
        if not all(aminokwas in self.valid_chars for aminokwas in aminokwasy) or not all(aminokwas in self.valid_chars for aminokwas in motyw_aminokwasu) :
            raise ValueError("Podano nieprawidlowy aminokwas")
            
        position = []
        motif_len = len(motyw_aminokwasu)
        for i in range(len(aminokwasy) - motif_len + 1):
            if aminokwasy[i: i + motif_len] == motyw_aminokwasu:
                position.append(i)
                
        if not position:
            print(f"Nie znaleziono motywu {motif}")
            
        return position    
        
if __name__ == "__main__":
    identifier = "Seq123"
    data = "AACTGG"
    motif = "CTG"
    sekwencja = DNASequence(identifier, data)
    
    print(f"Dlugosc sekwencji: {sekwencja.length}")
    if sekwencja.length == 6:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"DNA w formacie FASTA: {sekwencja.to_fasta_string()}")
    if sekwencja.to_fasta_string() == ">Seq123\nAACTGG":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    zmieniona_sekwencja = sekwencja.mutate(1, "C")
    print(f"Zmieniona sekwencja: {zmieniona_sekwencja}")
    if zmieniona_sekwencja == "ACCTGG":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    
    pozycja = sekwencja.find_motif(motif)
    print(f"Pozycja motywu {motif}: {pozycja}")
    if pozycja == [2]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    komplementarna = sekwencja.complement()
    print(f"Nic komplementarna: {komplementarna}")
    if komplementarna == "CCAGGT":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    komplementarna_odwrocona = sekwencja.complement()    
    transkrybujaca = sekwencja.transcribe(komplementarna_odwrocona)
    print(f"Nic RNA: {transkrybujaca}")   
    if transkrybujaca == "GGUCCA":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print("Test nie przeszedl")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print(f"Test nie przeszedl, bo funkcja zwrocila {pusteDNA.length}")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")  
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print(f"Test nie przeszedl, bo funkcja zwrocila {pusteDNA.to_fasta_string()}")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print(f"Test nie przeszedl, bo funkcja zwrocila {pusteDNA.mutate(1, "C")}")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")  
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print(f"Test nie przeszedl, bo funkcja zwrocila {pusteDNA.find_motif(motif)}")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print(f"Test nie przeszedl, bo funkcja zwrocila {pusteDNA.transcribe(komplementarna)}")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")      
        
    try:
        pusteDNA = DNASequence("PustaSeq", "")
        print(f"Test nie przeszedl, bo funkcja zwrocila {pusteDNA.transcribe(komplementarna)}")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}") 
        
    identifier1 = "Seq456"
    sekwencja1 = RNASequence((identifier1), transkrybujaca)
    
    print(f"Dlugosc sekwencji: {sekwencja1.length}")
    if sekwencja1.length == 6:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    print(f"RNA w formacie FASTA: {sekwencja1.to_fasta_string()}")
    if sekwencja1.to_fasta_string() == ">Seq456\nGGUCCA":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    zmieniona_sekwencja = sekwencja1.mutate(1, "C")
    print(f"Zmieniona sekwencja: {zmieniona_sekwencja}")
    if zmieniona_sekwencja == "GCUCCA":
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    motifRNA = "UCC"
    pozycja = sekwencja1.find_motif(motifRNA)
    print(f"Pozycja motywu {motif}: {pozycja}")
    if pozycja == [2]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
    
    try:
        sekwencja1.find_motif("ABH")
        print("Test nie przeszedl")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjatek: {e}")
        
    identifier3 = "Seq789"
    data3 = "MeLiTyST"
    sekwencja4 = ProteinSequence(identifier3, data3)
    print(f"Dlugosc: {sekwencja4.length}")
    if sekwencja4.length == 4:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl")
        
    motif_bialko = "Li"
    pozycja_bialko = sekwencja4.find_motif(motif_bialko)
    print(f"Pozycja motywu: {motif_bialko}: {pozycja_bialko}")

    if pozycja_bialko == [1]:
        print("Test przeszedl")
    else:
        print("Test nie przeszedl") 
        
    motif_bialko = "Se"
    if not sekwencja4.find_motif(motif_bialko):
        print(f"Test przeszedl, bo {motif_bialko} nie zostal znaleziony")
    else:
        print(f"Test przeeszedl, bo {motif_bialko} nie powinien zostac znaleziony")
     
    try:
        motif_bialko = "Ne"
        sekwencja4.find_motif(motif_bialko)
        print(f"Test nie przeszedł, bo funcja zwrocila {motif_bialko}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedł, wyjątek: {e}")    
    
    try:
        sekwencja5 = RNASequence("SeqB111", "CGFAUGCCCGAAAAC")
        sekwencja5.translate()
        print("Test nie przeszedł, bo funcja nie wyrzucila wyjatku")
    except ValueError as e:
        print(f"Test przeszedł, wyjątek: {e}") 
    
    try:    
        sekwencja6 = RNASequence("SeqB345", "CGFAUGCCCGAAUAGAAC")
        sekwencja6.translate()
        print(f"Test nie przeszedl, bo funkcja zwrocila: {sekwencja6.translate().to_fasta_string()}, a miala wyrzucic wyjatek")
    except ValueError as e:
        print(f"Test przeszedl, bo funkcja wyrzucila wyjątek: {e}") 
                 
            

    