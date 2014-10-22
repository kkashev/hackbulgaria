from orc import Orc
import unittest


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.gad_orc = Orc("Gad", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.gad_orc.berserk_factor, 1.5)


if __name__ == '__main__':
    unittest.main()
