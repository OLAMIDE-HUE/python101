# defining the custom_song
def custom_song(action, adjective, noun1, verb, preposition, place, object, noun2):
    print(f"{action}, {action} {adjective} {noun1}")
    print(f"How I {verb} what you are")
    print(f"Up {preposition} the {place} so high")
    print(f"Like a {object} in the {noun2}")
    print(f"{action}, {action} {adjective} {noun1}")
    print(f"How I {verb} what you are")


# getting the user responses
action = input("Enter an action: ")
adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
preposition = input("Enter a preposition(in regards to location): ")
place = input("Enter a place: ")
object = input("Enter an object: ")
noun2 = input("Enter another noun: ")


# calling the custom_song function
custom_song(action, adjective, noun1, verb, preposition, place, object, noun2)
