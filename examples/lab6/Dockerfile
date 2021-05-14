# definiujemy obraz na którym będziemy bazowali
FROM python

# ustawiamy katalog domyślny dla naszej aplikacji
WORKDIR /usr/src/app

# kopiujemy wszystkie pliki z obecnego katalogu do WORKDIR
COPY . .

# instalujemy zalezności
RUN pip install 'flask[async]'==2.0.0
RUN pip install MemeLib==0.1.5 
RUN pip install statsd

# definiujemy port który będzie otwarty w kontenerze
EXPOSE 5000

# definiujemy komendę startową
CMD ["python", "./app.py"]
