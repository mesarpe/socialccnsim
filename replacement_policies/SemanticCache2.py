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
from replacement_policies.Cache import Cache
from externmodules.semantic.virtuoso_webservice import SemanticService

class SemanticCache2(Cache):
    def __init__(self, size, *args, **kargs):
        super(SemanticCache2, self).__init__(size, **kargs)
        self.semantic_service = SemanticService(*args)
        #self.semantic_service.reconfigurate_equation(["0 0 0 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 0 0 0 1", "0 0 1 1 0 0 1 1 0 0 0", "0 1 1 1 0 0 1 0 0 0 1", "0 0 1 1 0 0 0 0 0 0 0", "0 0 1 0 0 0 0 0 0 0 0", "0 0 1 0 0 0 1 0 0 0 0", "0 1 1 1 0 0 1 1 0 0 0", "0 0 1 0 0 0 1 0 0 0 1", "1 0 1 1 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 1 0 0 1", "1 1 1 1 0 0 1 0 0 0 0", "0 0 0 0 0 0 1 0 0 0 0", "0 1 1 1 0 0 0 0 0 0 0", "0 0 1 1 0 0 1 1 1 1 0", "1 0 1 1 0 0 1 0 0 0 1", "0 0 0 1 0 0 0 0 0 0 0", "0 1 1 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 1 0 0 1", "0 0 1 1 0 1 1 1 0 0 0", "0 1 0 1 0 0 1 0 0 0 0", "0 1 1 0 0 0 1 0 0 0 0", "0 0 0 1 0 0 1 0 0 0 0", "0 1 1 1 0 0 1 0 1 0 0", "0 0 1 1 0 0 0 0 0 0 1", "0 0 1 0 0 0 1 1 0 0 0", "1 1 1 1 0 0 1 0 0 0 1", "1 0 1 0 0 0 0 0 0 0 0", "1 0 1 1 0 0 1 1 1 0 0", "1 0 1 1 0 0 1 0 1 0 0", "1 0 1 1 0 0 1 1 0 0 0", "0 0 1 0 0 0 0 0 0 0 1", "0 0 1 1 0 0 1 0 0 1 0", "1 1 0 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 0 0 1 0", "0 0 0 0 0 0 0 1 0 0 0", "1 0 1 1 0 0 1 1 0 0 1", "1 0 1 1 0 0 1 0 1 1 0"])
        # General for all the traces
        self.semantic_service.reconfigurate_equation(["0 0 0 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 0 0 0 0", "0 0 1 0 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 1 0 0 0", "0 0 1 1 0 0 1 0 0 0 1", "0 0 1 1 0 0 0 0 0 0 0", "0 0 1 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 1 0 0 0", "0 1 1 1 0 0 1 0 0 0 1", "0 0 1 0 0 0 1 0 0 0 1", "1 0 1 1 0 0 1 0 0 0 0", "0 1 1 1 0 0 0 0 0 0 0", "0 0 1 1 0 0 1 1 0 0 1", "1 0 1 1 0 0 1 0 0 0 1", "1 1 1 1 0 0 1 0 0 0 0", "0 1 1 1 0 0 1 1 0 0 1", "0 1 1 0 0 0 0 0 0 0 0", "0 0 1 0 0 0 1 1 0 0 0", "0 0 1 1 0 1 1 1 0 0 0", "1 1 1 1 0 0 1 0 0 0 1", "0 0 0 1 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 0 1 0 0", "0 1 1 1 0 0 1 1 1 1 0", "0 0 0 0 0 0 1 0 0 0 0", "0 1 1 0 0 0 1 0 0 0 0", "0 1 0 1 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 1 1 1 0", "1 0 1 1 0 0 1 1 0 0 0", "1 0 1 1 0 0 1 1 1 0 0", "0 0 0 1 0 0 1 0 0 0 0", "0 1 1 1 0 0 1 1 1 0 0", "0 0 1 1 0 0 0 0 0 0 1", "0 0 0 0 0 0 0 0 0 0 1", "0 0 1 0 0 0 0 0 0 0 1", "1 0 1 1 0 0 1 1 0 0 1", "0 0 1 1 0 0 1 0 0 1 0", "1 1 0 1 0 0 1 0 0 0 0", "0 1 1 0 0 0 1 0 0 0 1", "0 0 1 1 1 0 1 0 0 0 0"])
    def accept(self, content_name):
        # it can be implemented as a web service
        #f = urllib2.urlopen('http://127.0.0.1:4001/?name={0}'.format(urllib.quote_plus(content_name)))
        #res = f.read(4)
        #return res == 'True'
        return self.semantic_service.resolve_name(content_name)
