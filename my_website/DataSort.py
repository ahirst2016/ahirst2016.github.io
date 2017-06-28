name1 = 'Kevin'
name2 = 'Aaron'
# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__))

#initialize the aggregators
years1=[]
number_of_people1=[]
years2=[]
number_of_people2=[]


# Open the file
filename = os.path.join(directory,'AR.TXT')
datafile = open(filename, 'r')

# Go through all the names that year
for line in datafile:
    state, gender, year, name, number = line.split(',')
    # Aggregate based on name1
    if name == name1 and gender == 'M':
        years1.append(year)
        number_of_people1.append(number)
    #Aggregate based on name2
    if name == name2 and gender == 'M':
        years2.append(year)
        number_of_people2.append(number)
# Close that year's file
datafile.close()

# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot(years1, number_of_people1, '#0000FF')
ax.plot(years2, number_of_people2, '#FF00FF')

ax.set_title('Arkansas Babies Named Kevin(blue) or Aaron(pink)')
fig.show()
