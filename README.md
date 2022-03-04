# surfs_up

## Overview of the analysis 
Repository is based on analysis of weather data  analysis with the use of SQLite and SQLAlechemy. The purpose of this project is analyze a  weather data set that is within a  in Oahu, Hawaii to investigate if the weather is appropriate open an ice cream shop and present the findings to an investor. For this project, June and December temperature will be analyzed to determine if the ice cream shop business is profitable and sustainable year-round. The hawaii.sqlite database is where the the weather data is stored and is being queried from.



## Results

June results summary is seen in image belowe after building a query using SQLAlchemy.


![image](https://user-images.githubusercontent.com/96553992/156707463-7c2e92ca-5890-44a8-8d63-536fe391881e.png)




December results summary is seen in image belowe after building a query using SQLAlchemy.

![image](https://user-images.githubusercontent.com/96553992/156707550-918b7100-6890-4482-980a-1d1858365c39.png)




* Key differences
  *  June, according to the summary statistics has warmer weather on average. With June weather mean is 74.9 while December is at 71.0.
  *  December minimum weather value is 8 degrees lower than June's.
  *  There is more data on the June weather so it can be inferred that is a more accurate representation compared to December data.
  *  Standard deviation of December data is greater than June so more variation is expected in the december data.


##Additonal information 

The table below are summary statistifcs of June weather data that is greater than 70 degrees.
<img width="161" alt="Screen Shot 2022-03-04 at 8 47 22 AM" src="https://user-images.githubusercontent.com/96553992/156774704-a0a60711-7c97-4036-ac8c-b179a7d9c34c.png">


The table below are summary statistifcs of December weather data that is greater than 70 degrees.

<img width="179" alt="Screen Shot 2022-03-04 at 8 47 37 AM" src="https://user-images.githubusercontent.com/96553992/156774723-53a84fb6-a668-451c-b89d-fdbc62cfb4e1.png">

##Summary 

Based on the weather data, it can be concluded that the ice cream shop has a good chance of being successful in the Ohau, Hawaii. The average weather over the past 7 years of data for December and June look positive as both months are above 70 degrees. December may be a weaker sales based on the data, but this is as the lowest temperature it should get around the year. In context, June is not one of the warmest months according to other historical data.

Additional queries that could be run is the precipitation data for both June and Decembers. The amount of rain would definitely affect ice cream sales and is important to take into consideration. But keeping in mind that percipitation data on specific days could just be for a short amount of time. If data is availabe, a query that counted the amount of days that it rained over 3 hours as an example would be very useful. The weather stations that are near Oahu could also be queired for the months of December and June as well. Finally, it would be of best interest to run similar queries for all the data together throughout the years.


