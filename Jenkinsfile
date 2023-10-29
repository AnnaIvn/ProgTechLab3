pipeline {
    options {timestamps()}

    agent none
    environment {
        DOCKER_IMAGE = 'annaiiv/lab3_flask_app'
        FLASK_APP = 'lab3_flask_app.py'
    }

    stages {
        stage('Check scm') {
            agent any
            steps {
                // Checkout the code from your version control system (e.g., Git)
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build compleated."
            }
        }

        stage('Test') {
            agent{
                docker{
                    image 'alpine'
                    args '-u=\"root\"'
                }
            }
            steps{
                sh "apk add --update python3 py-pip"
                sh "pip install Flask"
                // sh 'pip install xmlrunner'
                sh "python3 ${FLASK_APP}"
                echo "Test section compleated."
            }
        }
    }

    // stage('Deploy') {
    //     steps {
    //         script {
    //             // Build Docker image
    //             sh "docker build -t ${DOCKER_IMAGE} -f Dockerfile ."
    //             // Push Docker image to Docker Hub
                
    //             // withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
    //             //     sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
    //             // }
                
    //             sh "docker push ${DOCKER_IMAGE}"
    //         }
    //     }
    // }

    // stage('Deploy') {
    //     steps {
    //         script {
    //             // Navigate to the directory containing Jenkinsfile
    //             dir('path/to/your/Jenkinsfile') {
    //                 // Deactivate virtual environment
    //                 sh "deactivate"
    //                 // Replace with your deployment steps
    //                 sh "echo 'Deploying Flask app...'"
    //             }
    //         }
    //     }
    // }

    post {
        success {
            // This block will be executed if the pipeline is successful
            echo 'Flask app successfully deployed!'
        }

        failure {
            // This block will be executed if the pipeline fails
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
