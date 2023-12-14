(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 11.9)
(= (angle L1 ZAXES) 260.4)
(= (angle L2 xyaxes) 304.8)
(= (angle L2 ZAXES) 348.7)
(= (angle L3 xyaxes) 278.6)
(= (angle L3 ZAXES) 192.5)
(= (angle L4 xyaxes) 222.0)
(= (angle L4 ZAXES) 198.9)
(= (angle L5 xyaxes) 313.9)
(= (angle L5 ZAXES) 332.2)

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




(> (angle L3 xyaxes) 40.1)
(> (angle L3 ZAXES) 107.2)


(> (angle L5 xyaxes) 92.3)
(> (angle L5 ZAXES) 249.7)
(< (angle L4 xyaxes) 157.4)

) )
)
