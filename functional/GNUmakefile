.PHONY: clean pdf html view
	
QMD_FILES = $(wildcard *.qmd)
HTML_FILES = $(patsubst %.qmd,%.html, $(QMD_FILES))
PDF_FILES = $(patsubst %.qmd,%.pdf, $(QMD_FILES))

.SUFFIXES : .pdf .qmd .html

all: html
html: notes.html
pdf : notes.pdf
	
view: notes.pdf
	open -a Skim notes.pdf

clean:
	rm -f notes.md *.bak* indent.log *.fls notes.pdf *.pdf.tmp *.fdb_latexmk *.tex notes.html

.qmd.pdf:
	quarto render $< --to pdf --cache

.qmd.html:
	quarto render $< --to html --cache
