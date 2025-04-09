<h1><b>Windows Only</b></h1>

Works for both Static and Dynamic Analysis

<h2><b>Download Windows MobSF</b></h2>

	https://github.com/MobSF/Mobile-Security-Framework-MobSF

	https://allabouttesting.org/quick-tutorial-mobsf-installation-on-linux-windows/

<h2><b>Install Docker Desktop for Windows</b></h2>

	https://docs.docker.com/desktop/install/windows-install/

<h2><b>Android Studio</b></h2>

<b>EMULATOR NEEDS TO BE UP AND RUNNING FIRST BEFORE STARTING MOBSF</b>

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

![image](https://github.com/user-attachments/assets/0bbdb091-b1d4-4c65-b0cb-09e3950c6580)

Phone > Pixel 5

![image](https://github.com/user-attachments/assets/8d322379-db60-42b7-a64d-712871a465d1)

Download and select Pie, 28, x86, Android 9.0 (Google APIs)

![image](https://github.com/user-attachments/assets/b1f94562-e1e3-4220-b9a3-d7862f9a0705)

<h3><b>!!! Do not start emulator in Android Studio !!!</b></h3>

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

![image](https://github.com/user-attachments/assets/b26664bf-1cba-4133-995f-62d9de7e453b)

	emulator -avd Pixel_5_API_28 -writable-system -no-snapshot
 	emulator -avd <emulator name> -writable-sysytem -no-snapshot

![image](https://github.com/user-attachments/assets/7c19bcf6-e077-45ce-90ae-4342a6bded8a)

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

![Uploading image.png…]()

Will take some time to complete upload and scan

Once done, go to recent scan

There should be a static scan report made available

Leave it running, don't start anything

Will be redirected to static analysis report once scanning is done

<h2><b>Dynamic Analysis</b></h2>

Documentation guide

	https://www.youtube.com/watch?v=rmveLGhVTG8

Must complete static first

<h2><b1>Method 1</b1></h2>

Recent Scans > Static Report

![image](https://github.com/user-attachments/assets/6b25a490-7b95-4a5e-bd1e-00f660c57d15)

Scan Options > Start Dynamic Analysis

![image](https://github.com/user-attachments/assets/8723f881-143d-42f7-8706-2ac350d11065)

<h2><b1>Method 2</b1></h2>

Start Dynamic analysis directly from dashboard

Top of page > Dynamic Analyzer

![image](https://github.com/user-attachments/assets/df47eca7-357c-4b89-9336-e1796dff209b)

![image](https://github.com/user-attachments/assets/387eb462-3533-4153-8760-f96895b19ce8)

Take note of 'Android version' and 'Detected Android Version'

![image](https://github.com/user-attachments/assets/d64eb2ab-404f-4d22-b800-9d989135529b)

Docker Desktop should notify that environment is ready for testing

![image](https://github.com/user-attachments/assets/cea2f9a3-5b3c-4d9d-969a-3d932132c607)

MobSF should display something like this

![image](https://github.com/user-attachments/assets/b787af4f-6b60-4ed2-868f-5a0c3a2260f3)

Click on Start Activity and launch the target application

![image](https://github.com/user-attachments/assets/90f02598-6d76-410e-8da3-8cb68adfd002)

![image](https://github.com/user-attachments/assets/bd9b7451-c99f-403e-bd3b-46a108cec38e)

Once analysis is complete, top right, generate report

![image](https://github.com/user-attachments/assets/66e017c2-eaad-47f6-bfc5-beb1d2bf6898)

End result

![image](https://github.com/user-attachments/assets/3442323b-e2af-4fc0-9c6e-a2ece985f788)
