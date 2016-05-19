tex :
	pdflatex halotools

all :
	pdflatex halotools
	bibtex halotools
	pdflatex halotools
	pdflatex halotools
	pdflatex halotools


clean :
	-rm *.aux *.bbl *.log *.synctex.gz
