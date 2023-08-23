# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 06:50:52 2023

@author: alexander.baumann
"""

# HON RTR Wastewater (WW) Applicability Tool

def main():
    
    while True:
        ww_type = input("Enter the type of wastewater stream at its point of determination - \
process wastewater or maintenace wastewater? ").lower().strip()
        if ww_type not in ["process", "process wastewater", "maintenance", "maintenance wastewater"]:
            continue
        else:
            break
        
    while True:
        try:
            ww_flow = float(input("Enter the flow rate of either (1) the individual \
wastewater stream at its point of determination or (2) of 2 or more wastewater\
streams that are combined and have its point of determination downstream where mixing occurs, \
if selected (L/min): ").strip())
        except ValueError:
            continue
        else:
            break
    
    if ww_flow == 0:
        print("N/A")
    
    else:
        
        while True:
            try:
                eo_conc = float(input("Enter the concentration of EO in the wastewater \
stream (ppmv): ").strip())
            except ValueError:
                continue
            else:
                break
    
        eo_service = eo(eo_conc, ww_flow)
        
        if eo_service:
    
            eo_det = "In EO Service"
            group_det = "Group 1"
            
            hon_disp = {"WW Name": ww_name(),"WW Type": ww_type.title(), "Group Determination": group_det, 
                        "EO Determination": eo_det
                        }
            for rtr in hon_disp:
                print(rtr, hon_disp[rtr], sep=": ")
        
        else:
            
            eo_det = "Not in EO Service"
            
            while True:
                try:
                    ww_conc = float(input("Enter the total concentration of Table 8 or 9 \
compounds present in the wastewater stream (ppmw): ").strip())
                except ValueError:
                    continue
                else:
                    break
    
            ww_applic = ww_def(ww_conc, ww_flow)
            group_applic = group(ww_conc, ww_flow)
            
            if ww_applic and group_applic and ww_type in ["process", "process wastewater"]:
                group_det = "Group 1"
            elif ww_applic and not group_applic and ww_type in ["process", "process wastewater"]:
                group_det = "Group 2"
            elif ww_applic and ww_type in ["maintenance", "maintenance wastewater"]:
                group_det = "Does not apply to non-EO service maintenance wastewater streams. \
Follow maintenance procedure standards in 40 CFR 63.105."
            else:    
                group_det = "N/A"
            
            hon_disp = {"WW Name": ww_name(),"WW Type": ww_type.title(), "Group Determination": group_det, 
                        "EO Determination": eo_det
                        }
            for rtr in hon_disp:
                print(rtr, hon_disp[rtr], sep=": ")
    
def ww_name():

    while True:
        name = input("Enter the name of the wastewater stream: ").strip()
        if name in ["", " "]:
            continue
        else:
            break 
    
    return name
      
def ww_def(conc, flow):

    if conc >= 5 and flow >= 0.02:
        return True
    elif conc >= 10000 and flow > 0:
        return True
    else:
        return False

def eo(i, j):
    
    if i >= 1 and j > 0:
        return True
    else:
        return False
    
def group(group_conc, group_flow):
    
    if group_conc >= 1000 and group_flow >= 10:
        return True
    elif group_conc >= 10000 and group_flow > 0:
        return True
    else:
        return False
    
main()