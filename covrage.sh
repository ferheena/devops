#!/bin/bash
set -e
pip install nose coverage nosexcover pylint

nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml
