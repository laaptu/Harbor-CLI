class MailPlugin():

    def apply(self, compiler):
        compiler.plugin('deploy/will_deploy', self.will_deploy)
        compiler.plugin('deploy/did_deploy', self.did_deploy)
        print('registered mail plugins')


    def will_deploy(self, compilation, *args, **kwargs):
        print('will_deploy received compilation: ',  compilation)

    def did_deploy(self, compilation, *args, **kwargs):
        print('did_deploy received compilation: ',  compilation)
