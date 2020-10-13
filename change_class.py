import os 
import glob

# Specify your directory (the full path) that contains all the txt files you need to change
# Here my directory is "test/"
txt_files = glob.glob("test/*.txt")

# Function to convert   
def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 

# Convert the class in the first line
def convert(txt_files):
    for i in range (len(txt_files)):

        with open(txt_files[i], 'rt') as fd:
            first_line = fd.readline()
            # convert str to list
            line = first_line.split(' ')
            
            #change class to 0
            line[0] = 0
            # using list comprehension, convert list to str using ' ' as a separator
            converted_line = ' '.join([str(elem) for elem in line]) 
            fd.close()
        
        with open(txt_files[i], 'w') as fd:
            fd.write(converted_line)
            fd.close()

convert(txt_files)



