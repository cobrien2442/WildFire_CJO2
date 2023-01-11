## WildFire_CJO

Extension of GTown

Overview:

Knowing the “growth potential” of a wildfire at the start of the fire can be a huge advantage to the people in charge of dispensing firefighting assets/resources

For example: if two locations 100 miles apart both have a wildfire start at the same time, how do you know where to allocate firefighting resources?

Description:

Satellites (lunched by NASA) circling earth detect wildfires bigger then XXX acres When a wildfire is detected the satellite sends latitude/longitude data to a Gmail account, location/time data is then sent to an AWS account for logging. 

The AWS account attaches two weeks’ worth of weather information to the location/time data. The weather data is processed (via machine learning algorithms) to tell how big the fire will grow. Below is a flow diagram of the project:
