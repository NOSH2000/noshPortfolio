import pandas
import matplotlib

data = pandas.read_csv("DATA/weather_year.csv")

#You can get the column names using the columns property.
print(data.columns)

# The column names in data are a little unweildy, so we're going to rename them.
# This is as easy as assigning a new list of column names to the columns property of the DataFrame.
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

#There are lots useful methods on columns, such as std() to get the standard deviation.
#Most of pandas' methods will happily ignore missing values like NaN.
print(data.mean_temp.std())

data.mean_temp.hist()
matplotlib.pyplot.show()
