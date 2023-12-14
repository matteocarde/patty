(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 67.1)
(= (angle L1 ZAXES) 27.3)
(= (angle L2 xyaxes) 17.8)
(= (angle L2 ZAXES) 160.5)
(= (angle L3 xyaxes) 101.6)
(= (angle L3 ZAXES) 43.0)
(= (angle L4 xyaxes) 271.9)
(= (angle L4 ZAXES) 123.9)

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




(> (angle L3 xyaxes) 5.8)
(> (angle L3 ZAXES) 177.5)


(< (angle L2 xyaxes) 286.5)

) )
)
