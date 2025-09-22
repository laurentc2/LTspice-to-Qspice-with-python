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
if in_file[-3:]!='asc' : print('\n'+in_file+' is not a .asc LTspice schematic\n')
else :  out_file = in_file.replace(".asc" , ".qsch")
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


# list of all the default LTspice symbols located in the user appdata directory
LTspice_dir = path.expandvars(r'%LOCALAPPDATA%\LTspice\lib\sym')
comp_LTspice = []
if os.path.exists(str(LTspice_dir)) :
  dir = os.listdir(LTspice_dir)
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(LTspice_dir,component))
if os.path.exists(str(os.path.join(LTspice_dir,'ADC'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'ADC'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'ADC'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'Comparators'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'Comparators'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'Comparators'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'CurrentMonitors'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'CurrentMonitors'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'CurrentMonitors'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'DAC'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'DAC'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'DAC'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'Digital'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'Digital'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'Digital'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'FilterProducts'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'FilterProducts'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'FilterProducts'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'Misc'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'Misc'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'Misc'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'OpAmps'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'OpAmps'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'OpAmps'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'Optos'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'Optos'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'Optos'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'PowerProducts'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'PowerProducts'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'PowerProducts'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'References'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'References'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'References'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'SpecialFunctions'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'SpecialFunctions'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'SpecialFunctions'),component))
if os.path.exists(str(os.path.join(LTspice_dir,'Switches'))) :
  dir = os.listdir(os.path.join(LTspice_dir,'Switches'))
  for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.path.join(LTspice_dir,'Switches'),component))

dir = os.listdir(os.getcwd())
for component in dir:
    if (component[-4:]==".asy") : comp_LTspice.append(os.path.join(os.getcwd(),component))

#--------------------------------------------------------------------
# parameters initialization

