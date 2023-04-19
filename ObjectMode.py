import pymel.core as pm
import maya.mel as mel

# Check if a display layer named "other" exists, and delete it if it does
if pm.ls('other', type='displayLayer'):
    pm.delete('other')
    
# Set Maya's select mode to object mode
mel.eval("changeSelectMode -object")
