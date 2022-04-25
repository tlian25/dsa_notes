# Yelp or Proximity Server

### High Level Ideas


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





