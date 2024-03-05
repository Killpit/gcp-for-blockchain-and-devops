# How to deploy

### Deploying a VM

`gcloud deployment-manager deployments create cdm-vm --config deploy-vm.yaml`

### Deploying a GCS Bucket

`gcloud deployment-manager deployments create [your-bucket] --config gcs-deploy.yaml`
