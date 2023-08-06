from localstack.utils.aws import aws_models
LBUxq=super
LBUxw=None
LBUxN=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  LBUxq(LambdaLayer,self).__init__(arn)
  self.cwd=LBUxw
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.LBUxN.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(RDSDatabase,self).__init__(LBUxN,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(RDSCluster,self).__init__(LBUxN,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(AppSyncAPI,self).__init__(LBUxN,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(AmplifyApp,self).__init__(LBUxN,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(ElastiCacheCluster,self).__init__(LBUxN,env=env)
class TransferServer(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(TransferServer,self).__init__(LBUxN,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(CloudFrontDistribution,self).__init__(LBUxN,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,LBUxN,env=LBUxw):
  LBUxq(CodeCommitRepository,self).__init__(LBUxN,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
