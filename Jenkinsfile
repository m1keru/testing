node {
    stage('Prep') {
		node('tyurnote'){
        	docker.image('mysql:5').withRun('-e "MYSQL_ROOT_PASSWORD=qwertyui"'){ c ->
				docker.image('mysql:5').inside("--link ${c.id}:db") {
                	sh 'while ! mysqladmin ping -hdb --silent; do sleep 1; done'
            	}
        		docker.image('python:3-alpine').inside{
            		sh 'python -V'
	        	}
			}
    	}
	}
}
