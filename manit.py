import numpy as np 
import math 
  
# Python 3 program for the 
# haversine formula 
def haversine(lat1, lon1, lat2, lon2): 
      
    # distance between latitudes 
    # and longitudes 
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
  
    # convert to radians 
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
  
    # apply formulae 
    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2)); 
    rad = 6371
    c = 2 * math.asin(math.sqrt(a)) 
    return rad * c 

def find_best_school(houses,schools):
    output=[]
    for i in range(len(houses)):
        lat1=houses[i][0]
        lon1=houses[i][1]
        a=[]
        for j in range(len(schools)):
            lat2=schools[j][0]
            lon2=schools[j][1]
            result=haversine(lat1,lon1,lat2,lon2)
            a.append(result)
        print(a)
        output.append(a.index(min(a)))
    
    print(output)
    return output



def basic_test(my_function):
    houses=[(28.1,78),(13,78),(13,26),(28,76)]
    schools=[(28,77),(13,77),(20,68)]
    output=my_function(houses,schools)
    answer=[0,1,2,0]
    try:
        print("Basic Score : {:0.2%}".format((np.array(answer)==output).mean()))
    except:
        print("Error : give the index of nearest school for each house in the list")


basic_test(find_best_school)