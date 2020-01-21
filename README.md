# Emittance growth due to rf noise in the crab cavities.
An Ipython script for plotting the emittance growth over tracking in the presence of phase and amplitude noise.
The turn by turn data are obtained by simulations performed using sixtracklib. 
All the data are saved in : /eos/user/n/natriant/sixtracklib_data.

### Prerequisites
You need to configure AFS client for access to cern.ch on Ubuntu/Debian. If not done already follow see thw twiki page below:
https://twiki.cern.ch/twiki/bin/view/ABPComputing/AFSDebian

### Run
In order to be able to use the data without copying them locally you need to copy them from /eos/ to an /afs/ directory.
To make sure that you have access to the directory execute in your terminal:
$ ssh USERNAME@CERN.CH
$ aklog
