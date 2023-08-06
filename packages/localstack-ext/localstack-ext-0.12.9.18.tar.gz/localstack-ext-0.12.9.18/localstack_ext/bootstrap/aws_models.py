from localstack.utils.aws import aws_models
lDgwK=super
lDgwn=None
lDgwR=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  lDgwK(LambdaLayer,self).__init__(arn)
  self.cwd=lDgwn
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.lDgwR.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(RDSDatabase,self).__init__(lDgwR,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(RDSCluster,self).__init__(lDgwR,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(AppSyncAPI,self).__init__(lDgwR,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(AmplifyApp,self).__init__(lDgwR,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(ElastiCacheCluster,self).__init__(lDgwR,env=env)
class TransferServer(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(TransferServer,self).__init__(lDgwR,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(CloudFrontDistribution,self).__init__(lDgwR,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,lDgwR,env=lDgwn):
  lDgwK(CodeCommitRepository,self).__init__(lDgwR,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
