# Zadania Lista 5

Celem listy jest budowa modelu klasyfikacji wydźwięku emocjonalnego (sentiment).

**Wymagania**

- Wszystkie procedury należy zintegrować z potokiem dvc.
- Końcową komendę `dvc repro` należy uruchomić korzystając ze środowiska w kontenerze Docker. W przeciwnym razie przyznane będzie 80% punktów (zgodnie z zasadami oceniania).

**Wskazówki**
1. Dokonując analizy modelu (zadania 2 i 3) wykonuj walidację krzyżową (cross-validation).
1. Uważaj na przeciek danych (data leakage) nie tylko podczas mierzenia skuteczności na zbiorze testowym, ale również w trakcie walidacji krzyżowej.
1. Aby uniknąć przecieku danych (data leakage) warto korzystać z klasy Pipeline [(docs)](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) z biblioteki `sklearn`.
1. Zanim cokolwiek dodasz do projeku zastanów się w którym stage'u powinno to być umieszczone. W wielu sytuacjach nie będzie jednego dobrego rozwiązania, należy wtedy postąpić według własnych preferencji zdając sobie sprawę z wad i zalet decyzji.


## 1. (3 pkt) Czyszczenie danych i przetwarzanie wstępne 

a) **(0.5 pkt)** Rozwiąż kwestię brakujących wartości - bazując na wykonanej EDA, uzupełnij brakujące wartości, usuń przypadki z brakującymi wartościami lub usuń kolumny zawierające brakujące wartości.

b) **(0.5 pkt)** Zakoduj zmienne kategoryczne

c) **(0.5 pkt)** Przeskaluj zmienne numeryczne

d) **(1 pkt)** Dokonaj czyszczenia danych tekstowych (należy zaproponować metodę czyszczenia). Można użyć do tego np. biblioteki Spacy, regex'y.

e) **(0.5 pkt)** Dokonaj wektoryzacji danych tekstowych metodą BoW

## 2. Uczenie modelu

**(3 pkt)** Wytrenuj i porównaj dwa klasyczne algorytmy ML - SVM i Random Forest oraz klasyfikator Dummy używany w trakcie listy 3.

Przeprowadź następujące eksperymenty:
- użyj tylko danych tekstowych
- użyj pozostałych danych oprócz tekstowych
- użyj wszystkich danych

Zaraportuj metryki klasyfikacji stosując walidację krzyżową (cross-validation). Nie korzystamy ze zbioru testowego.

## 3. Feature engineering

**(3 pkt)** Bazując na przeprowadzonej EDA, dokonaj inżynierii cech w celu polepszenia wyników z poprzedniego zadania:
- użyj metod selekcji cech
- użyj metod redukcji wymiarowości
- (opcjonalnie) zaproponuj nowe cechy

Wykonaj kilka iteracji i eksperymentów, sprawdź, jakie kombinacje metod/cech pozwalają poprawić rezultaty, a jakie nie.


## 4. Skuteczność na zbiorze testowym

**(1 pkt)** Przygotuj raport w tabeli Markdown, w której porównasz zastosowane modele (Dummy, SVM, Random Forest) w najlepszej dla nich konfiguracji na zbiorze testowym. Wyuczone mają być na całym zbiorze treningowym, czyli bez walidacji krzyżowej.  
Skorzystaj z "tabeli końcowej" z listy 6.2.

Przeanalizuj uzyskane wyniki pod kątem dokonanej podczas ostatnich zajęć EDA. Czy zdobyta wiedza była przydatna? Czy wysnute wtedy wnioski znalazły potwierdzenie w wynikach modelu? 

