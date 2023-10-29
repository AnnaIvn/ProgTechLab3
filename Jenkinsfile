pipeline {
    options {timestamps()}

    agent none

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
                sh 'apk add --update python3 py-pip'
                sh 'pip install Flask'
                // sh 'pip install xmlrunner'
                sh 'python3 lab3_flask_app.py'
                echo "Test section compleated."
            }
        }
    }

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
