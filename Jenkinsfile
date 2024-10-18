pipeline {
    agent any

    environment {
        DOCKER_PATH = '/usr/bin/docker' // Adjust path if necessary
        PATH = "${DOCKER_PATH}:${env.PATH}" // Add Docker to PATH
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                script {
                    def dockerVersion = sh(script: 'docker --version', returnStdout: true).trim()
                    if (dockerVersion) {
                        echo "Docker is installed: ${dockerVersion}"
                    } else {
                        error "Docker is not installed or not accessible"
                    }
                }
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker tag my-flask-app <dockerhub-username>/my-flask-app:latest'
                    sh 'docker push <dockerhub-username>/my-flask-app:latest'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker...'
            sh 'docker ps -q --filter ancestor=my-flask-app | xargs -r docker stop'
            sh 'docker ps -a -q --filter ancestor=my-flask-app | xargs -r docker rm'
            sh 'docker rmi my-flask-app'
        }
    }
}
