import computer_builds
from computer_builds.utils.validators import set_if_valid_string, set_if_valid_int, set_if_valid_cores
from computer_builds.models.resources import Resources, CPU, GPU, Storage, HDD, SSD
if __name__ == "__main__":
    r1 = Resources(name='Intel Core i9-9900K',
                   manufacturer='Nvidia', total=10, allocated=5)
    print(r1)
    print(r1.__repr__())
    r1.claim(2)
    print(r1.allocated)
    r1.died(1)
    print(r1.total)
    r1.purchased(5)
    print(r1.total)
    print(r1.category)
    print("______________________________________________________")

    gpu1 = GPU(name='GIntel Core i9-9900K',
               manufacturer='GNvidia', total=100, allocated=50)
    print(gpu1.category)
    print("______________________________________________________")
    cpu1 = CPU(name='CIntel Core i9-9900K', manufacturer='CNvidia',
               total=10_000, allocated=5_000, cores=16, socket='AM4', power_watts=94)
    print(cpu1.category)
    print(cpu1.__repr__())
    print("______________________________________________________")

    store1 = Storage(name='CIntel Core i9-9900K', manufacturer='CNvidia',
                     total=10_000, allocated=5_000,   capacity_GB=520)
    print(store1.category)
    hdd1 = HDD(name='CIntel Core i9-9900K', manufacturer='CNvidia',
               total=10_000, allocated=5_000,   capacity_GB=520, size='2.5"', rpm=7000)
    print(hdd1.category)
    print(hdd1.__repr__())
    print("______________________________________________________")

    ssd1 = SSD(name='CIntel Core i9-9900K', manufacturer='CNvidia',
               total=10_000, allocated=5_000,   capacity_GB=520, interface="PCIe NVMe 3.0 x4")
    print(ssd1.category)
    print(ssd1.__repr__())
