# Newsfeed Service


### High Level Ideas



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

**Non-functional**
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
- Post

Relationship Mapping
- User can become friends with other users
- User can follow other entities
- Users and entities can create Posts which contain text, images, videos
- Posts have UserID which record which user who created
- Posts can have EntityID pointing to page or group where that post was created

