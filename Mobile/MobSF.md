[test.md](https://github.com/user-attachments/files/24671910/test.md)<h1><b>Windows Only</b></h1>

Works for both Static and Dynamic Analysis

<h2><b>Download Windows MobSF</b></h2>

	https://github.com/MobSF/Mobile-Security-Framework-MobSF

	https://allabouttesting.org/quick-tutorial-mobsf-installation-on-linux-windows/

<h2><b>Install Docker Desktop for Windows</b></h2>

	https://docs.docker.com/desktop/install/windows-install/

<h2><b>Android Studio</b></h2>

Download any apk file to test

	https://apkpure.net/

Android Studio guide to how to link to MobSF

	https://github.com/MobSF/docs/blob/master/dynamic_analyzer.md
	
<h2><b>Download Android Studio</h2></b>

	https://developer.android.com/studio
	
Select empty project
	
Will take a while to install dependencies

Wait for all dependencies to be installed

![image](https://github.com/user-attachments/assets/ceaff4c4-d248-4cc2-b430-08782b625e03)

Top right > Device Manager

![image](https://github.com/user-attachments/assets/1df00ede-8fe9-4cb2-9c52-5267e9c521da)

<img width="895" height="682" alt="image" src="https://github.com/user-attachments/assets/75d203fd-95d8-4cb5-ab29-c3af8795a638" />

Download and select API 28 or below > Android 9.0. <h3><b>MUST BE Google API</b></h3> for full root

![image](https://github.com/user-attachments/assets/b1f94562-e1e3-4220-b9a3-d7862f9a0705)

<h2><b>Set emulator path in system path</b></h2>

Windows Search > Edit the system enrionment variables > Bottom right > Environment Variables

Under system path, edit 'Path'

![image](https://github.com/user-attachments/assets/29ca7e0b-bd14-4085-aaf7-b4c1dd5f301f)

Add this into the path

	C:\Users\User\AppData\Local\Android\Sdk\emulator

![image](https://github.com/user-attachments/assets/cc49f9c9-f3c7-46be-a31a-5c1a38ef8676)

<h2><b>Start Emulator</b></h2>

Open CMD

Identify emulator name

	emulator -list-avds

<img width="317" height="47" alt="image" src="https://github.com/user-attachments/assets/cdbb9d83-340a-4dfe-89d2-4fc0ce545293" />

	emulator -avd Pixel_3 -writable-system -no-snapshot-load -no-snapshot-save

<img width="1583" height="753" alt="image" src="https://github.com/user-attachments/assets/f70087f0-9b72-4a1c-a6bf-af51e579514d" />

<h2><b>Identify emulator serial number</b></h2>

Usually it's 'emulator-5554'

Help > About

![image](https://github.com/user-attachments/assets/8c4dd665-d7a1-4565-bc4c-65bb8ecebfa4)

![image](https://github.com/user-attachments/assets/b5cc3617-06d3-4f11-b9d3-b9262eecab31)

<h2><b>Running MobSF</b></h2>

<h3><b>Launch Docker Desktop</b></h3>

<h3><b>Launch CMD</b></h3>

Run commands from the documentation below

	https://pypi.org/project/mobsf/
 
	docker pull opensecurity/mobile-security-framework-mobsf:latest
 
![image](https://github.com/user-attachments/assets/722cabe4-7166-4344-9417-96499029155c)

Run Docker
	
	docker run -it --rm -e MOBSF_ANALYZER_IDENTIFIER=emulator-5554 -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest
	 MOBSF_ANALYZER_IDENTIFIER=<emulator serial number>

![image](https://github.com/user-attachments/assets/25588c2c-a995-4d01-8246-4853f2c6dbda)

<h2><b>Static Analysis</b></h2>

Browse to 127.0.0.1:8000

![image](https://github.com/user-attachments/assets/90a80e16-5420-4d76-8af5-a287a153c6d2)

Upload an APK file or download one to test it out

	https://apkpure.net/

<img width="1537" height="2212" alt="image" src="https://github.com/user-attachments/assets/d1490ecd-3d59-42e8-97ea-6c87fba2b1b4" />

Will take some time to complete upload and scan

Once done, go to recent scan

There should be a static scan report made available

Leave it running, don't start anything

Will be redirected to static analysis report once scanning is done

<h2><b>Dynamic Analysis</b></h2>

Dynamic analyzer

<img width="269" height="61" alt="image" src="https://github.com/user-attachments/assets/2d31f4c3-6840-424f-ae7f-0f08f7d88b94" />

If everything goes as planned

Otherwise, read the errors in docker desktop > containers > select container > Logs or refer to mobsf

<img width="690" height="142" alt="image" src="https://github.com/user-attachments/assets/fdcddfe2-bfa9-4772-9d4d-5a24c1661952" />

If Docker Desktop encountered VM /system is not writable

<img width="767" height="40" alt="image" src="https://github.com/user-attachments/assets/80f8f735-5af8-4029-8f04-9c2955ebd5b7" />

Make sure emulator is API 28 and below

Restart emulator

<h2>If using API 29 and above</h2>

<https://stackoverflow.com/questions/63875910/android-emulator-stuck-on-reboot-after-adb-disable-verity-or-adb-remount>

	adb root
	adb shell avbctl disable-verification
	adb reboot
	adb root
	adb remount

<img width="387" height="79" alt="image" src="https://github.com/user-attachments/assets/307d641a-d9ee-43f4-83f8-8d000dc26cf6" />

MobfSFy Android Runtime

<img width="391" height="439" alt="image" src="https://github.com/user-attachments/assets/67f45e83-232b-4a9a-aa61-ec8dce8dbc14" />

In Docker Desktop

<img width="661" height="80" alt="image" src="https://github.com/user-attachments/assets/867a3942-5131-4266-b19a-92647f565dbd" />

Once testing environment is ready,

<img width="1231" height="432" alt="image" src="https://github.com/user-attachments/assets/dcc8c0fd-2b78-4b79-9f08-cd657aac1a45" />

<h1></h1>Results to extract PDF</h1>

Use MobSF Scorecard to confirm vulnerabilities and severities

Recent Scans > Scoreboard

Link to paths

<img width="1762" height="660" alt="image" src="https://github.com/user-attachments/assets/b081426a-3e0a-47f2-a737-d828152a00d3" />
