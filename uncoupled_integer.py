l = [int(i) for i in raw_input().split(', ')]


memory = {}

for each in l:
	if memory.pop(each, None) is None:
		memory[each] = 1

print memory.keys()[0]
