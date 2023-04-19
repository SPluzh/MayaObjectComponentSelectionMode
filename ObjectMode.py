import maya.cmds as cmds

# Check if a display layer named "other" exists, and delete it if it does
if cmds.ls('other', type='displayLayer'):
    cmds.delete('other')

# Set Maya's select mode to object mode
cmds.selectMode(object=True)