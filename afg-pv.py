import epics
p = epics.PV('AFG3052C:DATA')
with open ("./data.bin", "rb") as file:
    wave=file.read()
file.close()
#print(wave)
p.put(wave)
