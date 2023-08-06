from localstack.utils.aws import aws_models
eitlj=super
eitlP=None
eitlD=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  eitlj(LambdaLayer,self).__init__(arn)
  self.cwd=eitlP
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.eitlD.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(RDSDatabase,self).__init__(eitlD,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(RDSCluster,self).__init__(eitlD,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(AppSyncAPI,self).__init__(eitlD,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(AmplifyApp,self).__init__(eitlD,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(ElastiCacheCluster,self).__init__(eitlD,env=env)
class TransferServer(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(TransferServer,self).__init__(eitlD,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(CloudFrontDistribution,self).__init__(eitlD,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,eitlD,env=eitlP):
  eitlj(CodeCommitRepository,self).__init__(eitlD,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
