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
                    docker run -d -p 5000:80 --rm --name ${CONTAINER_TEST_NAME} ${env.APP_NAME}:${env.VERSION}
                    python ./movies/test/test.py
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
    post {
        always {
            echo "Cleaning up.."
            sh """
            docker stop ${CONTAINER_TEST_NAME} || true
            docker rmi ${env.APP_NAME}:${env.VERSION}
            """
        }
    }
}

