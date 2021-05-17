# definiujemy obraz na którym będziemy bazowali
FROM python

# ustawiamy katalog domyślny dla naszej aplikacji
WORKDIR /usr/src/app

# kopiujemy wszystkie pliki z obecnego katalogu do WORKDIR
COPY . .

# instalujemy zalezności
#RUN pip install -r requirements.txt 
RUN pip install -r requirements2.txt

# definiujemy port który będzie otwarty w kontenerze
EXPOSE 5000

# definiujemy komendę startową
#CMD ["python", "./app.py"]
CMD ["streamlit", "run", "./app2.py", "--server.port", "5000"]
