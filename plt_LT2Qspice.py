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
#  last change: 2025, Sep 23.
#
# usage example : python plt_LT2Qspice.py Draft0.plt
#       This example will create the file : Draft0.pfg
#

import os,sys,re

in_file = sys.argv[1]
# infl = open(in_file,"r", encoding='ISO-8859-1', errors='replace');
if (in_file[-3:])!='plt' : 
  print('\n'+in_file+' is not a .plt plot file\n')
  sys.exit(0)
if os.path.exists(in_file) : 
  infl = open(in_file,"r", encoding='latin-1', errors='replace');
  out_file = in_file.replace(".plt" , ".pfg")
else : 
  print('\n'+in_file+' not found\n')
  sys.exit(0)
outfl = open(out_file,'w',encoding='utf-16le');

def filter_line(line):
  line=line.rstrip('\n')
  line=line.rstrip('\r')
  return line

unit=''
signals=[]
line=''
for line1 in infl:
  line1=filter_line(line1)
  # print(line1)

  if re.match('^AC',line1[1:]) : unit='Hz'
  if re.match('^Transient',line1[1:]) : unit='s'
  if re.match('^Noise',line1[1:]) : unit='V/Hz½ or A/Hz½'

  if re.match('^      traces:',line1) :
    words=re.split('"', line1)
    line='{{'
    for i in range(1,len(words),2) :
      if ':' in words[i] :
        subckt=re.split(':',words[i])
        line+=words[i][:words[i].find('(')+1]
        subckt[0]=subckt[0][words[i].find('(')+1:]
        subckt[len(subckt)-1]=subckt[len(subckt)-1][:-1]
        for j in range(len(subckt)-1,-1,-1) :
          line+=subckt[j]+chr(0x2022)
        line=line[:-1]+') '+str(int((i+1)/2))+', '
      else : line+=words[i]+' '+str(int((i+1)/2))+', '
    line=line[:-2]+'}'

  if re.match('^      X:',line1) :
    words=re.split(',', line1)
    line+='{"",0,0,'+words[2]+','+str((float(words[3])-float(words[3]))/10)+','+words[3]+',1,0,1,'+unit+'}'
  if re.match(r'^      Y\[0\]',line1) :
    words=re.split(',', line1)
    if words[2]=='1e+308' : line=''
    else : line+='{"",'+words[2]+','+words[3]+','+words[4][:-1]+'1,1,0}}}'
  if re.match(r'^      Y\[1\]:',line1) :
    words=re.split(',', line1)
    if words[2]!='1e+308' :
      line=line[:-2]+',{"",'+words[2]+','+words[3]+','+words[4][:-1]+'1,1,0}}}'

  if re.match('^   }',line1) and line!='':
    outfl.write(line+'\n')
    line=''

infl.close()
outfl.close()
