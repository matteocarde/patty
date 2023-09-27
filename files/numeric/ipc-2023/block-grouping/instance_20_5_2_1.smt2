; benchmark generated from python API
(set-info :status unknown)
(declare-fun x_b3_0 () Real)
(declare-fun y_b3_0 () Real)
(declare-fun x_b4_0 () Real)
(declare-fun y_b4_0 () Real)
(declare-fun x_b2_0 () Real)
(declare-fun y_b2_0 () Real)
(declare-fun x_b1_0 () Real)
(declare-fun y_b1_0 () Real)
(declare-fun x_b5_0 () Real)
(declare-fun y_b5_0 () Real)
(declare-fun y_b5_1 () Real)
(declare-fun y_b1_1 () Real)
(declare-fun y_b2_1 () Real)
(declare-fun y_b3_1 () Real)
(declare-fun y_b4_1 () Real)
(declare-fun x_b4_1 () Real)
(declare-fun x_b3_1 () Real)
(declare-fun x_b2_1 () Real)
(declare-fun x_b1_1 () Real)
(declare-fun x_b5_1 () Real)
(declare-fun |(move_block_up b1)_0| () Bool)
(declare-fun |(move_block_up b2)_0| () Bool)
(declare-fun |(move_block_up b3)_0| () Bool)
(declare-fun |(move_block_up b4)_0| () Bool)
(declare-fun |(move_block_up b5)_0| () Bool)
(declare-fun |(move_block_down b1)_0| () Bool)
(declare-fun |(move_block_down b2)_0| () Bool)
(declare-fun |(move_block_down b3)_0| () Bool)
(declare-fun |(move_block_down b4)_0| () Bool)
(declare-fun |(move_block_down b5)_0| () Bool)
(declare-fun |(move_block_right b1)_0| () Bool)
(declare-fun |(move_block_right b2)_0| () Bool)
(declare-fun |(move_block_right b3)_0| () Bool)
(declare-fun |(move_block_right b4)_0| () Bool)
(declare-fun |(move_block_right b5)_0| () Bool)
(declare-fun |(move_block_left b1)_0| () Bool)
(declare-fun |(move_block_left b2)_0| () Bool)
(declare-fun |(move_block_left b3)_0| () Bool)
(declare-fun |(move_block_left b4)_0| () Bool)
(declare-fun |(move_block_left b5)_0| () Bool)
(assert
 (= x_b3_0 17.0))
(assert
 (= y_b3_0 14.0))
(assert
 (= x_b4_0 17.0))
(assert
 (= y_b4_0 8.0))
(assert
 (= x_b2_0 19.0))
(assert
 (= y_b2_0 5.0))
(assert
 (= x_b1_0 20.0))
(assert
 (= y_b1_0 14.0))
(assert
 (= x_b5_0 5.0))
(assert
 (= y_b5_0 5.0))
(assert
 (let (($x95 (= (- y_b1_1 y_b5_1) 0.0)))
 (let (($x97 (= (- y_b2_1 y_b5_1) 0.0)))
 (let (($x99 (= (- y_b3_1 y_b5_1) 0.0)))
 (let (($x101 (= (- y_b4_1 y_b5_1) 0.0)))
 (let (($x85 (= (- y_b3_1 y_b4_1) 0.0)))
 (let (($x83 (= (- x_b3_1 x_b4_1) 0.0)))
 (let (($x81 (= (- y_b2_1 y_b4_1) 0.0)))
 (let (($x79 (= (- x_b2_1 x_b4_1) 0.0)))
 (let (($x77 (= (- y_b2_1 y_b3_1) 0.0)))
 (let (($x75 (= (- x_b2_1 x_b3_1) 0.0)))
 (let (($x73 (= (- y_b1_1 y_b4_1) 0.0)))
 (let (($x71 (= (- x_b1_1 x_b4_1) 0.0)))
 (let (($x69 (= (- y_b1_1 y_b3_1) 0.0)))
 (let (($x67 (= (- x_b1_1 x_b3_1) 0.0)))
 (let (($x65 (= (- y_b1_1 y_b2_1) 0.0)))
 (let (($x63 (= (- x_b1_1 x_b2_1) 0.0)))
 (let (($x93 (= (- x_b1_1 x_b5_1) 0.0)))
 (let (($x91 (= (- x_b2_1 x_b5_1) 0.0)))
 (let (($x89 (= (- x_b3_1 x_b5_1) 0.0)))
 (let (($x87 (= (- x_b4_1 x_b5_1) 0.0)))
 (let (($x103 (and $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x89 $x91 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x89 $x91 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x89 $x97 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x89 $x97 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x99 $x91 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x99 $x91 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x99 $x97 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x87 $x99 $x97 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x89 $x91 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x89 $x91 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x89 $x97 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x89 $x97 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x99 $x91 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x99 $x91 $x95 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x99 $x97 $x93 $x63 $x65 $x67 $x69 $x71 $x73 $x75 $x77 $x79 $x81 $x83 $x85 $x101 $x99 $x97 $x95)))
 (and and $x103)))))))))))))))))))))))
