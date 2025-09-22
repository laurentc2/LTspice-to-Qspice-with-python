#! usr/bin/python
# -*- coding: ISO-8859-1 -*-

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

#  Written by : Laurent CHARRIER
#  last change: 2025, Sep 21.
#
# usage example : python LT2Q.py Draft0.asc
#       This example will create the file : Draft0.qsch
#

import os,sys,re
from os import path
from pathlib import Path

in_file = sys.argv[1]
infl = open(in_file,"r", encoding='latin-1', errors='replace');
# infl = open(in_file,"r", encoding='latin-1');
if in_file[:3]!='asy' : print('\n'+in_file+' is not a .asy LTspice symbol\n')
else :  out_file = in_file.replace(".asy" , ".qsym")
outfl = open(out_file,"w",encoding='latin-1', errors='replace');

# filter the lines of the schematic or of the symbol
def filter_line(line):
  line=line.rstrip('\n')
  line=line.rstrip('\r')
  line=line.replace("     " , " ")
  line=line.replace("    " , " ")
  line=line.replace("   " , " ")
  line=line.replace("  " , " ")
  line=line.replace("  " , " ")
  line=line.replace(chr(0xB5), 'u')
  return line


#--------------------------------------------------------------------
# parameters initialization

# multiplication actor from LTspice (grid of 16) to Qspice (grid of 100)
# actually 5 would be the exact factor to get the same symbol sizes, but 6.25 is better for the wire to be on the grid of 100
mult=6.25
# different text sizes allowed by LTspice or Qspice
txtsize=[str(0.4*mult/5),str(0.625*mult/5),str(1*mult/5),str(1.5*mult/5),str(2*mult/5),str(2.5*mult/5),str(3.5*mult/5),str(5*mult/5),str(7*mult/5)]

