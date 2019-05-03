import time

def new_fib(n):
	known_nos={0:0,1:1}
	if n in known_nos:
		return known_nos[n]
	
	res = new_fib(n-1) + new_fib(n-2)
	known_nos[n] = res
	return res

def old_fib(n):
	if n ==0:
		return 0
	elif n==1:
		return 1
	else:
		n = old_fib(n-1) + old_fib(n-2)
		return n

clock = time.time()


result = new_fib(40)
print(result)


new_clock = time.time() - clock
print(clock, new_clock)

