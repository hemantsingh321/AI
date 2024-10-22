from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork([
    ('Disease_A', 'Symptom_X'),
    ('Disease_B', 'Symptom_X')
])

cpd_disease_a = TabularCPD(
    variable='Disease_A',
    variable_card=2,
    values=[[0.9],
            [0.1]]
)

cpd_disease_b = TabularCPD(
    variable='Disease_B',
    variable_card=2,
    values=[[0.95],
            [0.05]]
)

cpd_symptom_x = TabularCPD(
    variable='Symptom_X',
    variable_card=2,
    values=[
        [0.01, 0.6, 0.6, 0.8],
        [0.99, 0.4, 0.4, 0.2]
    ],
    evidence=['Disease_A', 'Disease_B'],
    evidence_card=[2, 2]
)

model.add_cpds(cpd_disease_a, cpd_disease_b, cpd_symptom_x)

assert model.check_model()

inference = VariableElimination(model)

query_result = inference.query(
    variables=['Disease_A'],
    evidence={'Symptom_X': 1}
)

print("Probability distribution for Disease A given Symptom X is present:")
print(query_result)
