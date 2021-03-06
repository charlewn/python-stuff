def pour_problem(X,Y, goal, start=(0,0)):
	"""X and Y are the capacity of glasses; (x, y) is current fill levels
	and represents a state. The goal is a level that can be in either glass.
	Start at start state and follow successors until we reach the goal.
	Keep track of frontier and previously explored; fail when no frontier."""
	if goal in start:
		return [start]
	explored = set()
	frontier = [ [start] ]
	while frontier:
		path = frontier.pop(0)
		print "frontier:", frontier
		print "path:", path
		(x, y) = path[-1]
		print x, y
		for (state, action) in successors(x,y, X, Y).items():
			#print "successors:", successors(x,y, X, Y).items()
			print "state: {} action: {}".format(state, action)
			if state not in explored:
				explored.add(state)
				path2 = path + [action, state]
				print "path2:" , path2 
				if goal in state:
					return path2
				else:
					frontier.append(path2)
	return Fail
				

Fail = []

def successors(x,y,X,Y):
	assert x<= X and y <= Y
	print "Var: x ={}, y ={}, X ={}, Y= {}".format(x,y,X,Y)
	print (0, y+x), "X->Y:"
	return {((0, y+x) if y+x<=Y else (x-(Y-y), y+(Y-y))): 'X->Y',
			((x+y, 0) if x+y<=X else (x+(X-x), y-(X-x))): 'X<-Y',
			(X, y): 'fill X', (x, Y): 'fill Y',
			(0, y): 'empty X', (x, 0):'empty Y'}
	print "test passed!"


print pour_problem(9, 4, (6,0))