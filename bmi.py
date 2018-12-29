import math
print("Body Mass Index (BMI) for adult")
name = str(input("Patient name:"))
age = int(input("Patient age:"))
gender = str(input("Patient gender:"))
#if gender == str(male) or str(M):
#    print("Hello! " + "Mr."+ name + " Please enter your weight and height")
#elif gender == str(female) or str(F):
#    print("Hello! " + "Mrs./Ms." + name + " Please enter your weight and height")
weight = float(input("Patient weight (in kg):"))
height = float(input("Patient height (in m):"))
def BMI():
    BMI = str( weight//(height)**2)
    print("Your Body Mass Index (BMI):" + BMI)
    BMI = float(BMI)
    if  BMI <= int(18.5):
        for BMI in range (int(0),int(18.5)):
            print(name + " is 'UNDERWEIGHT'" )
            suggestion = "A BMI is 'less than 18.5' indicates that you are 'UNDERWEIGHT' , so you may need tpo put on some weight. You are recommended to ask your doctor or a dietitian for advice"
            health_risks = " Having a BMI of 'UNDER 18.5' can increase the risk of ' MALNUTRITION ' , 'OSTEOPOROSIS' , 'ANEMIA' and a range of problems than can result from various nutrient deficiencies . It can also be a 'sign of a hormonal , digestive or other problems'"  
            print("SUGGESTIONS: " + suggestion)
            print("HEALTH RISKS:" + health_risks)
            break
    elif BMI > int(18.5) and BMI < int(24.5):
        for BMI in range (int(18.5) , int(24.5)):
            print(name + " is 'HEALTHY'")
            suggestion = "A BMI of '18.5 - 24.9' indicates that you are at a 'HEALTHY WEIGHT' for your height. By maintaining a healthy weight , you lower your risk of developing serious health problems"
            print("SUGGESTIONS: " + suggestion)
            break
    elif BMI > int(25.0) and BMI < int(29.9):      
        for BMI in range (int(25.0) , int(29.9)):
            print(name + " is'OVERWEIGHT'")
            suggestion = "A BMI of '25 - 29.9' indicates that you are 'SLIGHTLY OVERWEIGHT' . You may be advised to lose some weight for health reasons. You are recommended to talk to your doctor or a dietitian for advice"
            print("SUGGESTIONS: " + suggestion)
            break
    elif BMI >= int(30.0):
        for BMI in range (int(30.0)):
            print(name + " is'OBESE'")
            suggestion = "A BMI of 'over 30' indicates that you are 'HEAVILY OVERWEIGHT' . Your health may be at risk if you do not lose weight you are recommeneded to talk to your doctor or a dietitian for advice"
            health_risks = "People with a BMI of '30 or more' have a higher risk than others of diseases such as 'HEART DISEASES','TYPE 2 DIABETES', 'SLEEP APNEA', 'HIGH BLOOD PRESSURE' , ' COLORECTAL CANCER '."
            print("SUGGESTIONS: " + suggestion)
            print("HEALTH RISKS:" + health_risks)
            break
BMI()
