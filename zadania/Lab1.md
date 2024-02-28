# Zadania Lista 1

1. Korzystając z języka Python i jedynie z wbudowanych paczek, wykonaj poniższe zadania:
    <br><br>
    a) (2 pkt) Napisz dowolny skrypt pod ścieżką `<KATALOG_GŁÓWNY_PROJEKTU>/scripts/main_1.py`.
    <br><br>
    b) (3 pkt) W pliku `<KATALOG_GŁÓWNY_PROJEKTU>/src/utils.py` zamieść dowolną funkcję/klasę, którą zaimportujesz i wykorzystasz w skrypcie `scripts/main_2.py`.
    <br><br>
    **Wymagania**
    
   - Oba skrypty mają wyświetlać nazwę skryptu na początku jego działania.
   - Skrypty należy uruchomić korzystając ze środowiska w kontenerze Docker, w przeciwnym razie przyznane będzie 0pkt. (To wymaganie zostanie z nami do końca kursu.)
   - Pisząc skrypty należy skorzystać z instrukcji prezentując ich działanie: `if`, `else`, `for`, `range`, `return`, ze struktur `list`, `set`, `dict`, `tuple`, `class`, `dataclass`, z *list comprehension* oraz *funkcji lambda*. Każda instrukcja musi wystąpić **co najmniej raz** w zad. a **lub** b.
   - Nie należy importować funkcji/klas z innych skryptów - to zła praktyka.

---
2. Korzystając ze środowiska Docker:
    <br><br>
    a) (2pkt) zainstaluj paczkę `black` specyfikując na sztywno jej wersję w pliku `requirements.txt`. Sformatuj wszystkie pliki `.py` w projekcie. Zamieść 3 zrzuty ekranu pod ścieżką `screenshots`: dowolony plik przed formatowaniem, dowolony plik po formatowaniu oraz wyjście w terminalu wraz z komendą formatującą. 
    <br><br>
    b) (2pkt) uruchom Jupyter Notebook lub JupyterLab w kontenerze dockerowym. Następnie utwórz notebook pod ścieżką `<KATALOG_GŁÓWNY_PROJEKTU>/notebooks/notebook_1.ipynb`, w którym w komórce typu `Markdown` wyświetlisz swój numer indeksu oraz nickname z GitHuba, a w komórce typu `Code` zaimportujesz i użyjesz funkcji/klasy z `src/utils.py`.

---
3. (1pkt) Napisz plik Makefile w głównym katalogu projektu. Zdefiniuj polecenia (wszystkie wykorzystujące Docker):
    * build - budujące obraz dockerowy
    * run_main_1 - uruchamiające skrypt `main_1.py` 
    * run_main_2 - uruchamiające skrypt `main_2.py` 
    * black - formatujące pliki `.py`
    * run_jupyter - uruchamiające Jupyter Notebook/Lab 
   

---
**Uwagi**
- Przy wykonywaniu listy przyda się znajomość `PYTHONPATH` oraz umiejętność przekierowania portów ;)


---
Wypełnij formularz wykonania zadań:

| Zadanie | Wykonano? (T)ak/(N)ie/(C)zęściowo |
|---------|-----------------------------------|
| 1a      |                                   |
| 1b      |                                   |
| 2a      |                                   |
| 2b      |                                   |
| 3       |                                   |

(Próby oszustwa prowadzą do konsekwencji opisanych w zasadach.)
