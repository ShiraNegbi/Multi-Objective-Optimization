import datetime
import random

# The class represents an apartment and its characteristics that are relevant for renting it
class apartment():
    def __init__(self, id_number, rent_per_month, distance, entrance_date,
                 room_number, size_of_apartment, floor_number):
        self.id_number = id_number
        self.rent_per_month = rent_per_month
        self.distance = distance
        self.entrance_date = entrance_date
        self.room_number = room_number
        self.size_of_apartment = size_of_apartment
        self.floor_number = floor_number
        dictionary = {}
        dictionary["id_number"] = id_number
        dictionary["rent_per_month"] = rent_per_month
        dictionary["distance"] = distance
        dictionary["entrance_date"] = entrance_date
        dictionary["room_number"] = room_number
        dictionary["size_of_apartment"] = size_of_apartment
        dictionary["floor_number"] = floor_number
        self.dictionary = dictionary

    # Description
    def __str__(self):
        ret = ""
        for i in self.dictionary:
            ret += "\n" + i + " " + str(self.dictionary[i])
        return ret

# Keep only the apartments which have the proper number of rooms, size and floor.
# The apartments can be later chosen by their cost, distance and entrance date.
def screen_apartments(apartment_list, rooms, min_size, min_floor):
    return [a for a in apartment_list if (a.room_number == rooms and a.size_of_apartment >= min_size
                                          and a.floor_number >= min_floor)]

# Generate a list of apartments
def get_apartments(num_apartments):
    result = []
    for i in range(num_apartments):
        id_number = i
        distance = random.randrange(10, 50)
        entrance_date = random.randrange(1, 12)
        room_number = random.randrange(1, 6)
        size_of_apartment = room_number * (15 + random.randrange(0, 5)) + 20
        floor_number = random.randrange(1, 20)
        rent_per_month = (size_of_apartment * 70 + floor_number * 20 + random.randrange(0, 700))
        rent_per_month -= rent_per_month % 10
        result.append(apartment(id_number, rent_per_month, distance, entrance_date,
                                room_number, size_of_apartment, floor_number))
    return result

# Calculate the value by the given weights for the objectives
def get_objective_value(apartment, cost_weight, dist_weight, ent_weight):
    return cost_weight * apartment.rent_per_month + dist_weight * apartment.distance +\
           ent_weight * apartment.entrance_date

# Sort a list of apartments by the objective value
def sort_by_objectives(apartments, cost_weight, dist_weight, ent_weight):
    apartments.sort(key=lambda apartment: get_objective_value(apartment, cost_weight, dist_weight, ent_weight), reverse=True)

# Choose the optimal apartment
def main():

    # Generate a list of apartments that are optional for rent
    apartment_list = get_apartments(100)
    for apartment in apartment_list:
        print(apartment)

    start = datetime.datetime.now()

    # Screen the apartments by the constraints
    relevant_apartments = (screen_apartments(apartment_list, 3, 70, 2))
    print("\nRelevant:")
    for apartment in relevant_apartments:
        print(apartment)

    # Define the weights of the objectives and sort the apartments by them
    weight_cost = -20
    weight_dist = -13
    weight_ent = -10

    sort_by_objectives(relevant_apartments, weight_cost, weight_dist, weight_ent)
    print("\nSorted by objectives:")
    for apartment in relevant_apartments:
        print(apartment)
        print("Objective value = " + str(get_objective_value(apartment, weight_cost, weight_dist, weight_ent)))
        print()

    # Choose the best apartment from the list
    print("Optimal apartment:")
    optimal = relevant_apartments[0]
    print(optimal)

    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    main()
