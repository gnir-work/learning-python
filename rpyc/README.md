# Writing your own rpyc 
## What is an RPYC
_From Wikipedia_: RPyC, or Remote Python Call, is a Python library for remote procedure calls, as well as distributed computing. Unlike regular RPC mechanisms, such as ONC RPC, CORBA or Java RMI, RPyC is transparent, symmetric, and requires no special decoration or definition languages - [read more here](https://en.wikipedia.org/wiki/RPyC).

To make it a little more clear - We want to allow users to feel as if they are running the code
locally but in practice the code will be executed on a different server.

Let's take this example:  
We have a central server with a lot of CPU and GPU resources.  
That server is already running our rpyc server.  
All an employ needs to do in order to run a specific function on that server is: 
```python
from our_cool_rpyc_client import connect

def some_super_heavy_and_long_function(*args, **kwargs):
    # Do some shit.

if __name__ == "__main__":
    connection = connect("bamba:1227")
    remote_func = connection.teleport(some_super_heavy_and_long_function)
    remote_func(arg1, arg2, arg3, ...) # This will run on the remote
```

## What are you supposed to do?
You need to implement your own version of rpyc!  
I know its scary and unclear, but we will help you along the way.  
Soo Lets get started :)

### The basics
Let's think what are the basic building blocks we need in order for us to be
able to successfully implement a rpyc module:
1. A server - We will probably need to implement some kind of server that the client will connect to.
2. A client - Probably a python package that our users will import and will be their interface to the server.

### Start from the simple stuff
There is no doubt that teleporting a function to the remote server is awesome as shit.  
However before we go an implement all that crazy stuff lets start with the basic.

#### First Iteration
Allow importing already installed modules and calling their function with __basic literal types__.  
For example:
```python
from our_cool_rpyc_client import connect

if __name__ == "__main__":
    connection = connect("bamba:1227")
    remote_math = connection.modules.math # Will access the remotes site packages, not the local ones.
    result = remote_math.pow(3, 2) # Will run on remote 
    print(result) # Will print 9
    remote_func(arg1, arg2, arg3, ...) # This will run on the remote
```

Lets define the requirements a little better:  
1. You will be able to connect to the server via host name
2. You will have access to all the modules on the remote server.
3. Currently, you will only allow passing basic data types (`int`, `str`, `boolean`, ...).
4. You will also support accessing variables with basic data types from the modules, for example `os.path.sep`.
5. Currently, you cannot assign or mutate the state on the remote, but it may be a request in feature iterations.

Good Luck :)





