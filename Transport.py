# Transport.py

# This is a stripped-down script, which uses the Framework classes to assign MIDI notes to play, stop and record.

# Central base class for scripts based on the new Framework
from _Framework.ControlSurface import ControlSurface

# Class encapsulating all functions in Live's transport section
from _Framework.TransportComponent import TransportComponent

# Class representing a button a the controller
from _Framework.ButtonElement import ButtonElement 


class Transport(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)

        # Instantiate a Transport Component
        transport = TransportComponent()

        # ButtonElement(is_momentary, msg_type, channel, identifier)
        transport.set_play_button(ButtonElement(True, 0, 0, 118))
        transport.set_stop_button(ButtonElement(True, 0, 0, 117))
        transport.set_record_button(ButtonElement(True, 0, 0, 119))
