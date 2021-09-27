import numpy as np
import random
from math import cos, sin, sqrt


class Atom:
	def __init__(self, x, y, z, atom_type, bond_id):
		self.x = x
		self.y = y
		self.z = z
		self.type = atom_type
		self.bond_id = bond_id
		v0 = 0   #初速の大きさ
		z = random.random()*2.0-1
		s = random.random()*3.14*2.0
		self.vx = v0*sqrt(1.0-z**2)*cos(s)
		self.vy = v0*sqrt(1.0-z**2)*sin(s)
		self.vz = v0*z


#密度から格子数を計算　L: シミュレーションボックス　rho: 密度
def get_lattice_number(L, rho):
	m = np.floor((L**3 * rho / 4.0)**(1.0 / 3.0))
	drho1 = np.abs(4.0 * m **3 / L**3 - rho)
	drho2 = np.abs(4.0 * (m + 1)**3 / L**3 - rho)
	if drho1 < drho2:
		return m
	else:
		return m + 1


#特定の確率で原子番号2を選ぶ
def choice():
	l = [1, 2]
	w = [10, 5]
	
	p = random.choices(l, weights=w)
	if p[0] == 1:  #1を選択
		return 1
	else:  #2を選択
		return 2


def add_ball(atoms, L, rho):
	m = int(get_lattice_number(L, rho))  
	s = 1.54  #格子定数    
	h = 0.5 * s
	atom_type = 1
	bond_id = 0
	bond_num = 0
	index = 1
	for ix in range(0, m):   #原子数は8倍になる
		for iy in range(0, m): 
			for iz in range(0, m):
				x = ix * s
				y = iy * s
				z = iz * s
				atom_type1 = choice()
				if atom_type1 == 1:  #原子番号1の場合
					atoms.append(Atom(x, y, z, atom_type, bond_id))
					atoms.append(Atom(x, y+h, z+h, atom_type1, bond_id+1))  
					atoms.append(Atom(x+h, y, z+h, atom_type, bond_id+2))
					atoms.append(Atom(x+h, y+h, z, atom_type, bond_id+3))
					bond_id += 4
				else:  #原子番号2の場合
					atom_type1 = 2  #原子番号を2に置換
					bond_num += 1
					atoms.append(Atom(x, y, z, atom_type, bond_id))
					atoms.append(Atom(x, y+h, z+h, atom_type1, bond_id))  
					atoms.append(Atom(x+h, y, z+h, atom_type, bond_id+1))
					atoms.append(Atom(x+h, y+h, z, atom_type, bond_id+2))
					bond_id += 3
					bonds_list.append(index)
					bonds_list.append(index+1)
				index += 4
	return bond_num  #bond数を返す


def save_file(filename, atoms, bond_num):
	with open(filename, "w") as f:
		f.write("Position Data\n\n")
		f.write("{} atoms\n".format(len(atoms)))
		f.write("{} bonds\n\n".format(bond_num))
		f.write("2 atom types\n")
		f.write("1 bond types\n\n")
		f.write("0.00 30.80 xlo xhi\n")
		f.write("0.00 15.40 ylo yhi\n")
		f.write("0.00 15.40 zlo zhi\n")
		f.write("\n")
		f.write("Atoms\n\n")
		for i, a in enumerate(atoms):  #粒子番号、BondID、atom type、座標
			f.write("{} {} {} {} {} {}\n".format(i+1, a.bond_id, a.type, a.x, a.y, a.z))
		f.write("\n")
		f.write("Velocities\n\n")
		for i, a in enumerate(atoms):
			f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
		f.write("\n")
		f.write("Bonds\n\n")
		i = 1 
		j = 0  
		while len(bonds_list) > j:
			f.write("{} {} {} {}\n".format(i, 1, bonds_list[j], bonds_list[j+1]))
			i += 1
			j += 2
	print("Generated {}".format(filename))


atoms = []
bonds_list = []
bond_num = add_ball(atoms, 15.4, 1.1)
save_file("bond.atoms", atoms, bond_num)
