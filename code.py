from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

import board
from digitalio import DigitalInOut, Direction

D12 = DigitalInOut(board.D12)
D12.direction = Direction.OUTPUT
D11 = DigitalInOut(board.D11)
D11.direction = Direction.OUTPUT
D10 = DigitalInOut(board.D10)
D10.direction = Direction.OUTPUT
D9 = DigitalInOut(board.D9)
D9.direction = Direction.OUTPUT


ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1:
                        # The button_1 was pressed.
                        D12.value = not D12.value
                    elif packet.button == ButtonPacket.BUTTON_2:
                        # The button_2 was pressed.
                        D11.value = not D11.value
                    elif packet.button == ButtonPacket.BUTTON_3:
                        # The button_3 was pressed.
                        D10.value = not D10.value
                    elif packet.button == ButtonPacket.BUTTON_4:
                        # The button_4 was pressed.
                        D9.value = not D9.value
                    