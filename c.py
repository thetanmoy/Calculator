from m import M
from v import V


class Controller:
    def __init__(self):
        self.m = M()
        self.v = V(self)

    def main(self):
        self.v.main()

    def on_button_click(self,caption):
        result = self.m.calculate(caption)
        self.v.value_var.set(result)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
