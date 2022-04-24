# Newsfeed Service


### High Level Ideas
- pre-generate newsfeed for faster read operations
- hybrid pull/push posts for different entities based on number of followers
- 


### Business Purpose
- constantly updating list of stories on homepage 
- includes status updates, photos, videos, links, app activity, people, pages, groups
- compilation of a complete scrollable version of friends' photos, videos, locations, status updates, and other activities

### Business Requirements

**Functional**
1. Newsfeed generated based on the posts from people, pages, and groups that a user follows
2. User may have many friends and follow a large number of pages/groups
3. Feeds may contain images, videos, and text statuses
4. Service should support appending new posts as they arrive

**Non-Functional**
1. Generate any user's newsfeed in real-time. Max latency seen by user would be 2s.
2. A post shouldn't take more than 5s to make it to a user's feed.

### Capacity Estimation

Assumptions
- A user has 300 friends and follows 200 pages
- 300M DAUs with each user fetching their timeline an average of five times a day
- 1.5Bn newsfeed requests per day => 17.5k requests per second
- 500 posts in every user's feed that we would keep in memory for quick fetch
- Each post 1kb in size => 150Tb of memory

### Database Design

Tables
- User
- Entity (group, page, etc)
- Post (FeedItem)

Relationship Mapping
- User can become friends with other users
- User can follow other entities
- Users and entities can create Posts which contain text, images, videos
- Posts have UserID which record which user who created
- Posts can have EntityID pointing to page or group where that post was created

### System Design

**Feed Generation**
1. Retrieve IDs of all users and entities that Jane follows.
2. Retrieve latest, most popular and relevant posts for those IDs.
3. Rank posts based on the relevance to User. This represents User's current feed.
4. Store feed in cache and return top 20 posts to be rendered on Jane's feed.
5. On front-end, when User reaches end of current feed, fetch the next 20 posts from server.

**Feed Publishing**


1. **Web Servers**
    - maintain a connection with user, used to transfer data between user and server

2. **Application Server**
    - execute the workflows of storing new posts in database servers
    - retrieve and push newsfeed to end user

3. **Metadata Database and Cache**
    - user, pages, and groups metadata
    - relationship between follows

4. **Posts Database and Cache**
    - post metadata and content

5. **Media Storage and Cache**
    - videos, photos, multimedia

6. **Newsfeed Generation Service**
    - gather and rank all relevant posts for a user to generate newsfeed and store in cache
    - receive live updates and add newer feed items to any user's timeline
    - pre-generate timeline on a regular basis and store in memory
    - track last timestamp to generate next newsfeed block from
    - 1. LRU cache to only keep users that have recently accessed timeline
    - 2. figure out login pattern of users to pre-generate newsfeed

7. **Feed Publishing**
    - fanout-on-write: push a post out to all followers on write, users must maintain long-poll requests with server, significantly reduces read operations
    - fanout-on-load: pull post on read, new data not shown until pull request issued, hard to find right cadence to pull, could be lots of wasted resources on empty pulls
    - hybrid approach: only push data for users with small number of followers, pull data for users with high number of followers

8. **Feed Ranking**
    - easiest way to rank on timestamp
    - smarter way to select on features that are relevant to importance of feed item
    - calculate a score using these features
    - advanced way to rank by user interaction prediction

9. **Data Partitioning**
    - Shard feed data on UserID
    - can try storing all data of a user on one server
    - To get the feed of a user, we would always have to query only one server
    - Use consistent hashing for future growth and replication

10. **Feed Notification Service**
    - notify user that there are newer items available for their newsfeed


