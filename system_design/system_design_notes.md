# System Design Notes


### HTTP Long-Polling

1. Client makes initial HTTP GET request and waits for response
2. Server delays its response until an update is available or timeout occurs
3. When update is available, server sends full response to client
4. Client sends a new long-poll request to await next update

Each long-poll request has a timeout to prevent holding the connection open indefinitely.

### WebSockets

- Full duplex communication channels over a single TCP connection. 
- Persistent connection between client and server so that two-way communication can occur simultaneously
- facilitate real-time data transfer to and from server
 - standardized way for server to send content to the browser without being asked by the client and allowing messages to be passed back and forth while keeping the connection open


### Server-Sent Events (SSE)

- Client establishes a persistent and long-term connection with the server
- Server uses this connection to send data to the client
- Client does not send data to server
- Best when we need real-time traffic from server or server will be sending multiple events to client


### Gossip Protocols

- problem of knowing when other nodes are dea in a distributed system
- each node sends some data to a set of other nodes
- data propogates through the system node by node like a virus
- eventually data propogates to every node in the system
- allows nodes to build a global map from limited local interactions
- in distributed system, need at least two independent sources of information to mark a node down
