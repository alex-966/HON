# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 07:00:08 2023

@author: alexander.baumann
"""
# HON RTR Heat Exchange Systems (HES) Applicability Tool

def main():
    
    while True:
        exemptions = input("Does the exchanger meet any of the following exemptions [40 CFR 63.104(a)]? \
(1) The minimum pressure on the cooling water side is at least 35 kPa greater than the \
maximum pressure on the process side. (2) There is an intervening cooling fluid, \
containing <5 wt% total HAPs listed in table 4 of subpart F, between the process and \
the cooling water. (Y/N): ").lower().strip()
        if exemptions not in ("yes", "y", "no", "n"):
            continue
        else:
            break
    
    if exemptions in ("yes", "y"):
        print("N/A")
            
    else:
        while True:
            try:
                eo_comp = float(input("Enter the composition of EO on the process \
side of the exchanger (wt%): ").strip())
            except ValueError:
                continue
            else:
                break
        eo_service = eo(eo_comp)
        
        if eo_service in ("In EO Service"):
            while True:
                he_type = input("Enter the type of exchanger \
- recirculating or once-through? ").lower().strip()
                if he_type not in ("recirculating", "cooling tower", "cooling water tower", 
                                  "once-through", "once through"):
                    continue
                else:
                    break 
                    
            if he_type in ("recirculating", "cooling tower", "cooling water tower"):
                while True:
                    try: 
                        flow = float(input("Enter the recirculating flow rate of \
the exchanger (gpm): ").strip())
                    except ValueError:
                        continue
                    else:
                        break 
                flow_exemption = recirculating(flow)
                            
                if flow_exemption:
                    print("N/A")
                    
                else:
                    hon_disp = {
                                "Name": he_name(), 
                                "Type": he_type.title(), 
                                "EO Determination": eo_service, 
                                "Sampling Method": monitoring()
                                }
                    for rtr in hon_disp:
                        print(rtr, hon_disp[rtr], sep=": ")
            
            else:
                hon_disp = {
                            "Name": he_name(), 
                            "Type": he_type.title(), 
                            "EO Determination": eo_service, 
                            "Sampling Method": monitoring()
                            }
                for rtr in hon_disp:
                    print(rtr, hon_disp[rtr], sep=": ")
        
        else:
            while True:
                try:
                    ohap_comp = float(input("Enter the composition of total OHAP on the \
process side of the exchanger (wt%): ").strip())
                except ValueError:
                    continue
                else:
                    break
            ohap_service = ohap(ohap_comp)
                
            if ohap_service:
                
                while True:
                    he_type = input("Enter the type of exchanger \
- recirculating or once-through? ").lower().strip()
                    if he_type not in ("recirculating", "cooling tower", "cooling water tower", 
                                            "once-through", "once through"):
                        continue
                    else:
                        break 
                    
                if he_type in ("recirculating", "cooling tower", "cooling water tower"):
                    while True:
                        try: 
                            flow = float(input("Enter the recirculating flow rate of \
the exchanger (gpm): ").strip())
                        except ValueError:  
                            continue
                        else:
                            break 
                    flow_exemption = recirculating(flow)
                            
                    if flow_exemption:
                        return print("N/A")
                    
                    else:
                        hon_disp = {
                                    "Name": he_name(), 
                                    "Type": he_type.title(), 
                                    "EO Determination": eo_service, 
                                    "Sampling Method": monitoring()
                                    }
                        for rtr in hon_disp:
                            print(rtr, hon_disp[rtr], sep=": ")
                
                else:
                    hon_disp = {
                                "Name": he_name(), 
                                "Type": he_type.title(), 
                                "EO Determination": eo_service, 
                                "Sampling Method": monitoring()
                                }
                    for rtr in hon_disp:
                        print(rtr, hon_disp[rtr], sep=": ")
                        
            else:
                print("N/A")        
        
def he_name():
    
    while True: 
        he_name = input("Enter the name of the exchanger: ").strip()
        if not he_name:
            continue
        else:
            break
    
    return he_name
        
def eo(i):

    if i >= 0.1:
        return "In EO Service"
    else:
        return "Not in EO Service"

def ohap(k):
    
    if k >= 5:
        return True
    else:
        return False

def recirculating(l):

    if l <= 10:
        return True
    else:
        return False

def water_sampling(m, n):
    
    if m >= 99 and n < 5.0E-06:
        return True
    else:
        return False

def monitoring():    
  
    while True: 
        try:
            solubility = float(input("Enter the composition of total water soluble \
organics that could leak into the exchanger (wt%): ").strip())
        except ValueError:
            continue
        else:
            break
    
    while True: 
        try:
            henry = float(input("Enter the Henry's Law Constant (at 25 degrees C) \
of the water soluble organics that could leak into the exchanger \
(atmospheres-cubic meters/mol): ").strip())
        except ValueError:
            continue
        else:
            break
            
    water_method = water_sampling(solubility, henry)
    
    if water_method:
        sampling_method = "Sampling Methods in accordance with 40 CFR Part 136"
    else:
        sampling_method = "Modified El Paso"
    
    return sampling_method

if __name__ == "__main__":
    main()