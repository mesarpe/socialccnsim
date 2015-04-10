SocialCCNSim
============

Description
-----------
SocialCCNSim is a discrete-event simulator of a CCN network.

Features
--------
 * Simulator of a network of caches
 * Support SONETOR[0] traces
 * Supported Caching Strategies:
    * ProbCache [8]
    * Cache 'Less For More' [7]
    * Leave Copy Everywhere [6]
    * Leave Copy Down
    * MAGIC[5]
    * Rand Copy One
    * Most Popular Caching (MPC) [3]
    * Leave Copy on the Edge
 * Supported replacement policies:
    * Last Recently Used (LRU)
    * First-In First-Out (FIFO)
 * Supported Social Network topologies:
    * Facebook
    * LastFM
    * Every networkx graph can be used as topology, by placing it on the graphs folder.
 * Supported Network Topologies:
    * Abilene
    * GEANT
    * DTELECOM
    * Tiger
    * Tree
    * Diamond
    * Every networkx graph can be used as topology, by placing it on the graphs folder.
 * Implementation of Cache Hit, Stretch, Diversity and Cache Evictions metrics[1]
 * Supports mobility of the users
 * Plugins for new caching strategies
 * Plugins for every new replacement policy

Installation
------------

Typical Ubuntu installation:
```bash
> apt-get install python-networkx python-scipy python-numpy python-pyparsing
> git clone git://github.com/panisson/pymobility.git
> cd pymobility
> python setup.py install (run as admin/root)
> cd ..
```

Using virtualenv:
```bash
> virtualenv .
> source bin/activate
> easy_install networkx
> easy_install numpy
> easy_install scipy
> easy_install pyparsing
> easy_install pymobility
> git clone https://github.com/mesarpe/socialccnsim.git
> cd socialccnsim
```

Dependencies
------------
Networkx, scipy, numpy, pylru[2]

Examples
--------

Execute the trace test_trace in a CCN network with abilene as topology and Leave Copy Everywhere (LCE) as caching strategy.
LRU is used as replacement policy,
Links acquaintances among simulated users is represented with a graph of a Facebook social network.
```bash
> python -O socialccnsim.py 2 lce facebook abilene lru exampletrace/verysmall
```

Contributing
------------
If you have a Github account please fork the repository,
create a topic branch, and commit your changes.
Then submit a pull request from that branch.

License
-------
Written by César Bernardini <mesarpe@gmail.com>  
Copyright (C) 2014 César Bernardini.
You can contact us by email (mesarpe@gmail.com).  

References
----------
[0] Cesar Bernardini, Thomas Silverston, Olivier Festor. SONETOR: a Social Network Traffic Generator. IEEE ICC 2014.

[1] Cesar Bernardini, Thomas Silverston, Olivier Festor. 

[2] https://github.com/jlhutch/pylru

[3] Cesar Bernardini, Thomas Silverston, Olivier Festor. MPC: Popularity-based Caching Strategy for Content Centric Networks. IEEE ICC 2013

[4] Cesar Bernardini, Thomas Silverston, Olivier Festor. Socially-Aware Caching Strategy for Content Centric Networking. IFIP NETWORKING 2014

[5] Ren, Jing, et al. MAGIC: A distributed MAx-Gain In-network Caching strategy in information-centric networks. IEEE INFOCOM NOM WORKSHOP 2014.

[6] Zhang, B., Alexander Afanasyev, Jeffrey Burke, Van Jacobson, Patrick Crowley, Christos Papadopoulos, Lan Wang, and Beichuan Zhang. Named Data Networking. (2010).

[7] Chai, Wei Koong, et al. "Cache “less for more” in information-centric networks." NETWORKING 2012. Springer Berlin Heidelberg, 2012. 27-40.

[8] Psaras, Ioannis, Wei Koong Chai, and George Pavlou. "Probabilistic in-network caching for information-centric networks." Proceedings of the second edition of the ICN workshop on Information-centric networking. ACM, 2012.
