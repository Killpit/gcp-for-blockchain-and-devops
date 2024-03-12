# Cloud Run

Cloud Run is a service that allows you to run containers directly on Google Cloud's infrastructure. It allows you to develop in any language as long as you have the image necessary to use the service.

### How to run your code in Cloud Run?

You can use Cloud Run services and jobs to run your code.

### What is Cloud Run services?

Cloud Run services provide you with the infrastructure required to run HTTPS endpoint. You just have to make sure that your code listens on a TCP port and handle HTTP requests.

### What is Cloud Run Jobs?

Cloud Run Jobs are used to run the code and can be executed by using gcloud CLI. They can either be scheduled a recurring job or run as part of a workflow.

### How to create a service in Cloud Run?

- Go to Google Cloud console and choose Cloud Run
- After clicking Cloud Run, Google Cloud will enable Cloud Run API
- Choose a service name and a container image url
- Choose authentication type and click create
- If you want, you can change the region and modify autoscaling, ingress control and CPU allocation and pricing and Container(s), Volumes, Networking, Security.

### How to create a job in Cloud Run?

- Go to Cloud Run and click Create Job
- Choose container image URL
- Select job name
- You can choose other options similar to creating a job in cloud run
- You can either execute the job immediately after creation if you click Execute job immediately or you can create the job and execute later on