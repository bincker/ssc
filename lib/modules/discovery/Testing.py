from ModuleBase import ModuleBase as Base

class Testing(Base):
    """Some dummy module"""
    
    # Define/Init parameters
    # Better use params parser!
    
    def usage(self):
        print("This is the usage\n")

    def get_parameters(self):
        print("This are the parameters\n")
        
    def read_parameters(self, input):
        from collections import defaultdict
        
        d = defaultdict(list)
        for i in input.split(","):
            k,v = i.split("=")
            d[k].append(v)
        return d
    
    def stop(self):
        pass
        
    def start(self):
        pass
        
