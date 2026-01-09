[**https://redfoxsecurity.medium.com/burp-suite-install-how-to-add-burps-ca-certificate-as-a-system-certificate-on-android-05909e6a1d6b**](https://redfoxsecurity.medium.com/burp-suite-install-how-to-add-burps-ca-certificate-as-a-system-certificate-on-android-05909e6a1d6b)

---

<h1>Export Burp CA</h1>

Burp > Settings

<img width="307" height="321" alt="image" src="https://github.com/user-attachments/assets/1bde5184-8af1-48f9-9e65-e424dcc801e9" />

Certificate in DER format

<img width="355" height="245" alt="image" src="https://github.com/user-attachments/assets/3ee1bbc4-00c0-43b1-8b9c-08a0e6a8ace5" />

Save as burp_CA.crt

<img width="401" height="34" alt="image" src="https://github.com/user-attachments/assets/7f4b125c-d5c3-4cdc-98dc-ab237d6b6e39" />

<h1>Download openssl</h1>

[https://openssl-library.org/source/](https://openssl-library.org/source/)

Put it in path

<img width="218" height="24" alt="image" src="https://github.com/user-attachments/assets/e959baed-2412-4813-b97d-c86aff84b2fd" />

C:\Program Files\OpenSSL-Win64\bin

<h1>Identify hash of pem file</h1>

openssl x509 -inform DER -in burp_CA.crt -out burp_ca.pem

Converts burp_CA.crt to burp_ca.pem

openssl x509 -inform PEM -subject_hash_old -in burp_ca.pem

<img width="736" height="58" alt="image" src="https://github.com/user-attachments/assets/cc2c429a-a100-40c2-9477-25c393c796c8" />

Usually hash value is the same > 9a5ba575

Rename the PEM file to the hash value with '.0' (zero) as
        extension

<img width="85" height="103" alt="image" src="https://github.com/user-attachments/assets/d7f8d2d9-a086-4491-86a2-8c8654053246" />

<h1>Push the CA cert to emulator</h1>

adb -s emulator-5554 root

adb -s emulator-5554 remount

adb -s emulator-5554 push 9a5ba575.0 /system/etc/security/cacerts/

adb -s emulator-5554 shell chmod 644 /system/etc/security/cacerts/9a5ba575.0

adb -s emulator-5554 reboot

Emulator will reboot

<h1>Verify burp CA Cert installation</h1>

Emulator > Settings > Security and location > Advanced > Encryption and Credentials > System

<img width="364" height="185" alt="image" src="https://github.com/user-attachments/assets/9cb6c614-6872-43e2-9d5c-37d20a624474" />

Portswigger CA cert must be under System

<h1>Configure Proxy</h1>

Emulator \> Extended controls \> Proxy

Hostname = 127.0.0.1

Port = 8080

Apply

Basically the listener for burp

<img width="303" height="130" alt="image" src="https://github.com/user-attachments/assets/422a6765-1c60-467b-9373-eb14b8c8ea6e" />

This is how it should look like

<img width="867" height="642" alt="image" src="https://github.com/user-attachments/assets/489425ce-2c87-4cd8-a945-470cb70eaff6" />

End result

<img width="850" height="160" alt="image" src="https://github.com/user-attachments/assets/bdcce79b-d806-4b14-9f15-5b9f75e64fdc" />


