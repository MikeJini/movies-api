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
                    docker build --tag ${APP_NAME}:${VERSION} .
                    """
                }
            }
        }


        stage('Deploy') {
            steps {
                echo "******* Deploying a new version *******"
                script {
                    docker.withRegistry('', "${DOCKERHUB_CRED}") {
                        sh """
                        docker tag ${APP_NAME}:${VERSION} yourdockerhubusername/${APP_NAME}:${VERSION}
                        docker push yourdockerhubusername/${APP_NAME}:${VERSION}
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh """
            docker rm -f ${APP_NAME}_container || true
            docker images | grep ${APP_NAME} | awk '{print \$3}' | xargs -r docker rmi -f || true
            """
        }
    }
}
