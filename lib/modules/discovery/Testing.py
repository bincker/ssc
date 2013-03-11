from ModuleBase import ModuleBase as Base

class Testing(Base):
    """Some dummy module"""
    
    def output_usage(self):
        print("This is the usage\n")

    def output_parameters(self):
        print("This are the parameters\n")
        
    def read_parameters(self, input):
        from collections import defaultdict
        
        d = defaultdict(list)
        for i in input.split(","):
            k,v = i.split("=")
            d[k].append(v)
        return d
        
