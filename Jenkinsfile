pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Code checked out from GitHub"
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    echo "🧪 Setting up Python environment..."
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install httpx
                    echo "✅ Dependencies installed"
                    
                    echo "🧪 Running tests..."
                    python test_app.py
                    echo "✅ All tests passed!"
                '''
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    echo "🐳 Building Docker image..."
                    docker build -t fastapi-app .
                    echo "✅ Docker image built successfully!"
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    echo "🚀 Deploying application..."
                    # For now, just show deployment message
                    # Later we'll add Kubernetes deployment
                    echo "✅ Application deployment ready!"
                    echo "📊 Project Status:"
                    echo "   - FastAPI App: ✅"
                    echo "   - Docker: ✅" 
                    echo "   - GitHub Actions: ✅"
                    echo "   - Jenkins: ✅"
                    echo "   - Kubernetes: Next step"
                '''
            }
        }
    }
    
    post {
        always {
            echo "🏁 Pipeline execution completed"
        }
        success {
            echo "🎉 PFE Project Pipeline SUCCESS!"
            sh 'echo "All stages completed successfully!"'
        }
        failure {
            echo "❌ Pipeline failed - check logs"
        }
    }
}
