from pyteal import *


class Booking:
    class Variables:
        name = Bytes("NAME")
        duration = Bytes("DURATION")
        description = Bytes("DESCRIPTION")
        price = Bytes("PRICE")
        time = Bytes("TIME")

    class AppMethods:
        book = Bytes("book")

    def application_creation(self):
        return Seq([
            Assert(Txn.application_args.length() == Int(4)),
            Assert(Txn.note() == Bytes("nutrition-consultancy:uv1")),
            Assert(Btoi(Txn.application_args[3]) > Int(0)),
            App.globalPut(self.Variables.name, Txn.application_args[0]),
            App.globalPut(self.Variables.duration, Txn.application_args[1]),
            App.globalPut(self.Variables.description, Txn.application_args[2]),
            App.globalPut(self.Variables.price, Btoi(Txn.application_args[3])),
            App.globalPut(self.Variables.time, Int(1)),
            Approve()
        ])

    def book(self):
        valid_number_of_transactions = Global.group_size() == Int(2)

        valid_payment_to_seller = And(
            Gtxn[1].type_enum() == TxnType.Payment,
            Gtxn[1].receiver() == Global.creator_address(),
            Gtxn[1].amount() == App.globalGet(self.Variables.price) *
            App.globalGet(self.Variables.duration),
            Gtxn[1].sender() == Gtxn[0].sender(),
        )

        can_book = And(valid_number_of_transactions,
                       valid_payment_to_seller)

        return If(can_book).Then(Approve()).Else(Reject())
