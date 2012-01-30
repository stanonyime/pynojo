import unittest

class FuncUnitTests(unittest.TestCase):
    def test_Const(self):
        from ..lib import Const
        c = Const()
        c.x = 0
        self.assertEqual(c.x, 0)
        with self.assertRaises(Const.ConstError) as exc:
            c.x = 0
        self.assertTrue('const x' in str(exc.exception))

    def test_stooj_assert(self):
        from ..lib import stooj_assert
        from ..exception import StoojInnerError
        stooj_assert(True)
        with self.assertRaises(StoojInnerError) as exc:
            stooj_assert(False)

