MSI - Pyhop travelling example
==============================

Pyhop travelling example with more features.

## Objective

You are able to pay at most $m to get from park to home in at most t minutes.

You need to get a proper plan for doing this.

You are starting at hh:00 (for any hh in {00, 01, ..., 23}).

## City

I used the following map:

![City](map.png)

### Distances

Distances are measured in km.

### Taxi

You are able to board a taxi in any place.

The price for the taxi is $(20 + 1.5 * distance).
 
The taxi goes at 20 km/h.

### Buses

There are buses leaving every 10 minutes (6 per hour), starting from hh:00 (for hh in {00, 01, ..., 23}).
You are able to board/unboard buses at following points:

* Park
* Intersection 1
* Intersection 2
* Intersection 3

The bus goes at 15 km/h.

The price for the bus is $5 for any segment.

You need to wait for bus if it goes away.

### Walking (on foot)

You are also able to walk on foot.

Walking on foot is at 5 km/h.

## Operators

Some description will follow here.