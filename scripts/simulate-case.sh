#!/bin/bash

path_output=""
path_input=""

jarpath=$path_input"./cloudautoscaling-1.0.jar"

# receive simulation case parameters
caseParameters=$1

touch executedExperiments

caseID=`echo $caseParameters | sed "s/\-//g" | sed "s/ //g"`
matches=`cat executedExperiments | grep "$caseID" | wc -l`
if [ "$matches" != "0" ]
then
	echo "> already executed case, skipping... ($caseParameters)"
else
	echo ""
	echo "*****"
	echo "STARTING EXPERIMENT CASE: $caseParameters"
	echo "*****"
	java  -Xmx256m -cp "$jarpath" com.cloudautoscaling.experiments.StartSingleExperimentCase $caseParameters
	echo $caseID >> executedExperiments
fi
rm sim_trace 2> /dev/null
rm sim_report 2> /dev/null

echo "DONE"
