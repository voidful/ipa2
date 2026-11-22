#   📖  IPA2

Tools for convert Text to IPA in python

## Dictionary sources and citation

The 100 bundled dictionaries in [`ipa2/data/`](ipa2/data/) match the corresponding
[`CharsiuG2P/dicts` snapshot](https://github.com/lingjzhu/CharsiuG2P/tree/8130d5159b765fa167ab640e6fbb674dd33df411/dicts)
byte for byte. Cite [Zhu, Zhang, and Jurgens (Interspeech 2022)](https://doi.org/10.21437/Interspeech.2022-538)
when using the bundled dictionaries.

That collection combines pronunciation data from several upstream sources, including
[ipa-dict](https://github.com/open-dict-data/ipa-dict) and
[WikiPron](https://github.com/CUNY-CL/wikipron). It is not a direct import from
ipa-dict alone. For a specific language variety, consult
[CharsiuG2P’s source and license catalogue](https://github.com/lingjzhu/CharsiuG2P#g2p-datasets)
and the corresponding upstream source terms before redistributing dictionary data.

## Usage

Install:

```
pip install ipa2
```

Before using :
```
from ipa2 import IPA2
```

# Features
*   [Convert Text to IPA](#convert)  

<h2 id="convert">Convert Text to IPA</h2>    

### convert_sent(sent)
Arguments  
- `sent(String)` : sentence to convert (string)

Returns  
- `list(String)` : list of the result
Examples  
```
IPAConverter('yue')
print(IPAConverter.convert_sent("你好"))
## ['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥']
```
