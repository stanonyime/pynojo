import unittest

from pyramid.events import (subscriber, BeforeRender)

_layout_macro = None
@subscriber(BeforeRender)
def _add_global(event):
    from ..i18n import translators    # XXX
    from pyramid.renderers import get_renderer
    global _layout_macro
    if _layout_macro is None:
        _layout_macro = get_renderer('template/layout.pt').implementation()
    event['layout'] = _layout_macro
    event['_'] = translators


from ..func import *
from pyramid.view import view_config

class View:
    @view_config(route_name = mkroute(pattern = '/index'), renderer = 'template/index.pt')
    def method(self):
        return {'msg' : self._('msgfrompython')}

    def __init__(self, request):
        self._ = request._

class ViewUnitTests(unittest.TestCase):

    def setUp(self):
        from webtest import TestApp
        from pyramid.config import Configurator
        from ..i18n import init
        config = Configurator()
        setup_pyramid_route(config)
        config.scan()
        init(config)
        self.app = TestApp(config.make_wsgi_app())

    def check_occur(self, path, val):
        res = self.app.get(path, status = 200)
        for i in val:
            self.assertTrue(i in res.body)

    def test_it(self):
        self.check_occur('/index', ['msgfrom' + i for i in (
            'layout0', 'layout1', 'template', 'python')])

