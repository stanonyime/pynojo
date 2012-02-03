# $File: xgettext-pt.py
# $Date: Fri Feb 03 13:41:50 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

KEY = '_'
KEY_PL = '_pl'

from chameleon.zpt.template import PageTemplateFile
from chameleon.tales import PythonExpr
import ast

def extract_msg(source):
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call) and \
                isinstance(node.func, ast.Name):
            if node.func.id == KEY:
                arg = node.args[0]
                assert isinstance(arg, ast.Str)
                arg = arg.s
                print "{0}({1!r})" . format(KEY, arg)
            elif node.func.id == KEY_PL:
                args = node.args[:2]
                for i in args:
                    assert isinstance(i, ast.Str)
                print "{0}({1!r}, {2!r})" . format(KEY_PL,
                        args[0].s, args[1].s)

class XgettextPythonExpr(PythonExpr):
    def parse(self, string):
        extract_msg(string)
        return super(self.__class__, self).parse(string)


PageTemplateFile.expression_types['python'] = XgettextPythonExpr

if __name__ == '__main__':
    try:
        while True:
            fname = raw_input()
            print '#', fname
            template = PageTemplateFile(fname)
            template.cook_check()
    except EOFError:
        pass

