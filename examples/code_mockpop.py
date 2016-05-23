>>> from halotools.sim_manager import CachedHaloCatalog
>>> halocat = CachedHaloCatalog(simname = 'bolshoi', redshift = 0)

>>> from halotools.empirical_models import PrebuiltHodModelFactory
>>> model = PrebuiltHodModelFactory('leauthaud11')

>>> model.populate_mock(halocat)
>>> print(model.mock.galaxy_table[0:9]) # view the first ten galaxies in the catalog
