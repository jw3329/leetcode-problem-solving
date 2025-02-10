#  public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
#  * }

# f

#.        s


#             f
#.        p.      
# p.next = f.next
# return head

# p = f
# f = f.next
# p.next = f.next

# 1 - 2 - 3 - 4 - 5, n = 2
# 1 - 2 - 3 - 5

# 

class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next

def removeNthToLastNodeFromLL(head, n):
    curr1 = head
    curr2 = head
    # curr2 to be n next
    for _ in range(n):
        curr2 = curr2.next
    prev = None
    while curr2:
        prev = curr1
        curr1 = curr1.next
        curr2 = curr2.next
    # curr2 is null
    if prev:
        prev.next = curr1.next
    else:
        return head.next
    return head

def printNodes(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


head = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5,None)))))

removed = removeNthToLastNodeFromLL(head, 5)

printNodes(removed)


# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def num_of_island(grid):

    def dfs(i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
        if grid[i][j] == '0': return
        grid[i][j] = '0'
        dirs = [1,0,-1,0,1]
        for k in range(4):
            ii = i + dirs[k]
            jj = j + dirs[k+1]
            dfs(ii,jj)


    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # do dfs if 1
            if grid[i][j] == '1':
                res += 1
                dfs(i,j)
    return res


print(num_of_island(grid))
