# -*- coding: utf-8 -*-
# $File: xgettext-pt.py
# $Date: Tue Jan 31 13:16:34 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

KEY = '_'

from chameleon.zpt.template import PageTemplateFile
from chameleon.tales import PythonExpr
import ast

def extract_msg(source):
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call) and \
                isinstance(node.func, ast.Name) and \
                node.func.id == KEY:
            arg = node.args[0]
            assert isinstance(arg, ast.Str)
            arg = arg.s
            print "{0}({1!r})" . format(KEY, arg)

class XgettextPythonExpr(PythonExpr):
    def parse(self, string):
        extract_msg(string)
        return super(self.__class__, self).parse(string)


PageTemplateFile.expression_types['python'] = XgettextPythonExpr

if __name__ == '__main__':
    try:
        while True:
            template = PageTemplateFile(raw_input())
            template.cook_check()
    except EOFError:
        pass

