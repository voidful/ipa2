import unittest

from ipa2 import IPA2


class Test(unittest.TestCase):

    def test_IPA(self):
        ipa = IPA2('yue')
        self.assertEqual(['lei˩˧hou˧˥', 'nei˩˧hou˧˥'], ipa.convert_sent("你好"))

    def test_IPA_sentence(self):
        ipa = IPA2('yue')
        self.assertEqual(6, len(ipa.convert_sent("今天天氣不錯")))

    def test_pip(self):
        from ipa2 import IPA2
        ipa = IPA2('yue')
        self.assertEqual(['lei˩˧hou˧˥', 'nei˩˧hou˧˥'], ipa.convert_sent("你好"))

    def test_IPA_NotFound(self):
        ipa = IPA2('yue')
        self.assertEqual([''], ipa.convert_sent("hello"))