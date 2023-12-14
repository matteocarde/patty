(define 
    (problem instance1)
    (:domain hvac)
    (:objects r1  -room k1  -request)
    (:init
        (= (time_requested r1 k1) 10)
        (= (temp_requested r1 k1) 20)


        
        (= (temp r1) 15)
        (= (air_flow r1) 0)
        (= (temp_sa r1) 10)



        (= (time) 0)
        (= (comfort) 2)


    )
    ;; the goal encodes the horizon of control. 
    (:goal 
        (and  (satisfied k1))
    )
)
