# Surfs_Up

## Resources
- Data: hawii.sqlite
- Software: Python 3.7.9, Visual Studio Code, Flask
- <br/>

## Overview
The purpose of this analysis was to determine if Oahu, Hawaii was a suitable location for a surf business based on the precipitation year round. For this analysis, the months of June and Decemember were our focus. An sqlite database containing the measurements and stations was used. The measurements table contained information regarding precipitation, temperature, and stations. The stations table contained information on the stations recording the measurements. This information was extracted from the sqlite database was queried and turned into dataframes, and then summary statistics were provided for each dataframe.
<br/>

## Results
<br/>

### Process
Our goal was to determine the summary statistics for temperatures recorded in the months of June and December. This was accomplished by using a query to selected the temperatures from the measurements table. These queries also included an extract statement to extract the date from the date-structure in the table, and compare that to the number of the date that we were looking for. (ie. June = 6, December = 12). The data returned for each month was converted to a list using np.ravel, and then converted to a dataframe using pandas.
<br/>

### June Statistics
For the month of June for all years in the data set, there was a total of 1700 reported temperatures. June saw an average temperature of approximately 75 degree Fahrenheit, with a lowest temperature of 64 degrees and highest temperature of 85 degrees.
![june_statistics](https://user-images.githubusercontent.com/82389466/122625532-95531a80-d073-11eb-9313-f492491eedda.png)
<br/>

### December Statistics
For the month of December for all years in the data set, there was a total of 1517 recorded temperatures. December saw an average temperature of approximately 71 degrees Fahrenheit, with a lowest temperature of 56 degrees and a highest temperature of 83 degrees.
![december_statistics](https://user-images.githubusercontent.com/82389466/122625615-2b874080-d074-11eb-8aae-00173c430f90.png)
<br/>

## Summary
In comparison of the data, we can see that both June and December had very similar average monthly temperatures, 75 and 71 respectively, which may indicate a climate that remains the same year round. Both months also saw very similar minimum and maximum temperatures, and the distribution of temperatures for was also very similar.Additionally, we could run other queries on the data to return more information, as listed below.
<br/>
1. We could determine the precepitation statistics for the month of June using the following code:
<br/>

results=session.query(Measurement.prcp).filter(extract("month",Measurement.date)==6).all()
june_precip_df=pd.DataFrame(results)
june_precip_df.describe()
<br/>

2. We could also determine the most active stations in December by determining the number of recordings by station:
<br/>

session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
