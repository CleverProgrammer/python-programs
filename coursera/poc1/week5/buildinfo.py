class BuildInfo:
    """
    Class to track build information.
    """
    
    def __init__(self, build_info = None, growth_factor = BUILD_GROWTH):
        """
        Initialize the BuildInfo object. Use default arguments for the game.
        """
            
    def build_items(self):
        """
        Get a list of buildable items sorted by name.
        """
            
    def get_cost(self, item):
        """
        Get the current cost of an item.
        Will throw a KeyError exception if item is not in the build info.
        """
    
    def get_cps(self, item):
        """
        Get the current CPS of an item
        Will throw a KeyError exception if item is not in the build info.
        """
    
    def update_item(self, item):
        """
        Update the cost of an item by the growth factor
        Will throw a KeyError exception if item is not in the build info.
        """
        
    def clone(self):
        """
        Return a clone of this BuildInfo
        """