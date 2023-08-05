from localstack.utils.aws import aws_models
auEGs=super
auEGQ=None
auEGF=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  auEGs(LambdaLayer,self).__init__(arn)
  self.cwd=auEGQ
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.auEGF.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(RDSDatabase,self).__init__(auEGF,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(RDSCluster,self).__init__(auEGF,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(AppSyncAPI,self).__init__(auEGF,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(AmplifyApp,self).__init__(auEGF,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(ElastiCacheCluster,self).__init__(auEGF,env=env)
class TransferServer(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(TransferServer,self).__init__(auEGF,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(CloudFrontDistribution,self).__init__(auEGF,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,auEGF,env=auEGQ):
  auEGs(CodeCommitRepository,self).__init__(auEGF,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
