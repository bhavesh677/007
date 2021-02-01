# *Analysis of New York Yellow Taxi Trip Data*

## Introduction of NYC Yellow Taxi: 
- ### Yellow Taxis are the only vehicles licensed to pick up street-hailing passengers anywhere in NYC. 
- ### Yellow Taxis charge standard [metered fares](https://www1.nyc.gov/site/tlc/passengers/taxi-fare.page) for all street hail trips.
- ### Yellow Taxi smartphone apps can offer set, upfront pricing for trips booked through an app.
- ### Yellow Taxis are easily identified by their yellow color, taxi “T” markings, and license numbers on the roof and sides of the vehicle.

## Introduction of NYC Yellow Taxi Trip Data:
**vendorid :**    A code indicating the [TPEP provider](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) that provided the record.<br>
**pickup_datetime :**             The date and time when the meter was engaged.<br>
**dropoff_datetime :**            The date and time when the meter was disengaged.<br>
**passanger_count :**         The number of passengers in the vehicle. This is a driver-entered value.<br>
**trip_distance :**           The elapsed trip distance in miles reported by the taximeter.<br>
**PULocationID :** Taxi Zone in which the taximeter was engaged.<br>
**DOLocationID :** Taxi Zone in which the taximeter was disengaged.<br>
**ratecodeid :**             The final [rate code](https://www1.nyc.gov/site/tlc/passengers/taxi-fare.page) in effect at the end of the trip.<br>
**store_fwd_flg :**           This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward”, because the vehicle did not have a connection to the server.<br>
**pay_type :**                Signifying how the passenger paid for the trip.<br>
**fare_amount :**             The time-and-distance fare calculated by the meter.<br>
**surcharge :**               $0.30 improvement surcharge,  $0.50 overnight surcharge 8pm to 6am, New York State Congestion Surcharge of $2.50.<br>
**mta_tax :**                 $0.50 MTA tax that is automatically triggered based on the metered rate in use.<br>
**tip_amount :**              This field is automatically populated for credit card tips. Cash tips are not included.<br>
**toll_amount :**             Total amount of all tolls paid in trip.<br>
**total_amount :**            The total amount charged to passengers. Does not include cash tips.





## Objective:
- The core objective of this project is to analyse the factors for demand for taxis, to find the most pickups, drop-offs of public based on their location, time of most traffic and how to overcome the needs of the public.
