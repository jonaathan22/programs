""" You are given two positive integers. You have to calculate the result by performing +,-,*,/,% operations on them.

Input Format
The first line of input contains two space-separated integers A and B.

Output Format
The first line of the output should contain the sum of A and B.

The second line of the output should contain the difference of A and B.

The third line of the output should contain the product of A and B.

The fourth line of the output should contain the quotient of A divided by B.

The fifth line of the output should contain the remainder of A modulus by B.

Example 1"""

# Read two integers from input separated by space
A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)