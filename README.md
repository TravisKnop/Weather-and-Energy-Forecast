# Weather-and-Energy-Forecast

This is my final project for The Iron Yard. We were asked to create a project, using the data science and computer programming techniques we had learned. That was pretty much the entire assignment.

Because I am a huge energy nerd, I wanted to use machine learning to improve the energy market. There were a lot of potential targets for building predictive algorithms - the market disruption of the natural gas boom in the USA, the impact of severe winter events like the polar vortex, reducing peak energy demand in the summer, the exponential market share growth of renewable energy in the USA. The product I developed touched on several of these topics, and went as follows:

## Predicting Energy Demand From Weather Patterns
I access publicly-available, hourly weather data from the [Logan Boston Airport weather station] (http://www.wunderground.com/weather/api/d/docs?d=data/hourly). I also used hourly grid load data from ISO-New England's [Southeast Mass / Boston node] (http://www.iso-ne.com/isoexpress/web/reports/load-and-demand)*. I also looked at hourly and daily energy trading prices, New England "Algonquin Citygate" natural gas prices, and seasonal variations in energy fuel mix, but from a 30,000 ft view overall grid load was the easiest to model.

* - I chose Boston because it gave me a chance to model seasonal extremes (the polar vortex hit Boston pretty hard in 2014, but it is still warm enough to have a noticeable summer peak). ISO-NE has relatively user-friendly transmission data, which helps of course.

After cleaning and matching up the data, I used multiple linear regressions to place a best-fit line between average daily temperature and daily electric demand. This is a simple one-to-one correlation, showing a "Nike-swoosh"-shaped relationship between temperature and electricity. Grid load is lowest at 50-65 degrees. Below that, demand increases because of extra electric heat (and extra lighting demand in the dark winter months). Above that, energy demand increases mostly because of air conditioning.

Next came adding additional data, to create a more dynamic two-to-one, or even seven-to-one correlation. Some of the extra weather data that I added included:
 - humidity
 - precipitation
 - day of year
 - climatic average temperature for the day of year
 - time lags (does grid demand change a few days before or after large swings in the weather?)

With the standard split-model-predict method (built into Scikit-learn and other statistical modelling software), the algorithm I used reached its best accuracy with 5 variables: temperature, humidity, day of year, climatic average temp, and change in temp since yesterday. This combination of variables allowed the model to predict overall load with just over .82 variance. I am very proud of that result; the day-ahead trading average compared to the load record has a .91 variance. And the day-ahead market can account for events like a new development coming on-line, or the Super Bowl.
