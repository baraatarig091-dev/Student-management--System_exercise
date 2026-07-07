# --GPA Calculator --
student_gba =3.8
bonus =student_gba * 10
final_score = student_gba+(bonus/100)
passed  =final_score>3.0

print(f"GPA  :{student_gba} ")
print(f"bonus(x10) :{bonus}")
print(f"final_score:{final_score:.2f} ")
print(f"passed :{passed}")
