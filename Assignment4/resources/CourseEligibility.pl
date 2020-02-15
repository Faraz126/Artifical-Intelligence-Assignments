enrolled(a,c1).
enrolled(a,c2).
enrolled(b,c1).
enrolled(d,c2).
enrolled(c,c1).
enrolled(c,c2).
shortAttendance(a,c1).
shortAttendance(a,c2).
shortAttendance(c,c2).
dropped(b,c1).
feeNotPaid(a).
ineligible(S,C):-enrolled(S,C),(shortAttendance(S,C);dropped(S,C);feeNotPaid(S)).
underWarning(S):- findall(C1,shortAttendance(S,C1),SHORTS),findall(C2,enrolled(S,C2),ENROLLEDCOURSES),subset(ENROLLEDCOURSES,SHORTS).

