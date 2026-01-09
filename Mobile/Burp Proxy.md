[**https://redfoxsecurity.medium.com/burp-suite-install-how-to-add-burps-ca-certificate-as-a-system-certificate-on-android-05909e6a1d6b**](https://redfoxsecurity.medium.com/burp-suite-install-how-to-add-burps-ca-certificate-as-a-system-certificate-on-android-05909e6a1d6b)

1.  **Export Burp CA**

    1.  **Burp \> Settings**

        1.  <img src="media/image1.png" style="width:3.19792in;height:3.34375in" />

    2.  **Certificate in DER format**

        1.  <img src="media/image2.png" style="width:3.69792in;height:2.54167in" />

    3.  **Save as burp_CA.crt**

        1.  <img src="media/image3.png" style="width:4.17708in;height:0.34375in" />

2.  **Download openssl**

    1.  [**https://openssl-library.org/source/**](https://openssl-library.org/source/)

        1.  **Put it in path**

            1.  <img src="media/image4.png" style="width:2.26042in;height:0.25in" />

            2.  **C:\Program Files\OpenSSL-Win64\bin**

3.  **Gain hash of pem file**

    1.  **openssl x509 -inform DER -in burp_CA.crt -out burp_ca.pem**

        1.  **Converts burp_CA.crt to burp_ca.pem**

    2.  **openssl x509 -inform PEM -subject_hash_old -in burp_ca.pem**

        1.  <img src="media/image5.png" style="width:6.26806in;height:0.49444in" />

            1.  **Usually hash value is the same**

                1.  **9a5ba575**

    3.  **Rename the PEM file to the hash value with '.0' (zero) as
        extension**

        1.  <img src="media/image6.png" style="width:0.88542in;height:1.0625in" />

4.  **Push the CA cert to emulator**

    1.  **adb -s emulator-5554 root**

    2.  **adb -s emulator-5554 remount**

    3.  **adb -s emulator-5554 push 9a5ba575.0
        /system/etc/security/cacerts/**

    4.  **adb -s emulator-5554 shell chmod 644
        /system/etc/security/cacerts/9a5ba575.0**

    5.  **adb -s emulator-5554 reboot**

        1.  **Emulator will reboot**

5.  **Verify burp CA Cert installation**

    1.  **Emulator \> Settings \> Security and location \> Advanced \>
        Encryption and Credentials \> System**

        1.  <img src="media/image7.png" style="width:3.79167in;height:1.92708in" />

        2.  **Portswigger CA cert must be under System**

6.  **Configure Proxy**

    1.  **Emulator \> Extended controls \> Proxy**

        1.  **Hostname = 127.0.0.1**

        2.  **Port = 8080**

        3.  **Apply**

        4.  **Basically the listener for burp**

            1.  <img src="media/image8.png" style="width:3.15625in;height:1.34375in" />

        5.  **This is how it should look like**

            1.  <img src="media/image9.png" style="width:6.26806in;height:4.64167in" />

    2.  **End result**

        1.  <img src="media/image10.png" style="width:6.26806in;height:1.17222in" />

<!-- -->

7.  **s**

8.  **s**
