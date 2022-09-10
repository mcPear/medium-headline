import streamlit as st

headline = st.text_input(
    "Your headline idea",
    help="Type here what you got and we'll fix it then, don't worry.",
)
red = '<p style="color:#C6F1D6;">{}</p>'  # TODO consider error box and success box
green = '<p style="color:#FF8080;">{}</p>'
st.markdown(red.format("abcd"), unsafe_allow_html=True)
st.markdown(green.format("defg"), unsafe_allow_html=True)

# Use columns or expander to organise that

st.header("Make sure your headline answers below questions:")
st.checkbox("What the story is about?")
st.checkbox("Why the story matters now?")

st.header("Consider below actions:")
st.checkbox(
    "Share the headline with a few writing peers and see what they think the story is about."
)

st.header("Follow below principles:")
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

st.header("Guiding questions to consider:")
st.checkbox("Could the headline be clearer?")
st.checkbox("Is the headline specific enough?")
st.checkbox("Does the tone reflect the voice or point of view of the article?")
st.checkbox("How might the headline convey what is unique about the story?")
st.checkbox("Is the headline clear and honest about what the story offers the reader?")

st.header("Avoid:")
st.checkbox("all caps")  # implement
st.checkbox("all typos")  # implement
st.checkbox("links")  # implement
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

st.header("Viral tips:")
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

st.header("Sources:")
st.markdown(
    """[”How to Write a Headline” by Medium Creators](https://medium.com/creators-hub/how-to-write-a-headline-a72ab3449150)"""
)
st.markdown(
    """[”5 Majestic Headline Secrets from Medium’s Most Viral Writers” by Nick Waghorn](https://bettermarketing.pub/5-majestic-headline-secrets-from-mediums-most-viral-writers-506753732dc9)"""
)

# TODO https://medium.com/creators-hub/how-to-write-a-compelling-headline-that-isnt-clickbait-7cb816cec438
# TODO https://medium.com/creators-hub/23-examples-of-effective-headlines-2e7f753476f1
# some guidelines repeat
