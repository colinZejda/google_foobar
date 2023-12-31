"""
The latest gossip in the henchman breakroom is that "LAMBCHOP" stands for "Lambda's Anti-Matter Biofuel Collision Hadron Oxidating Potentiator". 
You're pretty sure it runs on diesel, not biofuel, but you can at least give the commander credit for trying.

Ion Flux Relabeling===================
Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired spectacularly. 
The Commander had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. 
Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. 
Commander Lambda is having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!
Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. 
To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. 
For example, a tree of 7 converters would look like the following:   7 3   61 2 4 5
Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  
For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].
The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  
The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages=========
To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases==========
Your code should pass the following test cases. Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:Solution.solution(3, {7, 3, 5, 1}) Output:    -1,7,6,3
Input:Solution.solution(5, {19, 14, 28}) Output:    21,15,29

-- Python cases --
Input:solution.solution(5, [19, 14, 28]) Output:    21,15,29
Input:solution.solution(3, [7, 3, 5, 1]) Output:    -1,7,6,3

Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.
"""

"""
MAIN IDEAS
    -- find parent of a node: must find if given node is left or right child of the parent, then compute parent's label
    -- post-order: left, right root (root has label 2**h - 1)
    -- the subtrees of root: each have height h-1, thus 2**(h-1) - 1 nodes  -->  recursion will be a big help
        - pattern for a node: left child is 2**(h-1)-2, right child is 2**h - 2
"""

def helper(r_val, n_val, h):              # r = root, n = node
    if h == 1: return -1                  # edge case, no parent for root
    l_child_val = r_val - (2**(h-1))      # right subtree size 2**(h-1) - 1, subtract that from r_val, -1's cancel
    r_child_val = r_val - 1
    if l_child_val == n_val or r_child_val == n_val:  # found!
        return r_val
    if n_val < l_child_val:                           # continue recursion
        return helper(l_child_val, n_val, h - 1)
    else:
        return helper(r_child_val, n_val, h - 1)

# h = height of perfect binary tree (thus, 2^h-1 nodes)
# q = list of pos ints (want to find the int above these numbers)
# call helper for each node, starting at root val, full height and node in queue
def solution(h, q):
    return [helper((2**h) - 1, n, h) for n in q]

if __name__ == "__main__":
    print(solution(3, [7, 3, 5, 1]))  # Out: [-1, 7, 6, 3]
    print(solution(5, [19, 14, 28]))  # Out: [21, 15, 29]