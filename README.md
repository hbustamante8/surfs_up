# surfs_up

## Overview of the analysis 
Repository is based on analysis of weather data with the use of Python, SQLite and SQLAlechemy. The purpose of this project is to analyze a database that contains information about Hawaii weather over a seven-year period. The overall goal is to investigate if the weather is appropriate to open an ice cream shop in O’ahu, Hawaii and present the findings to an investor. For this project, June and December temperature will be analyzed to determine if the ice cream shop business is profitable and sustainable year-round. The hawaii.sqlite database is where the weather data is stored and is being queried from.



## Results

June results summary is seen in dataframe below after building a query using SQLAlchemy.


![image](https://user-images.githubusercontent.com/96553992/156707463-7c2e92ca-5890-44a8-8d63-536fe391881e.png)




December results summary is seen in dataframe below after building a query using SQLAlchemy.

![image](https://user-images.githubusercontent.com/96553992/156707550-918b7100-6890-4482-980a-1d1858365c39.png)




* Key differences
  *  June, according to the summary statistics, has warmer weather on average. June weather mean is 74.9 while December is at 71.0.
  *  December’s weather data minimum value is 8 degrees lower than June's.
  *  There is more data on the June weather so it can be inferred that is a more accurate representation compared to December data.
  *  Standard deviation of December data is greater than June so more a bit more variation is expected in the December data.


### Additonal Results 

The dataframe below contains summary statistics of June weather data that is greater than 70 degrees with a SQLAlechmy query.

<img width="161" alt="Screen Shot 2022-03-04 at 8 47 22 AM" src="https://user-images.githubusercontent.com/96553992/156774704-a0a60711-7c97-4036-ac8c-b179a7d9c34c.png">


The dataframe below contains summary statistics of December weather data that is greater than 70 degrees with a SQLAlechmy query.

<img width="179" alt="Screen Shot 2022-03-04 at 8 47 37 AM" src="https://user-images.githubusercontent.com/96553992/156774723-53a84fb6-a668-451c-b89d-fdbc62cfb4e1.png">

* Key points from additional queries

  * Comparing both June queries, the count of days where weather has been greater than 70 degrees divided by the total count of June weather data comes out to 89.9% (1529/1700). 
 * Comparing both December queries to the data, the count of days where weather has been greater than 70 degrees divided by the total count of December weather data comes out to 58.5% (887/1517). 
  * Based on weather metrics available online, historically, weather in Oahu, Hawaii considered to be low if less than about 70 degrees. June weather looks great while December does not look as favorable. But it is also important to remember that December is one of the coldest months

## Summary 

Based on the weather data, it can be concluded that the ice cream shop has a good chance of being successful in the O’ahu, Hawaii. The average weather over the past 7 years of data for December and June look positive as both months on average are above 70 degrees. December may be a less profitable month based on the data, but this is as the around the lowest the temperature gets around the year. In context, June is not one of the warmest months according to other available online historical data, which favor in opening of the ice cream shop.

### Additional Queries
Additional queries that could be performed is the precipitation data for both June and December. The amount of rain would affect ice cream sales and is important to take into consideration. Considering that precipitation data on specific days could just be for a short amount of time, precipitation might not capture accurately what the sale of ice cream would be on that day. If data is available, a query that counted the days where it rained over 3 hours as an example would be very useful. Furthermore, the weather stations that are near Oahu could also be queried for the months of December and June as well. Finally, it would be important to run similar queries mentioned for all the data together throughout the years.

### Recommendation 
In all, the ice cream shop is on track to be successful based on the analysis. However, to be certain and have the best chance of success, the additional queries should be explored before officially starting the ice cream shop. The investor can have more confidence that this business venture is on the path to be not only profitable but sustainable in the O’ahu Hawaii.


