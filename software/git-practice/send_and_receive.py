import multiprocessing

import select
import time

import lcm

from test_message import test_message


def sender(chanel: str):
    message = test_message()
    _lcm = lcm.LCM()

    # # Sample
    # message.name = "Mathieu Tuli"
    # message.value = "TEST VALUE"
    # _lcm.publish(chanel, message.encode())
    # # End of sample

    message.name = "Divy Raval"
    message.value = "Git TEST VALUE"
    _lcm.publish(chanel, message.encode())
    # ADD CODE HERE
    ################
    # ADD CODE HERE
    message.name = "Practice Test"
    _lcm.publish(chanel, message.encode())
    ################
    # ADD CODE HERE
    ################
    message.name = "Divy Raval"
    message.value = "Git TEST VALUE"
    _lcm.publish(chanel, message.encode())
    message.name = "Joseph"
    message.value = "test"
    _lcm.publish(chanel, message.encode())
    message.name = "Rama"
    message.value = "Rama is testing"
    _lcm.publish(chanel, message.encode())


def listener(channel, data):
    message = test_message.decode(data)
    print(f"\nReceived test_message on {channel}")
    print(f"    {message.name}")
    print(f"    {message.value}")


def main():
    channel_name = "PRACTICE"
    sender_process = multiprocessing.Process(
        target=sender, args=(channel_name,))
    sender_process.start()

    lcm_1 = lcm.LCM()
    lcm_1.subscribe(channel_name, listener)

    timeout = 2
    while True:
        try:
            rfds, wfds, efds = select.select([lcm_1.fileno()], [], [],
                                             timeout)
            if rfds:
                lcm_1.handle()
            else:
                print("\nLCM 1: I think that's all folks")
        except KeyboardInterrupt:
            break


main()
