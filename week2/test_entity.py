from entity import Entity
from weapon import Weapon
import unittest


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.test_entity = Entity("Gad", 100)

    def test_entity_init(self):
        test_entity = Entity("Gad", 100)
        self.assertEqual(test_entity.name, "Gad")
        self.assertEqual(test_entity.health, 100)

    def test_is_alive(self):
        self.assertTrue(self.test_entity.is_alive())

    def test_get_health(self):
        self.assertEqual(self.test_entity.get_health(), 100)

    def test_take_damage(self):
        self.test_entity.take_damage(30)
        self.assertEqual(self.test_entity.get_health(), 70)

    def test_take_damage_less_than_zero(self):
        self.test_entity.take_damage(200)
        self.assertEqual(self.test_entity.get_health(), 0)

    def test_take_healing(self):
        self.test_entity.take_damage(50)
        self.test_entity.take_healing(20)
        self.assertEqual(70, self.test_entity.get_health())

    def test_take_healing_dead(self):
        self.test_entity.take_damage(150)
        self.assertFalse(self.test_entity.is_alive())

    def test_take_healing_max_health(self):
        self.test_entity.take_damage(30)
        self.assertTrue(self.test_entity.take_healing(50))
        self.assertEqual(self.test_entity.get_health(), 100)

    def test_eqiup_weapon(self):
        weapon = Weapon("hammer", 20, 0.5)
        self.test_entity.equip_weapon(weapon)
        self.assertTrue(self.test_entity.has_weapon())

    def test_attack(self):
        weapon = Weapon("hammer", 20, 0.5)
        self.test_entity.equip_weapon(weapon)
        self.assertEqual(self.test_entity.attack(), 20)

    def test_attack_without_weapon(self):
        weapon = None
        self.test_entity.equip_weapon(weapon)
        self.assertEqual(0, self.test_entity.attack())

if __name__ == '__main__':
    unittest.main()
