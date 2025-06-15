pipeline {
    agent any

    environment {
        CONTAINER_TEST_NAME = "movies_test"
        APP_NAME = "mike-movies-api"
        VERSION = "${BUILD_NUMBER}"
        IMAGE_NAME = "${APP_NAME}:${VERSION}"
        DOCKERHUB_CRED = "docker-credentials"
    }

    stages {
        stage('Build') {
            steps {
                echo "****** Building the app ******"
                script {
                    sh """
                    whoami
                    cd movies
                    docker build --tag ${env.APP_NAME}:${env.VERSION} .
                    """
                }    
            }
        }

        stage('Test') {
            steps {
                echo "****** Testing the app ******"
                script {
                    sh """
                    docker run -d -p 5000:80 --name ${CONTAINER_TEST_NAME} ${env.APP_NAME}:${env.VERSION}
                    python ./movies/test/test.py
                    docker stop ${CONTAINER_TEST_NAME}
                    docker rm ${CONTAINER_TEST_NAME}
                    """
                }    
            }
        }

        stage('Deploy') {
            steps {
                echo "******* Deploying a new version *******"
                script {
                    docker.withRegistry('', "${env.DOCKERHUB_CRED}") {
                    sh """
                    docker tag ${env.APP_NAME}:${env.VERSION} mikejini/${env.APP_NAME}:${env.VERSION}
                    docker push mikejini/${env.APP_NAME}:${env.VERSION}
                    """
                    }
                }    
            }
        }
    }
}

