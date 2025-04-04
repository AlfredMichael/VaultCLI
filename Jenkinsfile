pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t password-manager .'
            }
        }
        stage('Test') {
            steps {
                // Run the container and execute unit tests
                sh 'docker run password-manager python -m unittest discover -s test'
            }
        }
    }
}
