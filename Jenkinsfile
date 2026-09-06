

pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t british-gas-utility:ci .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    minikube image load british-gas-utility:ci
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl apply -f k8s/configmap.yaml
                    kubectl apply -f k8s/secret.yaml
                    kubectl rollout status deployment/british-gas-utility
                '''
            }
        }
    }
}
