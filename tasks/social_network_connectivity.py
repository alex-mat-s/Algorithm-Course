#!/usr/bin/env python3

'''Given a social network containing n members and a log file containing 
m timestamps at which times pairs of members formed friendships, design 
an algorithm to determine the earliest time at which all members 
are connected (i.e., every member is a friend of a friend of a friend ... of a friend). 
Assume that the log file is sorted by timestamp and that friendship is an equivalence 
relation. The running time of your algorithm should be m log n or better and use extra 
space proportional to n.'''

import os

class SocialNet:
    def __init__(self, data_path):
        """Initialize SocialNet class.
        Args:
            data_path (list): user-defined data
        """
        self.friends = []
        self.all_connected_timestamp = None
        self.load_data(data_path)

    def get_data(self):
        return self.friends

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            # Set id of each object to itself.
            self.friends = [i for i in range(int(data[0]))]
            self.trees_size = [1] * int(data[0])
            for line_id in range(1, len(data)):
                timestamp, friend1, friend2 = data[line_id].split()
                all_connected_flag = self.union(int(friend1), int(friend2))
                if all_connected_flag:
                    self.all_connected_timestamp = timestamp

    def root(self: list, i: int):
        """Chase parent pointers until reach root."""
        while i != self.friends[i]:
            self.friends[i] = self.friends[self.friends[i]]
            i = self.friends[i]
        return i

    def is_connected(self: list, p: int, q: int) -> bool:
        """Check whether p and q have the same root."""
        return self.root(p) ==  self.root(q)

    def __weighted_union(self: list, p_root: int, q_root: int):
        "Apply weighting."
        flag = False
        if self.trees_size[p_root] < self.trees_size[q_root]:
            self.friends[p_root] = q_root
            self.trees_size[q_root] += self.trees_size[p_root]
            friends_size = self.trees_size[q_root]
        else:
            self.friends[q_root] = p_root
            self.trees_size[p_root] += self.trees_size[q_root]
            friends_size = self.trees_size[p_root]
        
        if friends_size == len(self.friends) and self.all_connected_timestamp is None:
                flag = True
        return flag


    def union(self: list, p: int, q: int):
        """Change root of p to root of q."""
        flag = False
        if self.is_connected(p, q):
            print("The elements are already connected")
        else:
            p_root = self.root(p)
            q_root = self.root(q)
            
            flag = self.__weighted_union(p_root, q_root)
        return flag
                
if __name__ == '__main__':
    pth = os.getcwd() + '/../data/data_social_net.txt'
    data_social_network = SocialNet(pth)
    print("All members are connected:", data_social_network.all_connected_timestamp)
    
