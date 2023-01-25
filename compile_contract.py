from pyteal import *

from consultancy_contract import Booking

if __name__ == "__main__":
    approval_program = Booking().approval_program()
    clear_program = Booking().clear_program()

    compiled_approval = compileTeal(
        approval_program, Mode.Application, version=6)
    print(compiled_approval)
    with open("consultancy_approval.teal", "w") as teal:
        teal.write(compiled_approval)
        teal.close()

    # Mode.Application specifies that this is a smart contract
    compiled_clear = compileTeal(clear_program, Mode.Application, version=6)
    print(compiled_clear)
    with open("consultancy_clear.teal", "w") as teal:
        teal.write(compiled_clear)
        teal.close()
