
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocEQleftADDESUBleftMULDIVFDIVleftLPARENrightNEGPOSrightPOWADD ADDE AS AXE BBQ BUILD CHICKEN COMPARE CONST DIV DOT EQ FDIV FLOAT FOX FR HATCH ID IFF IFT INT LBRACE LBRACK LOOPF LOOPT LPAREN MUL NEWLINE PECK PICK POW PUSH RBRACE RBRACK REPF REPT ROOSTER RPAREN STR SUB TOP \texpressions : expressions NEWLINE block\n                       | expressions NEWLINE stmt\n                       | block\n                       | stmt\n        enter : BUILD FUNC LBRACEenter : LOOPT LBRACEenter : LOOPF LBRACEenter : REPT LBRACEenter : REPF LBRACEenter : IFT LBRACEenter : IFF LBRACEblock : enter NEWLINE expressions NEWLINE RBRACEstmt : AXE\n                | CHICKEN\n                | ADD\n                | FOX\n                | ROOSTER\n                | COMPARE\n                | PICK\n                | PECK\n                | FR\n                | BBQ\n        stmt : PICK INTstmt : PECK INTstmt : HATCH FUNCstmt : PUSH STR\n                | PUSH mathexpr\n        stmt : IDSTR AS IDSTRstmt : ID LBRACK INT RBRACK EQ VAL\n                | ID EQ VAL\n        stmt : ID LBRACK INT RBRACK\n                | ID\n        stmt : CONST ID EQ VALstmt : mathexpr : mathexpr MUL mathexprmathexpr : mathexpr LPAREN mathexpr RPARENmathexpr : mathexpr DIV mathexprmathexpr : mathexpr FDIV mathexprmathexpr : mathexpr ADDE mathexprmathexpr : mathexpr SUB mathexprmathexpr : mathexpr POW mathexprmathexpr : LPAREN mathexpr RPARENmathexpr : SUB mathexpr %prec NEGmathexpr : ADDE mathexpr %prec POSmathexpr : INT\n                    | FLOAT\n        mathexpr : IDFUNC : ID DOT FUNC\n                | ID\n        VAL : STR\n               | TOP\n               | mathexpr\n        IDSTR : ID\n                 | STR\n        '
    
