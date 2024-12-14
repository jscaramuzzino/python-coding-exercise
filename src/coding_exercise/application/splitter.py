from coding_exercise.domain.model.cable import Cable


class Splitter:
    
    MINTIMES = 1
    MAXTIMES = 64
    MINLENGTH = 2
    MAXLENGTH = 1024
    
    TENCABLES = 10
    HUNDREDCABLES = 100

    def __validate(self, cable: Cable, times: int):
        """validates all inputs before proceeding with calculations

        Args:
            cable (Cable): cable object
            times (int): number of times to be cut

        Raises:
            ValueError: cable length between 2 and 1024 inclusive
            ValueError: cut amount less than length of cable
            ValueError: cuts between 1 and 64
        """
        valid = True
        valid = self._validate_cable_length(cable.length)
        if not valid:
            raise ValueError(f"Cable not between {self.MINLENGTH} and {self.MAXLENGTH} inclusive.")
        valid = self._validate_times(times)
        if not valid:
            raise ValueError(f"Cuts not between {self.MINTIMES} and {self.MAXTIMES} inclusive.")
        valid = self._validate_enacted_cuts(cable.length, times)
        if not valid:
            raise ValueError(f"Amount of cuts will result in < 1 length cables. Can not cut.")

    def _validate_times(self, times: int) -> bool:
        return times >= self.MINTIMES and times <= self.MAXTIMES
    
    def _validate_enacted_cuts(self, cable_length: int, times: int) -> bool:
        return cable_length > times 

    def _validate_cable_length(self, cable_length: int) -> bool:
        return cable_length >= self.MINLENGTH and cable_length <= self.MAXLENGTH
    
    @staticmethod
    def plus_one(number: int) -> int:
        one = 1
        if isinstance(number, int):
            return number + one
        raise ValueError(f"You did not enter an int.")
    
    def get_new_cable_lengths(self, cable: Cable, times: int) -> list[int]:
        """
        Divide the cable into equal n + 1 lengths. Use the remainder to
        get as many of the newely cut lengths as possible. Return all the 
        lengths as a list

        Args:
            cable (Cable): cable object
            times (int): amount of times to be cut

        Returns:
            list[int]: list of lengths
        """
        remainder_cables = []
        number_of_main_new_cables = times + 1
        length_of_main_new_cables = cable.length // number_of_main_new_cables
        cables = [length_of_main_new_cables] * number_of_main_new_cables
        
        remainder = cable.length % number_of_main_new_cables
        if remainder == 0:
            return cables
        
        number_of_remainder_cable = remainder // length_of_main_new_cables
        length_of_remainder_cable = remainder % length_of_main_new_cables
        
        if number_of_remainder_cable > 0:
            remainder_cables = ([length_of_main_new_cables] * number_of_remainder_cable)
        
        if length_of_remainder_cable > 0:
            remainder_cables.extend([length_of_remainder_cable])
        
        cables.extend(remainder_cables)
        return cables   
        
    def get_zfill(self, length: int) -> int:
        if length < self.TENCABLES:
            return 1
        elif length < self.HUNDREDCABLES:
            return 2
        else:
            return 3
    
    def create_cables(self, cable_lengths: list[int]) -> list[Cable]:
        """Create a list of cables with lengths and names

        Args:
            cable_lengths (list[int]): list of lengths

        Returns:
            list[Cable]: list of cables with zfilled names
        """
        cables = []
        zfill_amount = self.get_zfill(len(cable_lengths))
        for index, cable_length in enumerate(cable_lengths):
            cable_number = str(index).zfill(zfill_amount)
            cable = Cable(cable_length, f'coconuts-{cable_number}')
            cables.append(cable)
        return cables
    
    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable, times)
        cables_lengths = self.get_new_cable_lengths(cable, times)
        return self.create_cables(cables_lengths)
        
        
if __name__ == "__main__":
    given_cable = Cable(10, "coconuts")
    result = Splitter().split(given_cable, 1)
    for c in result:
        print (c.name, c.length)

    given_cable = Cable(5, "coconuts")
    result = Splitter().split(given_cable, 2)
    for c in result:
        print (c.name, c.length)
    
    given_cable = Cable(14, "coconuts")
    result = Splitter().split(given_cable, 3)
    for c in result:
        print (c.name, c.length)
    
    given_cable = Cable(1000, "coconuts")
    result = Splitter().split(given_cable, 50)
    for c in result:
        print (c.name, c.length)