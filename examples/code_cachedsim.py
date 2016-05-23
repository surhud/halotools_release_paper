>>> from halotools.sim_manager import CachedHaloCatalog
>>> halocat = CachedHaloCatalog(simname = 'bolshoi', redshift = 0.5)

>>> print(halocat.halo_table[0:9]) # view the first ten halos in the catalog
>>> print(halocat.Lbox, halocat.particle_mass) # inspect the halo catalog metadata
