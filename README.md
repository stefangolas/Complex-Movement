# Complex-Movement
PyHamilton Complex Movement

To run:
`py robot_method.py`

Complex movement example:
```python
def iswap_move_wide_grip(ham_int, source, destination):
    CmplxGetDict = {'retractDist': 0, 'liftUpHeight': 21.0, 'labwareOrientation': 3}
    CmplxPlaceDict = {'retractDist': 1.0, 'liftUpHeight': 20.0, 'labwareOrientation': 3}
    move_plate(ham_int, source, destination, gripHeight = 12, gripWidth = 123.7, gripMode=1, openWidth=132, CmplxGetDict=CmplxGetDict, CmplxPlaceDict = CmplxPlaceDict)
```
