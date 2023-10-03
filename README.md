# Online RL-based Cloud Autoscaling for Scientific Workflows: Evaluation of Q-Learning and SARSA
This project contains the runnable code for the experiments of the work "Evaluation of Q-Learning and SARSA in the context of Cloud Autoscaling for Scientific Workflows". 

## Description

**Abstract** Q-Learning and SARSA are two well-known reinforcement learning (RL) algorithms that have shown promising results in several application domains. However, their approach to build solutions is quite different. For example, SARSA tends to be more conservative than Q-Learning while exploring the solution space. Motivated by such differences, in this paper, we conducted an evaluation of both algorithms in the
context of online workflow autoscaling in pay-per-use Clouds, where the goal is to learn optimal virtual machine scaling policies to optimize metrics such as execution time and monetary costs. To do so, we based our experiments on a state-of-the-art scaling strategy with encouraging results in learning optimal scaling policies for reducing execution time and monetary cost. We conducted experiments on simulated environments with four widespread benchmark workflows and two types of virtual machines. Results show that SARSA outperforms Q-Learning in almost all cases. For two workflows SARSA obtains significant gains of up to 40.8% in the first 100 and 300 episodes respectively and losses less than 6% in all episodes
observed. In one workflow SARSA achieves significant gains up to 13.9% and no significant losses were observed. There was only one workflow with no significant gains and one significant loss (16.2%) in 1 of 50 observations. In summary, we found multiple stages where SARSA achieves significant and remarkable gains, and the rest of the time both algorithms had a similar performance. In general terms, we can observe that SARSA performs better for learning scaling policies in the Cloud considering workflow applications commonly used by the community to benchmark Cloud workflow resource allocation techniques. These represent interesting results to further drive the design and selection of RL-based autoscaling strategies to
schedule workflow executions in the Cloud.


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
sh scripts/run-experiments.sh
```

The output of the experiments will be placed in the following folder:

```text
results/
```
### Output files

```text
1.training_results_experiments.csv  		# Training simulation results

2.analysis_train_mean-performace-strategies.csv  # Tableau-ready raw data
2.analysis_aggregatedMC-train-performace.csv
2.analysis_makespanH-train-performace.csv
2.analysis_totalCost-train-performace.csv

2.analysis_aggregatedMC-train-median-comp-test.csv 	# Statistical significance results
2.analysis_makespanH-train-median-comp-test         
2.analysis_totalCost-train-median-comp-test

2.analysis_wind_aggregatedMC-train-median-comp-test.csv  # Statistical significance results by window
2.analysis_wind_makespanH-train-median-comp-test         
2.analysis_wind_totalCost-train-median-comp-test
 

executedExperiments 				# Executed configurations
trainingInfo.csv 				# Elapsed runtime information (training)
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
casesRL_test.csv				# Run configurations
```

### Execution details and used libraries

The experiments reported in the paper were run on a virtul node of TOKO with a AMD Ryzen 7 2700/3700x with 8 cores, 16 logical processors, and 64 GB of RAM memory running (ToDo:SO?), Java 17 and Apache Maven 3.8.4.
The description of the four workflows studied are available on-line through the Pegasus WorkflowGenerator: https://confluence.pegasus.isi.edu/display/pegasus/WorkflowHub. 
The implementation of the Q-learning and SARSA algorithms was provided by the Brown-UMBC Reinforcement Learning and Planning (BURLAP) (http://burlap.cs.brown.edu/) Java code library version 3.0. 
Simulations were performed using the CloudSimPlus (https://cloudsimplus.org/) simulator version 7.2.0. 
The statistical significance of the results was assessed using the implementation of the Mann-Whitney U test incorporated in Apache Commons Math (http://commons.apache.org/proper/commons-math/) version 3.3. 
Finally, Tableau Public (http://public.tableau.com) version 2023.1 and matplotlib (https://matplotlib.org/) version 3.2.2 were used to generate the visualizations.
