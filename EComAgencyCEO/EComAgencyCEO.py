from agency_swarm.agents import Agent


class EComAgencyCEO(Agent):
    def __init__(self):
        super().__init__(
            name="EComAgencyCEO",
            description="Oversees the entire process and coordinates between other agents.",
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
        print("---------ECOM AGENCY CEO--------")
        print(message)
        print("---------ECOM AGENCY CEO--------")
        return message
