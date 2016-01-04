.PS
cct_init

M1: c_fet( up_ dimen_, , N); rlabel(-, "$V_{DS}$", +);
line from M1.G to (M1.G, M1.D) then to M1.D; dot;
move up dimen_/1.5; arrowline(down dimen_/1.5); rlabel(, "$I_D$")
move to M1.G then left dimen_/5; "+"
move down dimen_/3 then right dimen_/3; "$V_{GS}$"
.PE