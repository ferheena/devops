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
                sh "/opt/sonarscanner/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner -Dsonar.host.url=http://34.93.49.84:9000 -Dsonar.projectName=saas12 -Dsonar.projectVersion=1.0 -Dsonar.projectKey=saas12 -Dsonar.sources=. -Dsonar.projectBaseDir=/var/lib/jenkins/workspace/saas_master -Dsonar.python.coveragePlugin=cobertura -Dsonar.python.xunit.reportPath=build_results/testresults.xml -Dsonar.python.pylint=/usr/local/bin/pylint -Dsonar.python.pylint.reportPath=pylint-report.txt -Dsonar.python.coverage.reportPaths=build_results/coverage.xml"
            }
        }
        stage('Building image') {
            steps {
                sh'docker build -t ferheena/dockerkhan:eight .'
            }
        }
        stage ('Build Push') {
            steps {
                withCredentials([string(credentialsId: 'password1', variable: 'ff')]) {
                    sh"docker login -u ferheena -p ${ff}"
                }
                sh'docker push ferheena/dockerkhan:eight'
            }
        }
    }
}


