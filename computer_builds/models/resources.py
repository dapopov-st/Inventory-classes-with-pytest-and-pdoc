from computer_builds.utils.validators import set_if_valid_string, set_if_valid_int, set_if_valid_cores

"""
Inventory application for a tech video channel featuring computer builds.
Channel has a pool of inventory, (for example 5 x AMD Ryzen 2-2700 CPUs) used for builds.
When a CPU is taken from the pool, it will be indicated using the object that tracks that 
specific type of CPU. Channel may also purchase additional CPUs, or retire some.
"""


class Resources:
    """Resources base class"""

    def __init__(self, name, manufacturer, total, allocated):
        """
        Args:
           name (str): user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
           manufacturer (str): resource instance manufacturer (e.g. `Nvidia`)
           total (int): inventory total (how many are in the inventory pool)
           allocated (int): number allocated (how many are already in use), must be smaller than total
        """
        self._name = set_if_valid_string(name)
        self._manufacturer = set_if_valid_string(manufacturer)
        self._total = set_if_valid_int(total)
        # Initial allocated cannot be bigger than the total
        if self._total - set_if_valid_int(allocated) >= 0:
            self._allocated = set_if_valid_int(allocated)
        else:
            raise ValueError

    # Total and allocated should be read-only
    # modifiable through the various methods such as `claim`, `return`, `died` and `purchased`
    @property
    def total(self):
        """
        Returns:
            total (int): total amount of resource
        """
        return self._total

    @property
    def allocated(self):
        """
        Returns:
            allocated (int): amount of allocated resource
        """
        return self._allocated

    # name and manufacturer should be read-only
    @property
    def name(self):
        """
            Returns:
                name(str):resource name
        """
        return self._name

    @property
    def manufacturer(self):
        """
            Returns:
                manufacturer(str):resource manufacturer
        """
        return self._manufacturer

    def __repr__(self) -> str:
        return (f"\nResource: {self.name}\nManufacturer: {self.manufacturer}\nTotal available: {self.total}\n" +
                f"Allocated resource: {self._allocated}")

    def __str__(self) -> str:
        return self._name

    def claim(self, n):
        """
        Claim n inventory items if available
        Args:
            n(int): number of items to claim
        Returns:
            None
        """
        if self._total - n >= 0:
            self._allocated += set_if_valid_int(n)
        else:
            raise ValueError(
                "Allocated resources cannot exceed total resources")

    def freeup(self, n):
        """
        Free up n items if possible
        Args:
            n(int): number of items to free up
        Returns:
            None
        """
        if self._allocated - n >= 0:
            self._allocated -= set_if_valid_int(n)
        else:
            raise ValueError(
                "Cannot free up more resources than allocated")

    def died(self, n):
        """
        Subtract n items from total and allocated (if possible)
        Args:
            n(int): number of items to subtract
        Returns:
            None
        """
        if set_if_valid_int(self.total - set_if_valid_int(n)):
            self._total -= set_if_valid_int(n)
            self._allocated -= set_if_valid_int(n)

    def purchased(self, n):
        """
        Add n items to the total 
        Args:
            n(int): number of items to add
        Returns:
            None
        """
        if set_if_valid_int(n):
            self._total += set_if_valid_int(n)

    @property
    def category(self):
        """
            Returns:
                category(str):resource category
        """
        return (str(type(self)).split(".")[-1][:-2]).lower()


class CPU(Resources):
    """Resources subclass class for tracking CPU inventory"""

    # cores num is even and ranging from 2 to 100
    cores = [i*2 for i in range(1, 51)]

    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        """
        Args:
           name (str): user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
           manufacturer (str): resource instance manufacturer (e.g. `Nvidia`)
           total (int): inventory total (how many are in the inventory pool)
           allocated (int): number allocated (how many are already in use), must be smaller than total
           cores (int): number of cores is even and ranges from 2 to 100 (e.g. `8`)
           socket (str): socket (e.g. `AM4`)
           power_watts (int): number of watts (e.g. `94`)

        """
        super().__init__(name, manufacturer, total, allocated)
        self._cores = set_if_valid_cores(cores)
        self._socket = set_if_valid_string(socket)
        self._power_watts = set_if_valid_int(power_watts)

    @property
    def cores(self):
        """
            Returns:
                cores (int): number of cores is even and ranges from 2 to 100 (e.g. `8`)
        """
        return self._cores

    @cores.setter
    def cores(self, val):
        self._cores = set_if_valid_cores(val)

    @property
    def socket(self):
        """
            Returns:
                socket (str): socket (e.g. `AM4`)
        """
        return self._socket

    @socket.setter
    def socket(self, val):
        self._socket = set_if_valid_string(val)

    @property
    def power_watts(self):
        """
            Returns:
                power_watts (int): number of watts (e.g. `94`)

        """
        return self._power_watts

    @power_watts.setter
    def power_watts(self, val):
        self._power_watts = set_if_valid_int(val)

    def __repr__(self):
        inherited = super().__repr__()
        return f"{inherited}\nCores: {self._cores}\nSocket:{self._socket}\nPower watt:{self._power_watts}"


