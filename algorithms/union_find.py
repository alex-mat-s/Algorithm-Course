#!/usr/bin/env python3

import os


class QuickFind:
    def __init__(self, data_path=None, init_flag=False, N=None):
        """Initialize QuickFind class.
        Args:
            data (list): user-defined data
            init_flag (bool): flag to create default set [0, 1, 2, ..]
            N (int): the length of the default set
        """
        if init_flag:
            # Set id of each object to itself.
            self.dis_set = [i for i in range(N)] 
        else:
            self.dis_set = []
            self.load_data(data_path)

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            # Set id of each object to itself.
            self.dis_set = [i for i in range(int(data[0]))]
            for line_id in range(len(data))[1:]:
                num1, num2 = data[line_id].split()
                self.union(int(num1), int(num2))

    def is_connected(self: list, p_ind: int, q_ind: int) -> bool:
        """Check whether p_ind and q_ind are in the samle component."""
        return self.dis_set[p_ind] ==  self.dis_set[q_ind]

    def union(self: list, p: int, q: int):
        """Change all entries with p_ind to q_ind."""
        if self.is_connected(p, q):
            print("The elements are already connected")
        else:
            p_ind = self.dis_set[p]
            q_ind = self.dis_set[q]

            for i, elem in enumerate(self.dis_set):
                if elem == p_ind:
                    self.dis_set[i] = q_ind


class QuickUnion:
    def __init__(self, data_path=None, init_flag=False, N=None):
        """Initialize QuickUnion class.
        Args:
            data (list): user-defined data
            init_flag (bool): flag to create default set [0, 1, 2, ..]
            N (int): the length of the default set
        """
        if init_flag:
            # Set id of each object to itself.
            self.dis_set = [i for i in range(N)] 
        else:
            self.dis_set = []
            self.load_data(data_path)

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            # Set id of each object to itself.
            self.dis_set = [i for i in range(int(data[0]))]
            for line_id in range(len(data))[1:]:
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
    
            self.dis_set[p_root] = q_root


if __name__ == '__main__':
    pth = os.getcwd() + '/../data/data.txt'
    data_QF = QuickFind(data_path=pth)
    data_QU = QuickUnion(data_path=pth)
    print(data_QF.dis_set)
    print(data_QU.dis_set)

    data_QU.union(0, 9)
    print(data_QU.dis_set)
    data_QU.union(5, 2)
    print(data_QU.dis_set)

    
