from .models import fault,site,etpflow


def data_parse(data):
    l1=data.split(",")
    fault_codes = {
    '255': 'No Fault',
    '000': 'Man Stop',
    '001': 'Single Phasing',
    '002': 'Overload',
    '003': 'Dry Running' }
    d1={}
    d2={}
    if l1[0][0]=='9' and l1[1]:
        l2=l1[0].split("*")
        d1["smno"]=l2[0][2:]
        try:
            oldsite=site.objects.get(smno=d1["smno"])
        except:
            oldsite=""
        l3=l2[1].split(" ")
        d1["name"]=l3[0]

        if l1[2][-1]=='1':
            frf=0.001
        elif l1[2][-1]=='2':
            frf=0.01

        if l1[3][-1]=='0':
            d1["fstatus"]="Sensor"
        elif l1[3][-1]=='1':
            d1["fstatus"]="Connected"
        else:
            d1["fstatus"]="Unknown"

        d1["ib"]=bin(int(l1[4]))[2:].zfill(8)

        d1["ob"]=bin(int(l1[5]))[2:].zfill(8)

        d1["etp"]=bin(int(l1[6]))[2:].zfill(2)

        d1["obh"]=bin(int(l1[7]))[2:].zfill(3)

        d1["flowvalue"] =int((256*int(l1[9]))+ int(l1[8]))*frf

        d1["tot"] =((65536*int(l1[12]))+( 256*int(l1[11]))+ int(l1[10]))*0.1

        d1["itp1"] = fault_codes.get(l1[14], 'Unknown Fault')
        d1["itp2"] = fault_codes.get(l1[15], 'Unknown Fault')
        d1["ffp1"] = fault_codes.get(l1[16], 'Unknown Fault')
        d1["ffp2"] = fault_codes.get(l1[17], 'Unknown Fault')
        d1["b1"] = fault_codes.get(l1[18], 'Unknown Fault')
        d1["b2"] = fault_codes.get(l1[19], 'Unknown Fault')
        d1["stp1"] = fault_codes.get(l1[20], 'Unknown Fault')
        d1["stp2"] = fault_codes.get(l1[21], 'Unknown Fault')

        d1["pos"]=bin(int(l1[22]))[2:].zfill(8)

        d1["nop"]=bin(int(l1[23]))[2:].zfill(8)

        d1["itpr"]=(256*int(l1[25]))+ int(l1[24])

        d1["ffpr"]=(256*int(l1[27]))+ int(l1[26])

        d1["blwrr"]=(256*int(l1[29]))+ int(l1[28])

        d1["stpr"]=(256*int(l1[31]))+ int(l1[30])

        d1["itpc"]=int(l1[32])*0.1

        d1["ffpc"]=int(l1[33])*0.1

        d1["bwlrc"]=int(l1[34])*0.1

        d1["stpc"]=int(l1[35])*0.1

        d1["mpv"]=(256*int(l1[37]))+ int(l1[36])

        d1["nobkwsh"]=(256*int(l1[39]))+ int(l1[38])

        d1["itpophr"]=(256*int(l1[41]))+ int(l1[40])

        d1["ffpophr"]=(256*int(l1[43]))+ int(l1[42])

        d1["blwrophr"]=(256*int(l1[45]))+ int(l1[44])

        d1["stpophr"]=(256*int(l1[47]))+ int(l1[46])

        d1["stpserhr"]=(256*int(l1[49]))+ int(l1[48])

        d1["stpon"]=(256*int(l1[51]))+ int(l1[50])

       

        try:
            eflow = etpflow.objects.filter(smno=d1["smno"]).order_by('dnt').last()
        except:
            eflow = None

        if eflow:
            d1['itp1ophr'] = eflow.itp1ophr + (d1["itpophr"] - (eflow.itp1ophr + eflow.itp2ophr)) if d1['ob'][-1] == '1' else eflow.itp1ophr
            d1['itp2ophr'] = eflow.itp2ophr if d1['ob'][-1] == '1' else eflow.itp2ophr + (d1["itpophr"] - (eflow.itp1ophr + eflow.itp2ophr))
            d1['itp1c'] = d1["itpc"] if d1['ob'][-1] == '1' else 0.00
            d1['itp2c'] = 0.00 if d1['ob'][-1] == '1' else d1["itpc"]

            d1['ffp1ophr'] = eflow.ffp1ophr + (d1["ffpophr"] - (eflow.ffp1ophr + eflow.ffp2ophr)) if d1['ob'][-2] == '1' else eflow.ffp1ophr
            d1['ffp2ophr'] = eflow.ffp2ophr if d1['ob'][-2] == '1' else eflow.ffp2ophr + (d1["ffpophr"] - (eflow.ffp1ophr + eflow.ffp2ophr))
            d1['ffp1c'] = d1["ffpc"] if d1['ob'][-2] == '1' else 0.00
            d1['ffp2c'] = 0.00 if d1['ob'][-2] == '1' else d1["ffpc"]

            d1['blwr1ophr'] = eflow.blwr1ophr + (d1["blwrophr"] - (eflow.blwr1ophr + eflow.blwr2ophr)) if d1['ob'][-3] == '1' else eflow.blwr1ophr
            d1['blwr2ophr'] = eflow.blwr2ophr if d1['ob'][-3] == '1' else eflow.blwr2ophr + (d1["blwrophr"] - (eflow.blwr1ophr + eflow.blwr2ophr))
            d1['bwlr1c'] = d1["bwlrc"] if d1['ob'][-3] == '1' else 0.00
            d1['bwlr2c'] = 0.00 if d1['ob'][-3] == '1' else d1["bwlrc"]

            d1['stp1ophr'] = eflow.stp1ophr + (d1["stpophr"] - (eflow.stp1ophr + eflow.stp2ophr)) if d1['ob'][-4] == '1' else eflow.stp1ophr
            d1['stp2ophr'] = eflow.stp2ophr if d1['ob'][-4] == '1' else eflow.stp2ophr + (d1["stpophr"] - (eflow.stp1ophr + eflow.stp2ophr))
            d1['stp1c'] = d1["stpc"] if d1['ob'][-4] == '1' else 0.00
            d1['stp2c'] = 0.00 if d1['ob'][-4] == '1' else d1["stpc"]

        else:
            d1['itp1ophr'] = d1["itpophr"] if d1['ob'][-1] == '1' else 0.00
            d1['itp2ophr'] = 0.00 if d1['ob'][-1] == '1' else d1["itpophr"]
            d1['itp1c'] = d1["itpc"] if d1['ob'][-1] == '1' else 0.00
            d1['itp2c'] = 0.00 if d1['ob'][-1] == '1' else d1["itpc"]

            d1['ffp1ophr'] = d1["ffpophr"] if d1['ob'][-2] == '1' else 0.00
            d1['ffp2ophr'] = 0.00 if d1['ob'][-2] == '1' else d1["ffpophr"]
            d1['ffp1c'] = d1["ffpc"] if d1['ob'][-2] == '1' else 0.00
            d1['ffp2c'] = 0.00 if d1['ob'][-2] == '1' else d1["ffpc"]

            d1['blwr1ophr'] = d1["blwrophr"] if d1['ob'][-3] == '1' else 0.00
            d1['blwr2ophr'] = 0.00 if d1['ob'][-3] == '1' else d1["blwrophr"]
            d1['bwlr1c'] = d1["bwlrc"] if d1['ob'][-3] == '1' else 0.00
            d1['bwlr2c'] = 0.00 if d1['ob'][-3] == '1' else d1["bwlrc"]

            d1['stp1ophr'] = d1["stpophr"] if d1['ob'][-4] == '1' else 0.00
            d1['stp2ophr'] = 0.00 if d1['ob'][-4] == '1' else d1["stpophr"]
            d1['stp1c'] = d1["stpc"] if d1['ob'][-4] == '1' else 0.00
            d1['stp2c'] = 0.00 if d1['ob'][-4] == '1' else d1["stpc"]

        

        

        if oldsite:
            fault_indices = range(14, 22)
            fault_names = ["ITP-1", "ITP-2", "FFP-1", "FFP-2", "Blower-1", "Blower-2", "STP-1", "STP-2"]

            for i, name in zip(fault_indices, fault_names):
                if l1[i] != '255' and l1[i] != '000':
                    f = fault(site=oldsite, fname=name + "-" + fault_codes.get(l1[i], 'Unknown Fault'))
                    f.save()

    else:
        return data

    

    return d1
