pipeline{
        agent any
        stages{
                stage('Source'){
                        steps{ checkout scm }
                }
                stage('Build'){
                        steps { echo "Compilando rama ${env.GIT_BRANCH}" }
                }
                stage('Test'){
                        steps { sh 'ls -la && cat app.py' }
                }
                stage('Deploy'){
                        steps { echo 'Despliegue simulado' }
                }
        }
}
