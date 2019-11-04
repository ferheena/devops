pipeline {
    agent any
    stages {
        stage('SCMCHECKOUT') {
            steps {
                checkout scm
            }
        }
        stage('compile code') {
            steps  {
                sh 'pip install -r requirements.txt'
                dir("app") {
                    sh 'python __init__.py'
                }    
            }
        }
        stage('unitest') {
            steps {
                sh "pip install -r requirements.txt"
                sh "python -m pytest --cov=app/ tests/test_app.py -v"
            }
        }
        stage ('sonarAnyalysis') {
            steps {
                sh "/opt/sonarscanner/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner -Dsonar.host.url=http://34.93.49.84:9000 -Dsonar.projectName=saas123 -Dsonar.projectVersion=1.0 -Dsonar.projectKey=saas123 -Dsonar.sources=. -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/saas_master -Dsonar.language=py -Dsonar.python.xunit.reportPath=nosetests.xml -Dsonar.python.coverage.reportPath=coverage.xml -Dsonar.python.pylint=/usr/local/bin/pylint -Dsonar.python.pylint_config=.pylintrc -Dsonar.python.pylint.reportPath=/app/pylint-report.txt"
            }
        }
        stage('Building image') {
            steps {
                sh'docker build -t ferheena/dockerkhan:nine .'
            }
        }
        stage ('Build Push') {
            steps {
                withCredentials([string(credentialsId: 'password1', variable: 'ff')]) {
                    sh"docker login -u ferheena -p ${ff}"
                }
                sh'docker push ferheena/dockerkhan:nine'
            }
        }
    }
}


