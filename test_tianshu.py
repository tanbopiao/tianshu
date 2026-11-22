"""天枢（TIANSHU）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_register_component_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.register_component(None, None)

    def test_dispatch_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.dispatch(None)


if __name__ == "__main__":
    unittest.main()
