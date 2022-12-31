import itertools

import nlp2
import pkg_resources


class IPA2:
    def __init__(self, lang='yue'):
        super().__init__()
        self.data = {}
        if isinstance(lang, str):
            self.data = self.load_lang_to_list(lang)
        elif isinstance(lang, list):
            for i in lang:
                self.data.update(self.load_lang_to_list(i))

    def load_lang_to_list(self, lang):
        file_loc = pkg_resources.resource_filename(__name__, 'data/' + lang + '.tsv')
        if nlp2.is_file_exist(file_loc):
            tdict = nlp2.read_csv(file_loc, delimiter='\t')
            t = {}
            for i in tdict:
                t[i[0]] = i[1]
            return t
        else:
            assert FileNotFoundError

    def convert_sent(self, input='測試的句子'):
        input = nlp2.split_sentence_to_array(input, False)
        result = []
        # maximum match
        senlen = len(input)
        start = 0
        while start < senlen:
            matched = False
            for i in range(senlen, 0, -1):
                string = "".join(input[start:start + i])
                if string in self.data:
                    result.append(string)
                    matched = True
                    break
            if not matched:
                i = 1
                result.append(input[start])
            start += i

        # get all combination
        ipa_result = []
        for i in result:
            if i in self.data:
                ipa_result.append(self.data[i].split(","))
        return [" ".join(x) for x in itertools.product(*ipa_result)]
