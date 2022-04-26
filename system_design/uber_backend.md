# Uber Backend

### High Level Ideas
- use mix of HashTable QuadTree structure to track geolocations
- bulk data updates in Tree to reduce load
- push vs pull notifications



### Business Purpose
- enables customers to book drivers for taxi rides
- drivers use personal cars to drive customers around
- customers and drivers communicate with each other through the app

### Business Requirements

**Functional**
- drivers need to regularly notify service about current location and availability
- passengers need to see all nearby available drivers
- passengers can request a ride; nearby drivers notified and respond
- once a ride is accepted by both passenger and driver, they can see each other's location until trip finishes
- at the end of the ride, the driver marks the journey complete
- system should be able to contact drivers in real-time

### Capacity Estimation
- 300M customers, 1M daily active customers, and 1M drivers, 500k daily active drivers
- 1M daily rides
- Active drivers notify their current location every 3 seconds


### System Design and Algorithm

**Algorithm for Updating Driver Locations**
- Modified QuadTree solution (from Yelp system design)
- Data structure needs to handle frequent geolocation updates
- Keep latest position reported by drivers in a hash table and update QuadTree within 15 seconds

**Driver Location HashTable**
- DriverID (4b)
- Prev Longitude/Latitude (8b x2)
- New Longitude/Latitude (8b x2)
- total storage = 1M drivers * 36 btyes => 36 MB
- bandwidth = 500k active drivers * 20 btyes / 3 sec = 3.3MB/s

**Driver Location Server**
- distribute DriverLocationHT across multiple servers
- partition on DriverID using consistent hashing
- notify respective QuadTree server to refresh every 10 seconds
- can leave 10% extra buffer before resizing/partitioning a grid in QuadTree
- as soon as update for driver location is received, broadcast info to all interested customers


**Notification Service**
*Option 1 - PUSH*
- push model to broadcast current location of drivers to all interested customers
- build on publisher/subscriber model
- when customer opens app on device, they subscribe to driver feed
- server will continuously push out driver location updates to subscribed customers
- use either HTTP long polling or push notifications

*Option 2 - PULL*
- clients send their current location and server finds all nearby drivers from QuadTree to return them to the client
- limit pulls to once every 5 seconds to limit number of calls to server


**Algorithm for Request Ride**
1. customer put in request for ride
2. Aggregator servers will take request and query QuadTree server to return nearby drivers
3. Aggregator server collects all results and sorts by ratings
4. Aggregator server sends notification to top X drivers simultaneously
5. First driver to accept will be assigned ride. Others receive cancellation request
6. If none of top X drivers respond, aggregator will request a ride from next X drivers from the list
7. Once driver accepts request, customer notified


### Fault Tolerance and Replication
- As in Yelp, store a reverse index of QuadTree to quickly rebuild any failed QuadTree server
- 



