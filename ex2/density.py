#x軸方向の密度を測定


#シミュレーションボックスを幅dに区切る
def density(filename, d):
	with open(filename, "r") as f:
		data = f.readlines()
	group = []
	for i, line in enumerate(data):
		if "ITEM: TIMESTEP" in line:
			group.append(i)
	atoms_num = int(data[3])
	l = data[6]
	L = float(l.split()[1])  #立方体の一辺
	v = L ** 2 * d  #分割した体積
	atom_list = []
	for i in range(atoms_num):
		position = data[group[-1]+9+i]  #最後のグループの座標のdata
		x = float(position.split()[2])
		x = x * 2 * L  #xをrescale
		atom_list.append(x)
	atom_list.sort()
	for i in range(int(2.0*L/d)):
		i = d * i
		n = sum(i<j<=i+d for j in atom_list)  #i<j<=i+dに含まれる原子の数
		rho = float(n) / v
		print(rho, i)



density("bond.lammpstrj", 0.1)
