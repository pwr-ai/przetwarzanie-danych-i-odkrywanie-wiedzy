# Zadania Lista 6.2: Rozwiązywanie realnego problemu PDiOW

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
i uniwersalny względem stosowanych zbiorów danych.

**Będzie to zweryfikowane poprzez dodanie
poniższego zbioru danych.**


### Nowy zbiór

Zbiór danych: [tutaj](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz)

Podstawowa dokumentacja: w paczce

Dalsza dokumentacja: [tutaj](http://www.cs.cornell.edu/people/pabo/movie-review-data/) 

### Wymagania

1. (3pkt) Nowy zbiór musi przejść poprzez etapy przetwarzania opracowane w ramach list 3-6:
   * lista 3: wszystkie etapy zdefiniowanego potoku; mlflow
   * lista 4: podstawowa EDA (konstrukcja dodatkowych cech nieobowiązkowo; bez raportu)
   * lista 5: czyszczenie danych i przetwarzanie wstępne; uczenie modeli; feature engineering (
     tworzenie dodatkowych cechy nieobowiązkowo; bez wniosków)
   * lista 6: tuning hiperparametrów, wektoryzacja tekstu (bez wyjaśnialności)

   Słowne uzasadnienia i analizy nie są wymagane. EDA może być ograniczona do względem pierwszego
   zbioru danych.
1. (2pkt) Podsumowaniem całego projektu będzie tabela w markdown z metrykami dla obu zbiorów i kilku
   konfiguracji potoku (wstępne przetwarzanie + model + itd). Wzór tabeli umieszczony poniżej. 
   Tworzenie tabeli może być jako osobny stage (ale nie musi).
1. (2pkt) Zastosowanie `foreach`/`matrix` w dvc.yaml dla co najmniej 3 z 4 etapów zdefiniowanych w 
   laboratorium nr 3.
   Iteracja ma się odbywać po zbiorach danych (oczywiście może też jednocześnie po innych
   parametrach). Dla etapów, w których nie chcemy zastosować foreach, trzeba napisać dedykowany stage 
   dla każdego ze zbioru.
1. (1pkt) Napisanie instrukcji w README.md jak zreprodukować wyniki korzystając z Dockera. Dostarcz
   odpowiedni Dockerfile. Jeśli nie udostępniasz publicznie `remote` wskaż, gdzie konkretnie należy
   umieścić pliki wejściowe lub napisz skrypt, który je pobiera (np. jako dodatkowy stage).
1. (1pkt) Wyspecyfikowanie konkretnych wersji paczek użytych w projekcie.
1. (1pkt) Tam gdzie to konieczne: stosowanie random seed.
1. Projekt w ramach oceniania może być reprodukowany przez prowadzącego na podstawie instrukcji.


### Tabela końcowa

Tabela prezentuje wyniki na zbiorze testowym.

Kolumna params - wybieramy najważniejsze parametry, które chcemy pokazać np. `n_estimators` dla 
Random Forest.

| Dataset     | Model           | Params          | Accuracy | Precision | Recall | F1 Score |
|-------------|-----------------|-----------------|----------|-----------|--------|----------|
| [Dataset 1] | Dummy           |                 |          |           |        |          |
| [Dataset 1] | SVM             |                 |          |           |        |          |
| [Dataset 1] | Random Forest   |                 |          |           |        |          |
| [Dataset 2] | Dummy           |                 |          |           |        |          |
| [Dataset 2] | SVM             |                 |          |           |        |          |
| [Dataset 2] | Random Forest   |                 |          |           |        |          |

Tabele można modyfikować w uzasadnionych przypadkach.

### Wskazówki

1. Pisz czytelny i modyfikowalny kod, regularnie go formatuj, używaj typowania. Stosuj dobre praktyki. Polecana
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
3. Korzystaj z `assert`.
4. Korzystaj z plików konfiguracyjnych, np. `configs/MNIST.yaml`:
   ```yaml
   num_features: 7312
   ```
5. Polecane narzędzia:
   1. [Typer](https://typer.tiangolo.com/)
   2. [papermill](https://papermill.readthedocs.io/en/latest/)
   3. [omegaconf](https://omegaconf.readthedocs.io/en/)
   4. [hydra](https://hydra.cc/)
   3. [Poetry](https://python-poetry.org/docs/basic-usage/)
