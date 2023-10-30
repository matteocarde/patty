#!/bin/bash
DL_DELTA=10
DL_NODELTA=10
INSTANCE="instance_1_30.0_0.1_10.0.pddl";
SEARCH=gbfs
HEURISTIC=hmrp
T=$(date +%s)

rm *.sp_log


enhsp \
  -o domain.pddl \
  -f instances/$INSTANCE \
  -de 0.1 \
  -dp 0.1 \
  -dh 0.1 \
  -dl $DL_NODELTA \
  -sjr \
  -s $SEARCH \
  -h $HEURISTIC \
  -ties larger_g

mv instances/$INSTANCE.sp_log sjr-1∂-$T.sp_log


enhsp \
  -o domain.pddl \
  -f instances/$INSTANCE \
  -de 0.1 \
  -dp 1 \
  -dh 1 \
  -dl $DL_NODELTA \
  -sjr \
  -s $SEARCH \
  -h $HEURISTIC \
  -ties larger_g

mv instances/$INSTANCE.sp_log sjr-2∂-$T.sp_log


enhsp \
  -o delta/domain.pddl \
  -f delta/instances/$INSTANCE \
  -de 0.1 \
  -dp 0.1 \
  -dh 0.1 \
  -dl $DL_DELTA \
  -sjr \
  -s $SEARCH \
  -h $HEURISTIC\
  -ties larger_g

mv delta/instances/$INSTANCE.sp_log sjr-K∂-$T.sp_log

