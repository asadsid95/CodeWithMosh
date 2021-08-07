class MasterClass():

    def __init__(self, redshift_conn_id="some passed down value", *arg, **kwargs):
        print("Master constructor")
        self.redshift = redshift_conn_id
        print("this prints redshift variable from parent's __init__", self.redshift)


    def execute(self):
        print("redshift conn id: ", self.redshift)

#master = MasterClass()
#print(master.execute())

class SubClass(MasterClass):

    def __init__(self, table="some rows and columns"):
        print("Sub Constructor")
        print("table: ", table)
        super().__init__()
        super().execute()



sub = SubClass()
print(sub.__init__())
#print(SubClass().__mro__)