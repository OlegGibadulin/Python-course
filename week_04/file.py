import tempfile
import os

class File(object):
	"""docstring for File"""

	def __init__(self, path):
		super(File, self).__init__()
		self.path = path

	def __str__(self):
		return '{}'.format(self.path)

	def __add__(self, obj):
		new_path = tempfile.gettempdir()
		new_path = os.path.join(new_path, "File.txt")

		new_obj = File(new_path)

		with open(self.path, "r") as f:
			str1 = f.readlines()

		with open(obj.path, "r") as f:
			str2 = f.readlines()

		with open(new_path, "w") as f:
			for str3 in str1:
				f.write(str3)
			for str3 in str2:
				f.write(str3)

		return new_obj

	def __getitem__(self, index):
		with open(self.path, "r") as f:
			new_str = f.readlines()

		return new_str[index]


	def write(self, text):
		with open(self.path, "w") as f:
			f.write(text)

if (__name__ == "__main__"):
	obj1 = File("file1.txt")
	obj1.write("text_text\n")
	print(obj1)
	obj2 = File("file2.txt")
	obj2.write("text_text")
	print(obj2)
	new_obj = obj1 + obj2
	print(new_obj)
	for line in obj1:
		print(line)

