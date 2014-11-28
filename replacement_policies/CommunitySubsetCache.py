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
from replacement_policies.SubsetCache import SubsetCache

class CommunitySubsetCache(SubsetCache):
    #Only accept content from the same community
    def __init__(self, size, **args):
        
        social_users_in_node = args['users']

        nodes_ = {}
        
        comu = []
        for n in social_users_in_node:
            comu.append(args['partition'][int(n)])

        #We get all the users in the same community
        for k,v in args['partition'].items():
            if v in comu:
                nodes_[str(k)] = k

        SubsetCache.__init__(self, size, subset=nodes_)
