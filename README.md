# surfs_up

## Overview of analysis
Tasked with constructing a comprehensive weather analysis for the Hawaiian island, with a view to determining the viability of a surf shop's sustained operation throughout the year.

## Resources
Software used:
* Python
* Visual Studio Code
* Jupyter Notebook
* SQLite
* SQLAlchemy
* JSON
* Flask

Data Source:
hawaii.sqlite

## Results
My initial approach involved data extraction, commencing with importing all the required dependencies in Jupyter Notebook, followed by importing the SQL toolkit.


```
# Dependencies
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
```


I constructed a query to filter the Measurement table and retrieve the temperature readings specifically for the months of June and December.

### Query code for June


```
june_temperatures= session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date)==6).all()
print(june_temperatures)
```

### Query code for December

```
dec_temperatures= session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date)==12).all()
print(dec_temperatures)
```

Upon successful retrieval of temperature data for June and December, I proceeded to create a DataFrame featuring a "Date" column and columns for "June Temps" and "December Temps". Further, I utilized the ".describe()" method to present a comprehensive summary of my results.

![](Images/Junetempslist.png)
![](Images/decembertempslist.png)

From our findings above the key differences between June and December are:
* June has a low of 64 degrees while December hits a low of 56 degrees.
* The max temperature for June is 85 degrees while the max temperautre for December is 83 degrees.
* The temperatures of both months stay pretty consistent with the std being around 3/4.

## Summary
Based on the current forecasts and temperature trends, it is evident that Oahu represents a strategic location for establishing the Surf Shop, with minimal risk posed by weather fluctuations. This observation is reinforced by the marginal differences between the temperature readings for June and December.



