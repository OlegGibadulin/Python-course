class FileReader(object):
	"""docstring for FileReader"""

	def __init__(self, path):
		super(FileReader, self).__init__()
		self.path = path

	def read(self):
		try:
			lines = ""
			with open(self.path, "r") as f:
				for line in f:
					lines += line
			return lines
		except IOError:
			return ""
		

if (__name__ == "__main__"):
	reader = FileReader("0.txt")
	print(reader.read())