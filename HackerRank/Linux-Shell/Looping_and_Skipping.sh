#!/bin/env bash
###################################################################
#
# Looping and Skipping
######################
#
# Your task is to use for loops to display only odd natural numbers
# from to 1 - 99.
#
####################################################################

solution_one () {
  seq 1 3 99


solution_two () {
  for i in {1..99}; do
    if [[ ! $(($i % 2)) -eq 0 ]]; then
      echo $i
    fi
  done
}

solution_one
solution_two
