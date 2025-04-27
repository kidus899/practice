print("Mid exam results")
eng_mid = eval(input("Enter your english exam result:"))
amh_mid = eval(input("Enter your amharic exam result:"))
maths_mid = eval(input("Enter your maths exam result:"))
geo_mid = eval(input("Enter your geography exam result:"))
chem_mid = eval(input("Enter your chemistry exam result:"))
bio_mid = eval(input("Enter your biology exam result:"))
his_mid = eval(input("Enter your history exam result:"))
eco_mid = eval(input("Enter your economics exam result:"))
phy_mid = eval(input("Enter your physics exam result:"))
ao_mid = eval(input("Enter your AO exam result:"))
hpe_mid = eval(input("Enter your HPE exam result:"))
it_mid = eval(input("Enter your IT exam result:"))
ce_mid = eval(input("Enter your CE exam result:"))

print("Final exam result")
eng_fin = eval(input("Enter your english exam result:"))
amh_fin = eval(input("Enter your amharic exam result:"))
maths_fin = eval(input("Enter your maths exam result:"))
geo_fin = eval(input("Enter your geography exam result:"))
chem_fin = eval(input("Enter your chemistry exam result:"))
bio_fin = eval(input("Enter your biology exam result:"))
his_fin = eval(input("Enter your history exam result:"))
eco_fin = eval(input("Enter your economics exam result:"))
phy_fin = eval(input("Enter your physics exam result:"))
ao_fin = eval(input("Enter your AO exam result:"))
hpe_fin = eval(input("Enter your HPE exam result:"))
it_fin = eval(input("Enter your IT exam result:"))
ce_fin = eval(input("Enter your CE exam result:"))

# Checking inputs
def check():
    mid_scores = [eng_mid, amh_mid, maths_mid, geo_mid, chem_mid, bio_mid, his_mid, eco_mid, phy_mid, ao_mid, hpe_mid, it_mid, ce_mid]
    fin_scores = [eng_fin, amh_fin, maths_fin, geo_fin, chem_fin, bio_fin, his_fin, eco_fin, phy_fin, ao_fin, hpe_fin, it_fin, ce_fin]
    
    for score in mid_scores:
        if score > 20 or score < 0:
            print(f"Please enter your mid-term result correctly. Error in score: {score}")
            return False
    
    for score in fin_scores:
        if score > 100 or score < 0:
            print(f"Please enter your final result correctly. Error in score: {score}")
            return False
    
    return True

def results():
    if not check():
        return
    
    mid_total = eng_mid + amh_mid + maths_mid + geo_mid + chem_mid + bio_mid + his_mid + eco_mid + phy_mid + ao_mid + hpe_mid + it_mid + ce_mid
    fin_total = eng_fin + amh_fin + maths_fin + geo_fin + chem_fin + bio_fin + his_fin + eco_fin + phy_fin + ao_fin + hpe_fin + it_fin + ce_fin
    
    # Convert mid-term to be out of 100 (since final is out of 100)
    mid_total_converted = mid_total * (100/260)  # 13 subjects * 20 = 260
    
    semester_total = mid_total_converted * 0.3 + fin_total * 0.7  # 30% mid, 70% final
    semester_average = semester_total / 13
    
    mid_average = mid_total / 13
    fin_average = fin_total / 13
    
    # Grade calculation based on final average
    if fin_average >= 90:
        grade = "A"
    elif fin_average >= 80:
        grade = "B"
    elif fin_average >= 70:
        grade = "C"
    elif fin_average >= 60:
        grade = "D"
    elif fin_average >= 50:
        grade = "E"
    else:
        grade = "F"

    print("\n=====Mid Exam Result=====")
    print(f"Total result: {mid_total}/260")
    print(f"Average result: {mid_average:.2f}/20")

    print("\n=====Final Exam Result=====")
    print(f"Total result: {fin_total}/1300")
    print(f"Average result: {fin_average:.2f}/100")

    print("\n=====Semester Exam Result=====")
    print(f"Combined total (30% mid + 70% final): {semester_total:.2f}/1000")
    print(f"Combined average: {semester_average:.2f}")
    print(f"Final Grade: {grade}")

results()
