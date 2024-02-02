# How to connect to GCE instance through terminal?

In this section, we will look at two different ways to connect to GCE instances.

### Connecting to GCE instance (VMs) through your computer terminal?

1 - Install and configure gcloud CLI

2 - After configuring your gcloud CLI with `gcloud init`, run the following command: `gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME`

For example, `gcloud compute ssh --project=gcp-zero-to-hero-demos --zone=us-central1-c instance-1`, in this command, PROJECT_ID is known as gcp-zero-to-hero-demos,ZONE is written as us-central1-c and VM_NAME is written as instance-1

For PROJECT_ID, replace it with your Google Cloud Project ID, replace YOUR_ZONE with your VM's zone and replace VM_NAME with the name of your VM. After you've entered the command, the CLI will autogenerate a key and will ask you a passphrase (optional) and updates project ssh metadata.

Even though OpenSSH is possible to connect to Google Cloud VMs, Google Cloud recommends using gcloud CLI for security and convenience reasons.