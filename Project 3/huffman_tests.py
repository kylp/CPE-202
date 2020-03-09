import unittest
import filecmp
from huffman_coding import cnt_freq, create_huff_tree, create_code, huffman_encode

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("test1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("test1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 'a')
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 'a')
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 'd')

   def test_create_code(self):
      freqlist = cnt_freq("test1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

   def test_create_code2(self):
      freqlist = cnt_freq("test2.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      print(codes[ord('g')])
      print(codes[ord('o')])
      print(codes[ord('\n')])

   def test_create_code3(self):
      freqlist = cnt_freq("test3.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      print(codes[ord('s')])
      print(codes[ord('t')])
      print(codes[ord('\n')])

   def test_01_encodefile(self):
      huffman_encode("test1.txt", "encodetest1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest1.txt", "test1.out"))

   def test_02_encodefile(self):
      huffman_encode("test2.txt", "encodetest2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest2.txt", "test2.out"))

   def test_03_encodefile(self):
      huffman_encode("test3.txt", "encodetest3.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest3.txt", "test3.out"))

   def test_01_decodefile(self):
      freqlist = cnt_freq("test1.txt")
      huffman_decode(freqlist,"test1.out", "decodetest1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest1.txt", "test1.txt"))

   def test_02_decodefile(self):
      freqlist = cnt_freq("test2.txt")
      huffman_decode(freqlist,"test2.out", "decodetest2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest2.txt", "test2.txt"))

   def test_03_decodefile(self):
      freqlist = cnt_freq("test3.txt")
      huffman_decode(freqlist, "test3.out", "decodetest3.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest3.txt", "test3.txt"))

if __name__ == '__main__': 
   unittest.main()
