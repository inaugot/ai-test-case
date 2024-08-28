from agency_swarm import Agency
from QAEngineer import QAEngineer
from TestCaseGenerator import TestCaseGenerator
from EComAgencyCEO import EComAgencyCEO

ceo = EComAgencyCEO()
test_case_generator = TestCaseGenerator()
qa_engineer = QAEngineer()

agency = Agency([ceo,  [ceo, test_case_generator],
                 [test_case_generator, qa_engineer]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()