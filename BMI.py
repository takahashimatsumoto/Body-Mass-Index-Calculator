height = float (input("Enter the height in cm:"))
weight = float (input("Enter the weight in kg:"))
BMI = weight/(height/100)**2

print ("Your Height:", height)
print ("Your Weight:", weight)
print ("Your Body Mass Index is", BMI)

print ()

if BMI <= 18.5:
    print ("You are underweight. In order for you to gain weight, please eat five to six smaller meals during the day rather than two or three large meals. Choose whole-grain breads, pastas, and cereals, fruits and vegetables, dairy products, lean protein sources, and nuts and seeds as part of a balanced diet. Smoothies and shakes are great options. Don't overindulge in diet Coke, coffee, or other low-calorie, low-nutrient beverages.")
elif BMI <= 25:
    print ("Congratulations you are in a healthy body state! Just a reminder to keep your healthy diet. Eat fruits and vegetables. Here are some list of food you need to intake and have a proper balanced diet: Low fat milk; Protein foods such as poultry, meat, dry beans, eggs and nuts; Seafood such as salmon, tuna, crab, mussels and oysters; Continue eating your balanced diet. Don't forget to stay hydrated ang drink water. You are healthy and doing good! ")
elif BMI <= 30:
    print ("You are overweight.")
else: 
    print ("The category you fall under is in Obese. This means your body weight is greater than what is considered normal or healthy for a certain height. This puts your health at danger and to prevent getting diseases or illness, here are some things you can do to have a healthy body: Do regular physical activity and exercise; Avoid consuming more calories particularly in fatty and sugary foods such as fatty meats, poultry skin, heavy cream, butter, soft cheese, bacon, processed food, and chocolate; Consume good fatty foods such as nuts, peanut butter, almond butter, avocado, salmon, herring, sardines, trout, walnuts, flaxseed, chia seeds, tofu, roasted soybeans and soy nut butter, coconut, 70% cococa dark chocolate, whole eggs, and yogurt; Try exercises such as walking, jogging, swimming, tennis, running, dancing and other sports and activities that will make you sweat and loose weight. Practice eating slowly and avoid situations where you know you could be tempted to overeat")
    

