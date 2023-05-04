#!/bin/bash

total=`cat cases*.csv | grep -v "#" | wc -l`
progress=`cat executedExperiments | wc -l`
echo "$progress cases from $total"
echo `echo "$progress * 100 / $total" | bc`"%"

