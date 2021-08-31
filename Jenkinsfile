pipeline {
    agent any
    environment {
        image_name = "mefaldemisov/devops_course"
    }
    stages {
        stage('Linting and testing') {
            agent {
                docker {
                    image 'python:3.9-alpine'
                }
            }
            steps {
                sh 'pip3 install --no-cache-dir -r app_python/requirements.txt'
                sh 'pylint app_python/*.py tests/*.py'
                sh 'pip3 install -e .'
                sh 'python3 -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    dockerImage = docker.build(image_name, './app_python')
                    docker.withRegistry('', 'docker-hub') {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push("latest")
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