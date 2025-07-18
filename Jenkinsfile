pipeline {
    agent any

    environment {
        IMAGE = 'feedback-tracker:latest'
        CONTAINER = 'feedback'
        PORT = '5000'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/hardik0501/feedback-tracker.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Clean Docker') {
            steps {
                bat 'docker stop %CONTAINER% || exit 0'
                bat 'docker rm %CONTAINER% || exit 0'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p %PORT%:%PORT% --name %CONTAINER% %IMAGE%'
            }
        }
    }

    post {
        success {
            echo '✅ Feedback Tracker Deployed!'
        }
        failure {
            echo '❌ Build failed. Check logs.'
        }
    }
}
