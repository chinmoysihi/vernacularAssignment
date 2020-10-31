from typing import List,Dict,Callable,Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]

class Validate:

    def __init__(self):
        self.filled = True
        self.partially_filled = False
        self.trigger = ''
        self.parameters = {}

    def set_trigger(self, value:str):
        self.trigger = value

    def set_filled(self, value:bool):
        self.filled = value

    def set_partially_filled(self, value:bool):
        self.partially_filled = value

    def set_Parameter(self, values: List[str], key: str, support_multiple: bool = True, pick_first: bool = False) -> None:

        if values != []:
            if support_multiple or (not support_multiple and not pick_first):
                self.parameters = {key : values}
            else:
                self.parameters = {key : values[0]}
    def get_trigger(self) -> str:
        return self.trigger

    def get_filled(self) -> bool:
        return self.filled
    def get_partially_filled(self) -> bool :
        return self.partially_filled
    def get_parameter(self) -> Dict :
        return self.parameters

    def get_response(self):
        return {
            "filled" : self.get_filled(),
            "partially_filled" : self.get_partially_filled(),
            "trigger" : self.get_trigger(),
            "parameters" : self.get_parameter()

        }
