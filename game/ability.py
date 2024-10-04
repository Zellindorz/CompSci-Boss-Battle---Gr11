from .character import Stats


class AbilityRegistry:
    registry = {}

    @classmethod
    def register(cls, ability_identifier: str, ability_class):
        """
        Registers a new ability with the given name and class.
        """
        cls.registry[ability_identifier.lower()] = ability_class


class Ability:
    identifier: str
    name: str
    effect: Stats
    cost: Stats

    def __init_subclass__(cls, **kwargs):
        """
        Automatically registers subclasses of Ability in the AbilityRegistry
        based on their defined 'name' attribute.
        """
        super().__init_subclass__(**kwargs)
        if hasattr(cls, 'identifier'):
            AbilityRegistry.register(cls.identifier, cls)

    def verify(self, op_token, solve_token):
        return solve_token == self.algorithm(op_token)

    def algorithm(self, op_token):
        pass

# Resource Spells
class Rest(Ability):
    identifier = "rest"
    name = "Rest"
    effect = Stats(stamina=5)

    def algorithm(self, op_token):
        return op_token[::-1]
    

class Recharge(Ability):
    identifier = "recharge"
    name = "Recharge"
    effect = Stats(mana=10)

    def algorithm(self, op_token):
        return f"mana{op_token}mana"

# Healing Spells
class Heal(Ability):
    identifier = "heal"
    name = "Heal"
    effect = Stats(health=5)
    cost = Stats(mana=-4)

    def algorithm(self, op_token):
        return f"heal{op_token}heal"
    

class Resurrect(Ability):
    identifier = "resurrect"
    name = "Resurrect"
    # TODO: Code 
    effect = Stats(health=1)
    cost = Stats(mana=-5)

    def algorithm(self, op_token):
        return f"alive{op_token}alive"
    

# Chance Spells
class Train(Ability):
    identifier = "train"
    name = "Train"
    effect = Stats(health=5)
    cost = Stats(mana=-5)

    def algorithm(self, op_token):
        return f"train{op_token}train"
    

class Dodge(Ability):
    identifier = "dodge"
    name = "Dodge"
    effect = Stats(agility=5)
    cost = Stats(stamina=-1)

    def algorithm(self, op_token):
        return op_token[::-1]

# Offense: Blunt Spells
class BasicAttack(Ability):
    identifier = "attack"
    name = "Basic Attack"
    effect = Stats(health=-1)
    cost = Stats(stamina=-1)

    def algorithm(self, op_token):
        correct_solve_token = ""
        for i in range(0, len(op_token), 2):
            correct_solve_token += op_token[i]

        return correct_solve_token
    

class DoubleStrike(Ability):
    identifier = "strike"
    name = "Double Strike"
    effect = Stats(health=-2)
    cost = Stats(stamina=-2)

    def algorithm(self, op_token):
        correct_solve_token = ""
        correct_solve_token += op_token*2
        return correct_solve_token
    
# Offense: Magic Spells
class Fireball(Ability):
    identifier = "fireball"
    name = "Fireball"
    effect = Stats(health=-5)
    cost = Stats(mana=-5, stamina=-4)

    def algorithm(self, op_token):
        correct_solve_token = ""
        correct_solve_token += f"burning{op_token}heat"
        return correct_solve_token
        
    
class Bolt(Ability):
    identifier = "bolt"
    name = "Bolt"
    effect = Stats(health=-4)
    cost = Stats(mana=-3, stamina=-3)

    def algorithm(self, op_token):
        correct_solve_token = ""
        correct_solve_token += f"lightning{op_token}thunder"
        return correct_solve_token

    
class Frost(Ability):
    identifier = "frost"
    name = "Frost"
    effect = Stats(health=-3)
    cost = Stats(mana=-2, stamina=-3)

    def algorithm(self, op_token):
        correct_solve_token = ""
        correct_solve_token += f"brr{op_token}brr"
        return correct_solve_token
    

# Other Spells
class Observe(Ability):
    identifier = "observe"
    name = "Observe"
    #Write code for observe here in effect variable

    def algorithm(self, op_token):
        return f"seek{op_token}out"