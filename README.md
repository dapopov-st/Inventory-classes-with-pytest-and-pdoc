This is an inventory application for a tech video channel featuring computer builds.
The channel has a pool of inventory, (for example 5 x AMD Ryzen 2-2700 CPUs) used for builds.
When a CPU is taken from the pool, it will be indicated using the object that tracks that 
specific type of CPU. The channel may also purchase additional CPUs, or retire some.

The base class is a general Resource. This class provides functionality common to all of the resources (CPU, GPU, Memory, HDD, SSD).  Please see the [Documentation](https://dapopov-st.github.io/Inventory-classes-with-pytest-and-pdoc/#Resources.category) to learn about the available methods.

The tests are performed with Pytest.  To run these, navigate to the root project directory and type 
```bash 
pytest 
``` 
in a shell.

Documentation can be generated at the command line by running
```bash 
pip install pdoc
``` 
(if not already installed), then
```bash 
pdoc resources.py 
```
from computer_builds/models directory

To run the a Docker container, git clone this repository, navigate into it,  and run 
```bash 
docker build -t inventory .
```
then
```bash 
docker run inventory 
```


[Documentation](https://dapopov-st.github.io/Inventory-classes-with-pytest-and-pdoc/#Resources.category)
<br/>The directory structure is below. The `__init__.py` files are not strictly necessary, but help with pytest and pdoc usage.

![alt text](https://github.com/dapopov-st/Inventory-classes-with-pytest-and-pdoc/blob/main/directory_tree.png?raw=true)

Many thanks to Fred [Baptiste](https://www.udemy.com/user/fredbaptiste/) for problem description and teaching many of the necessary techniques

