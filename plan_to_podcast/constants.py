import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# From: https://huggingface.co/spaces/hexgrad/Kokoro-TTS/blob/main/app.py
VOICES = {
    "🇺🇸 🚺 Heart ❤️": "af_heart",
    "🇺🇸 🚺 Bella 🔥": "af_bella",
    "🇺🇸 🚺 Nicole 🎧": "af_nicole",
    "🇺🇸 🚺 Aoede": "af_aoede",
    "🇺🇸 🚺 Kore": "af_kore",
    "🇺🇸 🚺 Sarah": "af_sarah",
    "🇺🇸 🚺 Nova": "af_nova",
    "🇺🇸 🚺 Sky": "af_sky",
    "🇺🇸 🚺 Alloy": "af_alloy",
    "🇺🇸 🚺 Jessica": "af_jessica",
    "🇺🇸 🚺 River": "af_river",
    "🇺🇸 🚹 Michael": "am_michael",
    "🇺🇸 🚹 Fenrir": "am_fenrir",
    "🇺🇸 🚹 Puck": "am_puck",
    "🇺🇸 🚹 Echo": "am_echo",
    "🇺🇸 🚹 Eric": "am_eric",
    "🇺🇸 🚹 Liam": "am_liam",
    "🇺🇸 🚹 Onyx": "am_onyx",
    "🇺🇸 🚹 Santa": "am_santa",
    "🇺🇸 🚹 Adam": "am_adam",
}

USAGE_NOTE = """
💡 Customize pronunciation with Markdown link syntax and /slashes/ like `[Kokoro](/kˈOkəɹO/)`
💬 To adjust intonation, try punctuation `;:,.!?—…"()“”` or stress `ˈ` and `ˌ`
⬇️ Lower stress `[1 level](-1)` or `[2 levels](-2)`
⬆️ Raise stress 1 level `[or](+2)` 2 levels (only works on less stressed, usually short words)
"""

BANNER_TEXT = """
# PLAN TO PODCAST
Generate a full podcast using local models.
This application uses Ollama and Kokoro TTS to generate realistic podcast episodes about any topic.
"""

EXAMPLES = {
    "Red Hat Enterprise Linux 🤠": {
        "topic": "Red Hat Enterprise Linux (RHEL)",
        "script": """<|Lily|>: Welcome to our podcast, where today we're diving into the world of Red Hat Enterprise Linux or RHEL for short. It's one of the most widely used enterprise-level operating systems in the business.

<|Marshall|>: So Lily, why is this particular version of Linux so popular among businesses? Isn't it just another flavor of Linux?

<|Lily|>: That's a great question Marshall. While RHEL shares its core with other varieties of Linux, what sets it apart is the support and stability that Red Hat provides. It's designed for mission-critical applications where downtime can't be an option.

<|Marshall|>: Ah, so it's about reliability and support then? What kind of support are we talking about here?

<|Lily|>: Absolutely. Red Hat offers comprehensive technical support for RHEL, including updates that address security vulnerabilities as well as bug fixes. This long-term support is crucial for businesses that need to maintain their systems over many years.

<|Marshall|>: And what about cost? I imagine this level of support doesn't come cheap?

<|Lily|>: You're right. RHEL is a commercial product, and there are subscription fees involved which can be substantial. However, many businesses see the investment as worthwhile given the peace of mind that comes with reliable enterprise-level support.

<|Marshall|>: Alright, so it's not just about the software itself but also what Red Hat brings to the table in terms of service and support. What else makes RHEL stand out?

<|Lily|>: RHEL is known for its stability and security features. It undergoes rigorous testing before release, ensuring that it's ready for production environments right from the start. Additionally, Red Hat focuses on integrating open-source technologies into RHEL in a way that makes them enterprise-ready.

<|Marshall|>: That sounds like a lot of value added to what might otherwise be free software. So, is there anything unique about how RHEL handles updates and changes compared to other Linux distributions?

<|Lily|>: Yes, RHEL follows a policy of maintaining backward compatibility with previous versions for a very long time. This means that once you've set up your systems on one version of RHEL, they'll continue to work even as new features and updates are rolled out.

<|Marshall|>: That's quite an advantage for businesses that need stability over innovation speed. Thanks for breaking down the key points about Red Hat Enterprise Linux today Lily!
""",
    },
    "Puppies 🐶": {
        "topic": """Topic: Puppies!
Key Points:
- Lily LOVES corgis, and thinks they are objectively the cutest!
- Marshall agrees corgis are the best, but he thinks pugs are a close second.""",
        "script": """<|Lily|>: Hello and welcome everyone, today we're talking about something that's universally loved: Puppies! I'm Lily, always excited to talk about anything cute.

<|Marshall|>: And I'm Marshall. While I can get behind the excitement around puppies, I do have a few questions for you Lily, especially since we're going to be talking about some specific breeds today.

<|Lily|>: Sure thing! What's on your mind?

<|Marshall|>: Well, I've heard you say before that corgis are the cutest puppies. Can we start with why you think that way? And is there any science to back up this claim?

<|Lily|>: Absolutely! When it comes to cuteness in puppies, and animals in general, scientists have found a few factors that make us go 'aww.' Large eyes relative to the size of their faces, a round head, and short limbs are all key. Corgis have these features in spades! Their big, expressive eyes, combined with those adorable stubby legs, just tickle our sense of cuteness.

<|Marshall|>: That's really interesting. So, if we're talking about other breeds that might come close to corgis in the 'cutest' category, what would you say? I've always had a soft spot for pugs myself.

<|Lily|>: Pugs are definitely up there! They have those big, round eyes and their squished faces give them an endearing look of perpetual surprise or curiosity. It's hard not to find that adorable. Plus, they're incredibly affectionate and make great companions.

<|Marshall|>: I couldn't agree more! Alright, so we've talked about corgis being the cutest puppies according to Lily, and pugs coming in as a close second. Any other interesting facts or tips for those considering adopting one of these adorable pups?

<|Lily|>: Absolutely! Both breeds have their unique personalities. Corgis are known for being intelligent and lively but can be stubborn at times, so they need a confident owner who's consistent with training. Pugs, on the other hand, are generally laid-back and great with families, though they do require careful monitoring around extreme temperatures due to their flat faces.

<|Marshall|>: Great points! And just remember folks, whichever breed you decide is cutest or best for your family, make sure it's a decision that considers both the needs of the puppy and the lifestyle of the owner. Thanks Lily for sharing all this information with us today!

<|Lily|>: My pleasure! And thanks to everyone out there for tuning in. Remember, no matter what breed you love, puppies are always worth a smile.""",
    },
}
