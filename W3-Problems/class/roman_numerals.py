class RomanNumerals:
    def __init__(self, integer):
        self.integer = integer

    def convert(self):
        numerals = ['I', 'II', 'III', 'IV=IIII', 'V', 'VI', 'VII', 'VIII=IIX',
                    'IX=VIIII', 'X', 'XI']
        
        return numerals

obj = RomanNumerals(12)


