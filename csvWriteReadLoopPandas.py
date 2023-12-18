import csv
import pandas
import statistics
"""
# Open and Create the file 
csvfile = open("myfile3.csv", "w", newline='')
print("File Created")
# Create column headers
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Temp', 'Noise'])
print("Columns Created")

# Create 2 rows of data 
csvwriter.writerow([55, 29])
csvwriter.writerow([45, 64])

print("Data Created")
# Close the file
csvfile.close()
print("closed after created rows")


# Open the file read it and print the first 2 rows
csvfile = open("myfile3.csv","r", newline='')
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
line = csvfile.readline()
print(line, "readline4")
line = csvfile.readline()
print(line, "readline5")
csvfile.close()
print("closed after printing rows")


# open the file to append to it
csvfile = open('myfile3.csv',"a", newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow([20, 28])
csvwriter.writerow([19, 10])
csvfile.close()
print("closed append")
"""
################## LOOP ########################
########################Loop thru file###################################
#No need to close the file when using this "with open .....as csv file etc"

#alternative way of looping thru file
#dont have to know what length or number of records
#dont have to close the file
tot_temp = 0
rec_ct = 0
with open("myfile3.csv", "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None)
    print("Header with:", header)
    for row in csvreader:
        print(row[0])
        #print(row[1])
        tot_temp = tot_temp + int(row[0])
        rec_ct = rec_ct +1
        #add code to accum average here
        #add code to count the records here
avg_temp = tot_temp/rec_ct
print("avg ",avg_temp)
"""
################## PANDAS ########################
# open the file and read it all into one variable
# Read the entire CSV file into a pandas DataFrame
# Calculate the Mean of each searate column by referring to the Column Heading
#DOES FILE NEED TO BE OPENED FIRTS???
df = pandas.read_csv('myfile3.csv')
print(df.to_string())
# Filter out the column, value_eur
temp_values = df['Temp']
mean_value_temp = round(statistics.mean(temp_values), 2)
print("Mean Value Temp:", mean_value_temp)
noise_values = df['Noise']
mean_value_noise = round(statistics.mean(noise_values), 2)
print("Mean Value Noise:", mean_value_noise)
"""