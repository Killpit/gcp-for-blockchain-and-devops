# Artifact Registry

Artifact Registry is used to store artifacts, dependents and containers on Google Cloud with the help of container registry (gcr). However, GCR is migrated to Artifact Registry. They are useful to manage and store Docker images, dependency management and software delivery.

### How to enable the service?

You need to activate Artifact Registry API in Google Cloud for your project.

### What are repositories?

Repositories are used to store different artifact types and they're classified as standard, remote or virtual repositories. 

#### What are remote repositories?

Remote repositories are used to store artifacts that are coming from external sources. They download and caches the whole package in this repository and saves the copy if you request the same version of a certain package. It supports authentication for DockerHub and you can see your repositories on DockerHub if pushed.

#### What are standard repositories?

Standard repositories are used to upload and download artifacts directly.

#### What are virtual repositories?

Virtual repositories are used as a single access point to install or deploy artifacts in the same format. Upstream repositories can either be standard or remote. Unlike other repositories, they have better protection against dependency confusion attack.

### Creating a repository in Artifact Registry

1 - Choose the name and format of your repository.
2 - Choose the mode and region of your repository.
3 - Click "Create".

### How to push Docker images in Artifact Registry?

```docker push region-name-docker.pkg.dev/PROJECT/quickstart-docker-repo/repo-image:tag1```

### How tp pull Docker images in Artifact Registry?

```docker pull region-name-docker.pkg.dev/PROJECT/quickstart-docker-repo/repo-image:tag1```

Clean up your resources in order to prevent unnecessary charges to your artifact registry.