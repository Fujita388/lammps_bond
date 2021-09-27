all: bond.lammpstrj

bond.lammpstrj: 
	python3 generate.py
	/home/Fujita388/github/lammps/src/lmp_serial < bond.input

test:
	python3 density.py > test.atoms

density:
	python3 density.py > density.dat
	gnuplot density.plt

clean: 
	rm *.lammpstrj *.atoms *.png *.dat

rm_png:
	rm *.png *.dat test.atoms


