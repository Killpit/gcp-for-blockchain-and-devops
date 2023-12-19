# Configure Internal Load Balancing

1 - Create a new project, ensure all permissions needed for a project and enable Google Compute API.

2 - Go to IAM Admin and click IAM. After going to IAM, add Compute Network Admin, Compute Security Admin and Compute Instance Admin (v1) and click save.

3 - Go to VPC and click VPC networks.

4 - Click VPC Network and write lb-network in the name box.

5 - Choose custom subnet and write the configurations written below, this will be the first subnet:

    - Name: lb-subnet
    - Region: us-west1
    - IP stack type: IPv4 (single-stack)
    - IP address range: 10.1.2.0/24

Click Done .

6 - Add the second subnet and write the configurations written below:

    - Name: europe-subnet
    - Region: europe-west1
    - IP stack type: IPv4 (single-stack)
    - IP address range: 10.3.4.0/24

Click Done.

7 - Click Create.

8 - From the Google Cloud console, go to the Firewall policies page.

After going to the Firewall policies page, click Create Firewall Rule and write the configurations down below for fw-allow-lb-access:

    - Name: fw-allow-lb-access
    - Network: lb-network
    - Priority: 1000
    - Direction of traffic: Ingress
    - Action on match: Allow
    - Targets: All instances in the network
    - Source filter: IPv4 ranges
    - Source IPv4 ranges: 10.1.2.0/24 and 10.3.4.0/24
    - Protocols and ports: Allow all

Click create to create the first firewall rule.

To create fw-allow-ssh rule to allow incoming SSH connections, write down the configurations below after clicking Create Firewall Rule:

    - Name: fw-allow-ssh
    - Network: lb-network
    - Priority: 1000
    - Direction of traffic: Ingress
    - Action on match: Allow
    - Targets: Specified target tags
    - Target tags: allow-ssh
    - Source filter: IPv4 ranges
    - Source IPv4 ranges: 0.0.0.0/0
    - Protocols and ports: Specified protocols and ports
    - Select the TCP checkbox, and enter 22 as the Port number

For our final rule, click Create Firewall Rule and write down the configurations below:

    - Name: fw-allow-health-check
    - Network: lb-network
    - Priority: 1000
    - Direction of traffic: Ingress
    - Action on match: Allow
    - Targets: Specified target tags
    - Target tags: allow-health-check
    - Source filter: IPv4 ranges
    - Source IPv4 ranges: 130.211.0.0/22 and 35.191.0.0/16
    - Protocols and ports: Allow all

Click create and we are done for creating firewall rules.

