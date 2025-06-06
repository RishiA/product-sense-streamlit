
def get_answer(question):
    if "why this course" in question.lower():
        return "It’s a focused course for senior PMs on product judgment, strategy, and creative execution—taught by Shreyas Doshi."
    elif "sui" in question.lower():
        return "It will help validate SUI product bets, clarify pricing, and support execution on high-priority initiatives."
    elif "ai" in question.lower():
        return "The course helps distinguish true user value from novelty, shaping a stronger POV on AI-enhanced product experiences."
    elif "shreyas" in question.lower():
        return "Shreyas Doshi is a former product leader at Stripe, Twitter, and Google. He now advises top AI startups like Anthropic."
    elif "share" in question.lower():
        return "I'll host a team session and share written takeaways and frameworks within 30 days of completing the course."
    else:
        return "Great question! While this prototype only answers a few common prompts, I'm happy to discuss more offline too."