(assert
 (=> |(move_block_up b1)_0| (<= (- (+ 1.0 y_b1_0) 20.0) 0.0)))
(assert
 (=> |(move_block_up b1)_0| (= y_b1_1 (+ y_b1_0 1.0))))
(assert
 (=> |(move_block_up b2)_0| (<= (- (+ 1.0 y_b2_0) 20.0) 0.0)))
(assert
 (=> |(move_block_up b2)_0| (= y_b2_1 (+ y_b2_0 1.0))))
(assert
 (=> |(move_block_up b3)_0| (<= (- (+ 1.0 y_b3_0) 20.0) 0.0)))
(assert
 (=> |(move_block_up b3)_0| (= y_b3_1 (+ y_b3_0 1.0))))
(assert
 (=> |(move_block_up b4)_0| (<= (- (+ 1.0 y_b4_0) 20.0) 0.0)))
(assert
 (=> |(move_block_up b4)_0| (= y_b4_1 (+ y_b4_0 1.0))))
(assert
 (=> |(move_block_up b5)_0| (<= (- (+ 1.0 y_b5_0) 20.0) 0.0)))
(assert
 (=> |(move_block_up b5)_0| (= y_b5_1 (+ y_b5_0 1.0))))
(assert
 (=> |(move_block_down b1)_0| (>= (- (- y_b1_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_down b1)_0| (= y_b1_1 (- y_b1_0 1.0))))
(assert
 (=> |(move_block_down b2)_0| (>= (- (- y_b2_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_down b2)_0| (= y_b2_1 (- y_b2_0 1.0))))
(assert
 (=> |(move_block_down b3)_0| (>= (- (- y_b3_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_down b3)_0| (= y_b3_1 (- y_b3_0 1.0))))
(assert
 (=> |(move_block_down b4)_0| (>= (- (- y_b4_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_down b4)_0| (= y_b4_1 (- y_b4_0 1.0))))
(assert
 (=> |(move_block_down b5)_0| (>= (- (- y_b5_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_down b5)_0| (= y_b5_1 (- y_b5_0 1.0))))
(assert
 (=> |(move_block_right b1)_0| (<= (- (+ 1.0 x_b1_0) 20.0) 0.0)))
(assert
 (=> |(move_block_right b1)_0| (= x_b1_1 (+ x_b1_0 1.0))))
(assert
 (=> |(move_block_right b2)_0| (<= (- (+ 1.0 x_b2_0) 20.0) 0.0)))
(assert
 (=> |(move_block_right b2)_0| (= x_b2_1 (+ x_b2_0 1.0))))
(assert
 (=> |(move_block_right b3)_0| (<= (- (+ 1.0 x_b3_0) 20.0) 0.0)))
(assert
 (=> |(move_block_right b3)_0| (= x_b3_1 (+ x_b3_0 1.0))))
(assert
 (=> |(move_block_right b4)_0| (<= (- (+ 1.0 x_b4_0) 20.0) 0.0)))
(assert
 (=> |(move_block_right b4)_0| (= x_b4_1 (+ x_b4_0 1.0))))
(assert
 (=> |(move_block_right b5)_0| (<= (- (+ 1.0 x_b5_0) 20.0) 0.0)))
(assert
 (=> |(move_block_right b5)_0| (= x_b5_1 (+ x_b5_0 1.0))))
(assert
 (=> |(move_block_left b1)_0| (>= (- (- x_b1_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_left b1)_0| (= x_b1_1 (- x_b1_0 1.0))))
(assert
 (=> |(move_block_left b2)_0| (>= (- (- x_b2_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_left b2)_0| (= x_b2_1 (- x_b2_0 1.0))))
(assert
 (=> |(move_block_left b3)_0| (>= (- (- x_b3_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_left b3)_0| (= x_b3_1 (- x_b3_0 1.0))))
(assert
 (=> |(move_block_left b4)_0| (>= (- (- x_b4_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_left b4)_0| (= x_b4_1 (- x_b4_0 1.0))))
(assert
 (=> |(move_block_left b5)_0| (>= (- (- x_b5_0 1.0) 1.0) 0.0)))
(assert
 (=> |(move_block_left b5)_0| (= x_b5_1 (- x_b5_0 1.0))))
(assert
 (let (($x236 (= x_b1_1 x_b1_0)))
 (or $x236 (or |(move_block_right b1)_0| |(move_block_left b1)_0|))))
(assert
 (let (($x239 (= y_b5_1 y_b5_0)))
 (or $x239 (or |(move_block_up b5)_0| |(move_block_down b5)_0|))))
(assert
 (let (($x242 (= x_b4_1 x_b4_0)))
 (or $x242 (or |(move_block_right b4)_0| |(move_block_left b4)_0|))))
(assert
 (let (($x245 (= x_b2_1 x_b2_0)))
 (or $x245 (or |(move_block_right b2)_0| |(move_block_left b2)_0|))))
(assert
 (let (($x248 (= x_b5_1 x_b5_0)))
 (or $x248 (or |(move_block_right b5)_0| |(move_block_left b5)_0|))))
(assert
 (let (($x251 (= y_b3_1 y_b3_0)))
 (or $x251 (or |(move_block_up b3)_0| |(move_block_down b3)_0|))))
(assert
 (let (($x254 (= y_b4_1 y_b4_0)))
 (or $x254 (or |(move_block_up b4)_0| |(move_block_down b4)_0|))))
(assert
 (let (($x257 (= y_b2_1 y_b2_0)))
 (or $x257 (or |(move_block_up b2)_0| |(move_block_down b2)_0|))))
(assert
 (let (($x260 (= y_b1_1 y_b1_0)))
 (or $x260 (or |(move_block_up b1)_0| |(move_block_down b1)_0|))))
(assert
 (let (($x263 (= x_b3_1 x_b3_0)))
 (or $x263 (or |(move_block_right b3)_0| |(move_block_left b3)_0|))))
(assert
 (let (($x267 (not |(move_block_down b1)_0|)))
 (let (($x266 (not |(move_block_up b1)_0|)))
 (or $x266 $x267))))
(assert
 (let (($x267 (not |(move_block_down b1)_0|)))
 (let (($x266 (not |(move_block_up b1)_0|)))
 (or $x266 $x267))))
(assert
 (let (($x270 (not |(move_block_down b2)_0|)))
 (let (($x269 (not |(move_block_up b2)_0|)))
 (or $x269 $x270))))
(assert
 (let (($x270 (not |(move_block_down b2)_0|)))
 (let (($x269 (not |(move_block_up b2)_0|)))
 (or $x269 $x270))))
(assert
 (let (($x273 (not |(move_block_down b3)_0|)))
 (let (($x272 (not |(move_block_up b3)_0|)))
 (or $x272 $x273))))
(assert
 (let (($x273 (not |(move_block_down b3)_0|)))
 (let (($x272 (not |(move_block_up b3)_0|)))
 (or $x272 $x273))))
(assert
 (let (($x276 (not |(move_block_down b4)_0|)))
 (let (($x275 (not |(move_block_up b4)_0|)))
 (or $x275 $x276))))
(assert
 (let (($x276 (not |(move_block_down b4)_0|)))
 (let (($x275 (not |(move_block_up b4)_0|)))
 (or $x275 $x276))))
(assert
 (let (($x279 (not |(move_block_down b5)_0|)))
 (let (($x278 (not |(move_block_up b5)_0|)))
 (or $x278 $x279))))
(assert
 (let (($x279 (not |(move_block_down b5)_0|)))
 (let (($x278 (not |(move_block_up b5)_0|)))
 (or $x278 $x279))))
(assert
 (let (($x266 (not |(move_block_up b1)_0|)))
 (let (($x267 (not |(move_block_down b1)_0|)))
 (or $x267 $x266))))
(assert
 (let (($x266 (not |(move_block_up b1)_0|)))
 (let (($x267 (not |(move_block_down b1)_0|)))
 (or $x267 $x266))))
(assert
 (let (($x269 (not |(move_block_up b2)_0|)))
 (let (($x270 (not |(move_block_down b2)_0|)))
 (or $x270 $x269))))
(assert
 (let (($x269 (not |(move_block_up b2)_0|)))
 (let (($x270 (not |(move_block_down b2)_0|)))
 (or $x270 $x269))))
(assert
 (let (($x272 (not |(move_block_up b3)_0|)))
 (let (($x273 (not |(move_block_down b3)_0|)))
 (or $x273 $x272))))
(assert
 (let (($x272 (not |(move_block_up b3)_0|)))
 (let (($x273 (not |(move_block_down b3)_0|)))
 (or $x273 $x272))))
(assert
 (let (($x275 (not |(move_block_up b4)_0|)))
 (let (($x276 (not |(move_block_down b4)_0|)))
 (or $x276 $x275))))
(assert
 (let (($x275 (not |(move_block_up b4)_0|)))
 (let (($x276 (not |(move_block_down b4)_0|)))
 (or $x276 $x275))))
(assert
 (let (($x278 (not |(move_block_up b5)_0|)))
 (let (($x279 (not |(move_block_down b5)_0|)))
 (or $x279 $x278))))
(assert
 (let (($x278 (not |(move_block_up b5)_0|)))
 (let (($x279 (not |(move_block_down b5)_0|)))
 (or $x279 $x278))))
(assert
 (let (($x287 (not |(move_block_left b1)_0|)))
 (let (($x286 (not |(move_block_right b1)_0|)))
 (or $x286 $x287))))
(assert
 (let (($x287 (not |(move_block_left b1)_0|)))
 (let (($x286 (not |(move_block_right b1)_0|)))
 (or $x286 $x287))))
(assert
 (let (($x290 (not |(move_block_left b2)_0|)))
 (let (($x289 (not |(move_block_right b2)_0|)))
 (or $x289 $x290))))
(assert
 (let (($x290 (not |(move_block_left b2)_0|)))
 (let (($x289 (not |(move_block_right b2)_0|)))
 (or $x289 $x290))))
(assert
 (let (($x293 (not |(move_block_left b3)_0|)))
 (let (($x292 (not |(move_block_right b3)_0|)))
 (or $x292 $x293))))
(assert
 (let (($x293 (not |(move_block_left b3)_0|)))
 (let (($x292 (not |(move_block_right b3)_0|)))
 (or $x292 $x293))))
(assert
 (let (($x296 (not |(move_block_left b4)_0|)))
 (let (($x295 (not |(move_block_right b4)_0|)))
 (or $x295 $x296))))
(assert
 (let (($x296 (not |(move_block_left b4)_0|)))
 (let (($x295 (not |(move_block_right b4)_0|)))
 (or $x295 $x296))))
(assert
 (let (($x299 (not |(move_block_left b5)_0|)))
 (let (($x298 (not |(move_block_right b5)_0|)))
 (or $x298 $x299))))
(assert
 (let (($x299 (not |(move_block_left b5)_0|)))
 (let (($x298 (not |(move_block_right b5)_0|)))
 (or $x298 $x299))))
(assert
 (let (($x286 (not |(move_block_right b1)_0|)))
 (let (($x287 (not |(move_block_left b1)_0|)))
 (or $x287 $x286))))
(assert
 (let (($x286 (not |(move_block_right b1)_0|)))
 (let (($x287 (not |(move_block_left b1)_0|)))
 (or $x287 $x286))))
(assert
 (let (($x289 (not |(move_block_right b2)_0|)))
 (let (($x290 (not |(move_block_left b2)_0|)))
 (or $x290 $x289))))
(assert
 (let (($x289 (not |(move_block_right b2)_0|)))
 (let (($x290 (not |(move_block_left b2)_0|)))
 (or $x290 $x289))))
(assert
 (let (($x292 (not |(move_block_right b3)_0|)))
 (let (($x293 (not |(move_block_left b3)_0|)))
 (or $x293 $x292))))
(assert
 (let (($x292 (not |(move_block_right b3)_0|)))
 (let (($x293 (not |(move_block_left b3)_0|)))
 (or $x293 $x292))))
(assert
 (let (($x295 (not |(move_block_right b4)_0|)))
 (let (($x296 (not |(move_block_left b4)_0|)))
 (or $x296 $x295))))
(assert
 (let (($x295 (not |(move_block_right b4)_0|)))
 (let (($x296 (not |(move_block_left b4)_0|)))
 (or $x296 $x295))))
(assert
 (let (($x298 (not |(move_block_right b5)_0|)))
 (let (($x299 (not |(move_block_left b5)_0|)))
 (or $x299 $x298))))
(assert
 (let (($x298 (not |(move_block_right b5)_0|)))
 (let (($x299 (not |(move_block_left b5)_0|)))
 (or $x299 $x298))))
(check-sat)
(get-info :all-statistics)
