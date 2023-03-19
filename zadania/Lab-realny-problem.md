# Zadania Lista: Rozwiązywanie realnego problemu PDiOW

## Wstęp

Projekty uczenia maszynowego powinny być reprodukowalne i uniwersalne względem danych wejściowych ze
względu na wiele powodów:

1. Weryfikacja wyników: Reprodukowalność pozwala na weryfikację wyników przez innych badaczy.
1. Zwiększenie zaufania: Reprodukowalność i uniwersalność zwiększają zaufanie do wyników projektu.
1. Oszczędność czasu i zasobów: Reprodukowalność i uniwersalność pozwalają na łatwiejsze
   dostosowanie projektu do innych zbiorów danych.
1. Wprowadzanie ulepszeń: Reprodukowalność ułatwia wprowadzanie ulepszeń do modelu.
1. Łatwiejsze przeprowadzanie badań: Reprodukowalność i uniwersalność są niezbędne dla prowadzenia
   badań naukowych. Dzięki nim można przeprowadzać badania, porównywać wyniki i weryfikować
   hipotezy. Jeśli wyniki badań są niepowtarzalne, to trudno będzie wyciągać z nich jakiekolwiek
   wnioski naukowe.

## 1. (10 pkt) Uniwersalny i reprodukowalny projekt

Przygotuj projekt, który powstaje w ramach laboratorium 3-6 w taki sposób, żeby był reprodukowalny
i uniwersalny względem stosowanych zbiorów danych. Będzie to zweryfikowane poprzez dodanie
zbioru danych, który zostanie ogłoszony na zajęciach nr 6 (2023-04-13/2023-04-14).

#### Nowy zbiór

todo!

#### Wymagania

1. Nowy zbiór musi przejść poprzez wszystkie etapy przetwarzania opracowane w ramach list 3-6.
2. Słowne uzasadnienia i analizy nie są wymagane. EDA może być ograniczona do względem pierwszego
   zbioru danych.
2. Zastosowanie `foreach` w dvc.yaml dla co najmniej 3 z 5 etapów zdefiniowanych w laboratorium nr 3. 
   Iteracja ma się odbywać po zbiorach danych (oczywiście może też jednocześnie po innych
   parametrach).
2. Napisanie instrukcji w README.md jak zreprodukować wyniki korzystając z Dockera. Dostarcz
   odpowiedni Dockerfile.
3. Wyspecyfikowanie konkretnych wersji paczek użytych w projekcie.

#### Wskazówki

1. Pisz czytelny kod, regularnie go formatuj, używaj typowania. Stosuj dobre praktyki. Polecana
   literatura: https://effectivepython.com/ (dostępna
   poprzez [Safari](https://biblioteka.pwr.edu.pl/e-zasoby/platformy/oreilly-safari))
2. Pisząc kod traktuj każdy zbiór danych jako specyficzny przypadek, nawet jeśli jest tylko jeden,
   np. zamiast
   ```python
   dataset = load_mnist()
   ```
   zaimplementuj
   ```python
   if dataset_name == "MNIST":
      dataset = load_mnist()
   else:
      raise ValueError()
   ```
3. Korzystaj z plików konfiguracyjnych, np. `configs/MNIST.yaml`:
   ```yaml
   num_features: 7312
   ```
4. Polecane narzędzia:
    1. [Typer](https://typer.tiangolo.com/)
    2. [papermill](https://papermill.readthedocs.io/en/latest/)
    2. [Poetry](https://python-poetry.org/docs/basic-usage/)
