from localstack.utils.aws import aws_models
TukHr=super
TukHa=None
TukHw=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  TukHr(LambdaLayer,self).__init__(arn)
  self.cwd=TukHa
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.TukHw.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(RDSDatabase,self).__init__(TukHw,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(RDSCluster,self).__init__(TukHw,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(AppSyncAPI,self).__init__(TukHw,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(AmplifyApp,self).__init__(TukHw,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(ElastiCacheCluster,self).__init__(TukHw,env=env)
class TransferServer(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(TransferServer,self).__init__(TukHw,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(CloudFrontDistribution,self).__init__(TukHw,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,TukHw,env=TukHa):
  TukHr(CodeCommitRepository,self).__init__(TukHw,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
