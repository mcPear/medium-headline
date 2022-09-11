import streamlit as st
from titlecase import titlecase
from spellchecker import SpellChecker
import nltk
from nltk.tokenize import word_tokenize
import itertools

nltk.download("punkt")

spell = SpellChecker()

st.title("Medium Headline")
st.caption(
    "The most important Medium Headline writing articles turned into an interactive app."
)
""
""
""
""

st.header("Start with typing your headline idea")
headline = st.text_input(
    "",
)

# TODO Use columns or expander to organise that
# TODO try to write a headline with that tool
# TODO maybe using markdown's H1-6 will result in better spacing
# TODO split to the most important quidelined (answear question, few traits, auto editing features) and expandable/on button click advanced guidelines

st.header("Then follow below guidelines")
st.subheader("Make sure your headline answers the ultimate questions:")
st.checkbox("What the story is about?")
st.checkbox("Why the story matters?")

st.subheader("Make sure the headline is:")
st.checkbox("clear")
st.checkbox("direct")
st.checkbox("assertive")
st.checkbox("focused on what is most interesting")

st.subheader("Consider below actions:")
st.checkbox(
    "Share the headline with a few writing peers and see what they think the story is about."
    "When published, look at what people are saying when they share the article."
)

st.subheader("Follow below principles:")
st.checkbox(
    "Be direct.",
    help="Your story is among many a reader is browsing. Be straightforward in what it is about.",
)
st.checkbox(
    "Use conventional language.",
    help="Avoid jargon, and think of what makes sense in casual conversation. Know the language that your audience is familiar with.",
)
st.checkbox(
    "Focus on what’s interesting.",
    help="Be straightforward about why a reader should read the article. Don’t bury or hide this.",
)
st.checkbox(
    "Deliver on your promises.",
    help="You’re building a relationship with your readers. The headline sets the expectations, and the story must deliver on that.",
)
st.checkbox(
    "If you want to be poetic or clever in your headline, follow it up with a strong subheadline.",
    help="You may want to be poetic, clever, or artistic in the title. The challenge with crafting a title this way is that it becomes opaque. It’s also much easier to write a bad title when striving for something poetic or clever than if you’re going for clarity. In most cases, the reader won’t click to find out more because they didn’t understand what the story was about in the first place.",
)

st.subheader("Guiding questions to consider:")
st.checkbox("Could the headline be clearer?")
st.checkbox("Is the headline specific enough?")
st.checkbox("Does the tone reflect the voice or point of view of the article?")
st.checkbox("How might the headline convey what is unique about the story?")
st.checkbox("Is the headline clear and honest about what the story offers the reader?")

st.subheader("Avoid:")
st.checkbox("all caps")  # implement warning?
st.checkbox("all typos")  # implement separately?
if headline:
    ll = [[word_tokenize(w), " "] for w in headline.split()]
    tokens = list(itertools.chain(*list(itertools.chain(*ll))))
    tokens = [
        spell.correction(t) if spell.unknown([t]) and t != " " else t for t in tokens
    ]
    headline = "".join(tokens)
    headline = titlecase(headline)
    "Especially consider:"
    st.info(headline)

st.checkbox("links")  # implement warning with regex
st.checkbox("profanity")  # implement?
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

"In the short term this may help drive traffic, but in the long term it undermines your integrity as a writer."

st.subheader("Viral tips:")
st.checkbox(
    "The key to writing a tempting benefit-based headline is to be specific.",
    help="“How to Wake Up Smiling: The 9 Decisions That Led To A Life I Love”\n“This 3-Minute Exercise Will Change the Way You Solve Problems”\n“How I Doubled My Writing Income Overnight By Focusing on One Skill”",
)
st.checkbox(
    "Negative headlines outperform positive ones.",
    help="“Six Habits of Deeply Happy People“\n“7 Things You Should Do in the Morning“\n“A Rarely Mentioned Relationship Virtue That Strengthens Couples“\n\nV.S\n\n“Six Habits of Deeply Miserable People”\n“7 Things You Should Never Do in the Morning“\n“A Rarely Mentioned Relationship Sin That Bulldozes Couples”",
)
st.checkbox(
    "Offer unconventional wisdom.",
    help="“Six Habits of Deeply Happy People“\n“7 Things You Should Do in the Morning“\n“A Rarely Mentioned Relationship Virtue That Strengthens Couples“\n\nV.S\n\n“Six Habits of Deeply Miserable People”\n“7 Things You Should Never Do in the Morning“\n“A Rarely Mentioned Relationship Sin That Bulldozes Couples”",
)
st.checkbox(
    "Make it controversial and divisive.",
    help="Here are a few perfect examples:\n“You Will Destroy Yourself Financially If You Save”\n“Pepsi’s $32 Billion Typo Caused Deadly Riots”\n“11 Things Socially Aware People Don’t Say”",
)  # TODO explain it is in opposite to Meodum guidelines
st.checkbox(
    "Share practical life advice that puts Universities to shame.",
    help="“A Behind the Scenes Look at My Writing Schedule That’s Helped Write 5000+ Articles”\n“Steve Jobs Advice Turned This Programmer Into A Billionaire”\n“8 Really Small Things That Tell You a Lot About Someone”",
)

st.subheader("Headline categories for inspiration")
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

st.write("**Quote**")
st.markdown("- Mom, Why Don’t You Have Any Black Friends?")

st.write("**Coining terms**")
st.markdown(
    """
- When Black Women Go From Office Pet to Office Threat
- Nazi Hippies: When the New Age and Far Right Overlap
"""
)

st.header("Sources:")
st.markdown(
    """[”How to Write a Headline” by Medium Creators](https://medium.com/creators-hub/how-to-write-a-headline-a72ab3449150)"""
)
st.markdown(
    """[”5 Majestic Headline Secrets from Medium’s Most Viral Writers” by Nick Waghorn](https://bettermarketing.pub/5-majestic-headline-secrets-from-mediums-most-viral-writers-506753732dc9)"""
)
st.markdown(
    """[”23 Examples of Effective Headlines” by Nadia Rawls](https://medium.com/creators-hub/23-examples-of-effective-headlines-2e7f753476f1)"""
)

# TODO https://medium.com/creators-hub/how-to-write-a-compelling-headline-that-isnt-clickbait-7cb816cec438
# some guidelines repeat
