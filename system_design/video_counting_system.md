# Video Counting System


### Business Requirements

**Functional**
- system have to count video view events

**Non-Functional**
- scalable - handle tens of thousands of video views per second
- performant - tens of milliseconds to return total views count for a video
- highly available - survives hardware/network failures, no single point of failure


**API**
Write API
- countViewEvent(videoId)
- countEvent(videoId, eventType)
- processEvent(videoId, eventType, function)
- processEvents(listOfEvents)

Read API
- getViewsCount(videoId, startTime, endTime)
- getCount(videoId, eventType, startTime, endTime)
- getStats(videoId, eventType, function, startTime, endTime)



### High Level Architecture
- Database
- Processing Service
- Browser UI
- Query Service


### Data Model

Individual Events (every click)
- videoId
- timestamp
- event
Pros:
1. fast writes
2. can slice and dice data however we need
3. can recalculate numbers if needed
Cons:
1. slow reads
2. costly for large scale storage


Aggregate Data in read-time (e.g. per minute) 
- videoId
- timestamp
- aggregated count
Pros:
1. fast reads
2. data is ready for decision-making
Cons:
1. can query data only the way it was aggregated
2. requires data aggregation pipelin
3. hard or impossible to fix errors


For SQL databases, define data model by thinking about nouns and relationship between nouns
- Video_Info table
- Video_stats table
- Channel_Info table


For NoSQL databases, define data model by thinking about queries
- for Cassandra, keep adding columns for a particular query


### Processing Service
- receive video view event and increment several counters
- pre-aggregate data with in-memory buffer to hold multiple events before flushing at once to database
- push vs pull - use a queue to hold events until processing service is ready to handle
- checkpointing - fixed order with offset to indicate event position in queue


Internal Queue
- used to separate different processing streams 
- fast stream / slow stream
- we can place items from fast stream on an internal queue
- have mulitple slow streams pop from internal queue in parallel

Dead-Letter Queue
- collects messages that fail to deliver
- when we need to preserve data in case of downstream service degredation


Embedded Database
- place database on same machine as processing service
- if we need multiple streams to finish processing, we can hold processed streams in embedded db
- Item X needs data A, B, C
- A, B are done processing but waiting on C
- Place A, B in embedded db with key X, waiting for C
- When C is done, aggregate back with A, B and flush from db


### Ingestion Path Components
- Partitional Service Client
    - blocking vs non-blocking I/O
    - buffering and batching
    - timeouts - connection and request
    - retries - exponential backoff and jitter
    - circuit breaker

- Load Balancer
    - software vs hardware
    - networking protocols
    - load-balancing algorithms
    - health-checking

- Partitioner Service and Partitions
    - partition strategy
    - service discovery - server-side and client-side
    - replication
    - message format
 
 

### Data Retrieval Path
- Timeseries Data
    - roll up data after a certain time period to larger grouping
    - keep older data in blob storage / cold storage
    - keep recent data in hot storage or cache
    - query server stitches data together


### Testing
- load-testing: able to handle expected load
- stress-testing: discover system limits


### Golden Metrics
- Latency - time it takes to service a request
- Traffic - requests/sec
- Errors - rate of requests that fail
- Saturation - measure of system fraction, emphasizing resources that are most constrained










 

