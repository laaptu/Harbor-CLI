class FirebasePlugin():

    def apply(self, compiler):
        compiler.plugin('will_invite', self.will_invite)
        compiler.plugin('did_invite', self.did_invite)
        compiler.plugin('did_register', self.did_register)
        compiler.plugin('will_register', self.will_register)
        compiler.plugin('did_deploy', self.did_deploy)
        compiler.plugin('will_deploy', self.will_deploy)

    def did_invite(self):
        pass

    def will_invite(self, compilation):
        pass

    def will_register(self, compilation):
        pass

    def did_register(self, compilation):
        pass

    def will_deploy(self, compilation):
        pass

    def did_deploy(self, compilation):
        pass
