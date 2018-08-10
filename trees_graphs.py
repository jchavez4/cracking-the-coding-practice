from graph import Graph
from node import Node


"""
    Problem set from Chapter 4: Trees and Graphs in Cracking the Coding Interview
    Solved in Python
"""

def find_route(graph, start, end):
    """ Given a directed graph, design an algorithm to find out whether there is
        a route between two nodes. """

    queue = [[start]]

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current == end:
            return path

        if current in graph: #for adjacent in graph.get(current, []):
            for adjacent in graph[current]:
                temp_path = list(path)
                temp_path.append(adjacent)
                queue.append(temp_path)

    return None



def min_height_bst():
    """ Given a sorted (increasing order) array with unique integer elements,
        write an algorithm to create a bst with minimal height. """

    pass


def list_of_depths():
    """ Given a binary tree, design an algorithm which creates a linked list of
        all the nosed at each depth. """

    pass


def check_balanced():
    """ Implement a function to check if a binary tree is balanced. A balanced
        tree is defined to be a tree such that the heights of the two subtrees
        of any node never differ by more than one. """

    pass


def validate_bst():
    """ Implement a function to check if a binary tree is a bst. """

    pass


def find_successor():
    """ Write an algorithm to find the 'next' node of a given node in a bst.
        Each node has a link to its parent. """

    pass


def build_order():
    """ You are given a list of projexts and a list of dependencies (which is a
        list of pairs of projexts, where the second projext is dependent on the
        first project). All of a project's dependencies must be built before the
        project is. Find a build order that will allow the projects to be built.
        If there is no valid build order, return an error. """

    pass


def find_fca():
    """ Design an algorithm and write code to find the first common ancestor of
        two nodes in a binary tree. Avoid storing additional nodes in a data
        structure. NOTE: This is not necessarily a bst. """

    pass


def bst_sequences():
    """ A binary search tree was created by traversing through an arry from left
        to right and inserting each element. Given a binary search tree with
        distinct elements, print all possible arrays that could have led to this
        tree. """

    pass


def check_subtree():
    """ T1 and T2 are two very large binary trees, with T1 much bigger than T2.
        Create an algorithm to determine if T2 is a subtree of T1. A tree T2 is
        a subtree of T1 is there exists a node n in T1 such that the subtree of
        n is identical to T2. """

    pass


def random_node():
    """ Returns a random node from the tree. All nodes should be equally likely
        to be chosen. Design and implement an algorithm to get a random node. """

    pass


def find_sum_path():
    """ You are given a binary tree in which each node contains an integer value
        (which might be positive or negative). Design an algorithm to count the
        number of paths that sum to a given value. The path does not need to
        start or end at the root or a leaf, but it must go downwards (traveling
        only from parent nodes to child nodes). """

    pass

if __name__ == '__main__':
    #graph = {
        # '1': ['2', '3', '4'],
        # '2': ['5', '6'],
        # '5': ['9', '10'],
        # '4': ['7', '8'],
        # '7': ['11', '12']
        # }
    graph = {0:[1], 1:[2], 2:[0,3], 3:[2], 4:[6], 5:[4], 6:[5]}

    print find_route(graph, 0, 3)
