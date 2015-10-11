#!/usr/bin/env python
stages = []
positions = []
curr_stage = 1

stage = raw_input("Give me current stage: ")
stage = stage[:4]
stages.append(stage)

print '1 - ', stages[0][1]
print '2 - ', stages[0][1]
print '3 - ', stages[0][2]
print '4 - ', stages[0][3]

answer1 = raw_input("Answer: ")
position1 = stage.index(answer1)

stage = raw_input("Give me current stage: ")
stage = stage[:4]
stages.append(stage)

print '1 - ', '4'
print '2 - ', stage[position1]
print '3 - ', stage[0]
print '4 - ', stage[position1]

answer2 = raw_input("Answer: ")
position2 = stage.index(answer2)

stage = raw_input("Give me current stage: ")
stage = stage[:4]
stages.append(stage)

print '1 - ', answer2
print '2 - ', answer1
print '3 - ', stage[2]
print '4 - ', '4'

answer3 = raw_input("Answer: ")
position3 = stage.index(answer3)

stage = raw_input("Give me current stage: ")
stage = stage[:4]
stages.append(stage)

print '1 - ', stage[position1]
print '2 - ', stage[0]
print '3 - ', stage[position2]
print '4 - ', stage[position2]

answer4 = raw_input("Answer: ")
position4 = stage.index(answer4)

stage = raw_input("Give me current stage: ")
stage = stage[:4]
stages.append(stage)

print '1 - ', answer1
print '2 - ', answer2
print '3 - ', answer4
print '4 - ', answer3
