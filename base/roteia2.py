# CC 13 runs/terminates the klick process (alternatively,
# run "klick -P -o 1234"),
# CC 14 starts/stops the metronome, and CC 15 changes tempo.
#

from mididings import *
from mididings.extra.osc import SendOSC

port = 1235

run(
    Filter(NOTEON) >> KeySplit({
        48: SendOSC(port, '/button1', lambda ev: ev.velocity),
        49: SendOSC(port, '/button2', lambda ev: ev.velocity),
        50: SendOSC(port, '/button3', lambda ev: ev.velocity),
        51: SendOSC(port, '/button4', lambda ev: ev.velocity),
        44: SendOSC(port, '/button5', lambda ev: ev.velocity),
        45: SendOSC(port, '/button6', lambda ev: ev.velocity),
        46: SendOSC(port, '/button7', lambda ev: ev.velocity),
        47: SendOSC(port, '/button8', lambda ev: ev.velocity),
        40: SendOSC(port, '/button9', lambda ev: ev.velocity),
        41: SendOSC(port, '/button10', lambda ev: ev.velocity),
        42: SendOSC(port, '/button11', lambda ev: ev.velocity),
        43: SendOSC(port, '/button12', lambda ev: ev.velocity),
        36: SendOSC(port, '/button13', lambda ev: ev.velocity),
        37: SendOSC(port, '/button14', lambda ev: ev.velocity),
        38: SendOSC(port, '/button15', lambda ev: ev.velocity),
	39: SendOSC(port, '/button16', lambda ev: ev.note)
            })
)
#48 49 50 51 44 45 46 47 40 41 42 43 36 37 38 39
