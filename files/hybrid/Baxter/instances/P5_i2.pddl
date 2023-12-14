(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 178.4)
(= (angle L1 ZAXES) 54.4)
(= (angle L2 xyaxes) 314.5)
(= (angle L2 ZAXES) 203.7)
(= (angle L3 xyaxes) 340.9)
(= (angle L3 ZAXES) 21.9)
(= (angle L4 xyaxes) 18.7)
(= (angle L4 ZAXES) 24.0)
(= (angle L5 xyaxes) 207.5)
(= (angle L5 ZAXES) 188.5)

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




(> (angle L3 xyaxes) 223.4)
(> (angle L3 ZAXES) 78.1)


(> (angle L5 xyaxes) 266.4)
(> (angle L5 ZAXES) 165.1)
(< (angle L5 xyaxes) 334.9)

) )
)
