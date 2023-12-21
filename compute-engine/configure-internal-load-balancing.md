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

Now, we will create backend VMs (virtual machines) to create network load balancing.

9 - Go to Compute Engine and click VM instances. Here, we will create 4 virtual machines in region us-west-1, write the details below when creating virtual machines.

Name: vm-a1,

Zone: us-west1-a

Name: vm-a2,

Zone: us-west1-a

Name: vm-c1,

Zone: us-west1-c

Name: vm-c2,

Zone: us-west1-c

10 - Enter a name for each of the instances.

11 - Select us-west-1 as the region.

12 - Choose Debian 10 (buster) from boot disk section.

13 - Expand Advanced options section and then expand Networking section.

    - Add allow-ssh and allow-health-check as network tags.
    - Enter lb-network to at the Network interfaces section, don't forget to remove default network beforehand.
    - Choose lb-subnet as your subnet.
    - Choose IPv4 (single stack)
    - Choose Ephemeral (automatic) for Primary Internal IP
    - Choose Ephemeral for External IP
    - Click Done to finish modifying network interface

14 - Expand the Management section and specify the following script at the automation box.

``` shell script

#! /bin/bash
if [ -f /etc/startup_script_completed ]; then
exit 0
fi
apt-get update
apt-get install apache2 -y
a2ensite default-ssl
a2enmod ssl
file_ports="/etc/apache2/ports.conf"
file_http_site="/etc/apache2/sites-available/000-default.conf"
file_https_site="/etc/apache2/sites-available/default-ssl.conf"
http_listen_prts="Listen 80\nListen 8008\nListen 8080\nListen 8088"
http_vh_prts="*:80 *:8008 *:8080 *:8088"
https_listen_prts="Listen 443\nListen 8443"
https_vh_prts="*:443 *:8443"
vm_hostname="$(curl -H "Metadata-Flavor:Google" \
http://169.254.169.254/computeMetadata/v1/instance/name)"
echo "Page served from: $vm_hostname" | \
tee /var/www/html/index.html
echo "Page served from: $vm_hostname" | \
tee /var/www/html/index.html
prt_conf="$(cat "$file_ports")"
prt_conf_2="$(echo "$prt_conf" | sed "s|Listen 80|${http_listen_prts}|")"
prt_conf="$(echo "$prt_conf_2" | sed "s|Listen 443|${https_listen_prts}|")"
echo "$prt_conf" | tee "$file_ports"
http_site_conf="$(cat "$file_http_site")"
http_site_conf_2="$(echo "$http_site_conf" | sed "s|*:80|${http_vh_prts}|")"
echo "$http_site_conf_2" | tee "$file_http_site"
https_site_conf="$(cat "$file_https_site")"
https_site_conf_2="$(echo "$https_site_conf" | sed "s|_default_:443|${https_vh_prts}|")"
echo "$https_site_conf_2" | tee "$file_https_site"
systemctl restart apache2
touch /etc/startup_script_completed

```

15 - Click Create to create the VM.

16 - Go to Instance groups at Compute Engine

17 - Repeat each step for all the instance groups that will be created:

    - Click Create Instance Group and new unmanaged instance group
    
    - Instance group ig-a:

    Zone: us-west1-a

    VMs: vm-a1 and vm-a2

    - Instance group ig-c:

    Zone: us-west1-c

    VMs: vm-c1 and vm-c2

    - Select us-west-1 for the region and choose Zones according to configuration
    - Select lb-network for Nework
    - Select lb-subnet as Subnetwork
    - Add VM instances for VM instances that we indicated above
    - Click create to create each instance group

18 - Go to Network Services and click to Load balancing from the console navigation menu.

19 - Click Create Load Balancer.

20 - Click Start configuration in the TCP Load Balancing card.

21 - Select Only between my VMs for Internet facing or internal only.

22 - Select Pass-through for Load Balancer Type and click Continue.

