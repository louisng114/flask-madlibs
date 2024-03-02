"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, story_id):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.story_id = story_id

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    
# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""", "story1"
)

story2 = Story(
    ["name", "plural_noun", "past_tense_verb", "place"],
    """{name}, the inventer of {plural_noun}, often {past_tense_verb} at {place}""", "story2"
)

story3 = Story(
    ["any_word"],
    """One word: {any_word}!""", "story3"
)

story_list = [story1, story2, story3]

def find_story(story_id):
    for story in story_list:
        if story.story_id == story_id:
            return story
