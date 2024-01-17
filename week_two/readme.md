# add two number 

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# example 1 

![image](https://github.com/sura-genesis/leetcode_solution/assets/140810329/449b83ea-ec6f-4f54-a639-6c8d52a9c189)

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
# Example 2 

    Input: l1 = [0], l2 = [0]
    Output: [0]

# Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

TO SOLVE THIS PROBLEAM WE HAVE TO APPROCH THE PROBLEAM IN THE FOLLOWING METHODS 

Approach 1: Elementary Math

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.

![image](https://github.com/sura-genesis/leetcode_solution/assets/140810329/e1df74a4-7b96-4d71-a8fc-657f00e1b3bc)

Figure 1. Visualization of the addition of two numbers: 
342 + 465 = 807
342 + 465 = 807.
Each node contains a single digit and the digits are stored in reverse order.


