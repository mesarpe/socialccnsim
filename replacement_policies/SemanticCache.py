#####################################################################
#SocialCCNSim, a simulator of caches for Content Centric Networking.
#
#Developed by Cesar A. Bernardini Copyright (C) 2014.
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Library General Public
#License as published by the Free Software Foundation; either
#version 2 of the License, or (at your option) any later version.
#
#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#Library General Public License for more details.
#
#You should have received a copy of the GNU Library General Public
#License along with this library; if not, write to the
#Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
#Boston, MA  02110-1301, USA. 
#
#####################################################################
import operator
import urllib
import urllib2

from replacement_policies.Cache import Cache

class SemanticCache(Cache):
    def accept(self, content_name):
        try:
            name = content_name.split('/')[2:-1]
        except:
            return False
        ret = False
        for component in name:
            f = urllib2.urlopen('http://127.0.0.1:4000/?name={0}'.format(urllib.quote_plus(component)))
            res = f.read(100)
            ret = operator.or_(ret, res == 'True')
            if ret:
                break
        return ret
