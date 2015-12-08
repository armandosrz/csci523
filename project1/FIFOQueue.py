
#______________________________________________________________________________
# Queues: FIFOQueue (source: http://aima-python.googlecode.com/svn/trunk/utils.py)

class Queue:
	"""Queue is an abstract class/interface.
	Supports the following methods and functions:
		q.append(item)  -- add an item to the queue
		q.extend(items) -- equivalent to: for item in items: q.append(item)
		q.pop()         -- return the top item from the queue
		len(q)          -- number of items in q (also q.__len())
		item in q       -- does q contain item?
	If Python ever gets interfaces, Queue will be an interface."""

	def __init__(self):
		abstract

	def extend(self, items):
		for item in items: self.append(item)

class FIFOQueue(Queue):
	"""A First-In-First-Out Queue."""
	def __init__(self):
		self.A = []; self.start = 0
	def enqueue(self, item):
		self.A.append(item)
	def __len__(self):
		return len(self.A) - self.start
	def extend(self, items):
		self.A.extend(items)
	def dequeue(self):
		e = self.A[self.start]
		self.start += 1
		if self.start > 5 and self.start > len(self.A)/2:
			self.A = self.A[self.start:]
			self.start = 0
		return e
	def __contains__(self, item):
		return item in self.A[self.start:]
