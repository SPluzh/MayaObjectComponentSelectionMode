from maya import cmds

# Check if the 'other' display layer already exists
if not cmds.ls('other', type='displayLayer'):

    # Create the 'other' display layer
    other_layer = cmds.createDisplayLayer(name='other', empty=True)
    cmds.setAttr("{}.displayType".format(other_layer), 2)  # Set the display type to 'reference'
    
    # Get the list of selected transforms
    selected_transforms = cmds.ls(selection=True, type='transform')
    
    # Get the list of all transforms in the scene
    all_transforms = cmds.ls(type='transform')
    
    # Calculate the list of transforms not in the selected list
    other_transforms = list(set(all_transforms) - set(selected_transforms))
    
    # Add the other transforms to the 'other' display layer
    cmds.editDisplayLayerMembers(other_layer, other_transforms, noRecurse=True)

# Switch to component selection mode
cmds.selectMode(component=True)

# Set selection type to polygon vertex
cmds.selectType(polymeshVertex=True)

# Set selection type to polygon edges
#cmds.selectType(polymeshEdge=True)

# Set selection type to polygon faces
#cmds.selectType(polymeshFace=True)
