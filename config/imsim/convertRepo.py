import os.path

from lsst.obs.base.gen2to3 import ConvertRepoSkyMapConfig

config.skyMaps["DC2"] = ConvertRepoSkyMapConfig()
config.skyMaps["DC2"].load(os.path.join(os.path.dirname(__file__), "..", "makeSkyMap.py"))
# If there's no skymap in the root repo, but some dataset defined on
# tracts/patches is present there (i.e. brightObjectMask), assume this
# skymap.
config.rootSkyMapName = "DC2"
