# Select components only from current object

https://user-images.githubusercontent.com/131027290/233183978-a1333889-a5ad-4c36-9684-096f8dc8ac91.mp4


These scripts allow you to edit only the selected objects in component mode without switching to other objects. This allows you to modify only the selected components, making editing easier and reducing the risk of accidentally modifying other objects. At the same time, the scripts do not allow objects to be selected in component mode, ensuring that you work only in object mode.

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
