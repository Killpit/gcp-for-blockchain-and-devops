# Google Cloud Load Balancing

Load balancers distribute web traffic to multiple instances in applications and they are an integral part of modern applications. Google Cloud Load Balancing uses Google's own technologies unlike other cloud providers, increasing additional reliability to load balancing products. Load balancers are separated into application and network load balancers. 

### Application Load Balancer (ALB)

ALB is a Layer 7 Load balancer used to run and scale services and it's compatible with HTTP and HTTPS alongside with Google Cloud Services to provide external backends or with hybrid infrastructure. They're separated into external or internal load balancers. 

External ALBs use Google Front Ends (GFE) or managed proxies to distribute internet traffic globally by using open source Envoy proxy to enable traffic. They can be configured globally, regionally, or classically.

Internal ALBs allow you to run and scale your HTTP application traffic by using internal IP address. In addition to external load balancers, they have locality policies, global access, access from connected networks and compatibility with GKE by using ingress in a fully orchestrated fashion.

### Network Load Balancer (NLB)

NLBs are used to handle TCP, UDP or other IP protocols as a Layer 4 load balancer. They are useful for configuring reverse proxy with support for advanced traffic controls. They are separated into Proxy NLB and Passthrough NLB.

#### Proxy NLB 

Proxy NLBs allow Layer 4 reverse proxy load balancers to distribute TCP traffic to backends in Google Cloud VPC. It terminates traffic at LB layer and forwards the closest available backend using TCP.

#### Passthrough NLB

Passthrough NLBs are Layer 4 regional LBs that distribute traffic in the same region for backends. After load balancing is complete, connections are terminated and responses from a VM goes back to the clients. 