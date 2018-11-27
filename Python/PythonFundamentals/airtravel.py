"""Model for aircraft flight"""

class Flight:
	"""A flight with a perticular passanger aircraft"""
	def __init__(self, number, aircraft):
		if not number[:2].isalpha():
			raise ValueError("No airline code in '{}'".format(number))

		if not number[:2].isupper():
			raise ValueError("Invalid airline code '{}'".format(number))

		if not (number[2:].isdigit() and int(number[2:]) < 9999):
			raise ValueError("Invalid route number '{}'".format(number))

		self._number = number
		self._aircraft = aircraft

		rows, seats = self._aircraft.seating_plan()
		self._seating = [None] + [{letter:None for letter in seats} for _ in rows]
	    
	def number(self):
	    return self._number

	def airline(self):
		return self._number[:2]

	def aircraft_model(self):
		return self._aircraft.model()

	def _parse_seat(self, seat):
		"""Parse a seat designator into a valid row and letter.

		Args:
			seat: A seat designator such as 12F

		Returns:
			A tuple containing an integer and a string for row and seat.

		"""
		row_numbers, seat_letters = self._aircraft.seating_plan()

		letter = seat[-1]
		if letter not in seat_letters:
			raise ValueError("Invalid seat letter {}".format(letter))

		row_text = seat[:-1]
		try:
			row = int(row_text)

		except ValueError:
			raise ValueError("Invalid seat row {}".format(row_text))

		if row not in row_numbers:
			raise ValueError("Invalid row number {}".format(row))

		return row, letter

	def allocate_seat(self, seat, passanger):
		"""Allocate a seat to a passanger

		Args: 
			seat: A seat designator such as '12C' or '21F'
			passanger: The passanger name

		Raises:
			ValueError: If the seat is unavailable
		"""
		rows, seat_letters = self._aircraft.seating_plan()

		letter = seat[-1]
		if letter not in seat_letters:
			raise ValueError("Invalid seat letter {}".format(letter))

		row_text = seat[:-1]
		try:
			row = int(row_text)

		except ValueError:
			raise ValueError("Invalid seat row {}".format(row_text))

		if row not in rows:
			raise ValueError("Invalid row number {}".format(row))

		if self._seating[row][letter] is not None:
			raise ValueError("Seat {} already occupied".format(seat))

		self._seating[row][letter] = passanger

	def relocate_passanger(self, from_seat, to_seat):
		"""Relocate a passanger to a different seat.

		Args:
			from_seat: The existing seat designator for the 
						passanger to be moved.
			to_seat: The new seat designator
		"""
		from_row, from_letter = self._parse_seat(from_seat)
		if self._seating[from_row][from_letter] is None:
			raise ValueError("No passanger to relocate in seat {}".format(from_seat))

		to_row, to_letter = self._parse_seat(to_seat)
		if self._seating[to_seat][from_letter] is None:
			raise ValueError("Seat {} already occupied".format(to_seat))

		self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
		self._seating[from_row][from_letter] = None


	def num_available_seats(self):
		return sum(sum(1 for s in row.values() if s is None)
					for row in self._seating
					if row is not None)

	def make_boarding_cards(self, card_printer):
		for passanger, seat in sorted(self._passanger_seats()):
			card_printer(passanger, seat, self.number(), self.aircraft_model())

	def _passanger_seats(self):
		"""An iterable series of passanger seating allocations"""
		row_numbers, seat_letters = self._aircraft.seating_plan()
		for row in row_numbers:
			for letter in seat_letters:
				passanger = self._seating[row][letter]
				if passanger is not None:
					yield (passanger, "{}{}".format(row, letter))


class Aircraft:

	def __init__(self, registration):
		self.registration = registration

	def registration(self):
		return self._registration

	def num_seats(self):
		rows, rows_seats = self.seating_plan()
		return len(rows)*len(rows_seats)

class AirbusA319(Aircraft):

	def model(self):
		return "Airbus A319"

	def seating_plan(self):
		return range(1, 23), "ABCDEF"

class Boeing777(Aircraft):

	def model(self):
		return "Boeing 777"

	def seating_plan(self):
		return range(1, 56), "ABCDEFGHJK"



def make_flights():
	f = Flight("BA758", AirbusA319("G-EUPT"))
	f.allocate_seat('12F', 'Guido van Rossum')
	f.allocate_seat('15F', 'Bjarne Hejlsberg')
	f.allocate_seat('15E', 'Akash Giri')
	f.allocate_seat('1C', 'Vishal Giri')
	f.allocate_seat('1D', 'Richard Hickey ')

	g = Flight("AF72", Boeing777("F-GSPS"))
	g.allocate_seat('55K', 'Kiley Jenner')
	g.allocate_seat('33G', 'Ari')
	g.allocate_seat('4B', 'JLO')
	g.allocate_seat('4A', 'Roar')
	return f, g



def console_card_printer(passanger, seat, flight_number, aircraft):
	output = "| Name: {0}" 	 \
			 " Flight: {1}" \
			 " Seat: {2}"   \
			 " Aircraft: {3}"\
			 " |".format(passanger, flight_number, seat, aircraft)

	banner = "+" + "-"*(len(output) -2) + "+"
	border = "|" + " "*(len(output) -2) + "|"
	lines = [banner, border, output, border, banner]
	card = '\n'.join(lines)
	print(card)
	print()