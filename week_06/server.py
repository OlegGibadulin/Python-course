import asyncio

memory = []

class ClientServerProtocol(asyncio.Protocol):
	"""docstring for ClientServerProtocol"""
	def __init__(self):
		self.transport = None

	def connection_made(self, transport):
		self.transport = transport

	def data_received(self, data):
		resp = data.decode()
		arr = resp[0:-1].split()
		var = arr[0]
		line = arr[1:]
		if (var == "get" and len(line) == 1):
			resp = self.get(line)
		elif (var == "put" and len(line) == 3 and \
			self._is_float(line[1]) and self._is_int(line[2])):
			resp = self.put(line)
		else:
			resp = "error\nwrong command\n\n"
		self.transport.write(resp.encode())

	@staticmethod
	def _is_float(num):
		try:
			float(num)
			return True
		except ValueError:
			return False

	@staticmethod
	def _is_int(num):
		try:
			int(num)
			return True
		except ValueError:
			return False

	def get(self, key):
		array = ["ok"]
		if (key[0] == "*"):
			for line in memory:
				array.append(' '.join(line))
		else:
			for line in memory:
				if (key[0] == line[0]):
					array.append(' '.join(line))

		lines = '\n'.join(array)
		
		return f"{lines}\n\n"


	def put(self, line):
		check = 1
		for arr in memory:
			count = 0
			for i in range(3):
				if (line[i] == arr[i]):
					count += 1
			if (count == 3):
				check = 0

		if (check):
			memory.append(line)

		return "ok\n\n"

def run_server(host, port):
	loop = asyncio.get_event_loop()
	coro = loop.create_server(ClientServerProtocol, host, port)

	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

if (__name__ == "__main__"):
	run_server('127.0.0.1', 8888)