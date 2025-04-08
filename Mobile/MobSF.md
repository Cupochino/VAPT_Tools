<h1><b>Windows</b></h1>

Works for both Static and Dynamic Analysis

<h2><b>Download windows mobsf</b></h2>

	https://github.com/MobSF/Mobile-Security-Framework-MobSF

	https://allabouttesting.org/quick-tutorial-mobsf-installation-on-linux-windows/

<h2><b>Install docker desktop for windows</b></h2>

	https://docs.docker.com/desktop/install/windows-install/

<h2><b>Android Studio</b></h2>

<b>EMULATOR NEEDS TO BE UP AND RUNNING FIRST BEFORE STARTING MOBSF</b>

Download any apk file to test

	https://apkpure.net/

Android studio how to link to MobSF guide

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

<h3><b>!!! Do not start emulator in android studio !!!</b></h3>

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

Usually emulator-5554

Help > About

![image](https://github.com/user-attachments/assets/8c4dd665-d7a1-4565-bc4c-65bb8ecebfa4)

![image](https://github.com/user-attachments/assets/b5cc3617-06d3-4f11-b9d3-b9262eecab31)

<h2><b>Running MobSF</b></h2>





















































