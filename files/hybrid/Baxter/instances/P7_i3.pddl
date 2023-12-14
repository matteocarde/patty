(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 L6 L7 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 0.8)
(= (angle L1 ZAXES) 337.2)
(= (angle L2 xyaxes) 222.8)
(= (angle L2 ZAXES) 7.1)
(= (angle L3 xyaxes) 62.2)
(= (angle L3 ZAXES) 81.1)
(= (angle L4 xyaxes) 224.7)
(= (angle L4 ZAXES) 234.9)
(= (angle L5 xyaxes) 75.6)
(= (angle L5 ZAXES) 77.7)
(= (angle L6 xyaxes) 151.3)
(= (angle L6 ZAXES) 16.6)
(= (angle L7 xyaxes) 148.3)
(= (angle L7 ZAXES) 66.1)

(freeToMove L1) 
(freeToMove L2) 
(freeToMove L3) 
(freeToMove L4) 
(freeToMove L5) 
(freeToMove L6) 
(freeToMove L7) 

(connected L1 L2 )
(connected L2 L3 )
(connected L3 L4 )
(connected L4 L5 )
(connected L5 L6 )
(connected L6 L7 )


(affects L2 L3 )
(affects L2 L4 )
(affects L2 L5 )
(affects L2 L6 )
(affects L2 L7 )
(affects L3 L4 )
(affects L3 L5 )
(affects L3 L6 )
(affects L3 L7 )
(affects L4 L5 )
(affects L4 L6 )
(affects L4 L7 )
(affects L5 L6 )
(affects L5 L7 )
(affects L6 L7 )
)

(:goal (and




(> (angle L3 xyaxes) 223.7)
(> (angle L3 ZAXES) 178.4)


(> (angle L5 xyaxes) 156.5)
(> (angle L5 ZAXES) 62.3)


(> (angle L7 xyaxes) 25.4)
(> (angle L7 ZAXES) 23.0)
(< (angle L4 xyaxes) 324.5)

) )
)
