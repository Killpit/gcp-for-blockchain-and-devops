# Google Cloud DNS (Domain Name System)

Google Cloud DNS is a Domain Name Service that publishes your domain names to the global DNS. It supports IAM permissions at the project level and individual DNS zones. It supports public zones and private managed DNS zones. While public zones are visible to the public internet, private zones are only visible to specified VPC networks.

### DNS Forwarding

Private zones have inbound and outbound forwarding and they can be inbound and outbound forwarding known as bi-directional forwarding.

**Inbound**: These are IPv4 addresses derived from primary IPv4 addresses that are in range of every subnet in the applicable VPC network. They are used to provide on-premise services.

**Outbound**: Outbound rules allow for a name server and alternative servers for VPC network. It also allows internal and external IP addresses and an IP address of an on-premises system.

### Key terms for Google Cloud DNS

**Project**: Google Cloud Platform separates resources according to projects and make their billing on project bases. Also they serve as a container for resources and a domain for access control where billing is configured and aggregated.

**Managed zone**: They hold DNS records for the same DNS suffix. They all have to have unique names while multiple managed zones can be configured to a project.

**Public zone**: Public zones are visible to the internet and their zones are authoritative, which means they provide an answer about the resources in that zone. Users can enter the address through a web browser, or an application calls out a given name of a resource on the Internet. Name Server (NS) and SOA resource records are at the zone apex, which prevents them being deleted.