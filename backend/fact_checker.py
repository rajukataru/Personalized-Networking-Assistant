class FactChecker:
    def check_fact(self, topic):
        facts = {
            "AI": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
            "Cloud": "Cloud computing provides computing resources over the internet.",
            "Blockchain": "Blockchain is a distributed ledger technology.",
            "Healthcare": "AI is increasingly used in healthcare for diagnosis and prediction."
        }

        return facts.get(topic, "No fact available for this topic.")