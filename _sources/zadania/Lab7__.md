# Zadania Lista 7 (Work in progress)

## (5 pkt) 1. Zbuduj frontend aplikacji

W pliku `app.py`  dołączonego do niniejszej listy znajdziesz kod skryptu, który pobiera z Twittera dane z konkretnego profilu i dokonuje na nich analizy sentymentu.

W celu instalacji potrzebnych bibliotek, użyj poleceń (niestety, Twint z PyPi nie dziala):
```bash
pip install sentimentpl
pip install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

Używając biblioteki Streamlit, zbuduj na bazie w/w skryptu aplikację posiadającą następujące funkcjonalności:
* możliwość podania nazwy profilu do zescrapowania 
* użycie metody cachującej wyniki scrapowania, by zaoszczędzić transfer i czas
* wykres ilości postów w czasie
* wykres średniego sentymentu postów
* progressbar pokazujący postęp analizy sentymentu


## (2 pkt) 2. Zbuduj obraz Dockerowy aplikacji
Na bazie kodu z pkt 1 stwórz obraz Dockera zawierający i uruchamiający aplikację, umożliwiający dostać się do niej z komputera hosta. Jako portu dostępowego użyj 4 ostatnich cyfr swojego nr indeksu

## (3 pkt) 3. Zbieraj statystyki produkcyjne

Używając Docker Compose, stwórz środowisko umożliwiajace zbieranie statystyk:
* złącz swoją aplikację z obrazami Graphite i Grafany w jedno środowisko dockerowe
* rozpocznij zbieranie statystyk z aplikacji. Przykładowe statystyki - ilość uruchomień, ilość użyć cache, czas pobierania danych, czas analizy sentymentu, ilość zebranych postów, wyniki sentymentu (jako timing), ilość błędów pobierania danych itp.
* stwórz dashboard w Grafanie zawierający wykresy stworzone na bazie zbieranych metryk

Stworzone wykresy udokumentuj screenami

## (dodatkowe) (1 pkt) Załóż alert na któryś z wykresów Grafany
   

