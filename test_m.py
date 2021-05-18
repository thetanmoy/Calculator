from unittest import TestCase
import m


class TestM(TestCase):
    def test_calculate(self):
        model = m.M()
        self.assertEqual(model.calculate(5), '5')
        self.assertEqual(model.calculate('%'), str(5 / 100))
        self.assertEqual(model.calculate('C'), '')
        model.calculate(5)
        model.calculate('+')
        model.calculate(6)
        self.assertEqual(model.calculate('='), '11')
        model.calculate('-')
        model.calculate(2)
        self.assertEqual(model.calculate('='), '9')
        model.calculate('/')
        model.calculate(3)
        self.assertEqual(model.calculate('='), '3')
        model.calculate('*')
        model.calculate(3)
        self.assertEqual(model.calculate('='), '9')

    def test__evaluate(self):
        assert True
