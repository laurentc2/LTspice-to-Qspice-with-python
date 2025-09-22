## LTspice to Qspice

Here are some python scripts for the lazy guys to transfer schematics, symbols and plot from LTspice to Qspice.

I recommend to use the *'official'* method : import a spice netlist and redraw the schematic. It is the best to understand each component function in the circuit.
 
The goal under that script is to try quickly Qspice and compare it to LTspice and NGspice.

My personal conclusion : none is the best choice :
+ LTspice is very accurate especially for oscillation and for the component of Analog Devices !
+ Qspice is very fast with a good accuracy
+ NGspice is slower but very versatile with its .control commands and osdi VA-models support

### usage :

**python LT2Qspice.py my_schematic.asc**  : will generate  **my_schematic.qsch** file.

**python sym_LT2Qspice.py my_symbol.asy**  : will generate  **my_symbol.qsym** file.

**python plt_LT2Qspice.py my_simulation.plt**  :  will generate  **my_simulation.pfg** file.


### limitations :

If a schematic includes a symbol of Analog Devices, it will either no be in the schematic, or not be in the spice netlist.
At least, there will be a problem with its simulation.

Many .sub file are not automatically included in the spice netlist.

### to go further :

I encourage you to fork it and improve it or simply suggest me some improvement.

Unfortunately, I may not have time to help you if it does work for you :worried:

:star: If you like it, star it ! :smiley:
