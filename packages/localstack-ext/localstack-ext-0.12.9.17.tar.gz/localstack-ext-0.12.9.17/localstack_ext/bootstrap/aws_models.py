from localstack.utils.aws import aws_models
XTCQs=super
XTCQu=None
XTCQY=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  XTCQs(LambdaLayer,self).__init__(arn)
  self.cwd=XTCQu
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.XTCQY.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(RDSDatabase,self).__init__(XTCQY,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(RDSCluster,self).__init__(XTCQY,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(AppSyncAPI,self).__init__(XTCQY,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(AmplifyApp,self).__init__(XTCQY,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(ElastiCacheCluster,self).__init__(XTCQY,env=env)
class TransferServer(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(TransferServer,self).__init__(XTCQY,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(CloudFrontDistribution,self).__init__(XTCQY,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,XTCQY,env=XTCQu):
  XTCQs(CodeCommitRepository,self).__init__(XTCQY,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