# multiplication actor from LTspice (grid of 16) to Qspice (grid of 100)
# actually 5 would be the exact factor to get the same symbol sizes, but 6.25 is better for the wire to be on the grid of 100
mult=6.25
xmult=[mult, -mult, mult, -mult, mult, -mult, mult, -mult]
ymult=[-mult, mult, -mult, mult, -mult, mult, -mult, mult]
orientation=['R0', 'R90', 'R180', 'R270', 'M0', 'M90', 'M180', 'M270']
# different text sizes allowed by LTspice or Qspice
txtsize=[str(0.4*mult/5),str(0.625*mult/5),str(1*mult/5),str(1.5*mult/5),str(2*mult/5),str(2.5*mult/5),str(3.5*mult/5),str(5*mult/5),str(7*mult/5)]
# fixed shift for the sybols positionning : 8 values depending on the orientation
shift=70
xshift=[-shift, shift, shift, -shift, shift, shift, -shift, -shift]
yshift=[shift, shift, -shift, -shift, shift, -shift, -shift, shift]
# labels orientaation values : see test_label_orient.qsch in the test directory
labelorient=['NONE', 'LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'VLEFT', 'VRIGHT', 'VBOTTOM', 'VTOP', 'CENTER', 'VCENTER']
lab_orient=['7','103','71','39','7','103','71','103']
lab_xshift=[0,1,-1,0,0,1,-1,-1,0,0]
lab_yshift=[0,0,0,-1,1,0,0,-1,-1]
lab_oshift=['0','7','11','14','13','39','43','46','45']
val_orient=[0,7,11,14,13,7,11,14,13,8,8]
val_orientshift=[0,96,76,35,0,96,67,99]
vval_orientshift=[32,0,32,64,96,67,44,64]
pin_orientshift=[0,12,76,35,0,96,0,44]
vpin_orientshift=[32,0,32,64,32,0,109,64]
# symb_on is used to gather all the symbol data, then write the lines
symb_on=False
# flag_on is used to gather all the pin data, then write the lines
flag_on=True
# many more initialization
line_flag=''
sym_name=''
xsc=0
ysc=0
xm=mult
ym=-mult
lorient='7'
comporient=0
inst_x=30
inst_y=40
inst_size='1'
inst_ort='7'
lab_ort='7'
laborient='7'
val_x=30
val_y=76
val_size='1'
val_ort='7'
valorient='7'
xshft=0
yshft=0
lshft='0'
pin_name=''

#--------------------------------------------------------------------
# start to write the first lines of the .qsch file
outfl.write(chr(0xFF)+chr(0xD8)+chr(0xFF)+chr(0xDB)+chr(0xAB)+'schematic\n')
# start to parse the .asc file, line by line
for line1 in infl:
  line=''
  line1=filter_line(line1)
  words=re.split(' ', line1)
  # print(line1)

# if symb_on, we finish to write the data of the symbol lines in a better order
  if symb_on and not re.match('^SYMATTR',line1) and not re.match('^WINDOW',line1):
    if prefix=='X' and sym_SpiceModel=='' : sym_SpiceModel=sym_name.upper()
    if sym_SpiceModel in value3.upper() : sm_dis=' -2'
    else : sm_dis=' 0'
    if sym_SpiceModel!='' :
      outfl.write('      '+chr(0xAB)+'text ('+str(int(xsc+xm*valsp_x))+','+str(int(ysc+ym*valsp_y))+') '+valsp_size+' '+valsp_ort+sm_dis+' 0x1000000 -1 -1 "'+sym_SpiceModel+'"'+chr(0xBB)+chr(0x0A))
    if value!='' :
      outfl.write(value)
    if value2!='' :
      outfl.write(value2)
    if value3!='' :
      outfl.write(value3)
    ## finally write all the pins the order of the SPICE pins order
    for i in range(1,len(pin_line)+1) :
      for j in range(0,len(pin_line)) :
        if pin_spicenumber[j]==i :
          outfl.write(pin_line[j])
    outfl.write('    '+chr(0xBB)+chr(0x0A)+'  '+chr(0xBB)+chr(0x0A))
    symb_on=False

# we finish to write the data of the pin
  if flag_on :
    flag_on=False
    if re.match('^IOPIN',line1) : line=line_flag.replace(') 1 13 0 ',') 1 13 1 ')
    else : outfl.write(line_flag)
 
 # if a symbol is found on the schematic, we initialized all the data
  if re.match('^SYMBOL ',line1) :
    symb_on=True
    sym_name=''
    inst_x=30
    inst_y=40
    lab_ort='7'
    inst_size='0.7'
    val_x=30
    val_y=76
    val_ort='7'
    val_size='0.7'
    val2_x=30
    val2_y=112
    val2_ort='7'
    val2_size='0.7'
    valsp_x=30
    valsp_y=0
    valsp_ort='7'
    valsp_size='0.7'
    pin_spicenumber=[]
    pin_line=[]
    sym_SpiceModel=''
    value=''
    value2=''
    value3=''
    
    # search the file of the symbol = comp_file
    comp_file=next((s for s in comp_LTspice if '\\'+words[1]+'.asy' in s), None)
    if comp_file==None : 
      comp_file=next((s for s in comp_LTspice if '\\'+words[1].lower()+'.asy' in s), None)
      if comp_file==None : 
        comp_file=next((s for s in comp_LTspice if '\\'+words[1].upper()+'.asy' in s), None)
        if comp_file==None : 
          print('\n'+words[1]+'.asy not found in the current path\n')

    if comp_file!=None :
      # print(str(comp_file))
      compfl=open(comp_file,"r");
      lines_comp = compfl.readlines()
      compfl.close()

      comporient=orientation.index(words[4])
      sym_name=words[1]
      # the jumpers are changed to a resistor with its 2pins shorted (2 at the end pf the line)
      if sym_name.upper()=='JUMPER' : line='  '+chr(0xAB)+'component ('+str(int(mult*int(words[2])+shift))+','+str(int(-mult*int(words[3])-shift))+') '+str(2*comporient)+' 2\n'
      else : line='  '+chr(0xAB)+'component ('+str(int(mult*int(words[2])+shift))+','+str(int(-mult*int(words[3])-shift))+') '+str(2*comporient)+' 0\n'
      line+='    '+chr(0xAB)+'symbol '+sym_name.upper()+chr(0x0A)

      # parse the symbol file to find the prefix, with a defaulft value set at X
      prefix='X'
      for linecomp in lines_comp:
        linecomp=filter_line(linecomp)
        words_comp=re.split(' ', linecomp)
        if re.match('^SYMATTR Prefix',linecomp) : prefix=words_comp[2]
      if sym_name.upper()=='JUMPER' : prefix='R'
      # check if the subckt schematic exist in the same directory : needed for the netlist
      if not os.path.exists(str(os.path.join(os.getcwd(),sym_name+'.qsch'))) :
        if os.path.exists(str(os.path.join(os.getcwd(),sym_name+'.asc'))) :
          print('\n'+sym_name+'.asc  should be converted to  '+sym_name+'.qsch')
        else : line+='      '+chr(0xAB)+'type: '+prefix+chr(0xBB)+chr(0x0A)
      line+='      '+chr(0xAB)+'shorted pins: false'+chr(0xBB)+chr(0x0A)
      
      # parse the symbol file for the description and spice model
      for linecomp in lines_comp:
        linecomp=filter_line(linecomp)
        words_comp=re.split(' ', linecomp)
        if re.match('^SYMATTR Description',linecomp) :     line+='      '+chr(0xAB)+'description: '+linecomp[linecomp.find(words_comp[2]):]+chr(0xBB)+chr(0x0A)
        if re.match('^SYMATTR SpiceLine',line) : line+='      '+chr(0xAB)+'library file: '+line[line.find(words_comp[2]):]+chr(0xBB)+chr(0x0A)
        if re.match('^SYMATTR ModelFile',line) : line+='      '+chr(0xAB)+'library file: '+line[line.find(words_comp[2]):]+chr(0xBB)+chr(0x0A)

      # parse the symbol file for the symbol patterns, pins and attributes
      xm=xmult[comporient]
      ym=ymult[comporient]
      xsc=xshift[comporient]
      ysc=yshift[comporient]
      lorient=lab_orient[comporient]
      for linecomp in lines_comp:
        linecomp=filter_line(linecomp)
        words_comp=re.split(' ', linecomp)
        if re.match('^LINE Normal ',linecomp) :
          line+='      '+chr(0xAB)+'line ('+str(int(xsc+xm*int(words_comp[2])))+','+str(int(ysc+ym*int(words_comp[3])))+') ('+str(int(xsc+xm*int(words_comp[4])))+','+str(int(ysc+ym*int(words_comp[5])))+') 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
        if re.match('^RECTANGLE Normal ',linecomp) :
          line+='      '+chr(0xAB)+'rect ('+str(int(xsc+xm*int(words_comp[2])))+','+str(int(ysc+ym*int(words_comp[3])))+') ('+str(int(xsc+xm*int(words_comp[4])))+','+str(int(ysc+ym*int(words_comp[5])))+') 0 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
        if re.match('^ARC Normal ',linecomp) :
          line+='      '+chr(0xAB)+'arc ('+str(int(xsc+xm*int(words_comp[2])))+','+str(int(ysc+ym*int(words_comp[3])))+') ('+str(int(xsc+xm*int(words_comp[4])))+','+str(int(ysc+ym*int(words_comp[5])))+') ('+str(int(xsc+xm*int(words_comp[6])))+','+str(int(ysc+ym*int(words_comp[7])))+') ('+str(int(xsc+xm*int(words_comp[8])))+','+str(int(ysc+ym*int(words_comp[9])))+') 0 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
        if re.match('^CIRCLE Normal ',linecomp) :
          line+='      '+chr(0xAB)+'ellipse ('+str(int(xsc+xm*int(words_comp[2])))+','+str(int(ysc+ym*int(words_comp[3])))+') ('+str(int(xsc+xm*int(words_comp[4])))+','+str(int(ysc+ym*int(words_comp[5])))+') 0 0 0 0x00A000 -1 -1'+chr(0xBB)+chr(0x0A)
        if re.match('^SYMATTR Value ',linecomp) :
          if prefix=='X' and sym_SpiceModel=='' : sym_SpiceModel=linecomp[linecomp.find(words_comp[2]):]
          else : value='      '+chr(0xAB)+'text ('+str(int(xsc+xm*val_x))+','+str(int(ysc+ym*val_y))+') '+val_size+' '+val_ort+' 0 0x1000000 -1 -1 "'+linecomp[linecomp.find(words_comp[2]):]+'"'+chr(0xBB)+chr(0x0A)
        if re.match('^SYMATTR Value2 ',linecomp) :
          value2='      '+chr(0xAB)+'text ('+str(int(xsc+xm*val2_x))+','+str(int(ysc+ym*val2_y))+') '+val2_size+' '+val2_ort+' 0 0x1000000 -1 -1 "'+linecomp[linecomp.find(words_comp[2]):]+'"'+chr(0xBB)+chr(0x0A)
        if re.match('^SYMATTR SpiceModel ',linecomp) :
          sym_SpiceModel=linecomp[linecomp.find(words_comp[2]):]
        if re.match('^TEXT ',linecomp) :
          if (words_comp[3][0]=='V' and comporient!=1 and comporient!=3 and comporient!=5 and comporient!=7) or (words_comp[3][0]!='V' and comporient!=0 and comporient!=2 and comporient!=4 and comporient!=6) :
            txtort=str(val_orient[labelorient.index(words_comp[3].upper())]^vpin_orientshift[comporient])
            if txtort=='7' or txtort=='11' or txtort=='13' or txtort=='14' : txtort='15'
            if txtort=='96' : txtort='97'
            if txtort=='32' : txtort='39'
            vshft=-1
          else : 
            txtort=str(val_orient[labelorient.index(words_comp[3].upper())]^pin_orientshift[comporient])
            vshft=1
          value3+='      '+chr(0xAB)+'text ('+str(int(xsc+xm*int(words_comp[1])))+','+str(int(ysc+ym*int(words_comp[2])))+') '+txtsize[int(words_comp[4])]+' '+txtort+' 1 0x005000 -1 -1 "'+linecomp[linecomp.find(words_comp[5]):]+'"'+chr(0xBB)+chr(0x0A)
        if re.match('^PIN ',linecomp) :
          x_pin=int(words_comp[1])
          y_pin=int(words_comp[2])
          if (words_comp[3][0]=='V' and comporient!=1 and comporient!=3 and comporient!=5 and comporient!=7) or (words_comp[3][0]!='V' and comporient!=0 and comporient!=2 and comporient!=4 and comporient!=6) :
            pinort=str(val_orient[labelorient.index(words_comp[3].upper())]^vpin_orientshift[comporient])
            if pinort=='7' or pinort=='11' or pinort=='13' or pinort=='14' : pinort='12'
            if pinort=='96' : pinort='97'
            vshft=-1
          else : 
            pinort=str(val_orient[labelorient.index(words_comp[3].upper())]^pin_orientshift[comporient])
            vshft=1
          xshft=lab_xshift[labelorient.index(words_comp[3].upper())]*mult*int(words_comp[4])*vshft
          yshft=lab_yshift[labelorient.index(words_comp[3].upper())]*mult*int(words_comp[4])*vshft
          lshft=lab_oshift[labelorient.index(words_comp[3].upper())]
        if re.match('^PINATTR PinName ',linecomp) :
          pin_name=words_comp[2].replace('+','P').replace('-','M')
          pin_line.append('      '+chr(0xAB)+'pin ('+str(int(xsc+xm*x_pin))+','+str(int(ysc+ym*y_pin))+') ('+str(int(xshft))+','+str(int(yshft))+') 1 '+pinort+' 0 0x005000 -1 "'+pin_name+'"'+chr(0xBB)+chr(0x0A))
          pin_name=''
        if re.match('^PINATTR SpiceOrder ',linecomp) :
          pin_spicenumber.append(int(words_comp[2]))
        if re.match('^WINDOW 0 ',linecomp):
          inst_x=int(words_comp[2])
          inst_y=int(words_comp[3])
          inst_ort=str(val_orient[labelorient.index(words_comp[4].upper())])
          inst_size=txtsize[max(0,int(words_comp[5])-1)]
        if re.match('^WINDOW 3 ',linecomp):
          val_x=int(words_comp[2])
          val_y=int(words_comp[3])
          val_ort=str(val_orient[labelorient.index(words_comp[4].upper())])
          val_size=txtsize[max(0,int(words_comp[5])-1)]
        if re.match('^WINDOW 123 ',linecomp):
          val2_x=int(words_comp[2])
          val2_y=int(words_comp[3])
          val2_ort=str(val_orient[labelorient.index(words_comp[4].upper())])
          val2_size=txtsize[max(0,int(words_comp[5])-1)]
        if re.match('^WINDOW 38 ',linecomp):
          valsp_x=int(words_comp[2])
          valsp_y=int(words_comp[3])
          valsp_ort=str(val_orient[labelorient.index(words_comp[4].upper())])
          valsp_size=txtsize[max(0,int(words_comp[5])-1)]

# if a symbol is started some location and orientation and text size may be adjusted in the schematic
  # for the instance name
  if symb_on and (re.match('^SYMATTR InstName',line1)):
    line='      '+chr(0xAB)+'text ('+str(int(xsc+xm*inst_x))+','+str(int(ysc+ym*inst_y))+') '+inst_size+' '+lab_ort+' 0 0x1000000 -1 -1 "'+words[2]+'"'+chr(0xBB)+chr(0x0A)
  if symb_on and (re.match('^WINDOW 0 ',line1)):
    inst_x=int(words[2])
    inst_y=int(words[3])
    if (words[4][0]=='V' and comporient!=1 and comporient!=3 and comporient!=5 and comporient!=7) or (words[4][0]!='V' and comporient!=0 and comporient!=2 and comporient!=4 and comporient!=6) :
      lab_ort=str(val_orient[labelorient.index(words[4].upper())]^vval_orientshift[comporient])
    else : lab_ort=str(val_orient[labelorient.index(words[4].upper())]^val_orientshift[comporient])
    inst_size=txtsize[int(words[5])-1]

  # for the value
  if symb_on and (re.match('^WINDOW 3 ',line1)):
    val_x=int(words[2])
    val_y=int(words[3])
    if (words[4][0]=='V' and comporient!=1 and comporient!=3 and comporient!=5 and comporient!=7) or (words[4][0]!='V' and comporient!=0 and comporient!=2 and comporient!=4 and comporient!=6) :
      val_ort=str(val_orient[labelorient.index(words[4].upper())]^vval_orientshift[comporient])
    else : val_ort=str(val_orient[labelorient.index(words[4].upper())]^val_orientshift[comporient])
    val_size=txtsize[int(words[5])-1]
  if symb_on and (re.match('^SYMATTR Value ',line1)):
    value='      '+chr(0xAB)+'text ('+str(int(xsc+xm*val_x))+','+str(int(ysc+ym*val_y))+') '+val_size+' '+val_ort+' 0 0x1000000 -1 -1 "'+line1[line1.find(words[2]):]+'"'+chr(0xBB)+chr(0x0A)

  # for the value2
  if symb_on and (re.match('^WINDOW 123 ',line1)):
    val2_x=int(words[2])
    val2_y=int(words[3])
    if (words[4][0]=='V' and comporient!=1 and comporient!=3 and comporient!=5 and comporient!=7) or (words[4][0]!='V' and comporient!=0 and comporient!=2 and comporient!=4 and comporient!=6) :
      val2_ort=str(val_orient[labelorient.index(words[4].upper())]^vval_orientshift[comporient])
    else : val2_ort=str(val_orient[labelorient.index(words[4].upper())]^val_orientshift[comporient])
    val2_size=txtsize[int(words[5])-1]
  if symb_on and (re.match('^SYMATTR Value2 ',line1)):
    value2='      '+chr(0xAB)+'text ('+str(int(xsc+xm*val2_x))+','+str(int(ysc+ym*val2_y))+') '+val2_size+' '+val2_ort+' 0 0x1000000 -1 -1 "'+line1[line1.find(words[2]):]+'"'+chr(0xBB)+chr(0x0A)

 # for the SpiceModel
  if symb_on and re.match('^SYMATTR SpiceModel ',line1) :
    sym_SpiceModel='"'+line1[line1.find(words[2]):]+'"'
  if symb_on and (re.match('^WINDOW 38 ',line1)):
    valsp_x=int(words[2])
    valsp_y=int(words[3])
    if (words[4][0]=='V' and comporient!=1 and comporient!=3 and comporient!=5 and comporient!=7) or (words[4][0]!='V' and comporient!=0 and comporient!=2 and comporient!=4 and comporient!=6) :
      valsp_ort=str(val_orient[labelorient.index(words[4].upper())]^vval_orientshift[comporient])
    else : valsp_ort=str(val_orient[labelorient.index(words[4].upper())]^val_orientshift[comporient])
    valsp_size=txtsize[int(words[5])-1]

  # write all the schematic data
  if re.match('^WIRE',line1) :
    line='  '+chr(0xAB)+'wire ('+str(int(mult*int(words[1])))+','+str(int(-mult*int(words[2])))+') ('+str(int(mult*int(words[3])))+','+str(int(-mult*int(words[4])))+') ""'+chr(0xBB)+chr(0x0A)
  if re.match('^FLAG',line1) : 
    flag_on=True
    line_flag='  '+chr(0xAB)+'net ('+str(int(mult*int(words[1])))+','+str(int(-mult*int(words[2])))+') 1 13 0 "'+words[3]+'"'+chr(0xBB)+chr(0x0A)
  if re.match('^TEXT',line1) :
    # '!' = spice command text, ';' = comment text
    if words[5][0]=='!': tt=' 0'
    else : tt=' 1'
    if words[3][0]=='V' : txtorient=str(val_orient[labelorient.index(words[3].upper())]+32)
    else : txtorient=str(val_orient[labelorient.index(words[3].upper())])
    line='  '+chr(0xAB)+'text ('+str(int(mult*int(words[1])))+','+str(int(-mult*int(words[2])))+') '+txtsize[int(words[4])]+' '+txtorient+tt+' "'+chr(0xEF)+chr(0xBB)+chr(0xBF)+line1[line1.find(words[5])+1:]+'"'+chr(0xBB)+chr(0x0A)
  if re.match('^LINE Normal',line1) :
    if len(words)==6 : lin_shp='0'
    else : lin_shp=words[6]
    line='  '+chr(0xAB)+'line ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') 0 '+lin_shp+' 0xff0000 -1 -1'+chr(0xBB)+chr(0x0A)
  if re.match('^RECTANGLE Normal',line1) :
    if len(words)==6 : lin_shp='0'
    else : lin_shp=words[6]
    line='  '+chr(0xAB)+'rect ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') 0 0 '+lin_shp+' 0x4000000 0x1000000 -1 0 -1'+chr(0xBB)+chr(0x0A)
  if re.match('^CIRCLE Normal',line1) :
    if len(words)==6 : lin_shp='0'
    else : lin_shp=words[6]
    line='  '+chr(0xAB)+'ellipse ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') 0 0 '+lin_shp+' 0x4000000 0x1000000 -1 0'+chr(0xBB)+chr(0x0A)
  if re.match('^ARC Normal',line1) :
    if len(words)==6 : lin_shp='0'
    else : lin_shp=words[10]
    line='  '+chr(0xAB)+'arc ('+str(int(mult*int(words[2])))+','+str(int(-mult*int(words[3])))+') ('+str(int(mult*int(words[4])))+','+str(int(-mult*int(words[5])))+') ('+str(int(mult*int(words[6])))+','+str(int(-mult*int(words[7])))+') ('+str(int(mult*int(words[8])))+','+str(int(-mult*int(words[9])))+') 0 0 '+lin_shp+' 0x4000000 0xff0000 -1 -1'+chr(0xBB)+chr(0x0A)

  # finally write the line to the .qsch file
  outfl.write(line)

