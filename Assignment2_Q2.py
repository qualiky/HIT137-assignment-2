import numpy as np
import pandas as pd


# Listing all files to be read
files = [
    "temperatures/stations_group_1986.csv",
    "temperatures/stations_group_1987.csv",
    "temperatures/stations_group_1988.csv",
    "temperatures/stations_group_1989.csv",
    "temperatures/stations_group_1990.csv",
    "temperatures/stations_group_1991.csv",
    "temperatures/stations_group_1992.csv",
    "temperatures/stations_group_1993.csv",
    "temperatures/stations_group_1994.csv",
    "temperatures/stations_group_1995.csv",
    "temperatures/stations_group_1996.csv",
    "temperatures/stations_group_1997.csv",
    "temperatures/stations_group_1998.csv",
    "temperatures/stations_group_1999.csv",
    "temperatures/stations_group_2000.csv",
    "temperatures/stations_group_2001.csv",
    "temperatures/stations_group_2002.csv",
    "temperatures/stations_group_2003.csv",
    "temperatures/stations_group_2004.csv",
    "temperatures/stations_group_2005.csv"
]

all_data = []
for file in files:             # Reading all csv files at once
    df = pd.read_csv(file)
    all_data.append(df)


months = ["January","February","March","April","May","June", "July","August","September","October","November","December"]


full_df = pd.concat(all_data) # Merging all dataframes into one to find seasonal averages/temperature range/most stable and variable stations across all years



## SEASONAL AVERAGES ##

summer = full_df[["December", "January", "February"]].values.flatten()  # Taking numbers from these months and then flatten them into 1d array so that we can calcuate mean value
autumn = full_df[["March", "April", "May"]].values.flatten()
winter = full_df[["June", "July", "August"]].values.flatten()
spring = full_df[["September", "October", "November"]].values.flatten()

summer_avg = summer.mean()
autumn_avg = autumn.mean()
winter_avg = winter.mean()
spring_avg = spring.mean()


with open("average_temp.txt", "w") as f:         # Writing the seasonal averages to a text file
    f.write(f"Summer: {round(summer_avg,2)}°C\n")
    f.write(f"Autumn: {round(autumn_avg,2)}°C\n")
    f.write(f"Winter: {round(winter_avg,2)}°C\n")
    f.write(f"Spring: {round(spring_avg,2)}°C\n")
    


## STATION WITH LARGEST TEMPERATURE RANGE ##

months = ["January","February","March","April","May","June", "July","August","September","October","November","December"]

maxi_temp = full_df.groupby("STATION_NAME")[months].max().max(axis=1) # max temperature for all stations in each month, then takes overall max for each station)
mini_temp = full_df.groupby("STATION_NAME")[months].min().min(axis=1) # min temperature for all stations in each month, then takes overall min for each station)

tempeature_range = maxi_temp - mini_temp

largest_range = tempeature_range.max()
top_stations = tempeature_range[tempeature_range == largest_range] # only stations with the largest range (in case of ties)

with open("largest_temp_range_station.txt", "w") as f:
    for station in top_stations.index:
        f.write(
            f"{station}: Range {round(largest_range,2)}°C "
            f"(Max: {round(maxi_temp[station],2)}°C, "
            f"Min: {round(mini_temp[station],2)}°C)\n"
        )



## MOST STABLE AND MOST VARIABLE STATIONS ##

std_dev = full_df.groupby("STATION_NAME")[months].std().mean(axis=1)  # standard deviation for each month per station, then average these std devs to get variability)

most_stable_value = std_dev.min()       #smallest and largest std dev values
most_variable_value = std_dev.max()

most_stable_stations = std_dev[std_dev == most_stable_value]  # handles ties stations with most stable and most variable values
most_variable_stations = std_dev[std_dev == most_variable_value]

with open("temperature_stability_stations.txt", "w") as f:
    for station in most_stable_stations.index:
        f.write(f"Most Stable: {station}: StdDev {round(most_stable_value,2)}°C\n")

    for station in most_variable_stations.index:
        f.write(f"Most Variable: {station}: StdDev {round(most_variable_value,2)}°C\n")

