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
liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'



lmgr = LayoutManager('deck.lay')
plates = resource_list_with_prefix(lmgr, 'plate_', Plate96, 5)
tips = resource_list_with_prefix(lmgr, 'tips_', Tip96, 1)
liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'

aspiration_poss = [(plates[0], x) for x in range(8)]
dispense_poss = [(plates[0], x) for x in range(8,16)]
vols_list = [100]*8


tips_poss = [(tips[0], x) for x in range(8)]

def move_plate(ham, source_plate, target_plate, gripHeight, gripWidth, gripMode, openWidth, CmplxGetDict = None, CmplxPlaceDict = None, try_inversions=None):
    
    logging.info('move_plate: Moving plate ' + source_plate.layout_name() + ' to ' + target_plate.layout_name())
    src_pos = labware_pos_str(source_plate, 0)
    trgt_pos = labware_pos_str(target_plate, 0)
    try_inversions=(0,1)
    
    getCmplxMvmnt, getRetractDist, getLiftUpHeight, getOrientation = (0, 0.0, 20.0, 1)
    placeCmplxMvmnt, placeRetractDist, placeLiftUpHeight, placeOrientation = (0, 0.0, 20.0, 1)
    
    
    if CmplxGetDict:
        getCmplxMvmnt = 1
        getRetractDist = CmplxGetDict['retractDist']
        getLiftUpHeight = CmplxGetDict['liftUpHeight']
        getOrientation = CmplxGetDict['labwareOrientation']
    
    if CmplxPlaceDict:
        placeCmplxMvmnt = 1
        placeRetractDist = CmplxPlaceDict['retractDist']
        placeLiftUpHeight = CmplxPlaceDict['liftUpHeight']
        placeOrientation = CmplxPlaceDict['labwareOrientation']
    
    print(placeCmplxMvmnt)
    print(getCmplxMvmnt)
    
    for inv in try_inversions:
        cid = ham.send_command(ISWAP_GET, 
                               plateLabwarePositions=src_pos, 
                               inverseGrip=inv, 
                               gripHeight=gripHeight, 
                               gripWidth=gripWidth, 
                               widthBefore=openWidth, 
                               gripMode=gripMode,
                               movementType = getCmplxMvmnt,
                               retractDistance = getRetractDist,
                               liftUpHeight = getLiftUpHeight,
                               labwareOrientation = getOrientation,
                               )
        try:
            ham.wait_on_response(cid, raise_first_exception=True, timeout=120)
            break
        except PositionError:
            print("trying inverse")
            pass
    #else:
    #    raise IOError
    cid = ham.send_command(ISWAP_PLACE, 
                           plateLabwarePositions=trgt_pos, 
                           movementType = placeCmplxMvmnt, 
                           retractDistance = placeRetractDist,
                           liftUpHeight = placeLiftUpHeight,
                           labwareOrientation = placeOrientation
                           )
    try:
        ham.wait_on_response(cid, raise_first_exception=True, timeout=120)
    except PositionError:
        raise IOError



def iswap_move_wide_grip(ham_int, source, destination):
    CmplxGetDict = {'retractDist': 0, 'liftUpHeight': 21.0, 'labwareOrientation': 3}
    CmplxPlaceDict = {'retractDist': 1.0, 'liftUpHeight': 20.0, 'labwareOrientation': 3}
    move_plate(ham_int, source, destination, gripHeight = 12, gripWidth = 123.7, gripMode=1, openWidth=132, CmplxGetDict=CmplxGetDict, CmplxPlaceDict = CmplxPlaceDict)

if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        iswap_move_wide_grip(ham_int, plates[0], plates[1])