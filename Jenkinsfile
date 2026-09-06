

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
    }
}
