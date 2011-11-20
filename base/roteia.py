# CC 13 runs/terminates the klick process (alternatively,
# run "klick -P -o 1234"),
# CC 14 starts/stops the metronome, and CC 15 changes tempo.
#

from mididings import *
from mididings.extra.osc import SendOSC

port = 1234

run(
    Filter(CTRL) >> CtrlSplit({
        80: SendOSC(port, '/slider1', lambda ev: ev.value),
        81: SendOSC(port, '/slider2', lambda ev: ev.value),
        82: SendOSC(port, '/slider3', lambda ev: ev.value),
        83: SendOSC(port, '/slider4', lambda ev: ev.value),
        84: SendOSC(port, '/slider5', lambda ev: ev.value),
        85: SendOSC(port, '/slider6', lambda ev: ev.value),
        86: SendOSC(port, '/slider7', lambda ev: ev.value),
        87: SendOSC(port, '/slider8', lambda ev: ev.value),
        41: SendOSC(port, '/fader1', lambda ev: ev.value),
        42: SendOSC(port, '/fader2', lambda ev: ev.value),
        43: SendOSC(port, '/fader3', lambda ev: ev.value),
        44: SendOSC(port, '/fader4', lambda ev: ev.value),
        45: SendOSC(port, '/fader5', lambda ev: ev.value),
        46: SendOSC(port, '/fader6', lambda ev: ev.value),
        47: SendOSC(port, '/fader7', lambda ev: ev.value),
        48: SendOSC(port, '/fader8', lambda ev: ev.value)
    })
)

