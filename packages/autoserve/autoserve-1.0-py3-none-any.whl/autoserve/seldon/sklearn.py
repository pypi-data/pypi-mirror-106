from kubernetes import client, config
from subprocess import run, Popen, PIPE

config.load_kube_config()
k8s_beta = client.ExtensionsV1beta1Api()

def secret(DEPLOY_NAMESPACE, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_HOST, SECRET_NAME):
    secret = f"""apiVersion: v1
kind: Secret
metadata:
  name: {SECRET_NAME}
  namespace: {DEPLOY_NAMESPACE}
type: Opaque
stringData:
  AWS_ACCESS_KEY_ID: {MINIO_ACCESS_KEY}
  AWS_SECRET_ACCESS_KEY: {MINIO_SECRET_KEY}
  AWS_ENDPOINT_URL: http://{MINIO_HOST}
  USE_SSL: "false"
"""

    resp = k8s_beta.create_namespaced_deployment(
                body=secret, namespace=DEPLOY_NAMESPACE)
    print("Deployment created. status='%s'" % str(resp.status))

    ret = False
    
    if str(resp.status) == "Created":
          ret = True
          
    return ret



def serviceAccount(DEPLOY_NAMESPACE, SECRET_NAME):
    sa = f"""apiVersion: v1
kind: ServiceAccount
metadata:
  name: minio-sa
  namespace: {DEPLOY_NAMESPACE}
secrets:
  - name: {SECRET_NAME}
"""

    resp = k8s_beta.create_namespaced_deployment(
                body=sa, namespace=DEPLOY_NAMESPACE)
    print("Deployment created. status='%s'" % str(resp.status))

    ret = False
    
    if str(resp.status) == "Created":
          ret = True
          
    return ret

def seldonDeployement(MODEL_NAME, DEPLOY_NAMESPACE, MINIO_MODEL_BUCKET, INCOME_MODEL_PATH, SECRET_NAME):
    seldon_deployement = f"""apiVersion: machinelearning.seldon.io/v1
kind: SeldonDeployment
metadata:
  name: {MODEL_NAME}
  namespace: {DEPLOY_NAMESPACE}
spec:
  predictors:
  -  graph:
      implementation: SKLEARN_SERVER
      modelUri: s3://{MINIO_MODEL_BUCKET}/{INCOME_MODEL_PATH}
      envSecretRefName: {SECRET_NAME}
      name: classifier
      logger:
         mode: all
     name: default
     replicas: 1
"""

    resp = k8s_beta.create_namespaced_deployment(
                body=seldon_deployement, namespace=DEPLOY_NAMESPACE)
    print("Deployment created. status='%s'" % str(resp.status))

    ret = False
    if str(resp.status) == "Created":
          ret = True
          
    return ret


def main(MODEL_NAME, 
         DEPLOY_NAMESPACE, 
         MINIO_ACCESS_KEY, 
         MINIO_SECRET_KEY, 
         MINIO_HOST, 
         MINIO_MODEL_BUCKET, 
         INCOME_MODEL_PATH
):
    
    sucessful_deployement = False
    
    SECRET_NAME = "seldon-init-container-secret"
        
    secret = secret(DEPLOY_NAMESPACE, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_HOST, SECRET_NAME)
    service_account = serviceAccount(DEPLOY_NAMESPACE, SECRET_NAME)
    seldon_deployement = seldonDeployement(MODEL_NAME, DEPLOY_NAMESPACE, MINIO_MODEL_BUCKET, INCOME_MODEL_PATH, SECRET_NAME)
    
    if secret and service_account and seldon_deployement:
          sucessful_deployement = True
          
    return sucessful_deployement
    

def testModel_clusterIP(MODEL_NAME, DATA, DEPLOY_NAMESPACE):
      cmd=f"""curl -d '{DATA}' \
        http://{MODEL_NAME}-default.{DEPLOY_NAMESPACE}:8000/api/v1.0/predictions \
        -H "Content-Type: application/json"
      """
    
      ret = Popen(cmd, shell=True,stdout=PIPE)
      return ret.stdout.read().decode("utf-8")
    
def testModel_LoadBalancer(LOAD_BALANCER, MODEL_NAME, DATA, DEPLOY_NAMESPACE):
      cmd=f"""curl -d '{DATA}' \
        http://{LOAD_BALANCER}/seldon/{DEPLOY_NAMESPACE}/{MODEL_NAME}/api/v0.1/predictions \
        -H "Content-Type: application/json"
      """
    
      ret = Popen(cmd, shell=True,stdout=PIPE)
      return ret.stdout.read().decode("utf-8")