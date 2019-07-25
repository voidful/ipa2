import unittest
from ipa2.main import *


class Test(unittest.TestCase):

    def test_IPA(self):
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))

    def test_IPA_sentence(self):
        ipa = IPAConverter('yue')
        self.assertEqual(6, len(ipa.convert_sent("今天天氣不錯")))

    def test_pip(self):
        from ipa2 import IPAConverter
        ipa = IPAConverter('yue')
        self.assertEqual(['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥'], ipa.convert_sent("你好"))

    def test_IPA_NotFound(self):
        ipa = IPAConverter('yue')
        self.assertEqual([''], ipa.convert_sent("hello"))

    def test_IPA_MultiLang(self):
        ipa = IPAConverter(['yue', 'en_UK'])
        self.assertEqual(['həlˈə‍ʊ'], ipa.convert_sent("hello"))
