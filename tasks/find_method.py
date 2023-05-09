#!/usr/bin/env python3

'''Union-find with specific canonical element. Add a method find() to the union-find 
data type so that find(i) returns the largest element in the connected component 
containing i. The operations, union(), connected(), and find() should all take 
logarithmic time or better.
For example, if one of the connected components is {1, 2, 6, 9}, then the 
find() method should return 9 for each of the four elements in the connected components.'''

import os

class FindMax:
    def __init__(self, data_path=None):
        """Initialize QuickUnion class.
        Args:
            data_path (list): user-defined data
        """
        self.dis_set = []
        self.load_data(data_path)

    def get_data(self):
        return self.dis_set

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            # Set id of each object to itself.
            self.dis_set = [i for i in range(int(data[0]))]
            for line_id in range(1, len(data)):
                num1, num2 = data[line_id].split()
                self.union(int(num1), int(num2))

    def root(self: list, i: int):
        """Chase parent pointers until reach root."""
        while i != self.dis_set[i]:
            i = self.dis_set[i]
        return i

    def is_connected(self: list, p: int, q: int) -> bool:
        """Check whether p and q have the same root."""
        return self.root(p) ==  self.root(q)

    def union(self: list, p: int, q: int):
        """Change root of p to root of q."""
        if self.is_connected(p, q):
            print("The elements are already connected")
        else:
            p_root = self.root(p)
            q_root = self.root(q)
            
            if p_root > q_root:
                self.dis_set[q_root] = p_root
            else:
                self.dis_set[p_root] = q_root
    
    def find(self: list, i: int):
        """Find the largest element in the connected component containing i."""
        return(self.root(i))


if __name__ == '__main__':
    pth = os.getcwd() + '/../data/data2.txt'
    find_max_data = FindMax(pth)
    print(find_max_data.get_data())
    i = 5
    print(f"Max element in the connected component containing {i}: {find_max_data.find(i)}")
    i = 10
    print(f"Max element in the connected component containing {i}: {find_max_data.find(i)}")

    pth = os.getcwd() + '/../data/data.txt'
    find_max_data = FindMax(pth)
    print(find_max_data.get_data())
    i = 5
    print(f"Max element in the connected component containing {i}: {find_max_data.find(i)}")
    i = 3
    print(f"Max element in the connected component containing {i}: {find_max_data.find(i)}")
    i = 9
    print(f"Max element in the connected component containing {i}: {find_max_data.find(i)}")
