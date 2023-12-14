(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 331.3)
(= (angle L1 ZAXES) 259.0)
(= (angle L2 xyaxes) 296.4)
(= (angle L2 ZAXES) 32.7)
(= (angle L3 xyaxes) 304.8)
(= (angle L3 ZAXES) 320.5)
(= (angle L4 xyaxes) 332.6)
(= (angle L4 ZAXES) 164.6)
(= (angle L5 xyaxes) 102.2)
(= (angle L5 ZAXES) 131.7)

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




(> (angle L3 xyaxes) 338.4)
(> (angle L3 ZAXES) 304.2)


(> (angle L5 xyaxes) 15.3)
(> (angle L5 ZAXES) 248.7)
(< (angle L5 xyaxes) 346.8)

) )
)
