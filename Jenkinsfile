pipeline {
    agent any

    stages {
        stage('Confirm Successfull GitPull') {
            steps {
                echo 'GitPull Success'
            }
        }
        stage('PIP Install Requirments.txt'){
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Testing'){
            steps {
                echo 'This stage will run Pytest when written'
            }
        }

    }
}