from crew import TradingCrew
import agentops


agentops.init(tags=["financial-analysis-crew"])


def run():
    inputs = {
        "stock_selection": "WELL",
        "initial_capital": "100000",
        "risk_tolerance": "Medium",
        "trading_strategy_preference": "Day Trading",
        "news_impact_consideration": True,
    }
    result = TradingCrew().crew().kickoff(inputs=inputs)
    print(result)


if __name__ == "__main__":
    run()
