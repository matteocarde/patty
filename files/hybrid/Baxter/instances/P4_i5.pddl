(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 135.7)
(= (angle L1 ZAXES) 243.5)
(= (angle L2 xyaxes) 216.6)
(= (angle L2 ZAXES) 338.0)
(= (angle L3 xyaxes) 143.6)
(= (angle L3 ZAXES) 205.9)
(= (angle L4 xyaxes) 350.4)
(= (angle L4 ZAXES) 153.6)

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




(> (angle L3 xyaxes) 239.3)
(> (angle L3 ZAXES) 66.8)


(< (angle L4 xyaxes) 148.7)

) )
)
