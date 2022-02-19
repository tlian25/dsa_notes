# A* Algorithm in a Grid setting

# Reference: https://www.annytab.com/a-star-search-algorithm-in-python/

from heapq import *


class Node:
    def __init__(self, position:tuple, parent):
        self.position = position
        self.parent = parent
        self.g = 0 # distance/cost to start node
        self.h = 0 # distance/cost to end node
        self.f = 0 # total distance/cost = g + h
        
    # compare nodes
    def __eq__(self, other):
        return self.position == other.position
    
    # sort
    def __lt__(self, other):
        return self.f < other.f
    
    # print
    def __repr__(self):
        return f'({self.position}, {self.f})'
    

# Draw grid
def draw_grid(map, **kwargs):
    for r in range(len(map)):
        for c in range(len(map[0])):
            print(draw_tile(map, (r, c), kwargs), end='')
        print()
        
# Draw tile
def draw_tile(map, position, kwargs):
    value = map[position[0]][position[1]]
    if 'path' in kwargs and position in kwargs['path']: value = '+'
    elif 'start' in kwargs and  position == kwargs['start']: value = '@'
    elif 'goal' in kwargs and position in kwargs['goal']: value = '$'
    return value


# Taxicab distance
def nodeDist(node1, node2):
    dist =  abs(node1.position[0] - node2.position[0]) + \
            abs(node1.position[1] - node2.position[1])
            
    return dist



# A* search
def astar_search(map, start, end):
 
    
    # create start node and end goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    
    # lists for open and closed nodes
    heap = [start_node]
    seen = set()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    
    while heap:
        curr = heappop(heap)
        # Close lowest cost node
        seen.add(curr.position)
        
        # If goal found, trace back to get shortest path
        if curr == goal_node:
            path = []
            while curr != start_node:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1]
        
        r, c = curr.position
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            
            if 0 <= nr < len(map) and 0 <= nc < len(map):
                nextval = map[nr][nc]
            
                if nextval == '#' or (nr, nc) in seen:
                    continue #wall
                
                # Create neighbor node
                nbr = Node((nr, nc), curr)
                
                # Calculate distances
                nbr.g = nodeDist(nbr, start_node)
                nbr.h = nodeDist(nbr, goal_node)
                nbr.f = nbr.g + nbr.h
                heappush(heap, nbr)
            
    # Not found
    return None


def main():
       

    with open("grid1.txt") as f:
        lines = f.readlines()
    
    height = len(lines)
    width = len(lines[0])-1 # drop \n character
    map = [[0 for _ in range(width)] for _ in range(height)]
    
    # build grid
    for r in range(height):
        for c in range(width):
            map[r][c] = lines[r][c]
            if lines[r][c] == '@':
                start = (r, c)
            elif lines[r][c] == '$':
                end = (r, c)

    path = astar_search(map, start, end)
    print()
    print(path)
    print()
    draw_grid(map, path=path, start=start, goal=end)
    print()
    print(f"Steps to goal: {len(path)}")
    print()
        
        
        
        
        
        
if __name__ == '__main__':
    main()
        
        
        