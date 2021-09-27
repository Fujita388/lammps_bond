all: bond.lammpstrj

bond.lammpstrj: bond.input
	/home/Fujita388/github/lammps/src/lmp_serial < bond.input

bond.input: bond.atoms

bond.atoms:
	python3 generate.py

clean:
	rm *.atoms *.lammpstrj log.lammps 
