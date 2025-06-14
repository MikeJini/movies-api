pipeline {
    agent any

    environment {
        APP_NAME = "mike-movies-api"
        VERSION = "${BUILD_NUMBER}"
        IMAGE_NAME = "${APP_NAME}:${VERSION}"
        DOCKERHUB_CRED = "-cred"
    }

    stages {
        stage('Build') {
            steps {
                echo "****** Building the app ******"
                script {
                    sh """
                    cd movies
                    docker build --tag ${env.APP_NAME}:${env.VERSION} .
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
                    docker tag ${env.APP_NAME}:${env.VERSION} yourdockerhubusername/${env.APP_NAME}:${env.VERSION}
                    docker push yourdockerhubusername/${env.APP_NAME}:${env.VERSION}
                    """
                    }
                }    
            }
        }
    }
}
