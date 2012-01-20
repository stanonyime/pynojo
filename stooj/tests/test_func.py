import unittest

class ConstUnitTests(unittest.TestCase):
    def test_it(self):
        from ..func import Const
        c = Const()
        c.x = 0
        self.assertEqual(c.x, 0)
        with self.assertRaises(Const.ConstError) as exc:
            c.x = 0
        self.assertTrue('const x' in repr(exc.exception))
