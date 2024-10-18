pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
                sh 'source venv/bin/activate && pip install pytest flake8'
            }
        }
        
        stage('Run tests') {
            steps {
                sh 'source venv/bin/activate && pytest'
            }
        }
        
        stage('Lint') {
            steps {
                sh 'source venv/bin/activate && flake8 app.py tests/'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to production...'
                // Add your deployment steps here
            }
        }
    }
}