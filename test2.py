def my_decorator(fonction):
    """This is our decorator : it displays a message before calling the
    decorated function"""
    
    def modified_function():
        """This is the function returned by the decorator.
        
        It is actually a modified version of the original function,
        which displays a message before calling the original function."""
        
        print("Let's call {0}...".format(fonction))
        return fonction()
    return modified_function

@my_decorator
def hello():
    print("Hello !")
    
hello()