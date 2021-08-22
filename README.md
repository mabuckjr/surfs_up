# Surf's Up!
Resources: Python, Pandas, Flask, SQLAlchemy, SQLite, and Numpy
## Overview
In this challenge, we accessed a SQLite database using SQLAlchemy to look at weather data in Oahu. We were getting this data to see if it would be a good idea to open a surfing and ice cream shop there. W. Avy, our boss/investor, liked our initial analysis through the activities, but wanted to make sure that the location would be good for year-round business. He decided that the best way to see if it would work would be to analyze the weather in June and December to see how much it differed from each other. We used SQLAlchemy to pull the data from the database and analyze it using Pandas and Numpy.
## Results
![](https://github.com/mabuckjr/surfs_up/blob/main/Resources/June_Temps.PNG) ![](https://github.com/mabuckjr/surfs_up/blob/main/Resources/December_Temps.PNG)
#### Below are 3 main takeaways from the analysis:
- The average temperature in December (~71 degrees) was only ~4 degrees cooler than the temperature in June (~75 degrees)
- The minimum temperature can be as much as ~8 degrees cooler (~56 degrees) in December than it is in June (~64 degrees)
- The maximum temperature difference between June (85 degrees) and December (83 degrees) was only 2 degrees
## Summary
The results of this project showed us that the differences in temperature did not differ too much between December and June. It was expected that December would be colder, but for the most part, they are similar enough that people could come visit the shop at any point in the year and enjoy themselves. The only thing that may upset some customers would be a very cold day in December, which could be as low as the mid-50's. For some people, this would be far too cold for surfing or ice cream, and they may not come at all. It would be wise to check the forecast for days in the winter months, and it may even be worth closing the shop on cold days.

The initial analysis is helpful, but it doesn't give the full picture. Temperature isn't the only weather condition the customers will be thinking about when they want to visit our shop; they will also worry about if it will be raining! If there's one thing worse than eating ice cream on a cold day, it's eating it on a rainy day. The two additional queries I decided to run were on precipitation in June and December, to see the difference in rainfall between a winter and summer month.
![](https://github.com/mabuckjr/surfs_up/blob/main/Resources/June_Precipitation.PNG) ![](https://github.com/mabuckjr/surfs_up/blob/main/Resources/December_Precipitation.PNG)

As you can see from the tables above, the average precipitation did not increase that much, but the maximum amount of rainfall on a particulary rainy day can be more than 2 inches more in December than it is in June. This is good information for W. Avy to know when considering whether this shop should be seasonal or open year round.

Overall, Oahu seems like a perfect location to open a Surf and Ice Cream shop, and I can't wait to go into business with W. Avy!