class GPU(Resources):
    """GPU class inheriting from base Resources class without modifications"""

    def __init__(self, name, manufacturer, total, allocated):
        """
        Args:
           name (str): user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
           manufacturer (str): resource instance manufacturer (e.g. `Nvidia`)
           total (int): inventory total (how many are in the inventory pool)
           allocated (int): number allocated (how many are already in use), must be smaller than total
        """
        super().__init__(name, manufacturer, total, allocated)


class Storage(Resources):
    """Intermediate Resources subclass with GB capacity"""

    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        """
          Args:
           name (str): user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
           manufacturer (str): resource instance manufacturer (e.g. `Nvidia`)
           total (int): inventory total (how many are in the inventory pool)
           allocated (int): number allocated (how many are already in use), must be smaller than total
           capacity_GB (int): storage capacity in gigabytes (e.g. `120`)

        """
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        """
        Returns:
            capacity_GB (int): storage capacity in gigabytes (e.g. `120`)

        """
        return self._capacity_GB

    @capacity_GB.setter
    def capacity_GB(self, val):
        self._capacity_GB = set_if_valid_int(val)

    def __repr__(self):
        inherited = super().__repr__()
        return f"{inherited}\nCapacity in GB: {self._capacity_GB}"


class HDD(Storage):
    """Storage subclass with size and rpm"""

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        """
          Args:
           name (str): user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
           manufacturer (str): resource instance manufacturer (e.g. `Nvidia`)
           total (int): inventory total (how many are in the inventory pool)
           allocated (int): number allocated (how many are already in use), must be smaller than total
           capacity_GB (int): storage capacity in gigabytes (e.g. `120`)
           size (str): storage size (e.g. ``2.5"``)
           rpm (int): HDD's rpm count (e.g. `7000`)


        """
        super().__init__(name, manufacturer, total,
                         allocated, capacity_GB)
        self._size = set_if_valid_string(size)
        self._rpm = set_if_valid_int(rpm)

    @property
    def size(self):
        """
        Returns:
            size (str): storage size (e.g. ``2.5"``)

        """
        return self._size

    @size.setter
    def size(self, val):
        self._size = set_if_valid_string(val)

    @property
    def rpm(self):
        """
        Returns:
            rpm (int): HDD's rpm count (e.g. `7000`)

        """
        return self._rpm

    @rpm.setter
    def rpm(self, val):
        self._rpm = set_if_valid_int(val)

    def __repr__(self):
        inherited = super().__repr__()
        return f"{inherited}\nSize: {self._size}\nrpm:{self._rpm}"


class SSD(Storage):
    """Storage subclass with interface"""

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        """
          Args:
           name (str): user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
           manufacturer (str): resource instance manufacturer (e.g. `Nvidia`)
           total (int): inventory total (how many are in the inventory pool)
           allocated (int): number allocated (how many are already in use), must be smaller than total
           capacity_GB (int): storage capacity in gigabytes (e.g. `120`)
           interface (str): SSD's interface (e.g. `PCIe NVMe 3.0 x4`)


        """
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface

    @property
    def interface(self):
        """
        Returns:
            interface (str): SSD's interface (e.g. `PCIe NVMe 3.0 x4`)

        """
        return self._interface

    @interface.setter
    def interface(self, val):
        self._interface = set_if_valid_string(val)

    def __repr__(self):
        inherited = super().__repr__()
        return f"{inherited}\nInterface: {self._interface}"
