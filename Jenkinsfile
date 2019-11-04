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
                sh "/opt/sonarscanner/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner -Dsonar.host.url=http://34.93.49.84:9000 -Dsonar.projectName=saas -Dsonar.projectVersion=1.0 -Dsonar.projectKey=saas -Dsonar.sources=. -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/saas_master -Dsonar.python.coveragePlugin=cobertura -Dsonar.python.pylint=/usr/local/bin/pylint -Dsonar.python.pylint.reportPath=pylint-report.txt -Dsonar.python.coverage.reportPath=.coverage.xml"
            }
        }
        stage('Building image') {
            steps {
                sh'docker build -t ferheena/dockerkhan:six .'
            }
        }
        stage ('Build Push') {
            steps {
                withCredentials([string(credentialsId: 'password1', variable: 'ff')]) {
                    sh"docker login -u ferheena -p ${ff}"
                }
                sh'docker push ferheena/dockerkhan:six'
            }
        }
    }
}


