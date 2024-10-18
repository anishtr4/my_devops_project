pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                script {
                    try {
                        sh 'docker --version'
                    } catch (Exception e) {
                        error "Docker is not installed or not accessible. Please install Docker and ensure it's running."
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        sh 'docker build -t my-flask-app .'
                    } catch (Exception e) {
                        error "Failed to build Docker image: ${e.message}"
                    }
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    try {
                        sh 'docker run my-flask-app pytest'
                    } catch (Exception e) {
                        error "Failed to run tests in Docker: ${e.message}"
                    }
                }
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
            script {
                try {
                    sh 'docker rmi my-flask-app'
                } catch (Exception e) {
                    echo "Failed to remove Docker image: ${e.message}"
                }
            }
        }
    }
}