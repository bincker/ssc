class ModuleCollection:
    """Organizes collection of modules"""
    __collection_path   = None
    __collection        = {}
    
    def __init__(self, path):
        """ Initialize modules collection
            
            Creates collection dictionary containing:
                __collection[_module category_] = [list of scripts]
                
                e.g. __collection["discovery"]=["dns.py", "tcp.py", ..]
        """
        import os
        import re
        
        self._collection_path = path
        
        # Ignore unwanted files like "__init__.py" and "*.pyc"
        file_excludes = "(^__init__\.py)|(.*\.pyc$)"
        
        # Create collection from initial root path 
        for (root,dirs,files) in os.walk(path, topdown=False):
            # Skip the root path itself
            if not dirs:                       
                scripts = []
                
                # Exclude unwanted files
                for f in files:
                    if not re.match(file_excludes, f):
                        scripts.append(f)
                
                # Extract tail of path from current root    
                head, tail = os.path.split(root)
                self.__collection[tail] = scripts
                
            
    def __len__(self):
        """Returns number of available modules"""
        # FIXME: Return total number of available modules(files)
        return len(self.__collection)
        
    def __iter__(self):
        """ Returns an iterator for the collection"""
        # FIXME: Implement me
        pass
        
    def __next__(self):
        """ Iterates through the collection"""
        # FIXME: Implement me
        pass
        
    def __contains__(self, attr):
        """ Check if collection contains attribute """
        return self.__collection.has_key(attr)
        
    def print_collection(self):
        """ Output collection in a fancy way """
        if self.__collection:
            # TODO: Use some iterator
            #for key,value in self.__collection:
            #    print(self.__collection[key])
            pass
        
