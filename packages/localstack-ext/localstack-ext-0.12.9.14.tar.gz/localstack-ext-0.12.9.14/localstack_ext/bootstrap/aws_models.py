from localstack.utils.aws import aws_models
USQBd=super
USQBT=None
USQBG=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  USQBd(LambdaLayer,self).__init__(arn)
  self.cwd=USQBT
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.USQBG.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(RDSDatabase,self).__init__(USQBG,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(RDSCluster,self).__init__(USQBG,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(AppSyncAPI,self).__init__(USQBG,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(AmplifyApp,self).__init__(USQBG,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(ElastiCacheCluster,self).__init__(USQBG,env=env)
class TransferServer(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(TransferServer,self).__init__(USQBG,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(CloudFrontDistribution,self).__init__(USQBG,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,USQBG,env=USQBT):
  USQBd(CodeCommitRepository,self).__init__(USQBG,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
