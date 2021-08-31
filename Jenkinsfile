pipeline {
    agent { docker { image 'python:3.9-alpine' } }
    stages {
        stage('Preparation') {
            steps {
                sh 'pip install --no-cache-dir -r app_python/requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'pylint app_python/*.py tests/*.py'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install -e .'
                sh 'python -m pytest'
            }
        }
        stage('Push') {
	    	docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
				app.push("${env.BUILD_NUMBER}")
	        }
	    }
    }
}