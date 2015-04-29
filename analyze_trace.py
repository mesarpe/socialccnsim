import argparse
import networkx
import random
import re

from topology_manager import TopologyManager

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Analyze trace file simulating the placement of the nodes.')
    #parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                   help='an integer for the accumulator')
    parser.add_argument('--trace-file', required=True, action='store',
                       help='trace file to analyze')
    parser.add_argument('--topology', required=True, action='store',
                       help='topology where the users are located into.')
    parser.add_argument('--social-topology', required=True, action='store',
                       help='connections between users.')
    parser.add_argument('--mapping', required=True, action='store',
                       help='mapping algorithm between social-users and topology nodes.')
    parser.add_argument('--central-repository', dest='central_repository', action='store_true')
    

    args = parser.parse_args()

    print args

    # Load important graphs
    topology_graph = getattr(__import__('graphs.%s'%args.topology), args.topology).G
    social_graph = getattr(__import__('graphs.%s'%args.social_topology), args.social_topology).G

    topology_coords = {}
    for node in topology_graph.nodes():
        topology_coords[node] = (
                random.randint(0, 100),
                random.randint(0, 100)
        )

    #Initialize TopologyManager
    manager = TopologyManager(topology_graph, social_graph, topology_coords, enable_mobility = False, topology_file=args.topology)
    manager.set_method(args.mapping)
    manager.update_all_users_position()

    #Run topology: initialization
    nodes_in_path = {}
    for node in topology_graph.nodes():
        nodes_in_path[int(node)] = {}
        for position in range(len(topology_graph.nodes())):
            nodes_in_path[int(node)][position] = 0

    #Run topology
    content = {}
    seq_file = file(args.trace_file, 'r')
    line = seq_file.readline()
    while line != '': #Empty line, we reach the end of the sequence
        result = re.match ("(?P<timestamp>[0-9]*\.[0-9]+)\t(?P<activity>Retrieve|Publish|retrieve|publish|Retrievecontent|Publishcontent)\t(?P<user>[0-9]+)\t\((?P<dependent>.*)\)\t\((?P<mobility_x>[0-9\.]*), ?(?P<mobility_y>[0-9\.]*)\)", line)
        if result != None:

            if result.group('activity').lower() in ['publishcontent', 'publish']:
                content[result.group('dependent').split(',')[0] ] = int(result.group('user'))
                #
            elif result.group(2).lower() in ['retrieve', 'retrievecontent']:
                src = int(result.group('user'))
                if central_repository:
                    dst = 0
                else:
                    dst = content[result.group('dependent').split(',')[0]]

                path = manager.get_path(src, dst)
                for i in range(0, len(path)):
                    user = path[i]
                    position = i
                    
                    nodes_in_path[user][position] += 1

        else:
            print "repr line: %s"%repr(line)
            exit(-1)
        line=seq_file.readline()
        

    #Print results
    for node in topology_graph.nodes():
        print node,
        for position in range(len(topology_graph.nodes())):
            print nodes_in_path[node][position],
        print
