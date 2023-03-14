# this is a dictionary which reflects the available vehicles that a dealer has on their lot.
# there are 13 vehicles, and we have the brand, body type, and price for each vehicle.

available_vehicles = {1:["tesla", "sedan", 30000], 2:["honda", "SUV", 45000], 3:["honda", "sedan", 26000],
                      4:["ferarri", "sports car", 200000], 5:["volkswagen", "SUV", 32000], 6:["volkswagen", "sedan", 22000],
                      7:["maserati", "sports car", 110000], 8:["jeep", "truck", 48000], 9:["jeep", "SUV", 40000], 
                      10:["mazda", "sedan", 28000], 11:["mazda", "SUV", 34000], 12:["chevrolet", "truck", 66000],
                      13:["honda", "truck", 51000]}

# create a function that will filter through a dictionary of vehicle information, 
# and create a list of vehicle brands that meet a body type and budget filter.

def brand_filter(vehicles_dictionary, body_type, budget):
    brand_list = []
    for value in vehicles_dictionary.values():
        # check if body_type is correct
        # check if the price of the vehicle falls within the budget
        if body_type == value[1] and budget >= value[2]:             # if both conditions are satisfied, append the brand (e.g., "tesla") to brand_list
            brand_list.append(value[0])
    return brand_list    # return the brand_list

def bodytype_filter(vehicles_dictionary, brand, budget):
    bodytype_dict = {}
    ind = 1 #index variable so loop can add multiple options
    for value in vehicles_dictionary.values():
        # check if brand is correct
        # check if the price of the vehicle falls within the budget
        if brand == value[0] and budget >= value[2]:                 # if both conditions are satisfied, add the body type (e.g., "truck") to bodytype_dict
            bodytype_dict["Option " + str(ind)] = value[1]           # convert index integer variable to string in order to concatenate
            ind += 1
    return bodytype_dict # return the bodytype_dict

print(brand_filter(available_vehicles, "sedan", 29000)) # you can test your implementation by running this code (the answer should be ['honda', 'volkswagen', 'mazda'])

print(bodytype_filter(available_vehicles, "jeep", 49000)) # you can test your implementation by running this code (the answer should be {'Option 1': 'truck', 'Option 2': 'SUV'})
