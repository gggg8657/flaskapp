pipeline {
   agent any
   environment{
      NEW_VERSION = "1.0.0"
      ADMIN_CREDENTIALS = credentials('admin_user_credentials')
   }
   parameters {
      string(name: 'VERSION', defaultValue: '', description: 'deployment vers')
      choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description)
      booleanParam(name: 'executeTests', defaultValue: true, description: '')
   }
   stages {
      stage("build") {
         when{
            expression{
               env.GIT_BRANCH == 'origin/main'
            }
         }
         steps {
            echo 'building the applicaiton...'
            echo "building version ${NEW_VERSION}"
         }
      }
      stage("test") {
         when{
            expression{
               env.GIT_BRANCH =='origin/test' || env.GIT_BRANCH ==''
            }
         }
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
            withCredentials([[$class: 'UsernamePasswordMultiBinding',
            credentialsId: 'admin_user_credentials',
            usernameVariable: 'USER',
            passwordVariable: 'PWD'
            ]]){
               sh 'printf ${USER}'
            }
         }
      }
   }
   post {
         always {
            echo 'building..'
         }
         success {
               echo 'success'
         }
         failure {
               echo 'failure'
         }
      }
   }