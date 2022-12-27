# PyHamilton Complex Movement
Requires PyHamilton=>1.491.4

To run:
`py robot_method.py`

This method overwrites the current version of move_plate in PyHamilton, in order to enable complex movement parameters. This capability will be migrated to PyHamilton in the future.

The new parameters for move_plate are dictionaries that describe the complex movement, `ComplexGetDixt` and `CmplxPlaceDict, with the following fields: `retractDist`, `liftUpHeight`, and `labwareOrientation`.

Complex movement example:
```python
def iswap_move_wide_grip(ham_int, source, destination):
    CmplxGetDict = {'retractDist': 0, 'liftUpHeight': 21.0, 'labwareOrientation': 3}
    CmplxPlaceDict = {'retractDist': 1.0, 'liftUpHeight': 20.0, 'labwareOrientation': 3}
    move_plate(ham_int, source, destination, gripHeight = 12, gripWidth = 123.7, gripMode=1, openWidth=132, CmplxGetDict=CmplxGetDict, CmplxPlaceDict = CmplxPlaceDict)
```
