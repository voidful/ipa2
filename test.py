import unittest
from main import *


class Test(unittest.TestCase):

    def test_IPA(self):
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))
