# Creating an Apache web server on a Linux VM

1 - Go to Google Cloud Console and create a new project or choose an existing project. 

2 - Enable Google Compute API

3 - Click VM instances on the Compute Engine page.

4 - Enter a name for your instance, select your region and zone. Then choose an appropriate zone. 

5 - Go to the boot disk, select Debian as operating system, keep the version as the default value, select SSD persistent disk from Boot disk type and click select.

6 - Allow HTTP traffic from Firewall section.

7 - Click Create to create the instance

8 - Go to Connect column and click SSH from your instance. In this step, a cmd window opens up and if you authorize the window, the server is expected to open. You can use [this page]([https://cloud.google.com/compute/docs/machine-resource](https://cloud.google.com/compute/docs/machine-resource](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors)https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors))

9 - Update the packages with `sudo apt-get update`

10 - Install Apache2 HTTP Web Server with `sudo apt-get install apache2 php7.0`

11 - Overwrite Apache Web Server Default Web page with `sudo apt-get install apache2 php7.0`

12 - Overwrite the Apache Web Server with `echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html`

13 - Go to VM instances, copy the VMs IP address from External IP column.

14 - Paste the IP address in a new browser tap after copying external IP address.

**Reference** 

Google Cloud
