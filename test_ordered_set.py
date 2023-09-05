import unittest
from ordered_set import OrderedSet



class TestOrderedSet(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_set = OrderedSet()
        self.singleton_one = OrderedSet([1])
        self.five_first_integers = OrderedSet(range(1, 6))

    def test_str_empty(self):
        self.assertEqual("{}", str(self.empty_set))

    def test_str_singleton(self):
        self.assertEqual("{1}", str(self.singleton_one))

    def test_str_five_first_integers(self):
        self.assertEqual("{1, 2, 3, 4, 5}", str(self.five_first_integers))

    def test_add_empty(self):
        self.assertFalse(self.empty_set.search(1))
        self.empty_set.add(1)
        self.assertTrue(self.empty_set.search(1))

    def test_add_non_empty(self):
        self.assertFalse(self.five_first_integers.search(10))
        self.five_first_integers.add(10)
        self.assertTrue(self.five_first_integers.search(10))

    def test_search_empty(self):
        self.assertFalse(self.empty_set.search(1))
        self.assertFalse(self.empty_set.search(2))

    def test_search_singleton(self):
        self.assertTrue(self.singleton_one.search(1))
        self.assertFalse(self.singleton_one.search(2))

    def test_contains_sequence_empty(self):
        self.assertTrue(self.empty_set.contains_sequence(self.empty_set))
        self.assertFalse(self.empty_set.contains_sequence(self.singleton_one))
        self.assertFalse(self.empty_set.contains_sequence(self.five_first_integers))

    def test_contains_sequence_singleton(self):
        self.assertTrue(self.singleton_one.contains_sequence(self.empty_set))
        self.assertTrue(self.singleton_one.contains_sequence(self.singleton_one))
        self.assertFalse(self.singleton_one.contains_sequence(self.five_first_integers))

    def test_contains_sequence_five_first_integers(self):
        self.assertTrue(self.five_first_integers.contains_sequence(self.empty_set))
        self.assertTrue(self.five_first_integers.contains_sequence(self.singleton_one))
        self.assertTrue(self.five_first_integers.contains_sequence(self.five_first_integers))
        self.assertFalse(self.five_first_integers.contains_sequence(OrderedSet(range(1, 10))))

    def test_search_five_integers(self):
        for i in range(1, 6):
            self.assertTrue(self.five_first_integers.search(i))
        for i in range(6, 10):
            self.assertFalse(self.five_first_integers.search(i))

    def test_truncateprefix_empty(self):
        
        self.assertTrue(self.empty_set.truncate_prefix(1).is_empty_orederdset())
        
        self.assertTrue(self.empty_set.truncate_prefix(2).is_empty_orederdset())

    def test_truncateprefix_singleton(self):
        tester = self.singleton_one
        
        self.assertTrue(tester.truncate_prefix(1) == self.singleton_one)
        
        self.assertTrue(tester.truncate_prefix(2) == self.singleton_one)

    def test_truncateprefix_five_first_integers(self):
        tester = self.five_first_integers
        self.assertTrue(tester.truncate_prefix(5) == self.five_first_integers)
        self.assertTrue(tester.truncate_prefix(3) == OrderedSet([1,2,3]))
        self.assertTrue(tester.truncate_prefix(1) == self.singleton_one)

    def test_truncatesuffix_empty(self):
        self.assertTrue(self.empty_set.truncate_suffix(1).is_empty_orederdset())
        self.assertTrue(self.empty_set.truncate_suffix(2).is_empty_orederdset())

    def test_truncatesuffix_singleton(self):
        self.assertTrue(self.singleton_one.truncate_suffix(1) == self.singleton_one)
        self.assertFalse(self.singleton_one.truncate_suffix(2) == self.singleton_one)

    def test_truncatesuffix_five_first_integers(self):
        self.assertTrue(self.five_first_integers.truncate_suffix(3) == OrderedSet([5,4,3]))
        self.assertTrue(self.five_first_integers.truncate_suffix(5) == OrderedSet([5]))

    def test_equals(self):
        self.assertFalse(self.empty_set == self.singleton_one)
        self.assertFalse(self.five_first_integers == self.singleton_one)
        self.assertTrue(self.empty_set == OrderedSet())
        self.assertTrue(self.empty_set == OrderedSet([]))
        self.assertTrue(self.singleton_one == OrderedSet([1]))
        self.assertTrue(self.five_first_integers == OrderedSet([1,2,3,4,5]))


    def test_delete_item(self):
        self.assertFalse(self.empty_set.delete_item(5))
        self.assertTrue(self.singleton_one.delete_item(1))
        self.assertFalse(self.singleton_one.delete_item(2))
        
        



    if __name__ == '__main__':
        unittest.main()
