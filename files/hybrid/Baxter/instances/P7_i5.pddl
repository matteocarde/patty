(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 L6 L7 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 193.0)
(= (angle L1 ZAXES) 68.2)
(= (angle L2 xyaxes) 220.3)
(= (angle L2 ZAXES) 323.7)
(= (angle L3 xyaxes) 40.1)
(= (angle L3 ZAXES) 202.5)
(= (angle L4 xyaxes) 81.5)
(= (angle L4 ZAXES) 310.1)
(= (angle L5 xyaxes) 79.4)
(= (angle L5 ZAXES) 252.5)
(= (angle L6 xyaxes) 229.2)
(= (angle L6 ZAXES) 170.5)
(= (angle L7 xyaxes) 206.5)
(= (angle L7 ZAXES) 235.9)

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




(> (angle L3 xyaxes) 283.7)
(> (angle L3 ZAXES) 240.9)


(> (angle L5 xyaxes) 324.6)
(> (angle L5 ZAXES) 352.7)


(> (angle L7 xyaxes) 317.1)
(> (angle L7 ZAXES) 283.8)
(< (angle L2 xyaxes) 305.4)


) )
)
