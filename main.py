# Define mappings for descriptive outputs
face_types = {
    "MF1": "square", "MF2": "oval", "MF3": "round",
    "FF1": "square", "FF2": "oval", "FF3": "round"
}

hairstyles = {
    "MH1": "straight", "MH2": "wavy", "MH3": "curly", "MH4": "buzzcut", "MH5": "spiky",
    "FH1": "straight", "FH2": "wavy", "FH3": "curly", "FH4": "pixie", "FH5": "bun"
}

hair_colors = {
    "HC1": "black", "HC2": "brown", "HC3": "blonde", "HC4": "neon", "HC5": "red",
    "FHC1": "black", "FHC2": "brown", "FHC3": "blonde", "FHC4": "neon", "FHC5": "red"
}

class CharacterCustomization:
    def __init__(self):
        self.current_state = "q0"
        self.character_details = {"gender": None, "face": None, "hair": None, "color": None}

    def transition(self, input_symbol):
        # Define transitions
        transitions = {
            "q0": {"M": "q1", "F": "q4"},
            "q1": {"MF1": "q2", "MF2": "q2", "MF3": "q2", "B": "q0"},
            "q2": {"MH1": "q3", "MH2": "q3", "MH3": "q3", "MH4": "q3", "MH5": "q3", "B": "q1"},
            "q3": {"HC1": "q7", "HC2": "q7", "HC3": "q7", "HC4": "q7", "HC5": "q7", "B": "q2"},
            "q4": {"FF1": "q5", "FF2": "q5", "FF3": "q5", "B": "q0"},
            "q5": {"FH1": "q6", "FH2": "q6", "FH3": "q6", "FH4": "q6", "FH5": "q6", "B": "q4"},
            "q6": {"FHC1": "q7", "FHC2": "q7", "FHC3": "q7", "FHC4": "q7", "FHC5": "q7", "B": "q5"}
        }

        # Check if transition is valid for the current state
        if input_symbol in transitions[self.current_state]:
            self.current_state = transitions[self.current_state][input_symbol]
            if self.current_state == "q1":
                self.character_details["gender"] = "Male"
            elif self.current_state == "q4":
                self.character_details["gender"] = "Female"
            elif input_symbol.startswith("MF") or input_symbol.startswith("FF"):
                self.character_details["face"] = face_types[input_symbol]
            elif input_symbol.startswith("MH") or input_symbol.startswith("FH"):
                self.character_details["hair"] = hairstyles[input_symbol]
            elif input_symbol.startswith("HC") or input_symbol.startswith("FHC"):
                self.character_details["color"] = hair_colors[input_symbol]
            return True
        return False

    def is_accepted(self):
        return self.current_state == "q7"

    def get_character_details(self):
        return self.character_details

def main():
    print("Welcome to Character Customization!")
    print("Follow the steps to customize your character.")
    
    # Displaying available options
    print("\nGender Options:")
    print("M: Male")
    print("F: Female")

    game = CharacterCustomization()

    # User interaction loop
    while not game.is_accepted():
        if game.current_state == "q0":
            choice = input("Choose Gender (M/F): ")
        elif game.current_state == "q1":
            print("\nFace Options for Male:")
            print("MF1: Square, MF2: Oval, MF3: Round")
            choice = input("Choose Face Type (MF1/MF2/MF3) or 'B' to go back: ")
        elif game.current_state == "q2":
            print("\nHair Options for Male:")
            print("MH1: Straight, MH2: Wavy, MH3: Curly, MH4: Buzzcut, MH5: Spiky")
            choice = input("Choose Hairstyle (MH1-MH5) or 'B' to go back: ")
        elif game.current_state == "q3":
            print("\nHair Color Options for Male:")
            print("HC1: Black, HC2: Brown, HC3: Blonde, HC4: Neon, HC5: Red")
            choice = input("Choose Hair Color (HC1-HC5) or 'B' to go back: ")
        elif game.current_state == "q4":
            print("\nFace Options for Female:")
            print("FF1: Square, FF2: Oval, FF3: Round")
            choice = input("Choose Face Type (FF1/FF2/FF3) or 'B' to go back: ")
        elif game.current_state == "q5":
            print("\nHair Options for Female:")
            print("FH1: Straight, FH2: Wavy, FH3: Curly, FH4: Pixie, FH5: Bun")
            choice = input("Choose Hairstyle (FH1-FH5) or 'B' to go back: ")
        elif game.current_state == "q6":
            print("\nHair Color Options for Female:")
            print("FHC1: Black, FHC2: Brown, FHC3: Blonde, FHC4: Neon, FHC5: Red")
            choice = input("Choose Hair Color (FHC1-FHC5) or 'B' to go back: ")

        if not game.transition(choice):
            print("Invalid choice, please try again.")

    # Output final character details
    print("\nCharacter Accepted!")
    details = game.get_character_details()
    print("Character Details:")
    print(f"Gender: {details['gender']}, Face: {details['face']}, Hair: {details['hair']}, Hair Color: {details['color']}")

if __name__ == "__main__":
    main()
