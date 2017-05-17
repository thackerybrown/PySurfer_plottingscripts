"""
Basic Visualization
===================

Initialize a basic visualization session.

#first run
#export FREESURFER_HOME=/Applications/freesurfer
#source $FREESURFER_HOME/SetUpFreeSurfer.sh

"""
import os
os.environ['QT_API'] = 'pyqt'
os.environ['ETS_TOOLKIT'] = 'qt4'
#os.environ['SUBJECTS_DIR'] = "/path/to/subjects"

import sip
sip.setapi('QDate',2)


from surfer import Brain

print(__doc__)




from mayavi import mlab

"""
Define the three important variables.
Note that these are the first three positional arguments
in tksurfer (and pysurfer for that matter).
"""
subject_id = 'fsaverage'
hemi = 'lh'
surface = 'inflated'

"""
Call the Brain object constructor with these
parameters to initialize the visualization session.
"""
brain = Brain(subject_id, hemi, surface)

#mlab.show()
