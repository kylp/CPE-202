import unittest

from hashtables import HashTableSepchain, HashTableLinear, HashTableQuadratic, import_stopwords

FILE = "stop_words.txt"

class MyTest(unittest.TestCase):
    def test_sepchain1(self):
        ht = HashTableSepchain()
        for i in range(11):
            ht.put(str(i), i)

        self.assertEqual(ht.size(), 11)
        self.assertEqual(ht.load_factor(), 1.0)
        self.assertTrue(ht.contains('0'))
        self.assertTrue(ht.contains('1'))
        self.assertTrue(ht.contains('10'))
        self.assertFalse(ht.contains('11'))

    def test_sepchain2(self):
        ht = HashTableSepchain()
        for i in range(20):
            ht.put(chr(i), i)

        self.assertEqual(ht.size(), 20)
        self.assertTrue(ht.load_factor() <= 1.0)
        self.assertTrue(ht.contains(chr(0)))
        self.assertTrue(ht.contains(chr(1)))
        self.assertTrue(ht.contains(chr(19)))
        self.assertFalse(ht.contains(chr(20)))

    def test_sepchain3(self):
        ht = HashTableSepchain()
        for i in range(34):
            ht.put(chr(i), i)

        self.assertEqual(ht.size(), 34)
        self.assertTrue(1.0 < ht.load_factor() <= 1.5)

    def test_sepchain4(self):
        ht = HashTableSepchain()
        num_items = int(47 * 1.5) - 1
        for i in range(num_items):
            ht.put(chr(i), i)

        self.assertEqual(ht.size(), num_items)
        self.assertTrue(1.0 < ht.load_factor() <= 1.5)

    def test_sepchain5(self):
        ht = HashTableSepchain()
        stop_words = import_stopwords(FILE, ht)
        self.assertEqual(stop_words.size(), 305)
        self.assertTrue(stop_words.load_factor() <= 1.5)
        self.assertFalse("collision" in stop_words)
        self.assertTrue("very" in stop_words)
        self.assertFalse("linear" in stop_words)
        self.assertTrue("a" in stop_words)

    def test_sepchain6(self):
        ht = HashTableSepchain()
        for i in range(22):
            ht.put(chr(i), i)
        self.assertEqual(ht.size(), 22)
        self.assertEqual(ht[chr(0)], 0)
        self.assertEqual(ht[chr(1)], 1)
        self.assertEqual(ht[chr(19)], 19)

        self.assertRaises(KeyError, ht.get, 'a')

        for i in range(22):
            ht.remove(chr(i))
        self.assertFalse(ht.contains(chr(0)))
        self.assertFalse(ht.contains(chr(1)))
        self.assertFalse(ht.contains(chr(19)))

        self.assertRaises(KeyError, ht.remove, 'a')

    def test_linear1(self):
        ht = HashTableLinear()
        for i in range(11):
            ht.put(str(i), i)

        self.assertEqual(ht.size(), 11)
        self.assertTrue(ht.load_factor() <= 0.75)
        self.assertTrue(ht.contains('0'))
        self.assertTrue(ht.contains('1'))
        self.assertTrue(ht.contains('10'))
        self.assertFalse(ht.contains('11'))

    def test_linear2(self):
        ht = HashTableLinear()
        for i in range(22):
            ht.put(chr(i), i)

        self.assertEqual(ht.size(), 22)
        self.assertTrue(ht.load_factor() <= 0.75)
        self.assertTrue(ht.contains(chr(0)))
        self.assertTrue(ht.contains(chr(1)))
        self.assertTrue(ht.contains(chr(19)))
        self.assertFalse(ht.contains(chr(22)))

    def test_linear3(self):
        ht = HashTableLinear()
        stop_words = import_stopwords(FILE, ht)
        self.assertEqual(stop_words.size(), 305)
        self.assertTrue(0.3 <= stop_words.load_factor() <= 0.4)
        self.assertFalse("collision" in stop_words)
        self.assertTrue("very" in stop_words)
        self.assertFalse("linear" in stop_words)
        self.assertTrue("a" in stop_words)

    def test_linear4(self):
        ht = HashTableLinear()
        for i in range(22):
            ht.put(chr(i), i)
        self.assertEqual(ht.size(), 22)
        self.assertTrue(ht.load_factor() <= 0.75)
        self.assertEqual(ht[chr(0)], 0)
        self.assertEqual(ht[chr(1)], 1)
        self.assertEqual(ht[chr(19)], 19)

        self.assertRaises(KeyError, ht.get, 'a')

        for i in range(22):
            ht.remove(chr(i))
        self.assertFalse(ht.contains(chr(0)))
        self.assertFalse(ht.contains(chr(1)))
        self.assertFalse(ht.contains(chr(19)))

        self.assertRaises(KeyError, ht.remove, 'a')

    def test_quadratic1(self):
        ht = HashTableQuadratic()
        for i in range(11):
            ht.put(str(i), i)

        self.assertEqual(ht.size(), 11)
        self.assertTrue(ht.load_factor() <= 0.75)
        self.assertTrue(ht.contains('0'))
        self.assertTrue(ht.contains('1'))
        self.assertTrue(ht.contains('10'))
        self.assertFalse(ht.contains('11'))

    def test_quadratic2(self):
        ht = HashTableQuadratic()
        for i in range(22):
            ht.put(chr(i), i)

        self.assertEqual(ht.size(), 22)
        self.assertTrue(ht.load_factor() <= 0.75)
        self.assertTrue(ht.contains(chr(0)))
        self.assertTrue(ht.contains(chr(1)))
        self.assertTrue(ht.contains(chr(19)))
        self.assertFalse(ht.contains(chr(22)))

    def test_quadratic4(self):
        ht = HashTableQuadratic()
        for i in range(22):
            ht.put(chr(i), i)

        self.assertEqual(ht.size(), 22)
        self.assertTrue(ht.load_factor() <= 0.75)
        self.assertEqual(ht[chr(0)], 0)
        self.assertEqual(ht[chr(1)], 1)
        self.assertEqual(ht[chr(19)], 19)

        self.assertRaises(KeyError, ht.get, 'a')

        for i in range(22):
            ht.remove(chr(i))
        self.assertFalse(ht.contains(chr(0)))
        self.assertFalse(ht.contains(chr(1)))
        self.assertFalse(ht.contains(chr(19)))

        self.assertRaises(KeyError, ht.remove, 'a')

    def test_quadratic3(self):
        ht = HashTableQuadratic()
        stop_words = import_stopwords(FILE, ht)
        self.assertEqual(stop_words.size(), 305)
        self.assertTrue(0.3 <= stop_words.load_factor() <= 0.4)
        self.assertFalse("collision" in stop_words)
        self.assertTrue("very" in stop_words)
        self.assertFalse("linear" in stop_words)
        self.assertTrue("a" in stop_words)

if __name__ == '__main__':
    unittest.main()

