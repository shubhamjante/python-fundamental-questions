"""
Write a python program to help an airport manager to generate few statistics based on the ticket details
available for a day.
Go through the below program and complete it based on the comments mentioned in it.

Note: Perform case sensitive string comparisons wherever necessary.
"""


# Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
# Note: flight_no has the following format - "airline_name followed by three digit number


# Global variable
ticket_list = ["AI567:MUM:LON:014", "AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145", "AI077:MUM:CAN:060",
               "SI267:BLR:MUM:148", "AI567:CHE:SIN:015", "AI077:MUM:SIN:050", "AI077:MUM:LON:051", "SI267:MUM:SIN:146"]


def find_passengers_flight(airline_name="AI"):
    # This function finds and returns the number of passengers travelling in the specified airline.
    count = 0
    for i in ticket_list:
        string_list = i.split(":")
        if(string_list[0].startswith(airline_name)):
            count += 1
    return count


def find_passengers_destination(destination):
    count = 0
    for i in ticket_list:
        if destination == i.split(':')[2]:
            count += 1

    return count


def find_passengers_per_flight():
    """
    Write the logic to find and return a list having number of passengers traveling per flight based on the details
    in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].
    """

    flights = dict()

    for i in ticket_list:
        if i.split(':')[0] not in flights:
            flights[i.split(':')[0]] = 1
        else:
            flights[i.split(':')[0]] += 1

    return ["{}:{}".format(key, val) for key, val in flights.items()]


def sort_passenger_list():
    flights = {fly.split(':')[0]:int(fly.split(':')[-1]) for fly in find_passengers_per_flight()}
    flights_list = sorted(flights.items(), key=lambda x: x[1], reverse=True)

    return ["{}:{}".format(flight, passengers) for flight, passengers in flights_list]


print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())