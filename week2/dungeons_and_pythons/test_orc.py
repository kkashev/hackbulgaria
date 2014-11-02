from orc import Orc
from weapon import Weapon
import unittest


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.gad_orc = Orc("Gad", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.gad_orc.berserk_factor, 1.5)

    def test_attack(self):
        weapon = Weapon("tree", 10, 0.5)
        self.gad_orc.equip_weapon(weapon)
        self.assertEqual(self.gad_orc.attack(), 15)


if __name__ == '__main__':
    unittest.main()
