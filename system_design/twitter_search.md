# Twitter Search

### High Level Ideas
- Details of building a good index schema
- Distributed index storage in hash tables
- Distributed data storage and retrieval
- Process to rebuild any index server on-demand for fault tolerance



### Business Purpose
- Design a system that can efficiently store and query tweets


### Capacity Estimation
- 1.5bn total users
- 400m tweets/day
- 300b avg tweet size
- 500m searches/day

Storage:
- 400m tweets/day * 300b/tweet = 120gb/day
- 120gb/day / 24hrs/day / 3600s/hr = 1.38mb/s
- 12gb/day * 365days/yr * 5yrs * 20% buffer = 250tb

### System APIs
```
search( api_dev_key[str]: unique per user account,
        search_terms[str]: string containing search terms,
        maximum_results_to_return[int]: result limit,
        sort_type[enum]: 0-timestamp, 1-best-match, 2-most-liked,
        page_token[str]: pagination)
    -> JSON
```

### Component Design

**Storage**
- Need to store 250TB of data. 
- Need to partition data to distribute across multiple servers. 
- For backup, we need 500TB of data. 
- Assume modern server can store 4TB of data. 
- We would need 125 servers
- Hash on TweetID

**Index**
- build index on words in tweet object
- assume 500k English words
- average length of word is 5 chars
- 500k words * 5b = 2.5mb of keys
- For 2 years worth of tweets, we need 292b tweets * 5b/tweetID = 1.46TB
- Store full index in distributed hash table
- key=english word and value=[list of tweetIDS containing word]
- assume 15 words in each tweet to index
- Total memory = 1.46TB tweetIDs * 15keys + 2.5mb = 21TB
- assume high-end server has 144GB of memory, we would need 152 servers

**Sharding on Words**
- some words could be overloaded and "hot"
- word usage not evenly distrbuted, some words will be used in many more tweets than others
- need to use consistent hashing

**Sharding on TweetIDs**
- hash on tweetID to assign server
- index all the words of the tweet on that server
- while querying for particular word, we have to query all servers to aggregate all tweets containing that word

**Index-Builder Service**
- hold reverse index that map all TweetID to their index server
- key=index_server, value=hashset contain all tweetIDs routed to that server
- allows for quick rebuilding of an index server if primary + secondary both go down

**Cache**
- Can use memcached to store hot tweets in memory
- searches to index servers only give set of IDs, we then need to go to DB to retrieve tweet messages

**Load Balancer**
Two layers of load balancing
1. between clients and application servers
2. between application servers and backend server








