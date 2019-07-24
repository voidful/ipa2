import unittest
from ipa2.main import *

class Test(unittest.TestCase):

    def test_IPA(self):
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))

    def test_pip(self):
        from ipa2 import IPAConverter
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))
