# Maya Selection Isolation Tool

https://user-images.githubusercontent.com/131027290/233620762-30a888c8-a8b1-457e-a4f3-cefe4c5e9357.mp4

This script for Autodesk Maya automatically isolates selected objects by placing **unselected objects** into a special display layer (`sw_oc_other`) and making them unselectable. It then switches Maya into component selection mode (vertices, edges, faces), allowing you to safely work on the selected geometry only.

## 🧩 Features

- 🟦 Switches to component selection mode:
  - Vertices (`VertexMode`)
  - Edges (`EdgeMode`)
  - Faces (`FaceMode`)
- 🟥 Moves all **unselected** objects to a display layer `sw_oc_other` and sets them to `reference`
- 🟨 Returns to object selection mode and removes the isolation layer (`ObjectMode`)
- 🔁 Toggles the layer between `reference` and `template` modes (`ToggleTemplatedMode`)

# Install

1. Download the SwitchObjectComponentMode.py and place the SwitchObjectComponentMode.py file in your Maya scripts directory.

2. Assign a Hotkey with the following python code:

## Object Mode
```python
import SwitchObjectComponentMode as SwitchOCMode
SwitchOCMode.ObjectMode()
```
## Vertex Mode
```python
import SwitchObjectComponentMode as SwitchOCMode
SwitchOCMode.VertexMode()
```
## Edge Mode
```python
import SwitchObjectComponentMode as SwitchOCMode
SwitchOCMode.EdgeMode()
```
## Face Mode
```python
import SwitchObjectComponentMode as SwitchOCMode
SwitchOCMode.FaceMode()
```

## Toggle Templated Mode
```python
import SwitchObjectComponentMode as SwitchOCMode
SwitchOCMode.ToggleTemplatedMode()
```

https://user-images.githubusercontent.com/131027290/233621560-985e4dd1-bf48-49c9-bb09-f11202ef948f.mp4
