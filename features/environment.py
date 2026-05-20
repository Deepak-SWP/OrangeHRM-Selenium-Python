def before_scenario(context, scenario):
    print(f"Starting Scenario: {scenario.name}")

def after_scenario(context, scenario):
    print(f"Completed Scenario: {scenario.name}")