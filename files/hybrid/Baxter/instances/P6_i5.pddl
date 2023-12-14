(define (problem example)
(:domain paco3d)
(:objects L1 L2 L3 L4 L5 L6 - link

xyaxes ZAXES - axis
)
(:init

(= (speed-i) 10)
(= (speed-d) 10)

(= (angle L1 xyaxes) 224.2)
(= (angle L1 ZAXES) 111.9)
(= (angle L2 xyaxes) 59.5)
(= (angle L2 ZAXES) 195.8)
(= (angle L3 xyaxes) 110.9)
(= (angle L3 ZAXES) 138.0)
(= (angle L4 xyaxes) 160.9)
(= (angle L4 ZAXES) 76.9)
(= (angle L5 xyaxes) 161.1)
(= (angle L5 ZAXES) 49.7)
(= (angle L6 xyaxes) 99.3)
(= (angle L6 ZAXES) 269.6)

(freeToMove L1) 
(freeToMove L2) 
(freeToMove L3) 
(freeToMove L4) 
(freeToMove L5) 
(freeToMove L6) 

(connected L1 L2 )
(connected L2 L3 )
(connected L3 L4 )
(connected L4 L5 )
(connected L5 L6 )


(affects L2 L3 )
(affects L2 L4 )
(affects L2 L5 )
(affects L2 L6 )
(affects L3 L4 )
(affects L3 L5 )
(affects L3 L6 )
(affects L4 L5 )
(affects L4 L6 )
(affects L5 L6 )
)

(:goal (and




(> (angle L3 xyaxes) 359.8)
(> (angle L3 ZAXES) 49.3)


(> (angle L5 xyaxes) 21.1)
(> (angle L5 ZAXES) 257.9)



) )
)
