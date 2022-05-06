Inventory application for a tech video channel featuring computer builds.
Channel has a pool of inventory, (for example 5 x AMD Ryzen 2-2700 CPUs) used for builds.
When a CPU is taken from the pool, it will be indicated using the object that tracks that 
specific type of CPU. Channel may also purchase additional CPUs, or retire some.

The tests are performed with Pytest.
Documentation can be generated at the command line by running
pdoc resources.py from computer_builds directory

![alt text](https://github.com/dapopov-st/Inventory-classes-with-pytest-and-pdoc/blob/[branch]/directory_struct.jpg?raw=true)

Inheritance_Project
├── Project\ 3\ -\ Description.ipynb
├── computer_builds
│   ├── __init__.py
│   ├── models
│   │   └── resources.py
│   ├── tests
│   │   ├── test_cpu.py
│   │   ├── test_gpu.py
│   │   ├── test_hdd.py
│   │   ├── test_resources.py
│   │   ├── test_ssd.py
│   │   ├── test_storage.py
│   │   └── test_validators.py
│   └── utils
│       └── validators.py
├── conftest.py
└── main.py
