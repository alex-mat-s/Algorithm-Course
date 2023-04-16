#!/usr/bin/env python3

import os

class DisjointSet:
    def __init__(self, data_path=None, init_flag=False, N=None):
        """Initialize DisjointSet class.
        Args:
            data (list): user-defined data
            init_flag (bool): flag to create default set [0, 1, 2, ..]
            N (int): the length of the default set
        """
        if init_flag:
            self.dis_set = []
            self.find(N)
        else:
            self.dis_set = []
            self.load_data(data_path)

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            self.find(int(data[0]))
            for line_id in range(len(data))[1:]:
                num1, num2 = data[line_id].split()
                self.union(int(num1), int(num2))

    def find(self: list, N: int):
        """Set id of each object to itself."""
        self.dis_set = [i for i in range(N)]          

    def is_connected(self: list, p_ind: int, q_ind: int) -> bool:
        """Check whether p_ind and q_ind are in the samle component."""
        return self.dis_set[p_ind] == self.dis_set[q_ind]

    def union(self: list, p: int, q: int):
        """Change all entries with p_ind to q_ind."""
        p_ind = self.dis_set[p]
        q_ind = self.dis_set[q]
        for i, elem in enumerate(self.dis_set):
            if elem == p_ind:
                self.dis_set[i] = q_ind


if __name__ == '__main__':
    pth = os.getcwd() + '/../data/data.txt'
    data = DisjointSet(data_path=pth)
    print(data.dis_set)
    
