# -*- coding: utf-8 -*-
""" Repaso interactivo de python
    Traducido de: http://grading.codingthematrix.com/edition1/index.html
"""


def minutes_in_weeks(weeks):
    """ 1: (Task 0.5.1) Minutes in a Week

    >>> minutes_in_weeks(1)
    10080

    >>> minutes_in_weeks(2)
    20160
    """
    return weeks * 7 * 24 * 60


def reminder_without_mod(numerator, divisor):
    """
    2: (Task 0.5.2) Remainder
    >>> remainder_without_mod(28,7)
    0
    >>> remainder_without_mod(30,7)
    2
    """
    return numerator - ((numerator // divisor) * divisor)


def divisble_by_3(num):
    """
    3: (Task 0.5.3) Divisibility
    >>> divisible_by_3(9)
    True
    >>> divisibre_by_3(7)
    False
    """


def predict_expresion(x, y, prediction):
    """
    4: (Task 0.5.4) Conditional Expression
    Try to predict the value of 2**(y+1/2) if x+10<0 else 2**(y-1/2)
    >>> predict_expression(-9, 1/2, 1)
    1
    """


def squares_set(numbers):
    """
    5: (Task 0.5.5) Squares Set Comprehension
    Given a set of numbers return a set of the numbers squared
    >>> squares_set({1,2,3,4,5,5,5})
    set([16, 1, 4, 25, 9])
    """


def pows_two(numbers):
    """
    6: (Task 0.5.6) Powers-of-2 Set Comprehension
    Given a set of numbers return the powers of two of those numbers
    >>> pows_two({0,1,2,3,4})
    set([8, 1, 2, 4, 16])
    """


def set_product57(xs, ys):
    """
    7: (Task 0.5.7) Double comprehension evaluating to nine-element set
    Return a set containing the multiplication of every element in a set multiplied by the other
    >>> set_product57({1,2,3},{3,4,5})
    set([3, 4, 5, 6, 8, 9, 10, 12, 15])
    """


def set_product58(xs, ys):
    """
    8: (Task 0.5.8) Double comprehension evaluating to five-element set
    Return a set containing the multiplicacion of every elment in a set multiplied by the other
    where elements dont repeat
    >>> set_product58({1,2,3},{3,4,5})
    set([3, 4, 5, 6, 8, 10, 12, 15])
    """


def intersection(Ss, Ts):
    """
    9: (Task 0.5.9) Set intersection as a comprehension
    >>> intersection({1, 2, 3, 4},{3, 4, 5, 6})
    set([3, 4])
    """


def list_average(list_of_numbers):
    """
    10: (Task 0.5.10) Average
    A one-line expression that evaluates to the average of list_of_numbers.
    Your expression should refer to the variable list_of_numbers, and should work
    for a list of any length greater than zero.

    >>> list_average([20, 10, 15, 75])
    30
    """


def cartesian_product(Xs, Ys):
    """
    11: (Task 0.5.11) Cartesian-product comprehension
    a double list comprehension over {'A','B','C'} and {1,2,3}
    >>> cartesian_product(['A','B','C'],[1,2,3])
    [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2],['B', 3],['C', 1], ['C', 2], ['C', 3]]
    """


def LofL_sum(list_of_lists):
    """
    12: (Task 0.5.12) Sum of numbers in list of list of numbers
    a one-line expression of the form sum([sum(...) ... ]) that
    includes a comprehension and evaluates to the sum of all numbers in all the lists.

    >>> LofL_sum([[.25, .75, .1], [-1, 0], [4, 4, 4, 4]])
    16.1

    """


def zero_sum_list(list_of_numbers):
    """
    13: (Task 0.5.14) Three-element tuples summing to zero
    >>> zero_sum_list([-4, -2, 1, 2, 5, 0])
    [(-4, 2, 2), (-2, 1, 1), (-2, 2, 0), (-2, 0, 2), (1, -2, 1), (1, 1, -2), (2, -4, 2), (2, -2, 0), (2, 2, -4), (2, 0, -2), (0, -2, 2), (0, 2, -2), (0, 0, 0)]
    """


def non_zero_sum_list(list_of_numbers):
    """
    Task 0.5.15: Modify the comprehension of the previous task so that the resulting list does
    not include (0, 0, 0). Hint: add a filter.
    >>> non_zero_sum_list([-4, -2, 1, 2, 5, 0])
    [(-4, 2, 2), (-2, 1, 1), (-2, 2, 0), (-2, 0, 2), (1, -2, 1), (1, 1, -2), (2, -4, 2), (2, -2, 0), (2, 2, -4), (2, 0, -2), (0, -2, 2), (0, 2, -2)]
    """


def first_zero_sum_list(list_of_numbers):
    """
    16: (Task 0.5.16) first nontrivial three-element tuple summing to zero
    >>> first_zero_sum_list([-4, -2, 1, 2, 5, 0])
    [(-4, 2, 2)]
    """


def is_element_repeated(things):
    """
    17: Task 0.5.17: Find an example of a list L such that len(L) and len(list(set(L))) are diferent."
    >>> is_element_repeated([1,1,2,3])
    True
    >>> is_element_repeated([1,2,3,4])
    False
    """


def odd_num_list(n):
    """
    Task 0.5.18: Write a comprehension over a range of the form range(n) such that the
    value of the comprehension is the set of odd numbers from 1 to n.
    >>> odd_num_list(17)
    [1, 3, 5, 7, 9, 11, 13, 15]
    """


def range_and_zip(letters):
    """
    (Task 0.5.19) Using range and zip
    >>> range_and_zip("ABCDE")
    [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

    Do not use a list comprehension use range and zip
    """


def list_sum_zip(A, B):
    """
    (Task 0.5.20) Using zip to find elementwise sums
    A one-line comprehension that uses zip together with the variables A and B.
    The comprehension should evaluate to a list whose ith element is the ith element of
    A plus the ith element of B.
    >>> list_sum_zip([10,20,30],[1,2,3])
    [11, 22, 33]
    """


def value_list(k, dlist):
    """
    (Task 0.5.21) Extracting the value corresponding to key k from each dictionary in a list
    >>> value_list('James',[{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}])
    ['Sean', 'Roger', 'Pierce']
    """
    return [i[k] for i in dlist]
    
    


def value_list_m(k, dlist):
    """
    Task 0.5.22: Modify the comprehension in Task 0.5.21 to handle the case
                 in which k might not appear in all the dictionaries.
                 The comprehension evaluates to the list whose ith element is
                 the value corresponding to key k in the i
    th dictionary in dlist if that dictionary
    contains that key, and 'NOT PRESENT' otherwise.
    >>> value_list_m('Bilbo',[{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Rich'}])
    ['Ian', 'Martin']
    >>> value_list_m('Frodo',[{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Rich'}])
    ['Elijah', 'NOT PRESENT']
    """


def square_dict(n):
    """
    (Task 0.5.23) A dictionary mapping integers to their squares
    Replace {...} with a one-line dictionary comprehension
    >>> square_dict(10)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    """


def dictionary_mapping(names, id2salaries):
    """
    (Task 0.5.26) A dictionary mapping names to salaries
    >>> dictionary_mapping(['Larry', 'Curly', 'Moe'],{0:100.0, 1:120.50, 2:99})
    {'Larry': 100.0, 'Moe': 99, 'Curly': 120.5}
    """


def nextInts(L):
    """
    Task 0.5.28: Define a one-line procedure nextInts(L) specified as follows:
      input: list L of integers
      output: list of integers whose ith element is one more than the i
      th element of L
    >>> nextInts([1, 5, 7])
    [2, 6, 8]
    """
    return []


def cubes(L):
    """
    Task 0.5.29: Define a one-line procedure cubes(L) specified as follows:
    - input: list L of numbers
    - output: list of numbers whose ith element is the cube
              of the ith element of L
    >>> cubes([1, 2, 3])
    [1, 8, 27]
    """
    return []


def dict2list(dct, keylist):
    """
    Task 0.5.30: Define a one-line procedure
                 dict2list(dct,keylist) with this spec:
      input: dictionary dct, list keylist consisting of the keys of dct
      output: list L such that L[i] = dct[keylist[i]]
              for i = 0, 1, 2,..., len(keylist) % 1
    >>> dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a'])
    ['B', 'C', 'A']
    """
    return []


def list2dict(L, keylist):
    """
    Task 0.5.31: Define a one-line procedure list2dict(L, keylist)
                 specified as follows:
      input: list L, list keylist of immutable items
      output: dictionary that maps keylist[i] to L[i]
              for i = 0, 1, 2,..., len(L) % 1
    >>> list2dict([’A’,’B’,’C’],keylist=[’a’,’b’,’c’])
    {'a':'A', 'b':'B', 'c':'C'}
    """
    return {}
