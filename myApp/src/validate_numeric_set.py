from .validate import *

class Validate_Numeric_Values(Validate):

    def validate_numeric_entity(self,values: List[Dict], invalid_trigger: str = None, key: str = None,support_multiple: bool = True,
                                pick_first: bool = False, constraint=None, var_name=None, **kwargs) -> SlotValidationResult:
        """
        Validate an entity on the basis of its value extracted.
        The method will check if that value satisfies the numeric constraints put on it.
        If there are no numeric constraints, it will simply assume the value is valid.

        If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
        In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
        will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

        If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
        partially filled.

        :param pick_first: Set to true if the first value is to be picked up
        :param support_multiple: Set to true if multiple utterances of an entity are supported
        :param values: Values extracted by NLU
        :param invalid_trigger: Trigger to use if the extracted value is not supported
        :param key: Dict key to use in the params returned
        :param constraint: Conditional expression for constraints on the numeric values extracted
        :param var_name: Name of the var used to express the numeric constraint
        :return: a tuple of (filled, partially_filled, trigger, params)
        """

        valid_values = []

        if not values:
            values = []
            
        if len(values) == 0:
            self.set_trigger(invalid_trigger)
            self.set_filled(False)
            self.set_partially_filled(False)
        else:
            for each_items in values:
                if constraint:
                    expression = constraint.replace(var_name,str(each_items["value"]))
                    if eval(expression):
                        valid_values.append(each_items["value"])
                    else:
                        self.set_filled(False)
                        self.set_partially_filled(False)
                        self.set_trigger(invalid_trigger)
                else:
                    valid_values.append(each_items["value"])
            self.set_Parameter(valid_values,key,support_multiple,pick_first)

        return self.get_response()
