import streamlit as st
from titlecase import titlecase
from spellchecker import SpellChecker
import nltk
from nltk.tokenize import word_tokenize
import itertools

nltk.download("punkt")
spell = SpellChecker()

st.title("Medium Headline Guidelines")
st.caption("Turned into an interactive app")


st.subheader("Start with typing your headline idea")
headline = st.text_input(
    "",
    "7 Steps How To NOT Make an Oak Coffee Table",
)

st.markdown("---")

# TODO
# """
# MVP
# - keep merging guidelines
# - clean up helps
# - ask sources' authors for permission (or rephrase)
# - ask Danni for help

# Workshopping:
# - try to write a headline with that tool
# - use columns or expander to organise that
# - fill help when possible, for types too
# - ask in Facebook/reddit group/privs Medium Wroters/bloggers for feedback!
# - own domain (host on Streamlit)

# Features:
# - consider turning examplary headlines into links
# - bloom few shot for high-level guidelines
# - train paraphraser to specific types
# - BERT for suprise metric

# Design:
# - check out H1-6 instead of Streamlit's header/subheader
# """

# 1 Substantial guidelines
st.subheader("Substantial guidelines")
st.write("**Make sure your headline answers the ultimate questions:**")
st.checkbox("What the story is about?")
st.checkbox(
    "Why the story matters to a reader?"
)  # TODO does examplary headlines really answer that? maybe in sub-headlines, I don't get it but looks important, read more

st.write("**Moreover:**")

st.checkbox(
    "Focus on what is interesting",
    help="Your headline doesn’t need to address everything that’s in your story. It just needs to focus on the most interesting part of your story in a way that represents the overall truth of your story.",
)

st.checkbox(
    "Make it direct and clear",
    help="Your story is among many a reader is browsing. Be straightforward in what it is about.",
)

st.checkbox(
    "Deliver on your promises",
    help="You’re building a relationship with your readers. The headline sets the expectations, and the story must deliver on that.",
)

st.checkbox(
    "Don’t ask a question unless you know the answer",
    help="Same as above",
)

st.checkbox(
    "Use conventional language (if you write for a general audience)",
    help="Avoid jargon, and think of what makes sense in casual conversation. Know the language that your audience is familiar with.",
)

st.checkbox(
    "If you want to be poetic or clever in your headline, follow it up with a strong subheadline",
    help="You may want to be poetic, clever, or artistic in the title. The challenge with crafting a title this way is that it becomes opaque. It’s also much easier to write a bad title when striving for something poetic or clever than if you’re going for clarity. In most cases, the reader won’t click to find out more because they didn’t understand what the story was about in the first place.",
)

st.write("**Avoid:**")
st.checkbox("profanity")
st.checkbox("exaggeration")
st.checkbox("mystery")
st.checkbox(
    "particularly bold, hyperbolic, absolutist, or deliberately provocative claims"
)
st.checkbox("exploiting the readers’ emotions and insecurities")
st.checkbox(
    "obvious questions",
    help="Instead, see if there is a way to highlight the tension that the story conveys. Note that if a reader doesn’t share this question, they’ll skip over the piece. Also note that even if they do, they might skim the piece to find the answer, and leave.",
)
st.checkbox(
    "biases",
    help="“Be aware of who is in the room writing the headline and what the limits of their perspective might be,” shares Rawls. Often biases will show up in the adjectives you use, so double-check the ones you use, and consider what they may unintentionally express.",
)

# 2 Editorial guidelines DONE
st.subheader("Editorial Guidelines")
st.checkbox("Use Title Case (NEVER ALL CAPS)")  # implement warning?
# alpha_chars = [c for c in headline if c.isalpha()]
# upper_chars = [c for c in alpha_chars if c.isupper()]
# upper_ratio = upper_chars / alpha_chars
# is_mostly_upper = upper_ratio > 0.8
# TODO show is_mostly_upper

st.checkbox("Fix typos")  # red -> green, Spacy
# TODO try https://pypi.org/project/language-tool-python/
# if headline:
#     ll = [
#         [word_tokenize(w), " "] for w in headline.split()
#     ]  # TODO split whitespaces with regex to keep full whitespaces
#     tokens = list(itertools.chain(*list(itertools.chain(*ll))))
#     tokens = [
#         spell.correction(t) if spell.unknown([t]) and t != " " else t for t in tokens
#     ]
#     headline = "".join(tokens)
#     headline = titlecase(headline)
#     "Especially consider:"
#     st.info(headline)

st.checkbox("Remove links")  # implement warning with regex
st.checkbox(  # implement
    "Avoid gerunds (-ing words)",
    help="People are 70% more likely to click on the nongerund headlines",
)
st.checkbox(  # implement
    "Avoid one-word or two-word headlines",
    help="Don’t write a headline like you would a book title",
)

# 3 Proven Headline Types DONE

st.subheader("Proven Headline Types")

st.write("**Analysis**")
st.markdown(
    """
- What Everyone’s Getting Wrong About the Toilet Paper Shortage
- This Looks Like a Depression, Not a Recession
- Why All the Warby Parker Clones Are Now Imploding
- How the Black Death Radically Changed the Course of History
"""
)

