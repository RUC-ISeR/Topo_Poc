"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
	middleHost = self.addHost( 'h3' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's5' )
	middleSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftSwitch, middleSwitch )
	self.addLink( middleSwitch, rightSwitch )
        self.addLink( leftHost, leftSwitch )
        self.addLink( rightSwitch, rightHost )
	self.addLink( leftSwitch, middleHost )
	self.addLink( rightSwitch, middleHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }

