pipeline {
    agent any
    environment {
        CC = """ 
            ${sh(
                returnStdout: true,
                script: 'echo $PATH'
            )}
        """    
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo PATH is  ${CC}'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
