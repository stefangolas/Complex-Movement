# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 move_plate, labware_pos_str, ISWAP_GET, ISWAP_PLACE, PositionError)
import logging



lmgr = LayoutManager('deck.lay')
plates = resource_list_with_prefix(lmgr, 'plate_', Plate96, 5)



def iswap_move_wide_grip(ham_int, source, destination):
    CmplxGetDict = {'retractDist': 0, 'liftUpHeight': 21.0, 'labwareOrientation': 3}
    CmplxPlaceDict = {'retractDist': 1.0, 'liftUpHeight': 20.0, 'labwareOrientation': 3}
    move_plate(ham_int, source, destination, gripHeight = 12, gripWidth = 123.7, gripMode=1, openWidth=132, CmplxGetDict=CmplxGetDict, CmplxPlaceDict = CmplxPlaceDict)

if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        iswap_move_wide_grip(ham_int, plates[0], plates[1])