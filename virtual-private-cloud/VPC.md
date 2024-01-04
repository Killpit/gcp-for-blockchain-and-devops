# VPC

VPC is a secure, private and isolated area in the cloud to run applications and store data.

A VPC allows you to create a virtual network in th cloud, allowing us to have a private section of the internet. It allows you to create and manage Google Cloud resources.

Similar to a physical network, VPCs have their configurations and rules, allowing resource organization and control on how services communicate.

Gatewyays or routers can be set up to connect VPCs to the internet as other networks, making the exit points for inbound and outbound traffic. Traffic flow and security measures can be implemented to protect resources from unauthorized access.

Like all other cloud providers, GCP provides you with a default VPC as soon as you created an account and a project. That leaves us to create VPCs for our projects

## VPC Compnents

**Subnet**: Synonyms with subnetworks in Google Cloud, Subnets are a subdivision of VPC, they carve out IP addresses with specific functionalities and security considerations.

**Virtual Private Clouds (VPC)**: It is a private cloud within Google Cloud with its own set of rules and configurations created for specific needs. After creating a VPC, you can add subnets.

**IP Addressing**: You can either assign IPv4 and IPv6, or you can bring IPv4 and IPv6 addresses to your VPC and subnets and allocate resources in your VPC such as Compute Engine.

**Gateways**: Gateways are used to connect your VPC to another network.

**VM Instances**: VPC networks can leverage load balancers to use Compute Engine instances. In addition to Compute Engine capability, Compute Engine instance can include Google Kubernetes Engine, Google App Engine and other services provided by Google Cloud.

**Organization Policy Constraints**: Each project starts with a default VPC network and more VPCs can be created with VPC service at Google Cloud as soon as the VPC API is enabled. 

**VPC Network**: VPCs are used to configure prefix ranges for subnets and network policies, or can be easily configured on your own and allows expansion of CIDR ranges with no downtime.

**VPC Flow Logs**: Flow logs capture information about IP traffic on Compute Engine and they help with monitoring, forensics, expense optimization and real-time security. They're updated frequently to maintain immediate visibility.

**VPC Peering**: Private communication can be configured without bottlenecks or single point or failure within the VPC.

**Firewall**: Firewall is used to restricts access in a globally distributed manner. VPC Firewall Rules Logging allows auditing, verifying and analyzing the effects of firewall rules.

**Shared VPC**: VPCs can be shared across other projects. This allows flexibility and separate billing and quota for each project by connecting to a VPC. 

**Packet Mirroring**: It provides network traffic collection and inspection at scale, intrusion detection, application performance monitoring and compliance controls with troubleshooting at scale.

**VPN**: IPsec is used to connect securely on a VPC network.

**Private access**: Application front end can be configured and backend services can be shielded and private access can be maintained to Google services with all access to Google Cloud services.

**VPC Service Controls**: Sensitive data can be kept private and fully managed storage and data processing capabilities can be used by configuring private communications between cloud resources whether its cloud and on-premise deployments. 