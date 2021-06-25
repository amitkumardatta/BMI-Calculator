while True:

    weight = input("Please enter your weight: (Unit: Kg)")
    tall = input("Please enter your height: (unit: m)")
    weight = float(weight)
    tall = float(tall)
    BMI = weight / tall ** 2  # Calculation formula
    BMI = round(BMI, 3)

    if BMI < 18.5:
        print(
            f"Your body mass index is {BMI}, the weight is thin, the incidence of related diseases is low (but the risk of other diseases is increased)")
    elif BMI >= 18.5 and BMI < 24:
        print(
            f"Your body mass index is {BMI}, your weight is normal, and the incidence of related diseases is average. Please keep it up.")
    elif BMI >= 24 and BMI < 28:
        print(
            f"Your body mass index is {BMI}, pre-obesity, the incidence of related diseases has increased, please pay attention to your health.")
    elif BMI >= 28 and BMI < 30:
        print(
            f"Your body mass index is {BMI}, Class I obesity, and the incidence of related diseases has increased slightly. Please pay attention to your health.")
    elif BMI >= 30 and BMI < 40:
        print(
            f"Your body mass index is {BMI}, Grade II obesity, and the incidence of related diseases has increased moderately. Please pay attention to your health.")
    else:
        print(
            f"Your body mass index is {BMI}, grade III obesity, and the incidence of related diseases has increased severely. Please pay attention to your health.")



        print("created by Amit Kumar Datta")
# amitkumardatta
