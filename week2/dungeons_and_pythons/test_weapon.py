from weapon import Weapon
import unittest


class TestWeapon(unittest.TestCase):
    def test_weapon_init(self):
        test_weapon = Weapon("axe", 20, 0.2)
        self.assertEqual(test_weapon.type, "axe")
        self.assertEqual(test_weapon.damage, 20)
        self.assertEqual(test_weapon.critical_strike_percent, 0.2)

    def test_critical_hit(self):
        test_weapon = Weapon("axe", 20, 0.2)
        is_False = False
        is_True = False
        for i in range(100):
            if test_weapon.critical_hit():
                is_True = True
            else:
                is_False = True
        self.assertTrue(is_True)
        self.assertTrue(is_False)

if __name__ == '__main__':
    unittest.main()
