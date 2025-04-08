<h2><b>Requirements</b></h2>

	Docker Desktop
	JAVA

<h2><b>Download JAVA and set in System PATH</b></h2>

<h2><b>Download SonarQube</b></h2>

https://www.sonarsource.com/products/sonarqube/downloads/

<h2><b>Install SonarQube</b></h2>

https://www.sonarsource.com/products/sonarqube/downloads/https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/#windows

Open the text file shown below and modify accordingly

	C:\Users\User\.dotnet\tools\.store\dotnet-sonarscanner\10.1.0\dotnet-sonarscanner\10.1.0\tools\netcoreapp3.1\any\sonar-scanner-5.0.1.3006\conf\sonar-scanner.properties

Uncomment and add localhost:9000

![image](https://github.com/user-attachments/assets/d657fd42-d904-47f7-8a9d-10215fe55231)

<h2><b>Download and install Docker Desktop</b></h2>

https://docs.docker.com/desktop/setup/install/windows-install/

Create sonarqube container

	docker run -d -p 9000:9000 --name sonarqube sonarqube:latest

Open Docker Desktop and start sonarqube

![image](https://github.com/user-attachments/assets/b6068ecc-8697-4374-b578-0b4becee86b7)

Browse to http://localhost:9000
		
Default Credentials

	admin:admin
	Change password to Testing@12345

<h2><b>Start Scan</b></h2>

Browse to http://localhost:9000

Create local project > Name the Project accordingly > Use global setting > Create Project > Analyze Locally

Generate Token

Take note of the token value

![image](https://github.com/user-attachments/assets/ca354476-157f-4eb9-917d-d4c2c0f19a21)

Select language of source codes (Usually just go with 'Other')

![image](https://github.com/user-attachments/assets/8d09816c-e2ff-4e79-a9c6-c5452cf611a0)

Next step of the page should include instructions on how to start the scan 

![image](https://github.com/user-attachments/assets/a51ee8eb-fc40-4fbf-a5eb-93fbaf18188c)

	"C:\Users\User\Desktop\SCR\SonarQube Windows\sonar-scanner-7.0.2.4839-windows-x64\bin\sonar-scanner.bat" -D"sonar.projectKey=Test1" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_<Sonar Token Value>"

Scan should start in cmd

![image](https://github.com/user-attachments/assets/fd6d8a7a-84ca-4677-b7e0-1202a212db82)

Once the scan has completed, web page will automatically redirect to the results page

![image](https://github.com/user-attachments/assets/b988bf39-519f-4dcc-86b3-6dd99d107c20)
