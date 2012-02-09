# $File: simple-server.py
# $Author: Jiakai <jia.kai66@gmail.com>
# $Date: Thu Feb 09 11:15:43 2012 +0800
#
# This file is part of pynojo
# 
# pynojo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pynojo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with pynojo.  If not, see <http://www.gnu.org/licenses/>.
#

if __name__ == '__main__':
    print 'initializing...'

    import pynojo
    from wsgiref.simple_server import make_server

    app = pynojo.get_app()
    server = make_server('0.0.0.0', 8080, app)
    print 'server initialized, listening on 8080'
    server.serve_forever()


