# Maya Selection Isolation Tool

https://user-images.githubusercontent.com/131027290/233620762-30a888c8-a8b1-457e-a4f3-cefe4c5e9357.mp4

This script for Autodesk Maya prevents **accidental selection of other objects** when switching to component modes (vertex, edge, face) on a selected object.

It works by temporarily isolating the selected object(s): all other objects are placed into a display layer (`sw_oc_other`) and made unselectable (`reference`). This ensures you only interact with what you intended — nothing else.

---

## 🔑 Purpose

✅ **Avoid unwanted selection** of other objects when working in component mode  
✅ **Stay focused** on the currently selected object  
✅ **Quickly toggle** between object and component modes using hotkeys

---

## 🧩 Features

- Hotkey-based switching:
  - `Object Mode`
  - `Vertex Mode`
  - `Edge Mode`
  - `Face Mode`
- Isolates only the selected object(s)
- Unselected objects become `reference` (unselectable)
- `Object Mode` removes the isolation layer
- Toggle between `reference` and `template` for the isolation layer


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
