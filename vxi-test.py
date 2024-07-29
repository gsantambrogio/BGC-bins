import vxi11
from struct import pack
import time

instr = vxi11.Instrument("10.100.2.2",term_char=None)
print(instr.ask("*IDN?"))
instr.write("*RST")

wave=[]
with open ("./data.dat", "w") as file:
    for i in range (1000):
        wave.append(1000-int(i))
        file.write(str(int(i)))
        file.write("\n")
file.close()

#print (wave)
binwaveform = pack('>'+'H'*len(wave), *wave)
with open ("./data.bin", "wb") as file:
    file.write(binwaveform)
file.close()
#print (binwaveform)
ggstr="TRACE:DATA EMEMORY,#42000"
tt=pack('>'+('%i'%len(ggstr))+'s', ggstr.encode('utf-8'))
tt += binwaveform
#print(tt)
instr.write_raw(tt)
#tt=pack('>'+('%i'%len(ggstr))+'s', ggstr.encode('utf-8'))
#instr.write_raw(tt)
#instr.write_raw(binwaveform)
instr.write("TRAC:COPY USER2,EMEM")
#instr.write("TRAC:COPY EMEM,USER2")
instr.write("FUNCTION USER2")
instr.write("FREQUENCY 8K")
instr.write("OUTPUT ON")
#print(instr.write_raw(binwaveform))
