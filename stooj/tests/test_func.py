import unittest

class FuncUnitTests(unittest.TestCase):
    def test_stooj_assert(self):
        from stooj.lib import stooj_assert
        from stooj.exception import StoojInnerError
        stooj_assert(True)
        with self.assertRaises(StoojInnerError) as exc:
            stooj_assert(False)

