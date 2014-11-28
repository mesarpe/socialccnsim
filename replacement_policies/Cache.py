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
import externmodules.pylru as pylru

class Cache(object):
    def __init__(self, size, **args):
        assert size > 0
        self._store = pylru.lrucache(size)
        self.max_size = size
        self.args = args
    def accept(self, content_name):
        return True
    def remove(self, content_name):
        del self._store[content_name]
    def keys(self):
        return self._store.keys()
    def lookup(self, content_name):
        try:
            return self._store.peek(content_name)
        except KeyError:
            return False
    def store(self, content_name):
        if len(self._store) < self.max_size:
            self._store[content_name] = True
        else:
            if self.accept(content_name):
                self._store[content_name] = True
            else:
                return False
        return True
    def __iter__(self):
        return self._store.__iter__()
    def __len__(self):
        return self._store.__len__()
