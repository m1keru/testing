pipeline {
    agent any
    environment {
        CREDS=credentials('jnk-m1ke')
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
                echo '${CREDS_USR} ${CREDS_PSW}'
            }
        }
    }
}
