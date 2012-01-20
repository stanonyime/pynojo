# $File: index.py
# $Date: Fri Jan 20 10:56:39 2012 +0800
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

from pyramid.view import view_config
from ..func import mkroute

@view_config(route_name = mkroute(pattern = ''), renderer = 'template/index.pt')
def _index(request):
    return {'msg': request._('msgfrompython')}

