def call_cost_calculate(call):
    cost = 0
    if call.is_local:
        cost = calculate_local_cost_of(call)
    elif call.is_national():
        cost = calculate_national_cost_of(call)
    elif call.is_international():
        cost = calculate_internationa_cost_of(call)
    return cost


class CallCostCalculator(object):

    @classmethod
    def to_handle(klass, call):
        # Codigo que busca el CostCallCalculator correspondiente

    def calculate(self):
        raise NotImplementedError("Subclass Responsibility")


class LocalCallCostCalculator(CallCostCalculator):
    def calculate(self)
    # Codigo de calculate_local_cost_of


class NationalCallCostCalculator(CallCostCalculator):
    def calculate(self)
    # codigo de calculate_national_cost_of


class InternationalCallCostCalculator(CallCostCalculator):
    def calculate(self)
    # codigo de calculate_international_cost_of


cost_calculator = CallCostCalculator.to_handle(call)
cost_calculator.calculate()
