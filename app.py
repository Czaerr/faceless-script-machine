import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Prompt Templates
prompt_templates = {
    "Viral Story Explainer": """
You are a viral content writer. Write a short-form video script that starts with the hook: "{hook}" and explains a compelling story related to {topic}.
Use a conversational tone, short sentences, high curiosity pacing, and break it into three parts: Hook, Build, and Twist. End with a punchline or insight that’s surprising or emotionally satisfying.
Max 180 words. Write as if it's spoken dialogue.
""",

    "Controversial Opinion Hot Take": """
Act as a faceless TikTok creator known for bold opinions. Write a video script that starts with "{hook}" and delivers a polarizing or unexpected take on {topic}.
Use punchy, controversial language. Include one shocking stat or fact, then challenge mainstream beliefs. Format: Hook → Opinion → Evidence → Mic Drop.
""",

    "Psychology Breakdown": """
You're an edgy educational content creator. Write a short script explaining a weird psychological fact about {topic}. Start with "{hook}".
Include one shocking insight, one relatable example, and end with an uncomfortable truth. Format for short-form delivery (under 180 words).
Use high engagement language. Make it emotionally sticky.
""",

    "AI/Tech Hack Explainer": """
You're a digital creator exposing insane AI hacks. Write a script using the hook "{hook}" and explain a step-by-step process to use an AI tool for {topic}.
Use ultra-clear, rapid-fire delivery. Include shocking results, platform/tool names, and real-world application. Make it feel like you’re giving away a secret.
""",

    "Hidden Trend Reveal": """
You're a trend forecaster exposing viral shifts before they blow up. Start with "{hook}" and describe a trend from {topic}.
Explain why it's happening, who it affects, and what it means. Use pop culture references, bold claims, and emotional language. Finish with a prediction or callout.
"""
}

st.title("Faceless Script Machine")
st.markdown("Generate viral faceless video scripts with AI ✨")

# Inputs
topic = st.text_input("Enter your topic (e.g., AI side hustles):")
hook = st.text_input("Enter your hook (e.g., He made $500K flipping memes...):")
prompt_type = st.selectbox("Choose a prompt type:", list(prompt_templates.keys()))

generate = st.button("Generate Script")

if generate and topic and hook:
    prompt = prompt_templates[prompt_type].format(topic=topic, hook=hook)

    with st.spinner("Generating script..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a viral short-form scriptwriter."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=300
            )
            script = response["choices"][0]["message"]["content"]
            st.subheader("Generated Script")
            st.write(script)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Enter a topic and hook, then click Generate.")
