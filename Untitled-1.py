def weather_decision_tree():
    print("Welcome to the Wearable Decision Tree!")
    
    # Step 1: Check if it's sunny
    sunny = input("Is it sunny? (yes/no): ").strip().lower()
    if sunny == 'yes':
        print("You should wear sunglasses and light clothes!")
    else:
        # Step 2: Check if it's raining
        raining = input("Is it raining? (yes/no): ").strip().lower()
        if raining == 'yes':
            print("You should wear a raincoat and carry an umbrella!")
        else:
            # Step 3: Check if it's cold
            cold = input("Is it cold? (yes/no): ").strip().lower()
            if cold == 'yes':
                print("You should wear a jacket or sweater!")
            else:
                print("You can wear a T-shirt!")
    
    print("Stay comfortable and enjoy your day!")

# Run the decision tree
weather_decision_tree()
