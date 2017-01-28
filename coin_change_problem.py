total, num_coins = [int(i) for i in raw_input().split()]
if num_coins:
	coins = [long(i) for i in raw_input().split()]
upper_bound = [total/coin_val + 1 for coin_val in coins]
accepted_configurations = 0
normalisers = upper_bound + [1]


def prod(x):
	return reduce(lambda a, b: long(a) * long(b), x + [1])

if num_coins == 0 or total == 0:
	print 0

else:
	for i in xrange(1, prod(upper_bound)):
		configuration = [(i/prod(normalisers[j:])) % upper_bound[j-1] for j in range(1, len(upper_bound)+1)]
		value = sum([conf*coins[t] for t, conf in enumerate(configuration)])
		if value == total:
			accepted_configurations += 1

	print accepted_configurations	
