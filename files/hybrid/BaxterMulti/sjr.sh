#!/bin/bash
DL_DELTA=6
DL_NODELTA=3
INSTANCE="problem-10.pddl";
SEARCH=gbfs
HEURISTIC=hadd
T=$(date +%s)

rm *.sp_log


enhsp \
  -o domain.pddl \
  -f instances/$INSTANCE \
  -de 1 \
  -dp 1 \
  -dh 1 \
  -s $SEARCH \
  -h $HEURISTIC\
  -dl $DL_NODELTA \
  -sjr \

mv instances/$INSTANCE.sp_log sjr-1∂-$T.sp_log


enhsp \
  -o domain.pddl \
  -f instances/$INSTANCE \
  -de 1 \
  -dp 5 \
  -dh 5 \
  -dl $DL_NODELTA \
  -sjr \
  -s $SEARCH \
  -h $HEURISTIC 

mv instances/$INSTANCE.sp_log sjr-2∂-$T.sp_log


enhsp \
  -o delta/domain.pddl \
  -f delta/instances/$INSTANCE \
  -de 1 \
  -dp 1 \
  -dh 1 \
  -s $SEARCH \
  -h $HEURISTIC\
  -dl $DL_DELTA \
  -sjr \

mv delta/instances/$INSTANCE.sp_log sjr-K∂-$T.sp_log

