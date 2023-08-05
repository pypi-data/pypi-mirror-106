from localstack.utils.aws import aws_models
eKLvY=super
eKLvc=None
eKLvP=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  eKLvY(LambdaLayer,self).__init__(arn)
  self.cwd=eKLvc
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.eKLvP.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(RDSDatabase,self).__init__(eKLvP,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(RDSCluster,self).__init__(eKLvP,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(AppSyncAPI,self).__init__(eKLvP,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(AmplifyApp,self).__init__(eKLvP,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(ElastiCacheCluster,self).__init__(eKLvP,env=env)
class TransferServer(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(TransferServer,self).__init__(eKLvP,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(CloudFrontDistribution,self).__init__(eKLvP,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,eKLvP,env=eKLvc):
  eKLvY(CodeCommitRepository,self).__init__(eKLvP,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
