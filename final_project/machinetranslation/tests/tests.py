import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    ''' Unit tests for translator.py'''

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Goodbye'),'Bonjour')
        self.assertRaises( ValueError,englishToFrench, None ) # test for null input

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Goodbye')
        self.assertRaises(ValueError,englishToFrench, None ) # test for null input

if __name__=='__main__':
    unittest.main()
    

