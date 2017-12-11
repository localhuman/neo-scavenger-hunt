from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete


class StorageAPI():

    ctx = GetContext()

    def getitem(self, key):

        return Get(self.ctx, key)

    def putitem(self, key, value):

        Put(self.ctx, key, value)

    def deleteitem(self, key):

        Delete(self.ctx, key)
