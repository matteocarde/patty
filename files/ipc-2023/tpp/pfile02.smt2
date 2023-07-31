; benchmark generated from python API
(set-info :status unknown)
(declare-fun loc_truck0_depot0_0 () Bool)
(declare-fun loc_truck0_depot0_1 () Bool)
(assert
 loc_truck0_depot0_0)
(assert
 (and and (and false false loc_truck0_depot0_1)))
(assert
 (=> (and (not loc_truck0_depot0_0) loc_truck0_depot0_1) or))
(assert
 (=> (and loc_truck0_depot0_0 (not loc_truck0_depot0_1)) or))
(check-sat)
