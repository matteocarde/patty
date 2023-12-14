(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 275.3)
(= (angle L1 ZAXES) 185.2)
(= (angle L2 xyaxes) 104.5)
(= (angle L2 ZAXES) 299.8)
(= (angle L3 xyaxes) 266.2)
(= (angle L3 ZAXES) 222.4)
(= (angle L4 xyaxes) 107.2)
(= (angle L4 ZAXES) 303.7)
(= (angle L5 xyaxes) 327.5)
(= (angle L5 ZAXES) 100.8)

(freeToMove L1) 
(freeToMove L2) 
(freeToMove L3) 
(freeToMove L4) 
(freeToMove L5) 

(connected L1 L2 )
(connected L2 L3 )
(connected L3 L4 )
(connected L4 L5 )


(affects L2 L3 )
(affects L2 L4 )
(affects L2 L5 )
(affects L3 L4 )
(affects L3 L5 )
(affects L4 L5 )
)

(:goal (and




(> (angle L3 xyaxes) 110.5)
(> (angle L3 ZAXES) 39.7)


(> (angle L5 xyaxes) 113.8)
(> (angle L5 ZAXES) 323.3)


) )
)
