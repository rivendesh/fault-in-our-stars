# Yes, this is Claude :/

from astropy.time import Time

# If your value is already a BJD (large number like 2456000.0):
bjd = 2456000.0
t = Time(bjd, format='jd', scale='tdb')
print(t.iso)  # Correct date

# If your value is a true BKJD (small number like 1167.0):
bkjd = 1167.0
t = Time(bkjd + 2454833.0, format='jd', scale='tdb')
print(t.iso)  # Correct date