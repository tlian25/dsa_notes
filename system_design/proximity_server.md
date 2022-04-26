# Design Yelp (Proximity Server)

### High Level Ideas
- QuadTree structure to segment locations into dynamic grid sizes and keep number of places per grid low
- reverse index of set of places kept on each server to quickly rebuild a failed server
- 


### Business Purpose
- used to discover nearby attractions like places, events, etc
- storing information about different places so that users can perform a search on them
- querying based on geolocation


### Requirements

**Functional**
- Users should be able to add/delete/update places
- Given geolocation, users should be able to find all nearby places within a given radius
- Users should be able to add feedback/reviews about a place
- Feedback can have pictures, text, and a rating


**Non-Functional**
- Users should have a real-time search experience with minimum latency
- Service should support heavy search load. Read heavy.


### Sizing Estimation
- 500M places
- 100k queries per second (QPS)
- 20% growth in number of places and QPS each year


### Database Schema

**Places**
- LocationID (8b)
- Name (256b)
- Longitude/Latitude (8b x2)
- Desciption (512b)
- Category (1b)

**Reviews**
- LocationID (8b)
- ReviewID (4b)
- ReviewText (512b)
- Rating (1b)

**Photos**
- LocationID (8b)
- ReviewID (4b)
- Photo Location in S3 (20b)


### System Design and Algorithm

**SQL Solution**
- store all data in SQL database
- each place a separate row, identified by LocationID

``` sql
SELECT * FROM Places WHERE Latitude BETWEEN (X-D, X+D) AND Longitude BETWEEN (Y-D, Y+D)
```

**Grid Solution**
- divided whole map in smaller grids to group locations into smaller set
- each grid will store all the Places residing within a specific range of longitude and latitude
- reduce search to locations in nearby grids
- GridID (4b) to uniquely identify grids in system

``` sql
SELECT * FROM Places WHERE Latitude BETWEEN (X-D, X+D) and Longitude BETWEEN (Y-D, Y+D) AND GridID in (GridID1, GridID2,...)
```

**Dynamic Grid Sizes**
- assume we don't want to have more than 500 places in a grid for faster searching
- whenever a grid reaches this limit, we break it down into four grids of equal size and distribute places among them
- use tree data-structure to store information
- each node will represent a grid and contain information about all places in that grid
- if a node reaches limit of 500 places, we break it down to create four child nodes under it
- leaf nodes will represent the grids that cannot be further broken down
- keep a list of places in leaf nodes


### Data Partitioning

**Shard on Regions**
- all places belonging to a region will be stored on a fixed node
- drawback: hot regions will bottleneck system as high traffic read/write goes to that partition server
-  drawback: some regions grow faster than others so we will end up with skew in data uniformity


**Shard on LocationID**
- hash function on LocationID to map to server
- advantage: evenly distributes number of places on each shard
- disadvantage: places close together requires querying multiple shards


### Fault Tolerance
- secondary replica of each QuadTree server
- brute-force recovery: iterate through whole database and filter LocationIDs using hash function to rebuild failed server
- efficient recovery: keep a reverse index to map Places to QuadTree server, build HashMap where key=serverID, value=set of all Places kept on that server




