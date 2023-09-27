; benchmark generated from python API
(set-info :status unknown)
(declare-fun x_farm0_0 () Real)
(declare-fun x_farm1_0 () Real)
(declare-fun cost_0 () Real)
(declare-fun x_farm0_1 () Real)
(declare-fun x_farm1_1 () Real)
(declare-fun |(move-fast farm0 farm1)_0| () Bool)
(declare-fun cost_1 () Real)
(declare-fun |(move-fast farm1 farm0)_0| () Bool)
(declare-fun |(move-slow farm0 farm1)_0| () Bool)
(declare-fun |(move-slow farm1 farm0)_0| () Bool)
(assert
 (= x_farm0_0 700.0))
(assert
 (= x_farm1_0 1.0))
(assert
 (= cost_0 0.0))
(assert
 (let (($x32 (and (>= (- x_farm0_1 1.0) 0.0) (>= (- x_farm1_1 1.0) 0.0) (>= (- (+ (* x_farm1_1 (/ 17.0 10.0)) x_farm0_1) 980.0) 0.0))))
 (and and $x32)))
(assert
 (=> |(move-fast farm0 farm1)_0| (>= (- x_farm0_0 4.0) 0.0)))
(assert
 (=> |(move-fast farm0 farm1)_0| (= x_farm0_1 (- x_farm0_0 4.0))))
(assert
 (=> |(move-fast farm0 farm1)_0| (= x_farm1_1 (+ x_farm1_0 2.0))))
(assert
 (let (($x45 (= cost_1 (+ cost_0 1.0))))
 (=> |(move-fast farm0 farm1)_0| $x45)))
(assert
 (=> |(move-fast farm1 farm0)_0| (>= (- x_farm1_0 4.0) 0.0)))
(assert
 (=> |(move-fast farm1 farm0)_0| (= x_farm1_1 (- x_farm1_0 4.0))))
(assert
 (=> |(move-fast farm1 farm0)_0| (= x_farm0_1 (+ x_farm0_0 2.0))))
(assert
 (let (($x45 (= cost_1 (+ cost_0 1.0))))
 (=> |(move-fast farm1 farm0)_0| $x45)))
(assert
 (=> |(move-slow farm0 farm1)_0| (>= (- x_farm0_0 1.0) 0.0)))
(assert
 (=> |(move-slow farm0 farm1)_0| (= x_farm0_1 (- x_farm0_0 1.0))))
(assert
 (=> |(move-slow farm0 farm1)_0| (= x_farm1_1 (+ x_farm1_0 1.0))))
(assert
 (=> |(move-slow farm1 farm0)_0| (>= (- x_farm1_0 1.0) 0.0)))
(assert
 (=> |(move-slow farm1 farm0)_0| (= x_farm1_1 (- x_farm1_0 1.0))))
(assert
 (=> |(move-slow farm1 farm0)_0| (= x_farm0_1 (+ x_farm0_0 1.0))))
(assert
 (let (($x73 (or |(move-fast farm0 farm1)_0| |(move-fast farm1 farm0)_0| |(move-slow farm0 farm1)_0| |(move-slow farm1 farm0)_0|)))
 (let (($x72 (= x_farm0_1 x_farm0_0)))
 (or $x72 $x73))))
(assert
 (let (($x75 (= cost_1 cost_0)))
 (or $x75 (or |(move-fast farm0 farm1)_0| |(move-fast farm1 farm0)_0|))))
(assert
 (let (($x73 (or |(move-fast farm0 farm1)_0| |(move-fast farm1 farm0)_0| |(move-slow farm0 farm1)_0| |(move-slow farm1 farm0)_0|)))
 (let (($x78 (= x_farm1_1 x_farm1_0)))
 (or $x78 $x73))))
(assert
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (or $x80 $x81))))
(assert
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (or $x80 $x81))))
(assert
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (or $x80 $x83))))
(assert
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (or $x80 $x83))))
(assert
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (or $x80 $x85))))
(assert
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (or $x80 $x85))))
(assert
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (or $x81 $x80))))
(assert
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (or $x81 $x80))))
(assert
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (or $x81 $x83))))
(assert
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (or $x81 $x83))))
(assert
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (or $x81 $x85))))
(assert
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (or $x81 $x85))))
(assert
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (or $x83 $x80))))
(assert
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (or $x83 $x80))))
(assert
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (or $x83 $x81))))
(assert
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (or $x83 $x81))))
(assert
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (or $x83 $x85))))
(assert
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (or $x83 $x85))))
(assert
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (or $x85 $x80))))
(assert
 (let (($x80 (not |(move-fast farm0 farm1)_0|)))
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (or $x85 $x80))))
(assert
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (or $x85 $x81))))
(assert
 (let (($x81 (not |(move-fast farm1 farm0)_0|)))
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (or $x85 $x81))))
(assert
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (or $x85 $x83))))
(assert
 (let (($x83 (not |(move-slow farm0 farm1)_0|)))
 (let (($x85 (not |(move-slow farm1 farm0)_0|)))
 (or $x85 $x83))))
(check-sat)
