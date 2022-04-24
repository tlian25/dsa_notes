# Web Crawler

### High Level Ideas
- Cache DNS
- Deduplication on URLs and Pages using a checksum
- Checkpoint snapshots to continue crawling on aborts/failures



### Business Purpose
Browses the web in a methodical and automated manner. Documents by recursively fetching links from a set of starting pages. Used by search engines for indexing.

Other uses:
* Test web pages and links for valid syntax and structure
* Monitor sites to see when structure or contents change
* Maintain mirror sites for popular websites
* Search for copyright infringements
* Build special-purpose indexes

### Business Requirements
- Scalability to crawl entire web and used to fetch 100m's of web documents
- Extensibility in a modular way to easily add new functionality

### Scope and Sizing
- Assume we only care about HTML pages and HTTP protocol. Other protocols and media types can be extended later.
- Assume 1 bn websites
- Assume 15 pages per site on average => 15 bn different web pages
- Assume 4 weeks to build database => 15bn pages / (4 wks * 7 days * 86400 secs) ~= 6200 pages/sec
- Assume average page size of 100kb and 500b of metadata => 100kb * 15bn / 70% = 2.14 PB total storage


### High Level Design

Take a list of seed URLs as input and repeatedly execute following loop (BFS approach):
1. Pick a URL from unvisited URL list
2. Determine IP address of hostname
3. Establish a connection to host to download the corresponding document
4. Parse document contents to look for new URLs.
5. Add new URLs to list of unvisited URLs.
6. Process the downloaded document, e.g. store or index contents, etc.
7. Go to step 1 for next URL


Difficulties in Implementing
1. Large volume of web pages
2. Rate of change on web pages

### Components Overview

1. **URL Frontier Storage** - datastore of the list of URLs to download and also prioritize which URLs should be crawled first
    - distribute to multiple servers
    - hash function on URL to map to which server to process
    - should not overload a server by downloading too many pages at one time
    - should not have multiple machines connecting to a server at one time
    - collection of distinct FIFO sub-queues on each server

2. **HTTP Fetcher Service** - retrieve HTTP web page from server
    - maintain a fixed-sized cache mapping hostnmaes to robot exclusion rules

3. **Document Input Stream** - holds downloaded documents for processing by multiple modules
    - caches entire contents of documents read from internet
    - provides methods to re-read document

3. **Link Extractor Service** - extract links from HTML documents

4. **Document De-Duplication Service** - make sure same content not extracted twice
    - calculate a 64-bit checksum of every processed document and store in database
    - for every new document, compare checksum to see if document has been seen before
    - can use MD5 or SHA to calculate checksums
    - 15bn pages * 8 bytes per checksum = 120 gb 
    - Can keep a LRU based cache pulling from persistent storage

5. **URL De-Duplication Service** - avoid downloading and processing same URL multiple times
    - perform dedupe test on each extracted link before adding to URL frontier
    - store fixed-sized checksum of URLs in database
    - LRU cache of popular URL checksums


5. **URL Filter Service** - customized way to control the set of URLs that are downloaded
    - used to blacklist websites to be ignored
    - restrict URLs by domain, prefix, protocol, etc

6. **DNS Resolution Service** - maps web server's hostname to an IP address
    - DNS name resolution will be a big bottleneck of crawlers given the amount of URLs we will be working with
    - cache DNS results by building our local DNS server

5. **Content Storage** - datastore of retrieved pages, URLs, and metadata
    - partition on URL hashes
    - consistent hashing to expand/contract number of servers without too much change to keys
    - each host to checkpoint and periodically dump snapshot of data to a remote server
    - if server dies, another server can replace by taking data from last snapshot





### Other Considerations

**Bloom Filters**
- Bloom filters are a probabilistic data structure for set membership testing that may yield false positives. 
- False negatives are not possible. 
- An element is added to set by computing `n` hash functions of the element and setting the corresponding bits.
- An element is deemed to be in the set if the bits at all `n` of the element's hash locations are set.

**Checkpointing**
- A crawl of entire web takes weeks to complete
- To guard against failures, our crawler can write regular snapshots of state to disk
- An interrupted or aborted crawl can be easily restarted from the latest checkpoint

**Crawler Traps**
- URL or set of URLs that cause a crawler to crawl indefinitely
- Anti-spam traps are designed to catch crawlers used by spammers looking for email addresses
- Other traps are used to catch search engine crawlers to boost their search ratings





