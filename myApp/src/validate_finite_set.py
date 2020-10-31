from .validate import *

class Validate_finite_Values(Validate):
    def validate_finite_values_entity(self,values: List[Dict], supported_values: List[str] = None,
                                invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
        """
        Validate an entity on the basis of its value extracted.
        The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

        :param pick_first: Set to true if the first value is to be picked up
        :param support_multiple: Set to true if multiple utterances of an entity are supported
        :param values: Values extracted by NLU
        :param supported_values: List of supported values for the slot
        :param invalid_trigger: Trigger to use if the extracted value is not supported
        :param key: Dict key to use in the params returned
        :return: a tuple of (filled, partially_filled, trigger, params)
        """
        valid_values = []
        if len(values) == 0:
            self.set_filled(False)
            self.set_partially_filled(False)
            self.set_trigger(invalid_trigger)

        else:
            for eachPassedValue in values:
                if eachPassedValue["value"] in supported_values:
                    valid_values.append(eachPassedValue["value"])
                else:
                    self.set_filled(False)
                    self.set_partially_filled(True)
                    self.set_trigger(invalid_trigger)

            self.set_Parameter(valid_values,key,support_multiple,pick_first)
        return self.get_response()
