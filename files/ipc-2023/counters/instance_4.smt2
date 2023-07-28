; benchmark generated from python API
(set-info :status unknown)
(declare-fun value_c0_0 () Real)
(declare-fun value_c1_0 () Real)
(declare-fun value_c2_0 () Real)
(declare-fun value_c3_0 () Real)
(declare-fun value_c3_1 () Real)
(declare-fun value_c2_1 () Real)
(declare-fun value_c1_1 () Real)
(declare-fun value_c0_1 () Real)
(declare-fun |(decrement c0)_0| () Bool)
(declare-fun |(decrement c1)_0| () Bool)
(declare-fun |(decrement c2)_0| () Bool)
(declare-fun |(decrement c3)_0| () Bool)
(declare-fun |(increment c0)_0| () Bool)
(declare-fun |(increment c1)_0| () Bool)
(declare-fun |(increment c2)_0| () Bool)
(declare-fun |(increment c3)_0| () Bool)
(assert
 (= value_c0_0 6.0))
(assert
 (= value_c1_0 4.0))
(assert
 (= value_c2_0 2.0))
(assert
 (= value_c3_0 0.0))
(assert
 (let (($x40 (and (<= (- (+ 1.0 value_c0_1) value_c1_1) 0.0) (<= (- (+ 1.0 value_c1_1) value_c2_1) 0.0) (<= (- (+ 1.0 value_c2_1) value_c3_1) 0.0))))
 (and and $x40)))
(assert
 (=> |(decrement c0)_0| (>= (- value_c0_0 1.0) 0.0)))
(assert
 (=> |(decrement c0)_0| (= value_c0_1 (- value_c0_0 1.0))))
(assert
 (=> |(decrement c1)_0| (>= (- value_c1_0 1.0) 0.0)))
(assert
 (=> |(decrement c1)_0| (= value_c1_1 (- value_c1_0 1.0))))
(assert
 (=> |(decrement c2)_0| (>= (- value_c2_0 1.0) 0.0)))
(assert
 (=> |(decrement c2)_0| (= value_c2_1 (- value_c2_0 1.0))))
(assert
 (=> |(decrement c3)_0| (>= (- value_c3_0 1.0) 0.0)))
(assert
 (=> |(decrement c3)_0| (= value_c3_1 (- value_c3_0 1.0))))
(assert
 (=> |(increment c0)_0| (<= (- (+ 1.0 value_c0_0) 8.0) 0.0)))
(assert
 (=> |(increment c0)_0| (= value_c0_1 (+ value_c0_0 1.0))))
(assert
 (=> |(increment c1)_0| (<= (- (+ 1.0 value_c1_0) 8.0) 0.0)))
(assert
 (=> |(increment c1)_0| (= value_c1_1 (+ value_c1_0 1.0))))
(assert
 (=> |(increment c2)_0| (<= (- (+ 1.0 value_c2_0) 8.0) 0.0)))
(assert
 (=> |(increment c2)_0| (= value_c2_1 (+ value_c2_0 1.0))))
(assert
 (=> |(increment c3)_0| (<= (- (+ 1.0 value_c3_0) 8.0) 0.0)))
(assert
 (=> |(increment c3)_0| (= value_c3_1 (+ value_c3_0 1.0))))
(assert
 (let (($x91 (= value_c1_1 value_c1_0)))
 (or $x91 (or |(decrement c1)_0| |(increment c1)_0|))))
(assert
 (let (($x94 (= value_c3_1 value_c3_0)))
 (or $x94 (or |(decrement c3)_0| |(increment c3)_0|))))
(assert
 (let (($x97 (= value_c2_1 value_c2_0)))
 (or $x97 (or |(decrement c2)_0| |(increment c2)_0|))))
(assert
 (let (($x100 (= value_c0_1 value_c0_0)))
 (or $x100 (or |(decrement c0)_0| |(increment c0)_0|))))
(assert
 (let (($x104 (not |(increment c0)_0|)))
 (let (($x103 (not |(decrement c0)_0|)))
 (or $x103 $x104))))
(assert
 (let (($x104 (not |(increment c0)_0|)))
 (let (($x103 (not |(decrement c0)_0|)))
 (or $x103 $x104))))
(assert
 (let (($x107 (not |(increment c1)_0|)))
 (let (($x106 (not |(decrement c1)_0|)))
 (or $x106 $x107))))
(assert
 (let (($x107 (not |(increment c1)_0|)))
 (let (($x106 (not |(decrement c1)_0|)))
 (or $x106 $x107))))
(assert
 (let (($x110 (not |(increment c2)_0|)))
 (let (($x109 (not |(decrement c2)_0|)))
 (or $x109 $x110))))
(assert
 (let (($x110 (not |(increment c2)_0|)))
 (let (($x109 (not |(decrement c2)_0|)))
 (or $x109 $x110))))
(assert
 (let (($x113 (not |(increment c3)_0|)))
 (let (($x112 (not |(decrement c3)_0|)))
 (or $x112 $x113))))
(assert
 (let (($x113 (not |(increment c3)_0|)))
 (let (($x112 (not |(decrement c3)_0|)))
 (or $x112 $x113))))
(assert
 (let (($x103 (not |(decrement c0)_0|)))
 (let (($x104 (not |(increment c0)_0|)))
 (or $x104 $x103))))
(assert
 (let (($x103 (not |(decrement c0)_0|)))
 (let (($x104 (not |(increment c0)_0|)))
 (or $x104 $x103))))
(assert
 (let (($x106 (not |(decrement c1)_0|)))
 (let (($x107 (not |(increment c1)_0|)))
 (or $x107 $x106))))
(assert
 (let (($x106 (not |(decrement c1)_0|)))
 (let (($x107 (not |(increment c1)_0|)))
 (or $x107 $x106))))
(assert
 (let (($x109 (not |(decrement c2)_0|)))
 (let (($x110 (not |(increment c2)_0|)))
 (or $x110 $x109))))
(assert
 (let (($x109 (not |(decrement c2)_0|)))
 (let (($x110 (not |(increment c2)_0|)))
 (or $x110 $x109))))
(assert
 (let (($x112 (not |(decrement c3)_0|)))
 (let (($x113 (not |(increment c3)_0|)))
 (or $x113 $x112))))
(assert
 (let (($x112 (not |(decrement c3)_0|)))
 (let (($x113 (not |(increment c3)_0|)))
 (or $x113 $x112))))
(check-sat)
