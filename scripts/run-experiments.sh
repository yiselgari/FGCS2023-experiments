#!/bin/bash

#cleaning directories [logs, qTables, qTablesSum, results]
sh scripts/clean.sh

#running experiments
./scripts/simulate.py 4 casesRL_train.csv

#running analyses
java -Xmx256m -cp "./cloudautoscaling-1.0.jar" com.cloudautoscaling.Step2_LaunchAnalyses

echo "Experiments completed, check outputDirectory: results"


