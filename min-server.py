# $File: min-server.py
# $Author: Jiakai <jia.kai66@gmail.com>
# $Date: Sun Jan 29 11:22:52 2012 +0800
#
# This file is part of stooj
# 
# stooj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# stooj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with stooj.  If not, see <http://www.gnu.org/licenses/>.
#

import stooj

from wsgiref.simple_server import make_server

if __name__ == '__main__':
    print 'initializing...'
    app = stooj.get_app()
    server = make_server('0.0.0.0', 8080, app)
    print 'server initialized, listening on 8080'
    server.serve_forever()


