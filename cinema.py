from enum_class import SeatType
class CinemaSystem:
    def __init__(self):
        self.__cinema = []

    def add_cinema(self,cinema):
        if isinstance(cinema, Cinema):
            self.__cinema.append(cinema)

    def show_cinema(self):
        if self.__cinema is not None:
            for c in self.__cinema:
                print(c)


class Cinema:
    def __init__(self, name, location, total_cinema_hall=0):
        self.__name = name
        self.__location = location 
        self.__total_cinema_hall = total_cinema_hall
        self.__halls = [] # List of CinemaHall

    def add_halls(self,halls):
        if isinstance(halls, list):
            self.__halls.extend(halls)
        else:
            self.__halls.append(halls)
        self.__total_cinema_hall += 1

    def __str__(self):
        return self.__name+" in location " \
        + self.__location+" has total cinema hall " \
        + str(self.__total_cinema_hall)

class CinemaHall:
    def __init__(self,name, projection_system, total_seat):
        self.__name = name
        self.__projection_system = projection_system
        self.__total_seat = total_seat
        self.__shows = [] # List of Show
        self.__seats = []

        # Add A1 to F20
        for i in [chr(x) for x in range(ord('A'), ord('F')+1)]:
            for j in range(1,21):
                self.add_seat(CinemaHallSeat(str(i),str(j),SeatType.PRIME))
        # Add G1 to M20
        for i in [chr(x) for x in range(ord('G'), ord('M')+1)]:
            for j in range(1,21):
                self.add_seat(CinemaHallSeat(str(i),str(j),SeatType.PREMIUM))

        for i in range(7):
            self.add_seat(CinemaHallSeat('AA',str(i),SeatType.SUITE))

    def add_seat(self,seat):
        self.__seats.append(seat)

class CinemaHallSeat:
    def __init__(self, seat_row, seat_col, seat_type):
        self.__seat_row = seat_row
        self.__seat_col = seat_col
        self.__seat_type = seat_type

