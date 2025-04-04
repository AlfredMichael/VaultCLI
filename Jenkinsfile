pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Build the Docker image
                bat 'docker build -t password-manager .'
            }
        }
        stage('Test') {
            steps {
                // Run the container and execute unit tests
                bat 'docker run password-manager python -m unittest discover -s test'
            }
        }
    }
}
