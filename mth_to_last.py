m=int(raw_input())
l=[{int(i): j+1} for j, i in enumerate(raw_input().split())]

def traverse(traversed, address):

	if traversed == len(l) - m:
		return l[address].keys()[0]
	else:
		try:
			traversed += 1
			address = l[address].values()[0]
			return traverse(traversed, address)

		except:
			return 'NIL' 

print traverse(traversed=0, address=0)
