# Configure and manage a domain name using Google Cloud DNS

## Overview

- The VPC has public subnets and private subnets in two Availability Zones.
- Each public subnet contains a NAT gateway and a load balancer node.
- The servers run in the private subnets, are launched and terminated by using an Auto Scaling group, and receive traffic from the load balancer.
- The servers can connect to the internet by using the NAT gateway.

1. Create a VPC Network:

- Go to the VPC Networks section in the GCP Console.

- Click "Create VPC network."

- Choose "Custom" mode for granular control.

- Define subnet CIDR blocks for public and private subnets in different regions or zones.

- Configure firewall rules for each subnet to control traffic flow.

2. Deploy your application:

Option 1: VM instances:

- Create custom images or choose preconfigured machine types.

- Launch instances in private subnets based on your image or machine type.

Option 2: Kubernetes Engine (alternative path, optional):

- Deploy containerized applications in a managed Kubernetes cluster within the private subnet.

3. Set up Cloud NAT:

- Go to the Cloud NAT section in the GCP Console.

- Click "Create Cloud NAT gateway."

- Select a region and attach the gateway to a public subnet.

4. Configure Routing:

- Go to the VPC Network Routes section.

- Create route tables for public and private subnets.

- Public subnet route table: Add a route to the internet gateway.

- Private subnet route table: Add a route to the Cloud NAT gateway and a route to any VPC endpoints.

5. Cloud Load Balancing (optional):

- Go to the Cloud Load Balancing section.

- Create a Cloud Load Balancer in a public subnet.

- Configure the load balancer to distribute traffic to your server instances.

- (Kubernetes Engine) Use an Ingress Controller for internal and external load balancing.

6. VPC Endpoint (optional):

- Go to the VPC Network Endpoints section.

- Create a VPC endpoint for the desired Google Cloud service (e.g., Cloud Storage).

- Select the private subnet and the service you want to access.
