def write_to(filename, mode, info):
	with open(filename, mode) as f:
		f.write(info + '\n')
	