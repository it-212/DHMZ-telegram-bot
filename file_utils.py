from   os.path import exists as file_exists

def get_content(file_name : str):      
	return set(int(i) for i in read_all_lines(file_name))

def write_whole_file(file_name : str, lines : list) -> None:
	with open('data/' + file_name, 'w') as file:
		for line in lines:
			file.write(line + '\n')

def add_line(file_name : str, line : str) -> None:
	with open('data/' + file_name, 'a') as file:
		file.write(line + '\n')

def remove_line(file_name : str, line : str) -> None:
	data = read_all_lines(file_name)
	if line in data:
		data.remove(line)
		write_whole_file(file_name, data)

def read_all_lines(file_name : str) -> list:
	#procitaj sve jedinstvene linije u fileu
	path = 'data/' + file_name
	if file_exists(path):
		with open(path, 'r') as file:
			data = file.read()
			return list(i for i in filter(lambda x: x != '', data.split('\n')))
	return list()

