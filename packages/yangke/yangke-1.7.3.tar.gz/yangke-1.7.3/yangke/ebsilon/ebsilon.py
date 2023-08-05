# Sample python script to run an EBSILON model from python
# via the EbsOpen COM API
# Requires pywin32 and a valid EBSILON license with EbsOpen option
# By: Milton Venetos, Wyatt Enterprises, LLC
# Copyright (C) October 18, 2017
# http://www.wyattllc.com
import win32com.client


def ReadVar(model, sProf, sObj, sVar, iUOMCode, ebs):
    # Function to read data from EBSILON variables via EbsOpen in user specified UOM
    # acceptable eUOM values from EbsOpen.epUNIT enumeration

    ebsval = "NaN"

    # make sure a valid model object was passed in
    if model is None:
        print("Model Not Found! Please provide a valid Model Object.")
        return ebsval

    eProfile = model.ActiveProfile
    # check that desired profile exists and activate it if so
    if model.GetProfile(sProf, eProfile)[0] == True:
        model.ActivateProfile(sProf)

        # Find the specified object. 2nd argument to the ObjectByContext method is
        # True so that Nothing is returned if sObj does not exist

        eData = model.ObjectByContext(sObj, True)
        eData = ebs.ObjectCaster.CastToData(eData)

        if eData is None:
            print("Unable to find object " + sObj + " in the model.")
            return ebsval

        eValue = eData.EbsValues(sVar)
        if eValue is None:
            print("Unable to find variable " + sVar + " in object " + sObj + ".")
            return ebsval

        ebsval = eData.EbsValues(sVar).GetValueInUnit(iUOMCode)
    else:
        print("Profile " + sProf + " not found in model " + model.Name)

    return ebsval


def WriteVar(model, sProf, sObj, sVar, iUOMCode, vVal, SaveFlg, ebs):
    # Function to write data to EBSILON variables via EbsOpen in user specified UOM
    # acceptable iUOMCode values from EbsOpen.epUNIT enumeration
    # Returns True if writing succeeds and False if it fails

    bretval = False

    # make sure a valid model object was passed in
    if model is None:
        print("Model Not Found! Please provide a valid Model Object.")
        return bretval

    eProfile = model.ActiveProfile
    # check that desired profile exists and activate it if so
    if model.GetProfile(sProf, eProfile)[0] == True:
        model.ActivateProfile(sProf)

        # Find the specified object. 2nd argument to the ObjectByContext method is
        # True so that Nothing is returned if sObj does not exist

        eData = model.ObjectByContext(sObj, True)
        eData = ebs.ObjectCaster.CastToData(eData)
        if eData is None:
            print("Unable to find object " + sObj + " in the model.")
            return bretval

        eValue = eData.EbsValues(sVar)
        if eValue is None:
            print("Unable to find variable " + sVar + " in object " + sObj + ".")
            return bretval

        bretval = eData.EbsValues(sVar).SetValueInUnit(vVal, iUOMCode)
    else:
        print("Profile " + sProf + " not found in model " + model.Name)

    # Save change to disk if succesful & desired by user
    if bretval and SaveFlg:
        model.Save

    return bretval


