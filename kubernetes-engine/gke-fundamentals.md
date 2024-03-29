# GKE Fundamentals

### What is Google Kubernetes Engine (GKE)?

Google Kubernetes Engine is Google's managed kubernetes service that is created after Google Borg. It's used to manage kubernetes workloads across the project.

### How GKE Works?

GKE works with nodes that are grouped with clusters. Then your apps (workloads) are packages into containers. After packages, you deploy containers as Pods to your nodes and use Kubernetes API to interact with workloads.

In addition to its features, GKE automatically updates to newer Kubernetes versions or they can be manually updated through the control plane. Finally, they have autopilot mode that is useful managing nodes by Google Cloud on behalf of your projects.

### Cluster Architecture

Similar to Kubernetes architecture, a GKE cluster consists of a control plane and nodes for cluster orchestration. However, a GKE cluster has access to Google Cloud services and if needed, you can use multi-cloud solutions according to Google Cloud documentation. It can be created with Standard mode which allows you to manage the nodes or Autopilot can be used to automate management of the underlying infrastructure and nodes. Kubernetes API runs the whole control plane and it's managed until all resources are destroyed. Finally, Artifact registry is used to create clusters or upgrade cluster versions.

#### How nodes are created in GKE?

GKE creates nodes through Google Compute Engine virtual machines (VMs) and they manage self-reported status of nodes. Nodes run necessary services and the node agent (kubelet) for communicating with the control plane and starts and runs containers that are scheduled on the node. GKE runs DaemonSets as per-node agents for functionality.

#### How to create GKE clusters through Command Line Interface (CLI)?

You can either use `gcloud` or `gkectl`. However, `gkectl` is recommended for on-premise infrastructure while `gcloud` would be sufficient for creating clusters. To create a cluster, you need to install `gcloud`, configure your Google Cloud account, configure the project and then you should use `gcloud` container clusters create your-cluster. If you want to install `gkectl`, you can follow the [documentation](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads).

**By specifying a zone**

`gcloud container clusters create demo-cluster --zone us-central1-a`

**By specifying a region**

`gcloud container clusters create demo-cluster --region europe-west1`

**By specifying a location**

`gcloud container clusters create demo-cluster --location europe-west1-d`

- Never forget to use command to `delete` your GKE clusters, just write `delete` instead of `create` for the command above.

#### How to create GKE cluster through Google Cloud Console

1 - Go to your project and enable Kubernetes Engine API
2 - Click create to create your Autopilot Cluster from the clusters section
3 - Choose a name for your cluster and click Create, wait until your cluster is created
4 - Go to GKE workloads page and click Create Deployment
5 - Choose a certain image and choose a name for deployment page
6 - Choose the cluster you created and leave Port 1 to 80 and choose Target Port 1 as 8080 and click deploy
7 - Click the name of the app from workloads and click the IP address of endpoints

#### How to delete GKE cluster through Google Cloud Console

After creating the GKE cluster, it's generally recommended to delete it as it can be expensive to maintain the cluster. To delete your cluster,

1 - Go to GKE Clusters
2 - Select the cluster and click delete and enter the name of your cluster to confirm the deletion of the cluster