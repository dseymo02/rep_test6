class ListUtils:
	def __init__(self,contents,size):
		self.contents = contents
		self.size = size

	def add_item(self,item):
		self.contents.append(item)
		return self.contents

	def update_size(self):
		self.size = len(self.contents)
		return self.size

def main():
	list1 = ListUtils([],0)

	print(list1.contents,list1.size)

	print(list1.add_item("2"))
	print(list1.update_size())
	print(list1.size)

if __name__ == "__main__":
	main()