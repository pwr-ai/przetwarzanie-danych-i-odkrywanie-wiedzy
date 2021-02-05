#!/bin/sh

echo "Starting book building..."

if [ "$#" = 1 ] && [ $1 = "pdf" ] 
then

	jupyter-book build . --builder pdfhtml
        open _build/pdf/book.pdf
else
	jupyter-book build .
        open _build/html/index.html
fi
