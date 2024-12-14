#firstly i am going to define the mappings for the descriptive outputs

#face types of the characters
face_types = {
    "MF1": "square", "MF2": "oval", "MF3": "round",
    "FF1": "square", "FF2": "oval", "FF3": "round"
}

#hairstyles of the characters
hairstyles = {
    "MH1": "straight", "MH2": "wavy", "MH3": "curly", "MH4": "buzzcut", "MH5": "spiky",
    "FH1": "straight", "FH2": "wavy", "FH3": "curly", "FH4": "pixie", "FH5": "bun"
}

#hair colors of the characters
hair_colors = {
    "HCM1": "black", "HCM2": "brown", "HCM3": "blonde", "HCM4": "neon", "HCM5": "red",
    "HCF1": "black", "HCF2": "brown", "HCF3": "blonde", "HCF4": "neon", "HCF5": "red"
}


#creating a class for the character customization where the transitions are defined along with the input processing 
#and the character creation logic.

class CharacterCustomization:
    def __init__(self):
        self.current_state = "q0"
        self.character_details = {"gender": None, "face": None, "hair": None, "color": None}
        self.transitions = {
            "q0": {"M": "q1", "F": "q4"},
            "q1": {"MF1": "q2", "MF2": "q2", "MF3": "q2"},
            "q2": {"MH1": "q3", "MH2": "q3", "MH3": "q3", "MH4": "q3", "MH5": "q3"},
            "q3": {"HCM1": "q7", "HCM2": "q7", "HCM3": "q7", "HCM4": "q7", "HCM5": "q7"},
            "q4": {"FF1": "q5", "FF2": "q5", "FF3": "q5"},
            "q5": {"FH1": "q6", "FH2": "q6", "FH3": "q6", "FH4": "q6", "FH5": "q6"},
            "q6": {"HCF1": "q7", "HCF2": "q7", "HCF3": "q7", "HCF4": "q7", "HCF5": "q7"}
        }
        self.history_stack = []  # To track the history of states and inputs

#now this function will process the input string and will return the result of the character customization
    def process_input_string(self, input_string):
        inputs = input_string.split()  # Split the input string into individual choices
        for input_symbol in inputs:
            if self.current_state == "q7":
                return "Rejected: No actions allowed after reaching the final state!"

            if input_symbol == "B":
                if not self.history_stack:  
                    return "Rejected: Cannot backtrack further!"
                self.current_state, last_input = self.history_stack.pop() 
                self._clear_current_detail(last_input)
            elif input_symbol in self.transitions[self.current_state]:
                self.history_stack.append((self.current_state, input_symbol))
                self.current_state = self.transitions[self.current_state][input_symbol]
                self._update_character_details(input_symbol)
            else:
                return "Rejected: Invalid choice!"

        return "Accepted" if self.is_accepted() else "Rejected"

#this function will clear the last character detail based on the last input
    def _clear_current_detail(self, last_input):
        """Clear the last character detail based on the last input."""
        if last_input == "M" or last_input == "F":
            self.character_details = {"gender": None, "face": None, "hair": None, "color": None}
        elif last_input.startswith("MF") or last_input.startswith("FF"):
            self.character_details["face"] = None
        elif last_input.startswith("MH") or last_input.startswith("FH"):
            self.character_details["hair"] = None
        elif last_input.startswith("HCM") or last_input.startswith("HCF"):
            self.character_details["color"] = None

#now this fucnction here will update the character details based on the current state and the input
    def _update_character_details(self, input_symbol):
        """Update character details based on the current state and input."""
        if self.current_state == "q1":
            self.character_details["gender"] = "Male"
        elif self.current_state == "q4":
            self.character_details["gender"] = "Female"
        elif input_symbol.startswith("MF") or input_symbol.startswith("FF"):
            self.character_details["face"] = face_types[input_symbol]
        elif input_symbol.startswith("MH") or input_symbol.startswith("FH"):
            self.character_details["hair"] = hairstyles[input_symbol]
        elif input_symbol.startswith("HCM") or input_symbol.startswith("HCF"):
            self.character_details["color"] = hair_colors[input_symbol]

    def is_accepted(self):
        return self.current_state == "q7"

    def get_character_details(self):
        return self.character_details


#this is the main function where the user will interact with the program
def main():
    print("\n")
    print("Welcome to Character Customization!")
    print("Provide your choices as a single string separated by spaces.")
    print("Use 'B' to backtrack and replace a previous choice.")

    # Input from user
    print("\n")
    user_input = input("Enter your choices: ").strip()
    game = CharacterCustomization()
    result = game.process_input_string(user_input)

    if result == "Accepted":
        print("\nCharacter Accepted!")
        details = game.get_character_details()
        print("Character Details:")
        print(f"Gender: {details['gender']}, Face: {details['face']}, Hair: {details['hair']}, Hair Color: {details['color']}")
    else:
        print(f"\n{result}")


if __name__ == "__main__":
    main()
