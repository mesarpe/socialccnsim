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
import threading

class FifoCache(Cache):
    def __init__(self, size, **args):
        assert size > 0
        self.lock = threading.Lock()
        self._store = {}
        self._fifo = deque([])
        self.max_size = size
    def lookup(self, content_name):
        res = False
        try:
            self.lock.acquire()
            res = self._store[content_name]
        except KeyError:
            res = False
        finally:
            self.lock.release()
        return res
    def store(self, content_name):
        res = True
        if len(self._store) < self.max_size:
            self.lock.acquire()
            if not self._store.has_key(content_name):
                self._fifo.append(content_name)
            self._store[content_name] = True
            self.lock.release()
        else:
            if self.accept(content_name):
                self.lock.acquire()
                del self._store[self._fifo.popleft()]
                if not self._store.has_key(content_name):
                    self._fifo.append(content_name)
                self._store[content_name] = True
                self.lock.release()
            else:
                res = False
        return res
