(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 L6 L7 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 74.9)
(= (angle L1 ZAXES) 93.3)
(= (angle L2 xyaxes) 184.5)
(= (angle L2 ZAXES) 122.6)
(= (angle L3 xyaxes) 233.7)
(= (angle L3 ZAXES) 200.7)
(= (angle L4 xyaxes) 48.7)
(= (angle L4 ZAXES) 92.4)
(= (angle L5 xyaxes) 124.5)
(= (angle L5 ZAXES) 57.8)
(= (angle L6 xyaxes) 184.8)
(= (angle L6 ZAXES) 156.2)
(= (angle L7 xyaxes) 244.8)
(= (angle L7 ZAXES) 91.4)

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




(> (angle L3 xyaxes) 101.6)
(> (angle L3 ZAXES) 308.1)


(> (angle L5 xyaxes) 223.5)
(> (angle L5 ZAXES) 57.5)


(> (angle L7 xyaxes) 319.8)
(> (angle L7 ZAXES) 148.9)

(< (angle L6 xyaxes) 281.9)

) )
)
