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
                sh 'ls -lah ${CC}'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
