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
        BIN="server.py"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo PATH is  ${CC}'
            }
        }
        stage('Deploy') {
            agent {
		        //docker { image 'python3' }
				label 'tyurnote'
    		}
            steps {
                echo 'Deploying....'
                sh '/usr/bin/env python3 ${BIN}'
            }
        }
    }
}
