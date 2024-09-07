
import matplotlib.pyplot as plt
import pandas as pd

# changing window title to "IP Project"
window = plt.figure()
window_manager = plt.get_current_fig_manager()
window_manager.canvas.set_window_title("IP Project")


# here, "sep" argument has 5 spaces in it, because each column in csv file is sperated by 5 spaces
# "usecols" argument is used because we only need two columns out of all the three
# lastly,"engine=python" is given to avoid some unusual warning the program gives.
# however, this argument is not required
data  = pd.read_csv("data.csv",sep="     ",usecols=["Year","temp"],engine="python")

# colors is an empty list initially
colors = []

# we will change color of specific bar graph according to its value
# explanation ---> temperature less than 0 will be blue and temperature more than 0 will be red/orange

for index,row in data.iterrows():  # we use iterrows() here
    # we are initially obtaining temperature in string form
    # But here, we convert it to float(decimal) for the if-statements that follow
    temperature = float(row["temp"])
    if temperature < 0:
        colors.append("b") # b --> blue
    else:
        colors.append("r") # r --> red

plt.bar(data["Year"],data["temp"],color=colors)

# graph properties
plt.title("global annual temperature change")
plt.xlabel("years since 1800")
plt.ylabel("global annual temperature")

plt.show()