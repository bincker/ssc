#! /usr/bin/env python

import sys
import argparse
import argparse
#from ModuleBase import ModuleBase as Base


class ICMP():
    
    def __init__(self):
        """ FIXME: Describe here """
        
        # Check out http://docs.python.org/dev/library/argparse.html#argumentparser-objects
        # for full arguments
        self.parser = argparse.ArgumentParser(
            description="Send ICMP packets to some destination"
        )
        
        # Define CMP arguments
        icmp_parser = self.parser.add_argument_group('ICMP')
        icmp_parser.add_argument('--icmp-type', '-t', action='store', dest='icmp_type',
                            type=int, required=True, help='Set ICMP type')

        icmp_parser.add_argument('--icmp-code', '-c', action='store', dest='icmp_code',
                            type=int, required=True, help='Set ICMP code')
                            
        icmp_parser.add_argument('--icmp-payload', '-p', action='store', dest='icmp_payload',
                            type=str, help='Set ICMP payload/data')
                            
        icmp_parser.add_argument('--icmp-unused', '-u', action='store', dest='icmp_unused',
                            type=str, help='Set ICMP header field "unused"')

        # Define here other arguments
        misc_parser = self.parser.add_argument_group('Misc')
        misc_parser.add_argument('--dest', '-d', action='store', dest='icmp_dst',
                            type=str, required=True, help='Set destination (IP/host)')

        # Optional arguments
        self.parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')


    def run(self):
        from scapy.all import sr1,IP,ICMP
        
        target  = self.args['icmp_dst']
        data    = self.args['icmp_payload']
        unused  = self.args['icmp_unused']
        ip      = IP(dst=self.args['icmp_dst'])
        icmp    = ICMP(type=self.args['icmp_type'], 
                       code=self.args['icmp_code'],
                       unused=self.args['icmp_unused']
        ) 
        
        # Create ICMP packet(s) to send
        p=sr1(ip/icmp/data)
        if p:
            p.summary() 
        
    def usage(self):
        self.parser.print_usage()
        
    def read_parameters(self, params_source):
        if len(params_source)==0:
            self.usage()
            sys.exit(1)
        else:
            self.args = vars(self.parser.parse_args(params_source))
        
        
        
if __name__ == '__main__':
    myICMP = ICMP()
    myICMP.read_parameters(sys.argv[1:])
    myICMP.run()
