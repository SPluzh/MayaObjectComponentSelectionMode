import pymel.core as pm
import maya.mel as mel

# Check if the 'other' display layer already exists
if not pm.ls('other', type='displayLayer'):

    # Create the 'other' display layer
    other_layer = pm.createDisplayLayer(name='other', empty=True)
    pm.setAttr("{}.displayType".format(other_layer), 2)  # Set the display type to 'reference'
    
    # Get the list of selected transforms
    selected_transforms = pm.selected(type='transform')
    print (selected_transforms)
    
    # Get the list of all transforms in the scene
    all_transforms = pm.ls(type='transform')
    
    # Calculate the list of transforms not in the selected list
    other_transforms = list(set(all_transforms) - set(selected_transforms))
    print (other_transforms)
    
    # Add the other transforms to the 'other' display layer
    other_layer.addMembers(other_transforms)

# Switch to component selection mode
mel.eval("changeSelectMode -component")

# Set selection type to polygon vertex
mel.eval("selectType -polymeshVertex true")

# Set selection type to polygon edges
#mel.eval("selectType -polymeshEdge true")

# Set selection type to polygon faces
#mel.eval("selectType -polymeshFace true")