#--------------------------------------------------------------------
# all lines have been parsed : close the file .qsch properly

# we finish to write the symbol
if symb_on :
  if prefix=='X' and sym_SpiceModel=='' : sym_SpiceModel=sym_name.upper()
  if sym_SpiceModel in value3.upper() : sm_dis=' -2'
  else : sm_dis=' 0'
  if sym_SpiceModel!='' :
    outfl.write('      '+chr(0xAB)+'text ('+str(int(xsc+xm*valsp_x))+','+str(int(ysc+ym*valsp_y))+') '+valsp_size+' '+valsp_ort+sm_dis+' 0x1000000 -1 -1 "'+sym_SpiceModel+'"'+chr(0xBB)+chr(0x0A))
  if value!='' :
    outfl.write(value)
  if value2!='' :
    outfl.write(value2)
  if value3!='' :
    outfl.write(value3)
  ## finally write all the pins the order of the SPICE pin order
  for i in range(1,len(pin_line)+1) :
    for j in range(0,len(pin_line)) :
      if pin_spicenumber[j]==i :
        outfl.write(pin_line[j])
  outfl.write('    '+chr(0xBB)+chr(0x0A)+'  '+chr(0xBB)+chr(0x0A))
  symb_on=False

# we finish to write the pin
if flag_on :
  flag_on=False
  outfl.write(line_flag)

# character » to close the .qsch file
outfl.write(chr(0xBB)+chr(0x0A))

infl.close()

outfl.close()
