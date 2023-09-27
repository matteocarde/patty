(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 L6 L7 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 45.9)
(= (angle L1 ZAXES) 220.3)
(= (angle L2 xyaxes) 267.9)
(= (angle L2 ZAXES) 281.6)
(= (angle L3 xyaxes) 32.5)
(= (angle L3 ZAXES) 59.4)
(= (angle L4 xyaxes) 229.6)
(= (angle L4 ZAXES) 308.8)
(= (angle L5 xyaxes) 174.4)
(= (angle L5 ZAXES) 357.9)
(= (angle L6 xyaxes) 155.9)
(= (angle L6 ZAXES) 287.6)
(= (angle L7 xyaxes) 48.1)
(= (angle L7 ZAXES) 116.3)

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




(> (angle L3 xyaxes) 174.1)
(> (angle L3 ZAXES) 114.1)


(> (angle L5 xyaxes) 29.0)
(> (angle L5 ZAXES) 79.1)


(> (angle L7 xyaxes) 346.4)
(> (angle L7 ZAXES) 310.3)
(< (angle L2 xyaxes) 348.0)


) )
)
