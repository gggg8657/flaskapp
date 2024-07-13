
# Flask App CI/CD with Microsoft Azure 🚀

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white) ![CI/CD](https://img.shields.io/badge/CI%2FCD-007ACC?style=for-the-badge&logo=continuousintegration&logoColor=white)

---

## Introduction 🌟

In this project, I have explored various CI/CD methods using a simple Flask application. The deployment and automation processes leverage several tools and platforms, including Docker, GitHub Actions, Kubernetes (k8s), Jenkins, and Microsoft Azure. This document outlines the detailed steps and methodologies I have employed to achieve efficient and automated deployments.

## Tools Used 🛠️

- **Docker** ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- **GitHub Actions** ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
- **Kubernetes** ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
- **Jenkins** ![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)
- **Microsoft Azure** ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)

---

## CI/CD Process 📈

### Docker 🐳

Docker is used to create isolated environments for our applications. Each environment is encapsulated in a Docker image, ensuring consistency across different stages of the CI/CD pipeline.

- Created Docker images for the Flask application.
- Used these images as the base for further CI/CD processes.

### GitHub Actions ⚙️

GitHub Actions automates the CI/CD pipeline directly from the GitHub repository.

- Configured workflows to build and test the Docker images.
- Set up actions to deploy the images to various environments.

### Kubernetes (K8s) ☸️

Kubernetes orchestrates the deployment, scaling, and management of containerized applications.

- Deployed Docker images to a Kubernetes cluster.
- Managed CI/CD workflows using Kubernetes for scaling and resilience.

### Jenkins 🚀

Jenkins is an open-source automation server that facilitates CI/CD.

- Configured Jenkins pipelines to automate the build and deployment processes.
- Integrated Jenkins with Docker to build and push images.

### Microsoft Azure ☁️

Microsoft Azure provides cloud computing services, enabling easy and scalable deployments.

- Deployed Docker images to Azure Virtual Machines (VMs).
- Used Azure VM Scale Sets (VMSS) for scaling applications.
- Configured inbound and outbound rules for network traffic.
- Set up a Bastion server for secure access to VMs.

---

## Detailed Steps 📝

### Docker CI/CD 🐋

1. **Build Docker Image:**
   ```bash
   docker build -t flaskapp .
   ```

2. **Run Docker Container:**
   ```bash
   docker run -d -p 5000:5000 flaskapp
   ```

3. **Push Docker Image to Registry:**
   ```bash
   docker tag flaskapp:latest myregistry/flaskapp:latest
   docker push myregistry/flaskapp:latest
   ```

### GitHub Actions CI/CD 💻

1. **Configure Workflow:**
   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Build Docker Image
         run: docker build -t flaskapp .
       - name: Push to Registry
         run: |
           docker tag flaskapp:latest myregistry/flaskapp:latest
           docker push myregistry/flaskapp:latest
   ```

### Kubernetes CI/CD ☸️

1. **Deploy to K8s Cluster:**
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: flaskapp-deployment
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: flaskapp
     template:
       metadata:
         labels:
           app: flaskapp
       spec:
         containers:
         - name: flaskapp
           image: myregistry/flaskapp:latest
           ports:
           - containerPort: 5000
   ```

### Jenkins CI/CD 📦

1. **Jenkinsfile:**
   ```groovy
   pipeline {
       agent any

       stages {
           stage('Build') {
               steps {
                   script {
                       dockerImage = docker.build("flaskapp")
                   }
               }
           }
           stage('Deploy') {
               steps {
                   script {
                       docker.withRegistry('https://myregistry', 'credentials-id') {
                           dockerImage.push("latest")
                       }
                   }
               }
           }
       }
   }
   ```

### Microsoft Azure ☁️

1. **Deploy Docker Image to Azure VM:**
   ```bash
   az vm create --resource-group myResourceGroup --name myVM --image UbuntuLTS --admin-username azureuser --generate-ssh-keys

   az vm extension set --resource-group myResourceGroup --vm-name myVM --name DockerExtension --publisher Microsoft.Azure.Extensions --version 1.2

   ssh azureuser@<public-ip-address> "docker run -d -p 80:5000 myregistry/flaskapp:latest"
   ```

2. **Azure VM Scale Set (VMSS):**
   ```bash
   az vmss create --resource-group myResourceGroup --name myVMSS --image UbuntuLTS --upgrade-policy-mode automatic --admin-username azureuser --generate-ssh-keys

   az vmss extension set --resource-group myResourceGroup --vmss-name myVMSS --name DockerExtension --publisher Microsoft.Azure.Extensions --version 1.2

   ssh azureuser@<public-ip-address> "docker run -d -p 80:5000 myregistry/flaskapp:latest"
   ```

3. **Network Configuration:**
   - Set inbound and outbound rules.
   - Create a Bastion server for secure access.

---

## Conclusion 🏁

Through this project, I have gained extensive experience with CI/CD methodologies using a variety of tools and platforms. The integration of Docker with CI/CD pipelines, orchestrated deployments using Kubernetes, and scalable solutions on Microsoft Azure have significantly improved the efficiency and reliability of deployments. This comprehensive approach ensures that applications are deployed quickly, securely, and with minimal downtime.

Feel free to explore the provided code snippets and configurations to implement similar solutions for your own projects!
