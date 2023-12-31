# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 07:34:33 2023

@author: alexander.baumann
"""
# HON RTR Process Vent Applicability Tool

def main():
    
    while True:
        applic = input("Does the vent gas stream originate as a continuous flow from \
an air oxidation reactor, distillation unit, or reactor during \
operation of a chemical manufacturing process unit [40 CFR 63.107(b)]? (Y/N): ").strip().lower()    
        if applic not in ("yes", "y", "no", "n"):
            continue
        else:
            break
        
    if pv_applic(applic) == True:
        print("N/A")
        
    else:
        while True:
            pv_exemptions = input("Is the gas stream any of the following cases \
for this process vent? \
(1) A relief valve discharge. \
(2) A leak from equipment subject to 40 CFR 63 Subpart H. \
(3) A gas stream going to a fuel gas system as defined in §63.101. \
(4) A gas stream exiting a control device used to comply with §63.113. \
(5) A gas stream transferred to other processes (on-site or off-site) \
for reaction or other use in another process (i.e., chemical value as a product, \
isolated intermediate, byproduct, or coproduct, or for heat value). \
(6) A gas stream transferred for fuel value (i.e., net positive heating value), \
use, reuse, or for sale for fuel value, use, or reuse. \
(7) A storage vessel vent or transfer operation vent subject to §63.119 or §63.126. \
(8) A vent from a WMU subject to §63.132 through §63.137. \
(9) A gas stream exiting an analyzer. (Y/N): ").strip().lower()
            if pv_exemptions not in ("yes", "y", "no", "n"):
                continue
            else:
                break
        pv_type(pv_exemptions)

def pv_type(l):

    if l == "yes" or l == "y":
        print("N/A")
    else:
        return hon()
        
def hon():
    
    while True:
        try:
            eo_conc = float(input("Enter the undiluted EO concentration (ppmv): "))
        except ValueError:
            continue
        else:
            break 
    eo_service = eo(eo_conc)
    
    while True:
        try:
            ohap_comp = float(input("Enter the composition of total OHAP (wt%): "))
        except ValueError: 
            continue
        else:
            break 
    ohap_applic = ohap_conc(ohap_comp)
        
    if eo_service == "Not in EO Service" and ohap_applic == False:
        print("N/A")
    
    else:
        while True: 
            pv_name = input("Enter the name of the process vent: ").strip()
            if not pv_name:
                continue
            else:
                break
        
        while True:
            try:
                ohap_emissions = float(input("Enter the uncontrolled OHAP emissions (lb/hr): "))
            except ValueError:
                continue
            else:
                break 
        group_det = ohap(ohap_emissions, ohap_comp)
        
        hon_disp = {
                    "Name": pv_name, 
                    "Group Determination": group_det, 
                    "EO Determination": eo_service
                    }
        for rtr in hon_disp:
            print(rtr, hon_disp[rtr], sep=": ")
            
def pv_applic(j):
        
    if j == "no" or j == "n": 
        return True 
    else:
        return False
    
def eo(i): 
    
    if i >= 1:
        return "In EO Service"
    else:
        return "Not in EO Service"

def ohap_conc(k):
    
    if k > 0.005:
        return True
    else:
        return False

def ohap(n, k):
    
    if ohap_conc(k) == False:
        return "N/A"
    elif n >= 1:
        return "Group 1"
    else:
        return "Group 2"

if __name__ == "__main__":
    main()