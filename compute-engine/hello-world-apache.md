# Creating an Apache web server on a Linux VM

1 - Go to Google Cloud Console and create a new project or choose an existing project. 

2 - Enable Google Compute API

3 - Click VM instances on the Compute Engine page.

4 - Enter a name for your instance, select your region and zone. Then choose an appropriate zone. 

![Ekran Resmi 2023-12-11 12 17 16](https://github.com/Killpit/gcp-zero-to-hero/assets/57031187/d9ead5af-5c81-4e20-8a97-a00ae9c9cdc1)

5 - Go to the boot disk, select Debian as operating system, keep the version as the default value, select SSD persistent disk from Boot disk type and click select.

![Ekran Resmi 2023-12-11 12 18 05](https://github.com/Killpit/gcp-zero-to-hero/assets/57031187/4c9a8ab9-4011-481d-acc7-a81b5b23a57c)

6 - Allow HTTP traffic from Firewall section.

![Ekran Resmi 2023-12-11 12 19 59](https://github.com/Killpit/gcp-zero-to-hero/assets/57031187/555be9d6-e1ca-4ed1-b803-3ab1d3ca9130)

7 - Click Create to create the instance

8 - Go to Connect column and click SSH from your instance. In this step, a cmd window opens up and if you authorize the window, the server is expected to open. You can use [this page](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors)

9 - Update the packages with `sudo apt-get update`

10 - Install Apache2 HTTP Web Server with `sudo apt-get install apache2 php7.0`

11 - Overwrite Apache Web Server Default Web page with `sudo apt-get install apache2 php7.0`

12 - Overwrite the Apache Web Server with `echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html`

13 - Go to VM instances, copy the VMs IP address from External IP column.

14 - Paste the IP address in a new browser tap after copying external IP address.

**Reference** 

Google Cloud Tutorials
