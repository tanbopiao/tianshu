"""天枢（TIANSHU）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from tianshu import Tianshu


class TestTianshu(unittest.TestCase):
    def setUp(self):
        self.op = Tianshu()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "tianshu")
        self.assertEqual(d["code"], "TIANSHU")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_dispatch(self):
        self.op.register_component("算件甲", lambda p: p * 2)
        self.assertEqual(self.op.dispatch({"component": "算件甲", "payload": 21}), 42)
        with self.assertRaises(KeyError):
            self.op.dispatch({"component": "无有"})


if __name__ == "__main__":
    unittest.main()
