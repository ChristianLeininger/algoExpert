# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 18.06.2023


import unittest
from middleNode import middleNode, LinkedList, middleNodeNaive


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = LinkedList(0)
        linkedList.next = LinkedList(1)
        expected = LinkedList(2)
        linkedList.next.next = expected
        expected.next = LinkedList(3)
        actual = middleNodeNaive(linkedList)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        linkedList = LinkedList(0)
        linkedList.next = LinkedList(1)
        expected = LinkedList(2)
        linkedList.next.next = expected
        expected.next = LinkedList(3)
        actual = middleNode(linkedList)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        linkedList = LinkedList(0)
        linkedList.next = LinkedList(1)
        expected = LinkedList(2)
        linkedList.next.next = expected
        expected.next = LinkedList(3)
        expected.next.next = LinkedList(4)
        actual = middleNodeNaive(linkedList)
        self.assertEqual(actual, expected)
