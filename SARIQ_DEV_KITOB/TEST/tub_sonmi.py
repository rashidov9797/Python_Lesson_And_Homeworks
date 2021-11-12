import  unittest

from tekshiramiz import tubSonmi

class tubSonTest(unittest.TestCase):
  def test_true(self):
    self.assertTrue(tubSonmi(7))
    self.assertTrue(tubSonmi(199))
    self.assertTrue(tubSonmi(547))

  def test_false(self):
    self.assertFalse(tubSonmi(6))
    self.assertFalse(tubSonmi(244))
    self.assertTrue(tubSonmi(444))
unittest.main()      