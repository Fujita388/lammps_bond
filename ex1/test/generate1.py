import numpy as np
import random


class Atom:
	def __init__(self, x, y, z, xvel):
		self.x = x
		self.y = y
		self.z = z
		self.vx = xvel
		self.vy = 0.0
		self.vz = 0.0


#密度から格子数を計算　L: シミュレーションボックス　rho: 密度
def get_lattice_number(L, rho):
	m = np.floor((L**3 * rho / 4.0)**(1.0 / 3.0))
	drho1 = np.abs(4.0 * m **3 / L**3 - rho)
	drho2 = np.abs(4.0 * (m + 1)**3 / L**3 - rho)
	if drho1 < drho2:
		return m
	else:
		return m + 1


def add_ball(atoms, xpos, xvel, L, rho):
	m = int(get_lattice_number(L, rho))  #r = 8
	s = 1.7  #格子定数    
	h = 0.5 * s
	for ix in range(0, m):   #原子数は8倍になる
		for iy in range(0, m):
			for iz in range(0, m):
				x = ix * s
				y = iy * s
				z = iz * s
				atoms.append(Atom(x, y, z, xvel))
				atoms.append(Atom(x, y+h, z+h, xvel))
				atoms.append(Atom(x+h, y, z+h, xvel))
				atoms.append(Atom(x+h, y+h, z, xvel))


def save_file(filename, atoms):
	with open(filename, "w") as f:
		f.write("Position Data\n\n")
		f.write("{} atoms\n".format(len(atoms)))
		f.write("400 bonds\n\n")
		f.write("2 atom types\n")
		f.write("1 bond types\n\n")
		f.write("0.00 17.00 xlo xhi\n")
		f.write("0.00 17.00 ylo yhi\n")
		f.write("0.00 17.00 zlo zhi\n")
		f.write("\n")
		f.write("Atoms\n\n")
		for i, a in enumerate(atoms):
			if i < 800:  #粒子番号、BondID、atom type、座標
				f.write("{} {} {} {} {} {}\n".format(i+1, i//2, 2-(i+1)%2, a.x, a.y, a.z))
			else:
				f.write("{} {} {} {} {} {}\n".format(i+1, i-400, 1, a.x, a.y, a.z))
		f.write("\n")
		f.write("Velocities\n\n")
		for i, a in enumerate(atoms):
			f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
		f.write("\n")
		f.write("Bonds\n\n")
		for i in range(1, 401):  #bond数は粒子数の10分の1
			f.write("{} {} {} {}\n".format(i, 1, 2*i-1, 2*i))
	print("Generated {}".format(filename))


atoms = []

add_ball(atoms, 0.0, 0.0, 17, 0.8)

save_file("bond1.atoms", atoms)
