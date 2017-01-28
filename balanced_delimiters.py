brackets = raw_input()
pairs = {'{':'}', '[':']', '(':')'}

index = -1
indicator = [] 

for i, bracket in enumerate(brackets):

	if index == -1 and bracket not in pairs.keys():
		index = 1
		break

	elif bracket in pairs.keys() or indicator[index] not in pairs.keys() or bracket != pairs[indicator[index]]:
		indicator.append(bracket)
		index += 1
	else:
		# bracket == indicator[index]:
		del indicator[index]
		index -= 1

print index == -1
