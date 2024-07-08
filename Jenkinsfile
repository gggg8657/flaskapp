pipeline {
    agent any

    environment {
        NEW_VERSION = "1.0.0"
        ADMIN_CREDENTIALS = credentials('admin_user_credentials')
    }

    parameters {
        string(name: 'VERSION', defaultValue: '', description: 'Deployment version')
        choice(name: 'VERSION_CHOICE', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Choose a version to deploy')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Execute tests')
    }

    stages {
        stage("Build") {
            when {
                expression {
                    env.GIT_BRANCH == 'origin/main'
                }
            }
            steps {
                echo 'Building the application...'
                echo "Building version ${NEW_VERSION}"
            }
        }
        
        stage("Test") {
            when {
                expression {
                    env.GIT_BRANCH == 'origin/test' || env.GIT_BRANCH == ''
                }
            }
            steps {
                echo 'Testing the application...'
            }
        }
        
        stage("Deploy") {
            steps {
                echo 'Deploying the application...'
                withCredentials([usernamePassword(credentialsId: 'admin_user_credentials', usernameVariable: 'USER', passwordVariable: 'PWD')]) {
                    sh 'printf ${USER}'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Building...'
        }
        success {
            echo 'Success'
        }
        failure {
            echo 'Failure'
        }
    }
}