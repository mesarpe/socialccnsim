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
import random

class User(object):
    def __init__(self, _id):
        self._id = _id
        self.prob_topics = [0.2, 0.3, 0.5]
        self.topics = [0, 1, 2]
        assert sum(self.prob_topics) == 1
        assert len(self.prob_topics) == len(self.topics)
        
    def decide_next_topic(self):
        return 0

    def is_interesting(self, message_name, topic):
        return random.randint(0, 10) == 0

class UserA(object):
    def __init__(self, _id):
        self._id = _id
        self.topics = {0: 0.2, 1: 0.3, 2:0.5}
        self.aux_rand_topics = []
        for k, v in self.topics.items():
            for i in range(0, int(v*10)):
                self.aux_rand_topics.append(k)
        
        assert sum(self.topics.values()) == 1
        
    def decide_next_topic(self):
        return random.choice(self.aux_rand_topics)

    def is_interesting(self, message_name, topic):
        return topic*random.randint(0,1) == 2
    def __name__(self):
        return 'UserA'

class UserB(object):
    def __init__(self, _id):
        self._id = _id
        self.topics = {2: 0.2, 0: 0.3, 1:0.5}
        self.aux_rand_topics = []
        for k, v in self.topics.items():
            for i in range(0, int(v*10)):
                self.aux_rand_topics.append(k)
        
        assert sum(self.topics.values()) == 1
        
    def decide_next_topic(self):
        return random.choice(self.aux_rand_topics)

    def is_interesting(self, message_name, topic):
        return topic*random.randint(0,1) == 1
    def __name__(self):
        return 'UserB'

class UserC(object):
    def __init__(self, _id):
        self._id = _id
        self.topics = {1: 0.2, 2: 0.3, 0:0.5}
        self.aux_rand_topics = []
        for k, v in self.topics.items():
            for i in range(0, int(v*10)):
                self.aux_rand_topics.append(k)
        
        assert sum(self.topics.values()) == 1
        
    def decide_next_topic(self):
        return random.choice(self.aux_rand_topics)

    def is_interesting(self, message_name, topic):
        return topic+random.randint(0,1) == 0