def EbsErrCode2Msg(epCalcResultStat):
    # Function to translate EBSILON Calculation Result Codes to text
    EbsErrCodeTxt = "Unknown Error Code"
    if epCalcResultStat == 0:
        EbsErrCodeTxt = "Simulation Successful"
    if epCalcResultStat == 1:
        EbsErrCodeTxt = "Simulation Successful With Comments"
    if epCalcResultStat == 2:
        EbsErrCodeTxt = "Simulation Successful With Warnings"
    if epCalcResultStat == 3:
        EbsErrCodeTxt = "Simulation Failed With Errors"
    if epCalcResultStat == 4:
        EbsErrCodeTxt = "Simulation Failed with Errors before Calculation - Check Model set up"
    if epCalcResultStat == 5:
        EbsErrCodeTxt = "Simulation Failed - Fatal Error"
    if epCalcResultStat == 6:
        EbsErrCodeTxt = "Simulation Failed - Maximum Number of Iterations Reached"
    if epCalcResultStat == 7:
        EbsErrCodeTxt = "Simulation Failed - Maximum Number of Iterations Reached With Warnings"
    if epCalcResultStat == 8:
        EbsErrCodeTxt = "Simulation Failed - Maximum Simulation Duration Time Exceeded"
    if epCalcResultStat == 9:
        EbsErrCodeTxt = "Simulation Failed - Maximum Number of Iterations Reached With Errors"
    if epCalcResultStat == 10:
        EbsErrCodeTxt = "Simulation Failed - License Error"
    if epCalcResultStat == 11:
        EbsErrCodeTxt = "Simulation Failed- Already In Simulation Error"
    if epCalcResultStat == 12:
        EbsErrCodeTxt = "Simulation Failed - Internal Error"

    return EbsErrCodeTxt


# main code

# set the path to and name of your model below
sModelPath = r"D:\Program Files (x86)\Ebsilon\EBSILONProfessional 13 Patch 2\Data\Examples\block750.ebs"

# initialize an instance of EBSILON
try:
    # ebs = win32com.client.dynamic.Dispatch("EbsOpen.Application") #late binding / dynamic dispatch
    ebs = win32com.client.gencache.EnsureDispatch("EbsOpen.Application")  # early binding / static dispatch
except:
    print("Unable to Instantiate EBSILON. Please check your EBSILON License.\n")
    exit()

model = ebs.Open(sModelPath, True)
if model is None:  # unable to open specified model
    print("Unable to open the " + sModelPath + " model.\n")
    exit()

# Get lb/h code from EpUnit

eUOM = win32com.client.constants

PPHUOM = eUOM.epUNIT_lb_h
KGSUOM = eUOM.epUNIT_kg_s
MWUOM = eUOM.epUNIT_MW
INTEGRALUOM = eUOM.epUNIT_INTEGRAL
TXTUOM = eUOM.epUNIT_TEXT

print("lb/h UOM code = " + str(PPHUOM))
print("kg/s UOM code = " + str(KGSUOM))
print("MW UOM code = " + str(MWUOM) + "\n")
print("Text UOM code = " + str(TXTUOM) + "\n")
print("Integral UOM code = " + str(INTEGRALUOM) + "\n")

# **** ReadVar calls below work with Block750 model only ****
# read the steam flow setting from the Load90 profile in kg/s and lb/h
print("Main Steam Flow = " + str(ReadVar(model, "Load90", "DSP", "MEASM", KGSUOM, ebs)) + " kg/s")
print("Main Steam Flow = " + str(ReadVar(model, "Load90", "DSP", "MEASM", PPHUOM, ebs)) + " lb/h")
print("\n")

profile = model.RootProfile  # get the model's root profile
profile.Activate()  # activate the root profile

# **** ReadVar and WriteVar calls below work with Block750 model only ******
# Run a simulation in the root profile and check the result
print("Main Steam Flow = " + str(ReadVar(model, "Design", "DSP", "MEASM", KGSUOM, ebs)) + " kg/s")
epCalcResultStatus = model.SimulateNew()
print(EbsErrCode2Msg(epCalcResultStatus))
print("Generator Power = " + str(ReadVar(model, "Design", "ELEKTRO_LEITUNG", "Q", MWUOM, ebs)) + " MWe")
print("\n")
# change steam flow and run again
WriteVar(model, "Design", "DSP", "MEASM", KGSUOM, 532.8, False, ebs)
print("Main Steam Flow = " + str(ReadVar(model, "Design", "DSP", "MEASM", KGSUOM, ebs)) + " kg/s")
epCalcResultStatus = model.SimulateNew()
print(EbsErrCode2Msg(epCalcResultStatus))
print("Generator Power = " + str(ReadVar(model, "Design", "ELEKTRO_LEITUNG", "Q", MWUOM, ebs)) + " MWe")


