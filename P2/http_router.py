# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler


    def insert(self, path, handler):
        # Recursively add nodes
        current_node = self.root
        for path_block in path:
            current_node.insert(path_block)
            current_node = current_node.children[path_block]
        
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path_block in path:
            if path_block in current_node.children:
                current_node = current_node.children[path_block]
            else:
                return None
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, path_block):
        # Insert the node as before
        if path_block not in self.children:
            self.children[path_block] = RouteTrieNode()
        else:
            pass

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, non_found_handler):
        # Create a new RouteTrie for holding our routes
        self.router = RouteTrie(root_handler)
        self.non_found_handler = non_found_handler

    def add_handler(self, raw_path, handler):
        # Add a handler for a path
        path = self.split_path(raw_path)
        self.router.insert(path, handler)


    def lookup(self, raw_path):
        # lookup path (by parts) and return the associated handler
        path = self.split_path(raw_path)
        if len(path) <= 0:
            return self.router.handler

        if self.router.find(path) is None:
            return self.non_found_handler
        else:
            return self.router.find(path)

    def split_path(self, raw_path):
        # split the path into parts for both the add_handler and loopup functions,
        result_temp = raw_path.split('/')
        return [element for element in result_temp if element != '']

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one