# This is the script that should run the entire pipeline to reduce the delta Cyg data from Feb 2017

# created by E.S., 2017 Nov 11

from astrom import match_pinholes
from astrom import find_dewarp_solution, apply_dewarp_solution, derotation, intermission, find_asterism_star_locations
import ipdb

dateStringShort = '171106'
filenameString = dateStringShort+'_DX_only' # this string is added onto pickle files
plotTitleString = '2017 Nov 08 (DX only)' # for distortion vector plot title

# frame numbers of frames that will need to be derotated and dewarped
startNum = 8597
stopNum = 8942

### PART 1: FIND DEWARP SOLUTION

# match the empirical and ideal pinholes
match_pinholes.match_pinholes(
    [110,-110],
    48.0,
    [100,512],
    -1e-9,
    -3.2,
    filenameString,
    plotTitleString,
    plot=True) # add another flag for when user is just testing model grid first

# work out the solution
find_dewarp_solution.find_dewarp(
    filenameString,
    plotTitleString,
    plot=True)


### PART 2: APPLY DEWARP AND DEROTATE

# apply dewarp solution
'''
apply_dewarp_solution.apply_dewarp(
    startNum,
    stopNum,
    filenameString)

# derotate
derotation.derotate_image_forloop(startNum,stopNum,dateStringShort)
'''

### INTERMISSION, STEP 1: USER NEEDS TO MAKE DITHER MEDIANS

intermission.prompt_make_dithers()


### PART 3: FIND PLATE SCALE

# identify asterism stars in (x,y) space
find_asterism_star_locations.find_stars(
    dateStringShort,
    2)

# compare position angles between pairs of stars in (x,y) and (RA,DEC)
