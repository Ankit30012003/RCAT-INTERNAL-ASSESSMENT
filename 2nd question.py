import time

def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time} seconds")
        return result
    return wrapper

@execution_time_logger
def example_function(n):
    time.sleep(n)
  
example_function(3)

"""
output:-  Function 'example_function' executed in 3.0031821727752686 seconds
"""
