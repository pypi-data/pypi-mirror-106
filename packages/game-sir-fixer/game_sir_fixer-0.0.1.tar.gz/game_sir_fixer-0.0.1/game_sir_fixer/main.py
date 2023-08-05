import pygame
import pyvjoy
from game_sir_fixer.helpers import ScaleFloatToHex, ScaleFloatToHexInvert, HandleJoyButton, HandleJoyHatMotion

pygame.init()

pygame.joystick.init()
joysticks = [
    pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())
]
print(len(joysticks), 'controller detected')

print('creating a virtual controller')
c = pyvjoy.VJoyDevice(1)
print('virtual controller is ready')
while True:
    for event in pygame.event.get():
        if hasattr(event, 'joy') and event.joy == 0:

            if event.type in {
                pygame.JOYBUTTONUP,
                pygame.JOYBUTTONDOWN,
            }:
                a, k = HandleJoyButton(event.type, event.button)
                c.set_button(
                    *a, **k
                )
            elif event.type in {
                pygame.JOYHATMOTION,
            }:

                for a in HandleJoyHatMotion(event.value):
                    c.set_button(*a)

            elif event.type == pygame.JOYAXISMOTION:
                axis = {
                    0: pyvjoy.HID_USAGE_X,  # left stick x
                    1: pyvjoy.HID_USAGE_Y,  # left stick y
                    2: pyvjoy.HID_USAGE_RX,  # right stick x
                    3: pyvjoy.HID_USAGE_RY,  # right stick y
                    4: pyvjoy.HID_USAGE_Z,  # left analog trigger
                    5: pyvjoy.HID_USAGE_RZ,  # right analog trigger
                }[event.axis]

                v = ScaleFloatToHex(event.value) if event.axis != 4 else ScaleFloatToHexInvert(event.value)
                # print('event.value=', event.value, ', v=', v)
                c.set_axis(
                    axis,
                    v
                )
        else:
            # print('ignore')
            pass
