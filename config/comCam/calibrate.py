import os

obsConfigDir = os.path.join(os.path.dirname(__file__))
config.photoRefObjLoader.load(os.path.join(obsConfigDir, "filterMap.py"))
config.connections.astromRefCat = "the_monster_20240904"

# Loosen maxOffset to account for early pointing model inaccuracy.
config.astrometry.matcher.maxOffsetPix=1500
config.astromRefObjLoader.pixelMargin=1500

# Loosen minMatchDistanceArcSec, the match distance below which further
# iteration is pointless (arcsec) since we can only do as well as the
# camera model in SFM using the affine WCS fit.
# TODO: DM-47250. Tighten up (or remove) this override when an updated
# camera model is implemented.
config.astrometry.minMatchDistanceArcSec = 0.04

# Overrides to improved astrometry matching.
config.astrometry.doFiducialZeroPointCull = True
config.astrometry.load(os.path.join(obsConfigDir, "fiducialZeroPoint.py"))

# Loosened for early ComCam with large PSFs.
config.photoCal.match.sourceSelection.doUnresolved = False

# Exposure summary stats.
config.computeSummaryStats.load(os.path.join(obsConfigDir, "computeExposureSummaryStats.py"))
