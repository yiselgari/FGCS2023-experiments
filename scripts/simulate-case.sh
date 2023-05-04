#!/bin/bash

#path_output="/home/ygari/scratch/"
path_output=""
#path_input="/home/ygari/rla_input/"
path_input=""

classpath=$path_input"./target/classes"

OTHER_LIBS=$path_input"./target/lib"

for i in `find $OTHER_LIBS -name '*.jar' | grep -v OLD`
do
	classpath=$classpath":"$i
done

echo "------------------- LIBRARIES ------------------"
echo $classpath
echo "------------------------------------------------"
echo

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
	java -Xmx256m -cp "$classpath" -Djava.io.tmpdir=~/scratch/cloudautoscaling/tmp com.cloudautoscaling.experiments.StartSingleExperimentCase $caseParameters
	echo $caseID >> executedExperiments
fi
rm sim_trace 2> /dev/null
rm sim_report 2> /dev/null

echo "DONE"
