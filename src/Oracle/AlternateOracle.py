from Oracle import Oracle

class AlternateOracle(Oracle):
    
    def consult(self):
        die_result = self._die.throw()

        result_with_likelihood = die_result + self._likelihood

        if result_with_likelihood <=0:
            return "No, and..."
        elif die_result == 1:
            return "Interrupt: Combat Encounter"
        elif die_result == 20:
            return "Interrupt: Random Event"
        elif result_with_likelihood > 20:
            return "Yes, and..."

        match result_with_likelihood:
            case 1|2:
                return "No, and..."
            case 3|4|5|6|7:
                return "No"
            case 8|9:
                return "No, but..."
            case 10:
                return "Maybe (skill check or reroll)"
            case 11|12:
                return "Yes, but..."
            case 13|14|15|16|17|18:
                return "Yes"
            case 19|20:
                return "Yes, and..."