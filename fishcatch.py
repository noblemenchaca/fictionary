'''
/description: 
 - This program will open a file containing data from a scientific fishing trip.
 - It will then parse the data of the fish caught, adding each statistic to a certain dictionanry.
 - Then for each fish in the dicitonary, calculate the number of them caught and the mean weight
 - Finally it will print out a sorted report containing that ^ data.
'''


def fish_dict_from_file(file_name): #creates a literal dictionary for the fish species, then a weights dictionary  then reads the file. For every entry not already in the weight dict, the dict is then appended

    species = {
        '1': 'Bream',
        '2': 'Whitefish',
        '3': 'Roach',
        '4': '?',
        '5': 'Smelt',
        '6': 'Pike',
        '7': 'Perch'}
    weights = {}

    input_file = open(file_name, 'r')

    for line in input_file: #every line in the file will be read and put into the dictionary
        fish_datum = line.split()
        if fish_datum[2] == "NA":
            continue
        else:
            if species[fish_datum[1]] in weights:
                weights[species[fish_datum[1]]].append(fish_datum[2])
            else:
                weights[species[fish_datum[1]]] = []
                weights[species[fish_datum[1]]].append(fish_datum[2])

    input_file.close()
    return weights    
        
    
def find_weight(name, weights): #for every fish caught (in that species), add that wieght to the total then devide by the number of  fish caught. then print line of report
    total = 0.0
    for weight in weights: #the weights of all the fish of that species are added cumulatively
        float_weight = float(weight)
        total +=  float_weight

    print( (str(len(weights)).rjust(4)) + " " + name.ljust(10) + ("{0:.1f}".format(total / len(weights)) + "g").rjust(10 ) )




def main(): 
    '''
    - A cleverly titled dictionary is created containing data from a file called fishcatch.dat
    - Then the header bar for the report is printed
    - A for loop iterates find_weight with every key and value from the dictionary
    '''
    fictionary = fish_dict_from_file("fishcatch.dat") # get it? 'fictionary'...

    print( "#".rjust(4) + " " + "NAME".ljust(10) + "MEAN WT".rjust(10) )

    for fish in sorted(fictionary): #every fish will print a report
        find_weight(fish, fictionary[fish])


if __name__ == '__main__':
    main()
