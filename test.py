import unittest
from main import *
from ipa2 import IPAConverter

class Test(unittest.TestCase):

    def test_IPA(self):
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))

    def test_pip(self):
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))
