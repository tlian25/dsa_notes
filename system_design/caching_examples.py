# Caching Examples

import time


class BackingStore:
    def __init__(self):
        self.data = []

    def write(self, datum):
        print("Started writing to backing store.")
        time.sleep(2)
        self.data.append(datum)
        print("Finish writing to backing store.")

    def read(self, index):
        print("Started reading from backing store.")
        time.sleep(2)
        print("Finished reading from backing store.")
        return self.data[index]


class Cache:
    def __init__(self):
        self.data = []

    def write(self, datum):
        print("Started writing to cache.")
        self.data.append(datum)
        print("Finish writing to cache.")

    def read(self, index):
        print("Started reading from cache.")
        print("Finished reading from cache.")
        return self.data[index]


#### Write-through Cache
# data is written to cache and backing store at the same time
# I/O completion only confirmed once data has been written to both places
# Good for apps that write and re-read data frequently
# Trade-off lower read latency vs higher write latency
#
# +: fast retrieval while making sure data is not lost
# -: write latency as we write to two places
def write_through(cache, backing_store, datum):
    cache.write(datum)
    backing_store.write(datum)


#### Write-around
# Data only written to backing store without writing to cache
# I/O confirmed after data store only
# Good for apps that don't frequency re-read recently written data
# Trade-off lower write latency for cache miss + higher
#
# +: doesn't flood cache for data that may not be read
# -: reading recently written data will hit a cache miss
def write_around(backing_store, datum):
    backing_store.write(datum)


#### Write-back
# Data only written to cache
# I/O confirmed after cache only
# Good for mixed workloads as read/write has similar response time levels
# In practice, we can add resiliency by duplicating writes
#
# +: lower latency writes and high throughput for write-intensive apps
# -: data availability and data loss risk if cache crashes
def write_back(cache, datum):
    cache.write(datum)
    # Kick-off asynchronous process to write to backing store.
