class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops=0):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        - stops: The number of stops (default 0 for direct flights).
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

    def find_cheapest_flight(data):
        if data is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        itineraries = first_flight["itineraries"]
        origin = itineraries[0]["segments"][0]["departure"]["iataCode"]
        destination = itineraries[-1]["segments"][-1]["arrival"]["iataCode"]
        out_date = itineraries[0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = itineraries[-1]["segments"][-1]["departure"]["at"].split("T")[0]
        stops = sum(len(itinerary["segments"]) - 1 for itinerary in itineraries)

        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)

        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])
            itineraries = flight["itineraries"]
            if price < lowest_price:
                lowest_price = price
                origin = itineraries[0]["segments"][0]["departure"]["iataCode"]
                destination = itineraries[-1]["segments"][-1]["arrival"]["iataCode"]
                out_date = itineraries[0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = itineraries[-1]["segments"][-1]["departure"]["at"].split("T")[0]
                stops = sum(len(itinerary["segments"]) - 1 for itinerary in itineraries)
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)
                print(f"Lowest price to {destination} with {stops} stops is £{lowest_price}")

        return cheapest_flight
