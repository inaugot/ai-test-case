from agency_swarm.agents import Agent


class TestCaseGenerator(Agent):
    def __init__(self):
        super().__init__(
            name="TestCaseGenerator",
            description="Generates test cases based on the provided feature document or functional specs. Focuses on functionalities such as browsing, adding products to the cart, and the checkout process.",
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
        return message