st.write("**Bold declaration**")
st.markdown(
    """
- The Office Is Dead
- The End of the Girlboss Is Here
- Gen X Will Not Go Quietly
- The Parents Are Not Alright
- Meghan Markle Defeated the British Monarchy
- You Haven’t Earned the Right to Be a Basic B*tch Just Yet
- Your Inability to Do Pullups Is All In Your Head
- History Will Look Kindly on Trump, No Matter What
    """
)

st.write("**Assertive**")
st.markdown(
    """
- Alaska's Swimsuit Scandal Unfairly Polices Young Girls' Bodies
- Meghan Markle Defeated the British Monarchy
- Can Your Fitbit Predict the Flu? -> Your Fitbit Might Be Able to Predict the Flu
"""
)

st.write("**Descriptive teaser**")
st.markdown(
    """
- How a Hot $100 Million Home Design Startup Collapsed Overnight
- The Absurd Story Behind China’s Biggest Bank Robbery
- The Privileged Have Entered Their Escape Pods
- I Had to Leave My Home Because of the KKK
    """
)

st.write("**Instruction**")
st.markdown(
    """
- All Your Most Paranoid Transfer of Power Questions, Answered
- How to Avoid Going Insane as a Writer
- How to Become Popular Without Being Charming, Funny, or Outgoing
- 3 Ways to Rescue a Conversation That’s Going Nowhere
    """
)

st.write("**Clear promises**")
st.markdown(
    """
- How to Talk To an Employee Obsessed With Promotion
- An Embarassing Story Is a Secret Weapon to Work
"""
)

st.write("**Concise**")
st.markdown(
    """
- Your Office Chair Is Hurting You
- Our Skulls Are Out-Evolving Us
- Yes, She's Cheating On You
"""
)

st.write("**Benefit-based**")
st.caption(
    "Tip: The key to writing a tempting benefit-based headline is to be specific"
)
st.markdown(
    """
- How to Wake Up Smiling: The 9 Decisions That Led To A Life I Love
- This 3-Minute Exercise Will Change the Way You Solve Problems
- How I Doubled My Writing Income Overnight By Focusing on One Skill
"""
)

st.write("**Unconventional wisdom**")
st.markdown(
    """
- Your Life Is Full of Porn. Stop Getting Yourself Off
- How to Quietly Get People’s Attention in a Noisy World
- Lessons from a Billionaire Who Can’t Focus on Anything for More than 4 Hours
"""
)

st.write("**Promising life advice**")
st.markdown(
    """
- A Behind the Scenes Look at My Writing Schedule That’s Helped Write 5000+ Articles
- Steve Jobs Advice Turned This Programmer Into A Billionaire
- 8 Really Small Things That Tell You a Lot About Someone
"""
)

st.write("**Negative headlines**")
st.caption("Tip: Negative headlines often outperform positive ones")
st.markdown(
    """
- Six Habits of Deeply Happy People -> Six Habits of Deeply Miserable People
- 7 Things You Should Do in the Morning -> 7 Things You Should Never Do in the Morning
- A Rarely Mentioned Relationship Virtue That Strengthens Couples -> A Rarely Mentioned Relationship Sin That Bulldozes Couples
"""
)

st.write("**Personal headlines**")
st.markdown(
    """
- It's 2020, And I Had to Leave My Home Because of the KKK
"""
)

st.write("**Quote**")
st.markdown("- Mom, Why Don’t You Have Any Black Friends?")

st.write("**Validate readers’ feelings**")
st.markdown(
    """
- In Defense of the Super Low-Key Workout
"""
)

st.write("**Coining terms**")
st.markdown(
    """
- When Black Women Go From Office Pet to Office Threat
- Nazi Hippies: When the New Age and Far Right Overlap
"""
)


# st.write(
#     "**Controversial and divisive**"
# )  # TODO maybe remove, validate with other rules
# st.markdown(
#     """
# - You Will Destroy Yourself Financially If You Save
# - Pepsi’s $32 Billion Typo Caused Deadly Riots
# - 11 Things Socially Aware People Don’t Say
# """
# )

# 4 Actions DONE
st.subheader("Actions:")
st.checkbox(
    "Share the headline with someone you trust and see what they think the story is about"
)
st.checkbox("Give them a few options and tell them to make a choice")
st.checkbox(
    "When published, look at what people are saying when they share the article"
)

# 5 Sources DONE
st.subheader("Sources:")
st.markdown(
    """[”How to Write a Headline” by Medium Creators](https://medium.com/creators-hub/how-to-write-a-headline-a72ab3449150)"""
)
st.markdown(
    """[”How to Write a Compelling Headline That Isn’t Clickbait” by Medium Creators](https://medium.com/creators-hub/how-to-write-a-compelling-headline-that-isnt-clickbait-7cb816cec438)"""
)
st.markdown(
    """[”23 Examples of Effective Headlines” by Nadia Rawls](https://medium.com/creators-hub/23-examples-of-effective-headlines-2e7f753476f1)"""
)
st.markdown(
    """[”5 Majestic Headline Secrets from Medium’s Most Viral Writers” by Nick Waghorn](https://bettermarketing.pub/5-majestic-headline-secrets-from-mediums-most-viral-writers-506753732dc9)"""
)
