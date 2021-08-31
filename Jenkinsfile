pipeline {
    agent any
    environment {
        image_name = "mefaldemisov/devops-course"
    }
    stages {
        stage('Preparation') {
            steps {
                sh 'pip3 install --no-cache-dir -r app_python/requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'pylint app_python/*.py tests/*.py'
            }
        }
        stage('Test') {
            steps {
                sh 'pip3 install -e .'
                sh 'python3 -m pytest'
            }
        }
        stage('Build') {
            steps{
                script {
                    dockerImage = docker.build image_name
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub') {
                        app.push("$BUILD_NUMBER")
                        app.push("latest")
                    }
                }
            }
	    }
	    stage('Remove Unused docker image') {
            steps {
                sh "docker rmi $image_name:$BUILD_NUMBER"
                sh "docker rmi $image_name:latest"
            }
        }
    }
}