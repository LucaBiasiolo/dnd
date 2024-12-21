from src.Die import Die

class Oracle:
    
    _die: Die
    _likelihood: int = 0

    def __init__(self, likelihood: int):
        self._die = Die(1,20)
        self._likelihood = likelihood

    def consult(self):
        die_result = self._die.throw()
        
        result_with_likelihood = die_result + self._likelihood
        if result_with_likelihood <= 6:
            return "No"
        elif result_with_likelihood >= 7 and result_with_likelihood <= 12:
            return "Maybe"
        else:
            return "Yes"