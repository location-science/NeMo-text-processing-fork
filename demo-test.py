from nemo_text_processing.text_normalization.normalize import Normalizer


written = """Covering an expanse of 368.92 hectares, designated as nature reserve number NSG-00377.01, Lechauwald was established as a protected area in 1990. """
# improved output: 
# Covering an expanse of three hundred and sixty eight point nine two hectares, designated as nature reserve number nsg dash zero zero three seven seven dot zero one, Lechauwald was established as a protected area in nineteen ninety.

written = """The average temperature is around 7 °C, with June being the warmest month at an average of 18 °C, while January is the coldest, with temperatures dropping to −5 °C. """
# improved output: 
# The average temperature is around seven degrees Celsius, with June being the warmest month at an average of eighteen degrees Celsius, while January is the coldest, with temperatures dropping to minus five degrees Celsius.

written = """布伦嫩的年平均降水量为1,211毫米，其中8月为降水量最多的月份，降水量达到162毫米，而3月则是降水量最少的月份，仅为39毫米。"""
# Old output:
# 布伦嫩的年平均降水量为一,二百一十一毫米，其中八月为降水量最多的月份，降水量达到一百六十二毫米，而三月则是降水量最少的月份，仅为三十九毫米。

written = """Der wärmste Monat ist der Juni, in dem die Temperaturen durchschnittlich 18 °C erreichen, während der kälteste Monat der Januar mit durchschnittlich −5 °C ist."""
##### Old output:
# tokens { name: "durchschnittlich" } tokens { name: "−" }tokens { measure { cardinal { integer: "fünf" } units: "grad celsius" preserve_order: true } } tokens { name: "ist." }
# Der wärmste Monat ist der Juni, in dem die Temperaturen durchschnittlich achtzehn grad celsius erreichen, während der kälteste Monat der Januar mit durchschnittlich − fünf grad celsius ist.
#### Improved output:
# tokens { name: "durchschnittlich" } tokens { measure { cardinal { negative: "true" integer: "fünf" } units: "grad celsius" preserve_order: true } } tokens { name: "ist." }
# Der wärmste Monat ist der Juni, in dem die Temperaturen durchschnittlich achtzehn grad celsius erreichen, während der kälteste Monat der Januar mit durchschnittlich minus fünf grad celsius ist.

# written = "The Munich–Herrsching railway is a vital electrified main line stretching 31 kilometers in Upper Bavaria, serving as a branch line from Munich-Pasing to Herrsching"

normalizer = Normalizer(input_case='cased', lang='de')
normalized = normalizer.normalize(written, verbose=True, punct_post_process=True)
print(normalized)