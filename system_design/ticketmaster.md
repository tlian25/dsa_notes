# Design Ticketmaster

### High Level Ideas



### Business Purpose
- allows customers to purchase theater, sporting venue, and event tickets online
- allows customers to browse through movies, shows, currently being played
- for this exercise, limit scope to movies

### Business Requirements

**Functional Requirements**
1. list different cities where cinemas are located
2. list movies released in a particular city
3. display cinemas running a movie and available show times
4. user can choose a show at a particular cinema and book tickets
5. user can see seating arrangement and choose multiple seats
6. user can distinguish available seats from booked ones
7. user can put a hold on seats for five minutes before making payment
8. user can wait to see if holds by others expire and free up
9. waiting customers should be served FIFO

**Non-Functional Requirements**
1. highly concurrent to handle multiple booking requests for the same seat at any time
2. financial transactions should be secure and database ACID compliant


### Capacity Estimation
- 3Bn page views per month
- Sells 10m tickets per month
- 500 cities
- 10 cinemas per city
- 2000 seats per cinema
- 2 shows per day
- 50b for metadata and 50b for booking info
- 500 cities * 10 cinemas * 2000 seats * 2 shows * 100 bytes = 2 GB/day


### Database Design

Tables
- Movie
- Show
- Booking
- Cinema
- Seat
- City
- User

### Component Design

**Active Reservations Service**
- keep all reservations of a show in memory
- Linked HashMap or TreeMap
- allows us to jump to any reservation to remove it when booking is complete
- head of HashMap always points to oldest reservation record so we can expire it

**Waiting Users Service**
- keep all waiting users of a show in memory in a Linked HashMap or TreeMap
- clients use Long-Polling to keep updated with status
- 