#file to explore the relative length of the streets visualized by geo-chicas
#gets the length of female and male streets in km from a geojson file
import pandas as pd
import numpy as np
import sys

def read_length_csv(path):
    city = pd.read_csv(path)
    #select only the streets by gender
    city_f = city[city.gender == "Female"]
    city_m = city[city.gender == "Male"]

    abs_length_f = np.sum(city_f['length'])
    abs_length_m = np.sum(city_m['length'])
    total = abs_length_f + abs_length_m

    #print out the results
    print("the men have a total of: " + str(abs_length_m) + ", which is " + str(abs_length_m/total * 100) + "%")
    print("the females have a total of: " + str(abs_length_f) + ", which is " + str(abs_length_f/total * 100) + "%")

# running the function
read_length_csv(sys.argv[1])