_lr_action_items = {'AXE':([0,28,29,76,],[5,5,5,5,]),'CHICKEN':([0,28,29,76,],[6,6,6,6,]),'ADD':([0,28,29,76,],[7,7,7,7,]),'FOX':([0,28,29,76,],[8,8,8,8,]),'ROOSTER':([0,28,29,76,],[9,9,9,9,]),'COMPARE':([0,28,29,76,],[10,10,10,10,]),'PICK':([0,28,29,76,],[11,11,11,11,]),'PECK':([0,28,29,76,],[12,12,12,12,]),'FR':([0,28,29,76,],[13,13,13,13,]),'BBQ':([0,28,29,76,],[14,14,14,14,]),'HATCH':([0,28,29,76,],[15,15,15,15,]),'PUSH':([0,28,29,76,],[16,16,16,16,]),'ID':([0,15,16,20,21,28,29,36,37,38,42,44,56,57,58,59,60,61,62,63,74,76,90,],[19,33,41,45,33,19,19,41,41,41,68,41,33,41,41,41,41,41,41,41,41,19,41,]),'CONST':([0,28,29,76,],[20,20,20,20,]),'NEWLINE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,19,28,29,30,31,32,33,34,35,39,40,41,47,48,49,50,51,52,53,54,55,65,66,67,68,70,71,72,73,75,76,77,78,80,81,82,83,84,85,86,87,88,89,91,],[-34,28,-3,-4,29,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-54,-32,-34,-34,-23,-24,-25,-49,-26,-27,-45,-46,-47,-6,-7,-8,-9,-10,-11,-1,-2,76,-44,-43,-28,-53,-30,-50,-51,-52,-5,-34,-48,-35,-37,-38,-39,-40,-41,-42,-31,-33,-12,-36,-29,]),'$end':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,17,19,28,30,31,32,33,34,35,39,40,41,53,54,65,66,67,68,70,71,72,73,77,78,80,81,82,83,84,85,86,87,88,89,91,],[-34,0,-3,-4,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-54,-32,-34,-23,-24,-25,-49,-26,-27,-45,-46,-47,-1,-2,-44,-43,-28,-53,-30,-50,-51,-52,-48,-35,-37,-38,-39,-40,-41,-42,-31,-33,-12,-36,-29,]),'BUILD':([0,28,29,76,],[21,21,21,21,]),'LOOPT':([0,28,29,76,],[22,22,22,22,]),'LOOPF':([0,28,29,76,],[23,23,23,23,]),'REPT':([0,28,29,76,],[24,24,24,24,]),'REPF':([0,28,29,76,],[25,25,25,25,]),'IFT':([0,28,29,76,],[26,26,26,26,]),'IFF':([0,28,29,76,],[27,27,27,27,]),'STR':([0,16,28,29,42,44,74,76,90,],[17,34,17,17,17,71,71,17,71,]),'INT':([11,12,16,36,37,38,43,44,57,58,59,60,61,62,63,74,90,],[30,31,39,39,39,39,69,39,39,39,39,39,39,39,39,39,39,]),'LPAREN':([16,35,36,37,38,39,40,41,44,57,58,59,60,61,62,63,64,65,66,73,74,78,79,80,81,82,83,84,85,89,90,],[36,58,36,36,36,-45,-46,-47,36,36,36,36,36,36,36,36,58,-44,-43,58,36,58,58,58,58,58,58,-41,-42,-36,36,]),'SUB':([16,35,36,37,38,39,40,41,44,57,58,59,60,61,62,63,64,65,66,73,74,78,79,80,81,82,83,84,85,89,90,],[38,62,38,38,38,-45,-46,-47,38,38,38,38,38,38,38,38,62,-44,-43,62,38,-35,62,-37,-38,-39,-40,-41,-42,-36,38,]),'ADDE':([16,35,36,37,38,39,40,41,44,57,58,59,60,61,62,63,64,65,66,73,74,78,79,80,81,82,83,84,85,89,90,],[37,61,37,37,37,-45,-46,-47,37,37,37,37,37,37,37,37,61,-44,-43,61,37,-35,61,-37,-38,-39,-40,-41,-42,-36,37,]),'FLOAT':([16,36,37,38,44,57,58,59,60,61,62,63,74,90,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'AS':([17,18,19,],[-54,42,-53,]),'LBRACK':([19,],[43,]),'EQ':([19,45,86,],[44,74,90,]),'LBRACE':([22,23,24,25,26,27,33,46,77,],[47,48,49,50,51,52,-49,75,-48,]),'DOT':([33,],[56,]),'MUL':([35,39,40,41,64,65,66,73,78,79,80,81,82,83,84,85,89,],[57,-45,-46,-47,57,-44,-43,57,-35,57,-37,-38,57,57,-41,-42,-36,]),'DIV':([35,39,40,41,64,65,66,73,78,79,80,81,82,83,84,85,89,],[59,-45,-46,-47,59,-44,-43,59,-35,59,-37,-38,59,59,-41,-42,-36,]),'FDIV':([35,39,40,41,64,65,66,73,78,79,80,81,82,83,84,85,89,],[60,-45,-46,-47,60,-44,-43,60,-35,60,-37,-38,60,60,-41,-42,-36,]),'POW':([35,39,40,41,64,65,66,73,78,79,80,81,82,83,84,85,89,],[63,-45,-46,-47,63,63,63,63,63,63,63,63,63,63,63,-42,-36,]),'RPAREN':([39,40,41,64,65,66,78,79,80,81,82,83,84,85,89,],[-45,-46,-47,85,-44,-43,-35,89,-37,-38,-39,-40,-41,-42,-36,]),'TOP':([44,74,90,],[72,72,72,]),'RBRACK':([69,],[86,]),'RBRACE':([76,],[88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,29,],[1,55,]),'block':([0,28,29,76,],[2,53,2,53,]),'stmt':([0,28,29,76,],[3,54,3,54,]),'enter':([0,28,29,76,],[4,4,4,4,]),'IDSTR':([0,28,29,42,76,],[18,18,18,67,18,]),'FUNC':([15,21,56,],[32,46,77,]),'mathexpr':([16,36,37,38,44,57,58,59,60,61,62,63,74,90,],[35,64,65,66,73,78,79,80,81,82,83,84,73,73,]),'VAL':([44,74,90,],[70,87,91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expressions NEWLINE block','expressions',3,'p_program','main.py',262),
  ('expressions -> expressions NEWLINE stmt','expressions',3,'p_program','main.py',263),
  ('expressions -> block','expressions',1,'p_program','main.py',264),
  ('expressions -> stmt','expressions',1,'p_program','main.py',265),
  ('enter -> BUILD FUNC LBRACE','enter',3,'p_enter_block_build','main.py',273),
  ('enter -> LOOPT LBRACE','enter',2,'p_enter_block_loopt','main.py',277),
  ('enter -> LOOPF LBRACE','enter',2,'p_enter_block_loopf','main.py',281),
  ('enter -> REPT LBRACE','enter',2,'p_enter_block_rept','main.py',285),
  ('enter -> REPF LBRACE','enter',2,'p_enter_block_repf','main.py',289),
  ('enter -> IFT LBRACE','enter',2,'p_enter_block_ift','main.py',293),
  ('enter -> IFF LBRACE','enter',2,'p_enter_block_iff','main.py',297),
  ('block -> enter NEWLINE expressions NEWLINE RBRACE','block',5,'p_block','main.py',301),
  ('stmt -> AXE','stmt',1,'p_stmt_keyword','main.py',305),
  ('stmt -> CHICKEN','stmt',1,'p_stmt_keyword','main.py',306),
  ('stmt -> ADD','stmt',1,'p_stmt_keyword','main.py',307),
  ('stmt -> FOX','stmt',1,'p_stmt_keyword','main.py',308),
  ('stmt -> ROOSTER','stmt',1,'p_stmt_keyword','main.py',309),
  ('stmt -> COMPARE','stmt',1,'p_stmt_keyword','main.py',310),
  ('stmt -> PICK','stmt',1,'p_stmt_keyword','main.py',311),
  ('stmt -> PECK','stmt',1,'p_stmt_keyword','main.py',312),
  ('stmt -> FR','stmt',1,'p_stmt_keyword','main.py',313),
  ('stmt -> BBQ','stmt',1,'p_stmt_keyword','main.py',314),
  ('stmt -> PICK INT','stmt',2,'p_stmt_pick','main.py',319),
  ('stmt -> PECK INT','stmt',2,'p_stmt_peck','main.py',323),
  ('stmt -> HATCH FUNC','stmt',2,'p_stmt_HATCH','main.py',327),
  ('stmt -> PUSH STR','stmt',2,'p_stmt_PUSH','main.py',331),
  ('stmt -> PUSH mathexpr','stmt',2,'p_stmt_PUSH','main.py',332),
  ('stmt -> IDSTR AS IDSTR','stmt',3,'p_stmt_AS','main.py',337),
  ('stmt -> ID LBRACK INT RBRACK EQ VAL','stmt',6,'p_stmt_SETVAR','main.py',341),
  ('stmt -> ID EQ VAL','stmt',3,'p_stmt_SETVAR','main.py',342),
  ('stmt -> ID LBRACK INT RBRACK','stmt',4,'p_stmt_GETVAR','main.py',350),
  ('stmt -> ID','stmt',1,'p_stmt_GETVAR','main.py',351),
  ('stmt -> CONST ID EQ VAL','stmt',4,'p_stmt_SETCONST','main.py',359),
  ('stmt -> <empty>','stmt',0,'p_stmt_BLANKLINE','main.py',363),
  ('mathexpr -> mathexpr MUL mathexpr','mathexpr',3,'p_expr_MUL','main.py',366),
  ('mathexpr -> mathexpr LPAREN mathexpr RPAREN','mathexpr',4,'p_expr_IMPMUL','main.py',370),
  ('mathexpr -> mathexpr DIV mathexpr','mathexpr',3,'p_expr_DIV','main.py',374),
  ('mathexpr -> mathexpr FDIV mathexpr','mathexpr',3,'p_expr_FDIV','main.py',378),
  ('mathexpr -> mathexpr ADDE mathexpr','mathexpr',3,'p_expr_ADDE','main.py',382),
  ('mathexpr -> mathexpr SUB mathexpr','mathexpr',3,'p_expr_SUB','main.py',386),
  ('mathexpr -> mathexpr POW mathexpr','mathexpr',3,'p_expr_POW','main.py',390),
  ('mathexpr -> LPAREN mathexpr RPAREN','mathexpr',3,'p_expr_PARENMATH','main.py',394),
  ('mathexpr -> SUB mathexpr','mathexpr',2,'p_expr_NEG','main.py',398),
  ('mathexpr -> ADDE mathexpr','mathexpr',2,'p_expr_POS','main.py',402),
  ('mathexpr -> INT','mathexpr',1,'p_expr_MATH','main.py',406),
  ('mathexpr -> FLOAT','mathexpr',1,'p_expr_MATH','main.py',407),
  ('mathexpr -> ID','mathexpr',1,'p_expr_MATHVAR','main.py',412),
  ('FUNC -> ID DOT FUNC','FUNC',3,'p_FUNCTION','main.py',417),
  ('FUNC -> ID','FUNC',1,'p_FUNCTION','main.py',418),
  ('VAL -> STR','VAL',1,'p_VAL','main.py',423),
  ('VAL -> TOP','VAL',1,'p_VAL','main.py',424),
  ('VAL -> mathexpr','VAL',1,'p_VAL','main.py',425),
  ('IDSTR -> ID','IDSTR',1,'p_IDSTR','main.py',430),
  ('IDSTR -> STR','IDSTR',1,'p_IDSTR','main.py',431),
]
