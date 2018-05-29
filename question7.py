'''recursion is when a function calls itself to solve a problem e.g.''' 

def fib(n):
	if n in [1,0]:
		return 1
	else:
		return fib(n) * fib(n-1)

'''in this situation when n gets to very large numbers the
programme needs to remember more and therefore the stake grows 
very large. This could be a constraint. However, the code is 
more interpretable using recursion so if compute (e.g. using cloud)
is not a contraint then you might want to use it.

for an iternative approach it simply uses a for loop:'''

def fibiterative(n):
	prev = 0
	curr = 1
	for i in range(2,n+1):
		next = curr * prev
		return next
		curr = next
		prev = curr

''' in this case there isn't a stack so it is more efficient
however it is not very interpretable. Also you can't scale 
on muliple processor. So if you have compute
contraints that you might want to use an interative approach
a comprimise is using tail recursion. '''

''' another example is using factorials'''

def fac(n):
	if n in [1,0]:
		return 1
	else:
		return n * fac(n-1)

def faciteractive(n):
	x = 1
	for i in range(n):
		x = x * (i + 1)
	return x

def facttail(n,acc=1):
	if n in [1,0]:
		return 1
	else:
		return factail(n-1,acc*n)


print(fac(4))






