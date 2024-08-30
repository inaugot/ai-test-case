from agency_swarm.agents import Agent


class QAEngineer(Agent):
    def __init__(self):
        super().__init__(
            name="QAEngineer",
            description="Validates the generated test cases, scores them, and separates valid and invalid test cases based on a threshold score. Ensures that test cases cover all critical functionalities and edge cases.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o-mini",
        )

    def response_validator(self, message):
        print("---------QA ENGINEER--------")
        print(message)
        print("---------QA ENGINEER--------")
        return message
