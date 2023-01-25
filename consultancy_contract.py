from pyteal import *

class Booking:
    class Variables:
        name = Bytes("NAME")
        duration = Bytes("DURATION")
        description = Bytes("DESCRIPTION")
        price = Bytes("PRICE")
        time = Bytes("TIME")

    class AppMethods:
        buy = Bytes("buy")

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