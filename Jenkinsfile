pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run my-flask-app pytest'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Push to Docker registry (implement this step later)'
            }
        }
    }

    post {
        always {
            sh 'docker rmi my-flask-app'
        }
    }
}