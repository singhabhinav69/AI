def decision_tree():
    print("Welcome to the Basic AI Decision Tree!")
    
    # First decision point: Weather preference
    weather = input("Do you like sunny weather? (yes/no): ").lower()
    
    if weather == 'yes':
        # Second decision point if sunny
        activity = input("Do you want to go outside for a walk? (yes/no): ").lower()
        if activity == 'yes':
            print("Great! Go for a walk and enjoy the sunshine!")
        else:
            print("Maybe you can enjoy the sunny weather indoors with a good book or movie.")
    else:
        # If the person does not like sunny weather
        indoors_activity = input("Do you prefer indoor activities? (yes/no): ").lower()
        if indoors_activity == 'yes':
            print("How about reading a book or watching a movie?")
        else:
            print("Maybe it's time to try something new, like painting or cooking.")

# Running the decision tree
decision_tree()
