pipeline {
   agent any
   environment{
      NEW_VERSION = "1.0.0"
      ADMIN_CREDENTIALS = credentials('admin_user_credentials')
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
            echo "deploying with ${ADMIN_CREDENTIALS}"
            sh 'printf ${ADMIN_CREDENTIALS}'
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