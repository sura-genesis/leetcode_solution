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

ALGORITHM 
just like how you would sum two numbers on a piece of paper we begin by summing the lest -significant digits which is the head of l1 and l2. since each digit is in the range of 0. . .9

summing two digits may overflow for example 5 + 7 = 12 

in this case we set tthe current digits to 2 and bring over the carry = 1 to the next iteration carry must be either 0 or 1. because the largest possible sum of the digits (including the carry is 9 + 9 + 1 = 19)

the pseudocode is as following:

       1, intialize current node to dummy head of the returning list 
       2, intialize carry to 0
       3, loop through list l1 and l2 until yu reach both ends and carry is 0
            set x to node l1 value if l1 hase reached the end of l1 set tp 0.
            set y to node l2`s value if l2 has reached the end of l2 set to 0.
            set sum = x + y + carry 
            update a new node with the difit value of (sum, med 10 ) and set it to 
            current nodes next then advance current node to nect 
            advance both l1 and l2 
       4, return dummy head`s next node.
    
Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

take extra caution of the following cases:
                    -----------------------------------------------------------------------------------
                    test case                          expanation 
                    -----------------------------------------------------------------------------------
                    
                    l1 = [0,1]             when one list is longer than the other 
                    l2 = [0,1,2]
                    -----------------------------------------------------------------------------------
                    l1 = [] 
                    l2 = [0,1]             when one list is null which means an empty list 
                    -----------------------------------------------------------------------------------
                    l1 = [9,9]
                    l2 = [1]              the sum could have an extra carry of one at the end which 
                                          is easy to forget.
                    -----------------------------------------------------------------------------------

 


