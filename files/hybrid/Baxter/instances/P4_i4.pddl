(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 106.9)
(= (angle L1 ZAXES) 269.9)
(= (angle L2 xyaxes) 249.0)
(= (angle L2 ZAXES) 227.0)
(= (angle L3 xyaxes) 242.9)
(= (angle L3 ZAXES) 177.5)
(= (angle L4 xyaxes) 32.9)
(= (angle L4 ZAXES) 288.1)

(freeToMove L1) 
(freeToMove L2) 
(freeToMove L3) 
(freeToMove L4) 

(connected L1 L2 )
(connected L2 L3 )
(connected L3 L4 )


(affects L2 L3 )
(affects L2 L4 )
(affects L3 L4 )
)

(:goal (and




(> (angle L3 xyaxes) 149.5)
(> (angle L3 ZAXES) 223.7)



) )
)
