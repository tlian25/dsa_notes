# API Rate Limiter

### High Level Ideas
- Block vs Rolling window algorithms
- Keeping counters using key-value storage schema


### Business Purpose
* Safeguard against misbehaving clients/scripts
* Harden security to prevent brute force password breaches
* Prevent abusive behavior and bad design practices
* Keep costs and resources usage under control
* Eliminate spikiness in traffice
* Revenue control if client entitlement/contract based on a rate limit

### Functional Requirements
1. Limit number of requests a client can send to an API within a time window
2. Limit across multiple gateway servers in a distributed cluster

### Non-Functional Requirements
1. Highly available
2. Minimize performance drag on application

### Types of Throttling

**Hard Throttling:** number of API requests cannot exceed limit

**Soft Throttling:** set limit to exceed a certain percentage, i.e. 10% exceed-limit on limit of 100 msgs/min will allow 110 msgs/min

**Elastic or Dynamic Throttling:** number of requests can go beyond threshold if system has free resources available

### Rate Limiting Algorithms
- Fixed window
- Sliding window

### Basic Design and Algorithm
- Keep track of users by unique UserID
- Use a hashtable to store key-value pairs of [user_id]:([request_count], [StartTime])


**Fixed Window Algorithm**

When new request comes in:
1. If UserID not in table, insert with `count=1` and `startTime=now()`. Allow request.
2. Otherwise lookup record of UserID. 
    * If `currentTime - startTime >= TIME_WINDOW`, reset interval by setting `count=1` and `startTime=now()`. Allow request.
    * Else If `currentTime - startTime < TIME_WINDOW`, check if rate has been reached
        * If `count < LIMIT`, increment count and allow request
        * If `count >= LIMIT`, reject request


Drawbacks
- Fixed window algorithm, can load up requests if user knows when the window ends
- Atomicity - in a distributed environment, we could have a race condition if multiple new requests reach system at the same time
- We can use locks on the key-value store (Redis) to prevent race conditions
- Locks could possibly slow down the system if requests/limits are set very high


**Sliding Window Algorithm**

Store timestamp of each request in a Redis Sorted Set
```
Key: UserID
Value: (sorted set of unix timestamps)
```

When a new request comes in:
1. Look up sorted set for `UserID`. Remove all timestamps from sorted set older than `currentTime - TIME_WINDOW`
2. Count total number of elements in sorted set.
    * If `count < LIMIT`, allow request and add `currentTime` to sorted set
    * If `count >= LIMIT`, reject request


Drawbacks
- Sliding window takes a lot of memory to record all timestamps in a sorted set
- More calculations and operations needed in refreshing the sorted set on each request


**Sliding Window with Counters**

Hybrid approach. Break up `TIME_WINDOW` into smaller blocks. For each block, we employ a Fixed Window Algorithm, but over multiple blocks, we employ a Sliding Window Algorithm.

Store counters in a Redis Hash
```
Key: UserID
Hash:
    subkey: unixTimestamp for block interval
    subvalue: counts
```


### Data Sharding and Caching

- Shard based on `UserID` to distribute users' data across servers
- use consistent hashing
- If we want to have different throttling limits for different APIs, we can choose to shard per user per API
- Cache recently active users
- Write-back cache - update all counters and timestamp in cache only. Write to permanent storage at fixed intervals, reads always hit cache first, LRU cache eviction policy

### Other Considerations

Rate limit by IP 
- not optimal to differentiate between "good" and "bad" actors
- problem when multiple users share a single IP - coffeeshop, library, office building
- huge number of IPv6 addresses available from a single source, hard to block against spoofing

Rate limit by User
- after authentication and based on user's API key
- Need a different mechanism to rate-limit on login itself

Best approach to limit on both User and IP. More secure at the tradeoff of higher complexity, more memory and storage requirements.








