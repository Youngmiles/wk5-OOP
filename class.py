class TitanShifter:
    """Base class for all Titan shifters"""
    
    def __init__(self, name, titan_name, abilities):
        """
        Initialize a Titan shifter
        :param name: Human name (str)
        :param titan_name: Titan form name (str)
        :param abilities: List of special abilities (list)
        """
        self.name = name
        self._titan_name = titan_name  
        self.abilities = abilities
        self._transformation_count = 0  
        self._current_form = "human"
        self.motivation = "Protect humanity"
    
    def transform(self):
        """Transform into Titan form"""
        if self._transformation_count >= 3:
            print(f"{self.name} is too exhausted to transform!")
            return False
            
        self._current_form = "titan"
        self._transformation_count += 1
        print(f"{self.name} transforms into the {self._titan_name} Titan!")
        return True
    
    def revert(self):
        """Revert to human form"""
        self._current_form = "human"
        print(f"{self.name} reverts to human form")
    
    def use_ability(self, ability_name):
        """Use a Titan ability"""
        if ability_name in self.abilities:
            print(f"{self.name} uses {ability_name}!")
            return True
        print(f"{self._titan_name} Titan doesn't have that ability!")
        return False
    
    def __str__(self):
        """String representation"""
        return (f"Titan Shifter: {self.name}\n"
                f"Titan Form: {self._titan_name}\n"
                f"Abilities: {', '.join(self.abilities)}\n"
                f"Current Form: {self._current_form.title()}\n"
                f"Transformations Left: {3 - self._transformation_count}")


class FoundingTitan(TitanShifter):
    """Class representing the Founding Titan's power"""
    
    def __init__(self, name, titan_name, abilities, coordinate_control):
        super().__init__(name, titan_name, abilities)
        self._coordinate_control = coordinate_control 
        self._memory_access = True
        self._rumbling_activated = False
    
    def activate_rumbling(self):
        """Trigger the Rumbling"""
        if not self._coordinate_control:
            print("Cannot activate Rumbling without coordinate control!")
            return False
            
        self._rumbling_activated = True
        print(f"{self.name} activates the Rumbling! 🦶🔥")
        return True
    
    def alter_eldian_memories(self):
        """Use Founding Titan's memory power"""
        if self._memory_access:
            print(f"{self.name} accesses the Paths and alters Eldian memories!")
            return True
        print("Memory access unavailable!")
        return False
    
    def use_ability(self, ability_name):  
        """Special version for Founding Titan"""
        if ability_name == "Rumbling" and self._coordinate_control:
            return self.activate_rumbling()
        return super().use_ability(ability_name)
    
    def __str__(self):
        """Enhanced string representation"""
        base_info = super().__str__()
        return (f"{base_info}\n"
                f"Coordinate Control: {self._coordinate_control}\n"
                f"Rumbling Status: {'ACTIVATED' if self._rumbling_activated else 'inactive'}")


class ErenYeager(FoundingTitan):
    """Class specifically for Eren Yeager's evolution"""
    
    def __init__(self):
        super().__init__(
            name="Eren Yeager",
            titan_name="Attack/Founding",
            abilities=[
                "Hardening",
                "Regeneration",
                "War Hammer",
                "Rumbling"
            ],
            coordinate_control=True
        )
        self._phase = 1  
        self._determination = 100
        self.friends = ["Mikasa", "Armin"]
    
    def advance_phase(self):
        """Progress through Eren's character phases"""
        if self._phase < 3:
            self._phase += 1
            self._update_abilities()
            print(f"Eren advances to phase {self._phase}!")
    
    def _update_abilities(self):
        """Update abilities based on phase"""
        if self._phase == 2:
            self.abilities.append("War Hammer")
            print("Eren gained War Hammer Titan powers!")
        elif self._phase == 3:
            self.abilities.extend(["Founding Titan", "Memory Manipulation"])
            print("Eren accessed the Founding Titan's full power!")
    
    def use_ability(self, ability_name):
        """Phase-dependent ability usage"""
        if ability_name == "Rumbling" and self._phase < 3:
            print("Eren hasn't unlocked this power yet!")
            return False
        return super().use_ability(ability_name)
    
    def motivate(self):
        """Eren's iconic speeches"""
        speeches = [
            "I'll destroy all the Titans!",
            "I won't stop until I achieve freedom!",
            "I was born into this world!",
            "I'll keep moving forward..."
        ]
        speech = speeches[self._phase - 1]
        print(f'Eren: "{speech}"')
        self._determination += 10
    
    def __str__(self):
        """Complete character sheet"""
        base_info = super().__str__()
        phases = {
            1: "Early Season Eren",
            2: "Marley Arc Eren",
            3: "Founding Titan Eren"
        }
        return (f"{base_info}\n"
                f"Character Phase: {phases[self._phase]}\n"
                f"Determination: {self._determination}\n"
                f"Close Friends: {', '.join(self.friends)}")

if __name__ == "__main__":
    print("=== My Superhero Eren Yeager ===")
    
    eren = ErenYeager()
    
    print("\n--- Initial State ---")
    print(eren)
    
    print("\n--- Phase 1: Early Eren ---")
    eren.transform()
    eren.use_ability("Hardening")
    eren.use_ability("Rumbling")  
    eren.motivate()
    eren.revert()
    
    print("\n--- Phase 2: War Hammer Powers ---")
    eren.advance_phase()
    eren.transform()
    eren.use_ability("War Hammer")
    eren.motivate()
    
    print("\n--- Phase 3: Founding Titan ---")
    eren.advance_phase()
    eren.transform()
    eren.use_ability("Rumbling")
    eren.alter_eldian_memories()
    eren.motivate()
    
    print("\n--- Final State ---")
    print(eren)