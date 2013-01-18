
DOXYGEN=doxygen

doc:	doc/doxypy.py doxygen.conf src/
	$(DOXYGEN) doxygen.conf

clean:
	rm -R doc/html doc/doxygen_temp* && find . -iname '*.pyc' -exec rm {} \;

all: doc

#Tests here
test:
