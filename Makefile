
DOXYGEN=doxygen

doc:	doc/doxypy.py doxygen.conf src/
	$(DOXYGEN) doxygen.conf

clean:
	rm -R doc/html doc/doxygen_objdb_* && find . -iname '*.pyc' -exec rm {} \;

all: test

#Tests here
test:

#Setup pyexe
exepe: