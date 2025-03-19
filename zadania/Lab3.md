# Zadania Lista 3

## Wymagania

- Komendy `dvc` należy uruchomić korzystając ze środowiska w kontenerze Docker, w przeciwnym razie
  przyznane będzie 0pkt za zadania z DVC.
- MLflow należy uruchomić w Dockerze, w przeciwnym razie przyznane będzie 0pkt za zadania z MLflow.

---

## Analiza wydźwięku

Będziemy zajmować się zadaniem analizy wydźwięku emocjonalnego (sentiment).
Analiza wydźwięku (ang. sentiment analysis) będzie polegać na określeniu nacechowania emocjonalnego
recenzji internetowych.
Jest to rozbudowany i mocno subiektywny problem - tekst ma inny wydźwięk dla autora tekstu, inny dla
osoby czytającej, inny dla “podmiotu lirycznego”; mocno zależy też od kontekstu kulturowego.
Najczęstszym przypadkiem jest uproszczenie zadania do trójklasowej klasyfikacji - podziału na teksty
pozytywne, neutralne, negatywne.

### Żródło danych

Dzisiejsze zadania rozpoczynają przygodę ze zbiorem danych, którą kontynuować będziemy przez
najbliższe laboratoria. **Zadbaj o jakość i reprodukowalność kodu.**

Będziemy korzystać ze zbioru danych Sephora Products and Skincare Reviews, dokumentację
znajdziemy [tutaj](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews).
Zbiór jest lekko zmodyfikowany, w związku z tym niektórych kolumn możecie nie znaleźć w
dokumentacji.

Należy pobrać dane z google drive z folderu odpowiadającego grupie laboratoryjnej.
**W przypadku skorzystania z niewłaściwego folderu, zadanie nie zostanie ocenione!**

### Etykiety

Etykiety znajdują się w kolumnie zaczynającej się od "LABEL-".

---

## 1. (3 pkt) Przygotowanie potoku przetwarzaniadanych

Przygotuj poszczególne elementy rozwiązania problemu uczenia maszynowego w postaci osobnych
skryptów.

Do realizacji zastosować następujący podział:

1. Wstępne przetwarzanie danych
2. Podział danych
3. Analiza danych
4. Ekstrakcja cech, uczenie i ewaluacja modelu

Skrypty umieść w folderze `scripts`, parametry w pliku `params.yaml`, a pliki wejściowe i wyjściowe
w folderze `data` (najlepiej utwórz tam odpowiednie podfoldery). (Struktura projektu taka jak na
laboratorium 1.)
*Nie dodajemy danych do repozytorium git, tylko do dvc (zadanie 2). Za dodanie danych będą
odejmowane punkty.*
W ramach tej listy zajmiemy się budową klasyfikatora, który będzie punktem odniesienia (baseline) w
kolejnych listach. Będzie on predykował ignorując wszystkie cechy wejściowe. Ponieżej zamieszczono
opis działania poszczególnych skryptów.

- Wstępne przetwarzanie danych - połącz recenzje z odpowiadającymi im produktami w jeden dataframe; 
  usuń kolumny, które nie powinny być brane pod uwagę przy predykcji np. "author_id". Zapisz wynik jako plik/i.
- Podział danych - wydziel zbiór testowy bez stratyfikacji i oba zbiory zapisz. Zaleca się
  wykorzystanie funkcji [sklearn.model_selection.train_test_split
  ](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).
- Analiza danych - na razie pomijamy, zajmiemy się na przyszłych zajęciach.
- Ekstrakcja cech, uczenie i ewaluacja modelu - wytrenuj klasyfikator który będzie predykował
  najczęstszą klasę, następnie policz F1-score (w razie konieczności F1 macro) na zbiorze testowym,
  wyniki zapisz w formacie json (lub podobnym obsługiwanym przez dvc w kontekście metryk). Zaleca
  się
  wykorzystanie [sklearn.dummy.DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)
  oraz [sklearn.metrics.f1_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html).

**Uwagi**

* należy dużą uwagę przyłożyć do tego, w których skryptach umieścić poszczególne funkcjonalności
* należy dobrze się zastanowić jakie parametry umieścić w `params.yaml`
* decyzje nie zawsze będą proste i czasem będzie istniało więcej niż jedno rozwiązanie, należy
  jednak zdawać sobie sprawę z wad i zalet danej implementacji

## 2. (4 pkt)  Obsługa DVC

* Dodaj dane do DVC.
* Dodaj przygotowane skrypty jako elementy potoku `DVC`, zdefiniuj odpowiednie parametry, zależności (skrypty, dane wejściowe, ...)
  oraz wyjścia.
* Dodaj metryki do trackowania.
* Metryk nie należy umieszczać w cache dvc, mają być trackowane przez
  git. [więcej tutaj](https://dvc.org/doc/user-guide/project-structure/dvcyaml-files#metrics-and-plots-outputs)
* Zapisz wynik komendy `dvc status` (zrzut ekranu).
* Zreprodukuj potok. Zatwierdź zmiany i umieść je w repozytorium.
* Zmień podział danych na stratyfikowany. Zapisz wynik komendy `dvc status` (zrzut ekranu).
  Zreprodukuj potok. Zatwierdź zmiany i umieść je w repozytorium.

## 3. (3 pkt) Wykonanie eksperymentów

* Dodaj wsparcie dla modelu predykującego klasę z rozkładu jednostajnego ciągłego. Dodaj możliwość
  wybrania modelu w konfiguracji (params.yaml).
* Wykorzystaj api `dvc experiments` do porównania modeli.
* Załącz wyjście polecenia `dvc experiments show` (zrzut ekranu).

## 5. [OPCJONALNIE] (1 pkt) DVC remote

* Dodaj zewnętrzną lokację do przechowywania danych z DVC np. studencki Google Drive.
* Prześlij dane.
