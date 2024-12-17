data = ['1:hello', '1:beautiful', '2:world', '3:today']

sorted_data = sorted(data, key= lambda x: int(x.split(':')[0]))

print(sorted_data)

s1 = 'namelesst'
s2 = 'salesmeny'

def str_compare(s1, s2):
	if len(s1) != len(s2):
		return False

	map = {}
	for char in s1:
		map[char] = (map.get(char, 0)) + 1

	for char in s2:
		if char not in map.keys():
			return False
		map[char] -= 1

	return True


print(str_compare(s1, s2))
