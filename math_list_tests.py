import math_list
from math_list import MathList
import unittest
import list_generator
# TODO: Напишите тесты для проверки каждой операции и метода класса Mathlist
# Подсказка: для проверок используйте assertEqual, assertTrue

# TODO: Write tests to test each operation and method of the Mathlist class
# Hint: use assertEqual, assertTrue


test_list = [14, 6, 10.45, 1.0, -7]

class MathListTest(unittest.TestCase):
    def setUp(self):
        self.mathlist1 = MathList(test_list)
        self.mathlist2 = MathList(test_list)

    def test_str(self):
        """тест метода string"""
        self.assertEqual(str(self.mathlist1), 'MathList(14, 6, 10.45, 1.0, -7)')

    def test_len(self):
        """тест метода определения длины объекта"""
        self.assertEqual(len(self.mathlist1), 5)

    def test_sum(self):
        """тест суммы"""
        temp_result = self.mathlist1 + self.mathlist2
        self.assertEqual(temp_result.value,
                         list(map(lambda x: x * 2 , test_list)))

#    def test_sum_another(self):
#        temp_result = self.mathlist1 + self.mathlist2
#        self.assertEqual(str(temp_result),
#                         str(MathList([28, 12, 20.9, 2.0, -14])))

    def test_neg(self):
        """тест унарного минуса"""
        self.assertEqual((-self.mathlist1).value, (list(map(lambda x: -x , test_list))))

    @unittest.skip('имеется аналогичный тест')
    def test_neg_another(self):
        """тест унарного минуса 2"""
        self.assertEqual((-self.mathlist1).value, [-14, -6, -10.45, -1.0, 7])


    def test_sub(self):
        """тест разницы"""
        temp_result = self.mathlist1 - self.mathlist2
        self.assertEqual(temp_result.value, [0, 0, 0, 0, 0])

    def test_mul(self):
        """тест произведения"""
        temp_result = self.mathlist1 * self.mathlist2
        self.assertEqual(temp_result.value, [196, 36, 109.2025, 1.0, 49])

    def test_reverse(self):
        """тест обратной величины"""
        temp_result = MathList.reverse(self.mathlist1)
        self.assertEqual(temp_result.value, [0.0714, 0.1667, 0.0957, 1.0, -0.1429])

    def test_truediv(self):
        """тест разности"""
        temp_result = (self.mathlist1 / self.mathlist2)
        self.assertEqual(temp_result.value, [1, 1, 1, 1, 1])

    def test_add(self):
        """тест добавления элемента в список"""
        self.mathlist1.add(11)
        self.assertEqual(self.mathlist1.value, [14, 6, 10.45, 1.0, -7, 11])

    def test_add_1(self):
        """тест добавления элемента в список
        используя метод assertTrue"""
        self.mathlist1.add(11)
        self.assertTrue(11 in self.mathlist1.value)


    def test_remove_1(self):
        """тест удаления элемента из списка"""
        self.mathlist1.remove(6)
        self.assertEqual(self.mathlist1.value, [14, 10.45, 1.0, -7])

    @unittest.skip('проверка на отсутствие значения в списке')
    def test_remove_2(self):
        self.mathlist1.remove(11)
        self.assertEqual(self.mathlist1.value, [14, 6, 10.45, 1.0, -7])

    def test_update(self):
        """тест расширение списка элементами другого списка"""
        self.mathlist1.update([1, 2, 3])
        self.assertEqual(self.mathlist1.value, [14, 6, 10.45, 1.0, -7, 1, 2, 3])

    def test_check_correct(self):
        """тестирование проверки на тип элемента в списке"""
        with self.assertRaises(ValueError):
            MathList.check_correct([1, 0.3, 's'])

    def test_distance_same_len(self):
        """тестированике определния длины списков одной длины"""
        self.assertEqual(self.mathlist1.distance(self.mathlist2), 0)

    def test_distance_same_len_1(self):
        """тестированике определния длины списков одной длины, с разными значениями"""
        self.mathlist2.remove(-7)
        self.mathlist2.add(3)
        self.assertEqual(self.mathlist1.distance(self.mathlist2), 10)

    def test_distance_(self):
        """тестирование определния длины списков разной длины"""
        with self.assertRaises(NotImplementedError):
            MathList.distance(self.mathlist1.distance(self.mathlist2.add(11)))


if __name__ == '__main__':
    unittest.main()


