# Evaluation of Q-Learning and SARSA in the context of Cloud Autoscaling for Scientific Workflows
This project contains the runnable code for the experiments of the work "Evaluation of Q-Learning and SARSA in the context of Cloud Autoscaling for Scientific Workflows". 

## Description

**Abstract** Q-Learning and SARSA are two well-known reinforcement learning (RL) algorithms that have shown promising results in cloud autoscaling. However, no previous works have compared their performance for learning scaling policies in workflow applications. Given that SARSA tends to be more conservative than Q-Learning while exploring the solution space, we hypothesize that SARSA can perform better than Q-Learning without significant losses in policy performance. In this study, we conducted an in-depth evaluation of both algorithms in the context of workflow autoscaling in the cloud. To do so, we based our experiments on a state-of-the-art strategy that showed promising results in learning optimal scaling policies for reducing execution time and monetary cost. We conducted experiments on simulated environments with four benchmark workflows and two types of virtual machines. Results show that SARSA outperforms Q-Learning in almost all cases. This means that SARSA presents better performance during learning with gains between 8.2% and 16.8%, and also SARSA found policies with better performance, i.e., improvements between 1.4% and 17.9%. There is one case of loss during learning (1.8%) but with a gain in policy performance of 1.4%. There is also one case of loss in policy performance of 6.7%, but with a gain during learning of 16.8%. In both cases of loss, there is a trade-off between performance during learning and resulting policy performance. These are interesting results to consider when selecting the best RL strategy for workflow autoscaling in the cloud.


**Contact information**:
 - Yisel Garí: ygari@uncu.edu.ar
 - Elina Pacini: epacini@uncu.edu.ar
 - Luciano Robino: lrobino@conicet.gov.ar
 - Cristian Mateos: cristian.mateos@isistan.unicen.edu.ar
 - David A. Monge: dmonge@uncu.edu.ar

## Instructions

### How to run the code

To reproduce the experiments, please use the following entry-point script and command:

```shell
sh scripts/rl-runAll-experiments.sh
```

The output of the experiments will be placed in the following folder:

```text
results/
```
### Output files

```text
1.results_experiments.csv  			# Run (test) simulation results
1.training_results_experiments.csv  		# Training simulation results

2.analysis_train_mean-performace-strategies.csv  	# Tableau-ready raw data (training)
2.analysis_test_mean-performace-strategies.csv  	# Tableau-ready raw data (testing)

2.analysis_aggregatedMC-train-median-comp-test.csv 	# Statistical significance results (training)
2.analysis_totalReward-train-median-comp-test
2.analysis_makespanH-train-median-comp-test         
2.analysis_totalCost-train-median-comp-test

2.analysis_aggregatedMC-test-median-comp-test.csv  # Statistical significance results (testing)
2.analysis_totalReward-test-median-comp-test
2.analysis_makespanH-test-median-comp-test
2.analysis_totalCost-test-median-comp-test  

executedExperiments 				# Executed configurations
trainingInfo.csv 				# Elapsed runtime information (training)
testingInfo.csv 				# Elapsed runtime information (testing)
```

### Project structure

```text
data/instances/ 		# VM info
lib/ 				# Library dependencies (JAR format)
logs/ 				# Execution logs
qTables/ 			# qTables
qTablesSum/ 			# qTablesSummary
results/ 	# Experiment results
scripts/ 			# Python and command-line scripts
workflows/ 			# Workflow information

cloudautoscaling-1.0.jar 	# Project compiled code (JAR format)
casesRL_test.csv				# Run configurations for training
casesRL_train.csv       # Run configurations for testing
```

### Execution details and used libraries

The experiments reported in the paper were run on a virtul node of TOKO with a AMD Ryzen 7 2700/3700x with 8 cores, 16 logical processors, and 64 GB of RAM memory running (ToDo:SO?), Java 17 and Apache Maven 3.8.4.
The description of the four workflows studied are available on-line through the Pegasus WorkflowGenerator: https://confluence.pegasus.isi.edu/display/pegasus/WorkflowHub. 
The implementation of the Q-learning and SARSA algorithms was provided by the Brown-UMBC Reinforcement Learning and Planning (BURLAP) (http://burlap.cs.brown.edu/) Java code library version 3.0. 
Simulations were performed using the CloudSimPlus (https://cloudsimplus.org/) simulator version 7.2.0. 
The statistical significance of the results was assessed using the implementation of the Mann-Whitney U test incorporated in Apache Commons Math (http://commons.apache.org/proper/commons-math/) version 3.3. 
Finally, Tableau Public (http://public.tableau.com) version 2023.1 and matplotlib (https://matplotlib.org/) version 3.2.2 were used to generate the visualizations.
