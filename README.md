# Maya Selection Isolation Tool (`SwitchObjectComponentMode.py`)

https://user-images.githubusercontent.com/131027290/233620762-30a888c8-a8b1-457e-a4f3-cefe4c5e9357.mp4

This script for Autodesk Maya allows you to **quickly switch between object and component selection modes** (vertices, edges, faces) using hotkeys — while temporarily **isolating only the selected objects**. All other objects are placed into a display layer (`sw_oc_other`) and set to `reference` or `template`, preventing accidental edits.

## 🧩 Features

- 🔀 Hotkey-based switching between:
  - `Object Mode`
  - `Vertex Mode`
  - `Edge Mode`
  - `Face Mode`
- 🟥 Unselected objects are added to a `sw_oc_other` display layer and made unselectable (`reference`)
- 🟨 Automatically removes the isolation layer when returning to object mode
- 🔁 Toggle the display type of the isolation layer between `reference` and `template`

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
