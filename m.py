class M:
    def __init__(self):
        self.value = ''
        self.old_value = '0'
        self.operator = None

    def calculate(self, caption):
        if caption == 'C':
            self.old_value = ''
            self.value = ''
            self.operator = ''

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value / 100)

        elif caption == '.':
            if caption not in self.value:
                self.value += '.'

        elif caption == '=':
            _value = '0'
            if self.old_value is not '0':
                _value = self._evaluate()
                if _value == int(_value):
                    _value = int(_value)

                self.value = str(_value)

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:
                self.operator = caption
                self.old_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        return eval(self.old_value + self.operator + self.value)
