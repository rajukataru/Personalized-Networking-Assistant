class TopicGenerator:
    def generate_topics(self, themes):
        conversation_starters = []

        for theme in themes:
            conversation_starters.append(
                f"What are your thoughts on {theme}?"
            )

        return conversation_starters