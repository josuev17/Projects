# this is a dictionary which reflects the available vehicles that a dealer has on their lot.
# there are 13 vehicles, and we have the brand, body type, and price for each vehicle.

available_vehicles = {1:["tesla", "sedan", 30000], 2:["honda", "SUV", 45000], 3:["honda", "sedan", 26000],
                      4:["ferarri", "sports car", 200000], 5:["volkswagen", "SUV", 32000], 6:["volkswagen", "sedan", 22000],
                      7:["maserati", "sports car", 110000], 8:["jeep", "truck", 48000], 9:["jeep", "SUV", 40000], 
                      10:["mazda", "sedan", 28000], 11:["mazda", "SUV", 34000], 12:["chevrolet", "truck", 66000],
                      13:["honda", "truck", 51000]}

# create a function that will filter through a dictionary of vehicle information, 
# and create a list of vehicle brands that meet a body type and budget filter. 
# I have provided some starting code and hints below.

def brand_filter(vehicles_dictionary, body_type, budget):
    brand_list = []
    for value in vehicles_dictionary.values():
        # check if body_type is correct
        if body_type == value[1] and budget >= value[2]:
            brand_list.append(value[0])
            # check if the price of the vehicle falls within the budget
                # if both conditions are satisfied, append the brand (e.g., "tesla") to brand_list
    return brand_list
    # return the brand_list
    
# you can test your implementation by running this code (the answer should be ['honda', 'volkswagen', 'mazda'])

print(brand_filter(available_vehicles, "sedan", 29000))