23 - Enter the name of the load balancer along with the region and the network in which it needs to be configured:

Name: be-ilb

Region: us-west1

Network: lb-network

- Click Backend Configuration.

    - Select IP stack type as IPv4 to handle IPv4 traffic only
     
     Name: be-ilb

    Region: us-west1

    Network: lb-network

    - Click Backend configuration

    Add backend configuration:

        - Select IP stack type as IPv4
        - Choose ig-a instance group in the instance group list
        - Click done
        - Add ig-c instance group by repeating the steps after clicking Add Backend.

    - Add health check in the Health Check list by selecting Create a health check by entering the following values:
      
      - Name: hc-http-80
      - Protocol: HTTP
      - Port: 80
      - Proxy protocol: NONE
      - Request path: /
      - Click Save
      - Verify you have the blue check mark against Backend configuration.

- Click Frontend configuration

    - Enter the following values in the New Frontend IP and port section:

        - Name: fr-ilb
        - IP version: IPv4
        - Subnetwork: lb-subnet
        - In the Internal IP section, in the IP address list, select Create IP address, and then enter the following values:

            - Name: ip-ilb
            - Static IP address: Let me choose
            - Custom IP address: 10.1.2.99
            - Click Reserve to reserve the custom IP address.
            - Ports: Select Multiple, and enter 80, 8008, 8080, 8088 as the Port numbers.
            - Global Access: Select Enable so that the internal passthrough Network Load Balancer is accessible to clients in all regions.
            - Click Done.
            - Verify there is a blue check mark for Frontend configuration

24 - Click review and finalize, make sure both Frontend and Backend are configured.

25 - Click create 

26 - To create Client VMs, go to Compute Engine and click VM instances.

27 - We are going to create two client VMs for each instance group in the same region:

    For vm-client:

        - Name: vm-client
        - Region: us-west1
        - Zone: us-west1-a
        - Subnet: lb-subnet

    For vm-client2:

        - Name: vm-client2
        - Region: europe-west1
        - Zone: europe-west1-b
        - Subnet: europe-subnet

- Expand Advanced options section and in the Networking, add allow-ssh tag.

- Enter the following values in the Network interfaces section:

    - Network: lb-network
    - Subnet: as indicated in step 1
    - IP stack type: IPv4 (single-stack)
    - Primary internal IP: Ephemeral (automatic)
    - External IP: Ephemeral

- Click done to finish modifying the network interface.

28 - Click Create to create and start the VM.

As we have done creating the infrastructure for our load balancer, now we will test connection from client VM through Cloud Shell.

29 - Open Cloud shell.

30- Connect to the client VM instance with ``` gcloud compute ssh vm-client \--zone=us-west1-a ```. Authorize Cloud Shell to call Google Cloud APIs if needed.

31 - Make a curl request to contact with the IP address ``` curl http://10.1.2.99 ```. The expected responses should be Page served from: vm-a1, Page served from: vm-a2, and so on.

- According to forwarding rules, it should only serve ports 80, 8008, 8080 and 8088. To test connection, use ``` curl http://10.1.2.99:80 ```
 
32 - Connect to the client VM instance and ping the address with ``` gcloud compute ssh vm-client \--zone=us-west1-a ```, if connected, you don't have to enter the command and you can simply write this command: ``` timeout 10 ping 10.1.2.99 ```

33 - Test Global access with another cloud shell console and add  ``` gcloud compute ssh vm-client2 --zone=europe-west1-b ```

34 - Make web request with ``` curl http://10.1.2.99 ```. Expected results should be Page served from: vm-a1, Page served from: vm-a2, and so on.

35 - Forwarding port in the vm-client 2 is configured to serve ports 80, 8008, 8080 and 8088. Use these commands to test them:

- ``` curl http://10.1.2.99:80 ```
- ``` curl http://10.1.2.99:8008 ```
- ``` curl http://10.1.2.99:8080 ```
- ``` curl http://10.1.2.99:8088 ```