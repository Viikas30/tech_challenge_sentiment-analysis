pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Viikas30/tech_challenge_sentiment-analysis.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop old container if it exists
                    sh '''
                    docker rm -f myapp || true
                    docker run -d -p 5000:80 --name myapp ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployed successfully! Visit http://localhost:5000"
        }
        failure {
            echo "❌ Build or deploy failed."
        }
    }
}

