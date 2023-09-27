(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 L6 L7 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 171.2)
(= (angle L1 ZAXES) 188.5)
(= (angle L2 xyaxes) 282.6)
(= (angle L2 ZAXES) 130.0)
(= (angle L3 xyaxes) 224.2)
(= (angle L3 ZAXES) 18.3)
(= (angle L4 xyaxes) 201.2)
(= (angle L4 ZAXES) 14.4)
(= (angle L5 xyaxes) 211.4)
(= (angle L5 ZAXES) 302.5)
(= (angle L6 xyaxes) 71.0)
(= (angle L6 ZAXES) 278.0)
(= (angle L7 xyaxes) 234.6)
(= (angle L7 ZAXES) 183.5)

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




(> (angle L3 xyaxes) 27.3)
(> (angle L3 ZAXES) 106.9)


(> (angle L5 xyaxes) 275.6)
(> (angle L5 ZAXES) 351.4)


(> (angle L7 xyaxes) 255.9)
(> (angle L7 ZAXES) 168.4)
(< (angle L2 xyaxes) 294.1)


) )
)
