from abc import ABCMeta, abstractmethod

class ModuleBase(metaclass=ABCMeta):
    """
    Abstract class for inner structure of a module
    Defines abstract methodes which _have_ to be implemented by the 
    modules subclassing/inheriting this class.
    """

    """ Define here abstract methods """
    
    @abstractmethod
    def output_usage(self):
        """Output information how to use the module"""
        pass

    @abstractmethod
    def output_parameters(self, output, data):
        """Output parameters used by the module"""
        pass
        
    @abstractmethod
    def read_parameters(self, input):
        """Read parameters from input and return dictionary"""
        pass
        
