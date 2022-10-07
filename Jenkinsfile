pipeline {
    agent any

    stages {
        stage('Confirm Successfull GitPull') {
            steps {
                echo 'GitPull Success'
            }
        }
        stage('Docker destroy'){
            steps {
                sh 'docker-compose down -rmi all'
            }
        }
        stage('Docker Build'){
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Check App is up'){
            steps {
                sh 'sleep 20'
                sh 'docker ps'
            }
        }

    }
}