# give the index of the text or pin orientation
labelorient=['NONE', 'LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'VLEFT', 'VRIGHT', 'VBOTTOM', 'VTOP', 'CENTER', 'VCENTER']
val_orient=[0,7,11,14,13,7,11,14,13,8,8]
# default spice model
sym_SpiceModel=str(in_file.replace(".asy" , "")).upper()
pin_spicenumber=[]
pin_line=[]
# default values position and orientation and size
inst_x=30
inst_y=40
inst_ort='7'
inst_size='1'
value=''
val_x=30
val_y=76
val_size='1'
val_ort='7'
value2=''
val2_x=30
val2_y=76
val2_size='1'
val2_ort='7'
value3=''
valsp_x=30
valsp_y=0
valsp_ort='7'
valsp_size='0.7'

#--------------------------------------------------------------------
# start to write the first lines of the .qsym file
outfl.write(chr(0xFF)+chr(0xD8)+chr(0xFF)+chr(0xDB)+chr(0xAB)+'symbol '+str(in_file.replace(".asy" , ""))+chr(0x0A))
outfl.write('  '+chr(0xAB)+'type: X'+chr(0xBB)+chr(0x0A))
# start to parse the .asy file, line by line
for line1 in infl:
  line=''
  line1=filter_line(line1)
  words=re.split(' ', line1)
  # print(line1)
  if re.match('^SYMATTR Description ',line1) : line+='  '+chr(0xAB)+'description: '+line1[line1.find(words[2]):]+chr(0xBB)+chr(0x0A)
  if re.match('^SYMATTR SpiceLine ',line1) : line+='  '+chr(0xAB)+'library file: '+line1[line1.find(words[2]):]+chr(0xBB)+chr(0x0A)
  if re.match('^SYMATTR ModelFile ',line1) : line+='  '+chr(0xAB)+'library file: '+line1[line1.find(words[2]):]+chr(0xBB)+chr(0x0A)
  if re.match('^LINE Normal ',line1) :
    line+='  '+chr(0xAB)+'line ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
  if re.match('^RECTANGLE Normal ',line1) :
    line+='  '+chr(0xAB)+'rect ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') 0 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
  if re.match('^ARC Normal ',line1) :
    line+='  '+chr(0xAB)+'arc ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') ('+str(int(mult*int(words[6])))+','+str(int(-mult*int(words[7])))+') ('+str(int(mult*int(words[8])))+','+str(int(-mult*int(words[9])))+') 0 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
  if re.match('^CIRCLE Normal ',line1) :
    line+='  '+chr(0xAB)+'ellipse ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') 0 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
  if re.match('^SYMATTR Value ',line1) :
    value=line1[line1.find(words[2]):]
  if re.match('^SYMATTR Value2 ',line1) :
    value2=line1[line1.find(words[2]):]
  if re.match('^SYMATTR SpiceModel ',line1) :
    sym_SpiceModel=line[line.find(words[2]):]
  if re.match('^TEXT ',line1) :
    if words[3][0]=='V' : txt_ort=str(val_orient[labelorient.index(words[3].upper())]+32)
    else : txt_ort=str(val_orient[labelorient.index(words[3].upper())])
    value3+='  '+chr(0xAB)+'text ('+str(int(mult*int(words[1])))+','+str(int(-mult*int(words[2])))+') '+txtsize[int(words[4])]+' '+txt_ort+' 1 0x005000 -1 -1 "'+line1[line1.find(words[5]):]+'"'+chr(0xBB)+chr(0x0A)

  # all pins are first stored in a list and the spiceOrder in a another list but with the same index
  # the goal is to allows to restore in Qspice the pins in the spice order
  if re.match('^PIN ',line1) :
    x_pin=int(words[1])
    y_pin=int(words[2])
    pin_ort=str(val_orient[labelorient.index(words[3].upper())])
  if re.match('^PINATTR PinName ',line1) :
    # pin_name=words[2].replace('+','P').replace('-','M')
    pin_name=words[2]
    pin_line.append('  '+chr(0xAB)+'pin ('+str(int(mult*x_pin))+','+str(int(-mult*y_pin))+') (0,0) 1 '+pin_ort+' 0 0x005000 -1 "'+pin_name+'"'+chr(0xBB)+chr(0x0A))
    pin_name=''
  if re.match('^PINATTR SpiceOrder ',line1) :
    pin_spicenumber.append(int(words[2]))

  # adjust positions and orientation and size if set in the symbol
  # for the instance name
  if re.match('^WINDOW 0 ',line1):
    inst_x=int(words[2])
    inst_y=-int(words[3])
    inst_ort=str(val_orient[labelorient.index(words[4].upper())])
    inst_size=txtsize[int(words[5])]
  # for the value
  if re.match('^WINDOW 3 ',line1):
    val_x=int(words[2])
    val_y=-int(words[3])
    val_ort=str(val_orient[labelorient.index(words[4].upper())])
    val_size=txtsize[int(words[5])]
  # for the value2
  if re.match('^WINDOW 123 ',line1):
    val2_x=int(words[2])
    val2_y=-int(words[3])
    val2_ort=str(val_orient[labelorient.index(words[4].upper())])
    val2_size=txtsize[int(words[5])]
  # for the SpiceModel
  if re.match('^WINDOW 38 ',line1):
    valsp_x=int(words[2])
    valsp_y=-int(words[3])
    valsp_ort=str(val_orient[labelorient.index(words[4].upper())])
    valsp_size=txtsize[int(words[5])]
    
  # finally write the line to the .qsym file
  outfl.write(line)

#--------------------------------------------------------------------
# all lines have been parsed : close the file .qsym properly

outfl.write('  '+chr(0xAB)+'text ('+str(int(mult*inst_x))+','+str(int(mult*inst_y))+') '+inst_size+' '+inst_ort+' 0 0x1000000 -1 -1 "X1"'+chr(0xBB)+chr(0x0A))
outfl.write('  '+chr(0xAB)+'text ('+str(int(mult*valsp_x))+','+str(int(mult*valsp_y))+') '+valsp_size+' '+valsp_ort+' 2 0x1000000 -1 -1 "'+sym_SpiceModel+'"'+chr(0xBB)+chr(0x0A))
if value!='' :
  outfl.write('  '+chr(0xAB)+'text ('+str(int(mult*val_x))+','+str(int(mult*val_y))+') '+val_size+' '+val_ort+' 0 0x1000000 -1 -1 "'+value+'"'+chr(0xBB)+chr(0x0A))
if value2!='' :
  outfl.write('  '+chr(0xAB)+'text ('+str(int(mult*val2_x))+','+str(int(mult*val2_y))+') '+val2_size+' '+val2_ort+' 0 0x1000000 -1 -1 "'+value2+'"'+chr(0xBB)+chr(0x0A))
if value3!='' :
  outfl.write(value3)

## finally write all the pins the order of the SPICE pin order
for i in range(1,len(pin_line)+1) :
  for j in range(0,len(pin_line)) :
    if pin_spicenumber[j]==i :
      outfl.write(pin_line[j])

# character » to close the .qsch file
outfl.write(chr(0xBB)+chr(0x0A))

infl.close()
outfl.close()