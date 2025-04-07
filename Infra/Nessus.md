**Check Nessus Server status**

	https://status.tenable.com/?_gl=1*1t4gwg6*_ga*MjM5Njc3ODc2LjE3MTgyMjQ4Mjc.*_ga_HSJ1XWV6ND*MTczOTk2OTYxMC4yLjAuMTczOTk2OTYxMC42MC4xLjEyMDcyOTA4MzI.

**OFFLINE INSTALLATION**

Refer to this step-by-step guide

	https://docs.tenable.com/nessus/Content/InstallNessusOffline.htm

**Requirements**

	1 with internet
	1 without internet

**Download installer**
	
 	https://www.tenable.com/downloads/nessus
![image](https://github.com/user-attachments/assets/88dda516-9c0f-4f2d-8f7e-72fc62cff427)

**Once installation is completed**
	
Linux

	sudo dpkg -i <nessus deb>
	systemctl start nessusd.service
	
Windows

	net start "Tenable Nessus"

Browse to http://localhost:8834 or http://kali:8834

	Select Register Offline > Nessus Professional

Will end up in Register Nessus page

Take note of the challenge code

**Device with internet**

	https://plugins.nessus.org/v2/offline.php
Input challenge code and activation code

Challenge Code

	"C:\Program Files\Tenable\Nessus\nessuscli.exe" fetch --code-in-use

Activation code
	
	Login to Nessus web

Save license key into text file

**Download the latest plugin (!!! Note: Plugin be all-2.0.tar.gz !!!)**

![image](https://github.com/user-attachments/assets/bb9405c3-e979-4c3b-8fef-1863f7ee9972)

Transfer all-2.0.tar.gz to offline device

Input license key into offline device

Create new account

**Install plugins**

**CLI**

	"C:\Program Files\Tenable\Nessus\nessuscli.exe" update all-2.0.tar.gz
 	nessuscli update all-l-2.0.tar.gz

**GUI**

Top left Settings

![image](https://github.com/user-attachments/assets/61bdbe1e-91b3-4267-89fc-a5744d1bac17)

Top right > Manual Software update

![image](https://github.com/user-attachments/assets/29afd9bb-12fd-4ade-bb9a-b1fdd0604d48)

Upload your own plugin archive (Note: Plugin must be all-2.0.tar.gz

![image](https://github.com/user-attachments/assets/5c2dda82-ada8-431a-8ef9-79a24f4b2df1)

Bottom left will start to load
There's no progress bar. Typically takes between 30 mins to 1 hour

![image](https://github.com/user-attachments/assets/65796f33-2355-474a-a02a-d2fa7aad7115)

Once plugins installed, there will be a notification

![image](https://github.com/user-attachments/assets/b5be7fab-0ae9-4f95-85a2-faf04475d6c8)

**Troubleshoot**

**Not sure whether plugins have been uploaded and/or installed**
Upload using both CLI and GUI
After 1 hour or so, restart nessus service

Windows

	net stop "Tenable Nessus"
	net start "Tenable Nessus"

Linux

 	systemctl stop nessusd.service
	systemctl start nessusd.service

------------------------------------------------------------------------------

**License Expired (No Internet)**

Ensure license has been renewed or a new license is ready for use

https://docs.tenable.com/nessus/Content/UpdateLicenseOffline.htm

Offline device

Get the challenge code

	"C:\Program Files\Tenable\Nessus\nessuscli.exe" fetch --challenge

Device with Internet

https://plugins.nessus.org/v2/offline.php

Input challenge code and activation code

Download the license key output

Transfer to offline device

**Offline Device**

	"C:\Program Files\Tenable\Nessus\nessuscli.exe" fetch --register-offline "<Nessus License key>"

![image](https://github.com/user-attachments/assets/ac9ce422-f3c7-41c5-9bb4-49dbc6641d24)

Restart Nessus service

Windows

	net stop "Tenable Nessus"
	net start "Tenable Nessus"

Linux

 	systemctl stop nessusd.service
	systemctl start nessusd.service

**License Expired (Internet)**

Ensure license has been renewed or a new license is ready for use

nessuscli fetch --register <activation code>

![image](https://github.com/user-attachments/assets/ed05074c-cee6-4a1f-b58c-accac9321c7d)

Windows

	net stop "Tenable Nessus"
	net start "Tenable Nessus"

Linux

 	systemctl stop nessusd.service
	systemctl start nessusd.service

------------------------------------------------------------------------------

**Reset Password**

![image](https://github.com/user-attachments/assets/1605c969-cf09-46e6-b2c2-af2d3d7e45bd)

List usernames in device

	"C:\Program Files\Tenable\Nessus\nessuscli.exe" lsuser
 
