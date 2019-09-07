import os
import csv

class CarBase(object):
	"""docstring for CarBase"""

	def __init__(self, brand, photo_file_name, carrying):
		super(CarBase, self).__init__()
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = carrying

	def get_photo_file_ext(self):
		return os.path.splitext(self.photo_file_name)

class Car(CarBase):
	"""docstring for Car"""

	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		self.car_type = "car"
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = carrying
		self.passenger_seats_count = passenger_seats_count

class Truck(CarBase):
	"""docstring for Truck"""

	def __init__(self, brand, photo_file_name, carrying, body_whl):
		self.car_type = "truck"
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = carrying
		if (body_whl == ""):
			self.body_length = 0.0
			self.body_width = 0.0
			self.body_height = 0.0
		else:
			list = body_whl.split('x')
			self.body_length = float(list[0])
			self.body_width = float(list[1])
			self.body_height = float(list[2])

	def get_body_volume(self):
		return self.body_length * self.body_width * self.body_height

class SpecMashine(CarBase):
	"""docstring for SpecMashine"""

	def __init__(self, brand, photo_file_name, carrying, extra):
		self.car_type = "spec_machine"
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = carrying
		self.extra = extra

def get_car_list(csv_filename):
	car_list = []
	try:
		with open(csv_filename, "r") as f:
			reader = csv.reader(f, delimiter=';')
			next(reader)
			for row in reader:
				if (len(row) != 7):
					continue
				if (row[0] == "car"):
					a = []
					arr = [1, 2, 3, 5]
					check = 1
					for i in arr:
						if (row[i] == ""):
							check = 0
					if (check):
						for i in arr:
							s = row[i]
							if (i == 2):
								s = int(s)
							if (i == 5):
								s = float(s)
							a.append(s)
						obj = Car(a[0], a[2], a[3], a[1])
						car_list.append(obj)
				elif (row[0] == "truck"):
					a = []
					arr = [1, 3, 4, 5]
					check = 1
					for i in arr:
						if (row[i] == "" and i != 4):
							check = 0
					if (check):
						for i in arr:
							s = row[i]
							if (i == 5):
								s = float(s)
							a.append(s)
						obj = Truck(a[0], a[1], a[3], a[2])
						car_list.append(obj)
				elif (row[0] == "spec_machine"):
					a = []
					arr = [1, 3, 5, 6]
					check = 1
					for i in arr:
						if (row[i] == ""):
							check = 0
					if (check):
						for i in arr:
							s = row[i]
							if (i == 5):
								s = float(s)
							a.append(s)
						obj = SpecMashine(a[0], a[1], a[2], a[3])
						car_list.append(obj)
	except IOError:
		print("File does not exist")
	return car_list

if (__name__ == "__main__"):
	car_list = get_car_list("example.csv")
	count = 0
	str1 = ""
	for dig in car_list:
		str1 += str(dig) + " "
		count += 1
		if (count % 4 == 0):
			print(str1)
			print("\n")
			str1 = ""
	s = car_list[0]
	print(s.brand, s.passenger_seats_count, s.photo_file_name, s.carrying, s.get_photo_file_ext())
	s = car_list[1]
	print(s.brand, s.body_length, s.body_width, s.body_height, s.photo_file_name, s.carrying, s.get_body_volume())
	s = car_list[4]
	print(s.brand, s.photo_file_name, s.carrying, s.extra)