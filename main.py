import itertools
import json


class IPAConverter:
    def __init__(self, lang='yue'):
        super().__init__()
        with open('data/' + lang + '.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            self.data = data['yue'][0]

    def convert_sent(self, input='測試的句子'):
        result = []
        # maximum match
        senlen = len(input)
        start = 0
        while start < senlen:
            matched = False
            for i in range(senlen, 0, -1):
                string = input[start:start + i]
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
            ipa_result.append(self.data[i].replace('/', '').split(", "))

        return [" ".join(x) for x in itertools.product(*ipa_result)]
