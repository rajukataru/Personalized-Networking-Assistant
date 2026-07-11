class EventAnalyzer:
    def extract_themes(self, event_description):
        keywords = [
            "AI",
            "Machine Learning",
            "Cloud",
            "Blockchain",
            "Healthcare",
            "Education",
            "Sustainability",
            "Cybersecurity",
            "Data Science"
        ]

        themes = []

        for keyword in keywords:
            if keyword.lower() in event_description.lower():
                themes.append(keyword)

        if not themes:
            themes.append("General Networking")

        return themes