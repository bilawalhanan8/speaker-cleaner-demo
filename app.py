import streamlit as st

st.set_page_config(page_title="Speaker Cleaner — Free Online Tool", page_icon="🔊")

st.title("Speaker Cleaner — Free Online Tool")

st.markdown(
    'Try the free online tool here: <a href="https://speakercleaner.net" target="_blank">Speaker Cleaner</a>',
    unsafe_allow_html=True,
)

st.link_button("Open Speaker Cleaner", "https://speakercleaner.net")

st.write(
    "Speaker Cleaner is a free online speaker-cleaner tool for wet or muffled phone speakers. "
    "It helps remove trapped water, clear dust, and troubleshoot muffled or distorted audio."
)

st.header("💧 Water Ejection")
st.write(
    "If your phone speaker sounds muffled after rain, a splash, or being dropped in water, "
    "water may be trapped in the speaker grille. The tool plays special low-frequency tones "
    "and sound vibrations designed to push water out of the speaker. Turn the volume up, "
    "hold the phone speaker-side down, and let the sound run for a few cycles. Repeat until "
    "the audio sounds clear again."
)

st.header("🧹 Dust Clearing")
st.write(
    "Dust, lint, and pocket debris can build up in the speaker mesh and make sound quiet, "
    "muffled, or crackly. Gentle sound vibrations can help loosen dust, and a soft brush "
    "or a short burst of air can clear the grille. Do not poke sharp objects into the speaker."
)

st.header("🔧 Audio Troubleshooting")
st.write("Try these steps if your speaker still sounds quiet or distorted:")
st.write("1. Restart your phone and check the volume and mute settings.")
st.write("2. Remove the phone case and screen protector covering the speaker.")
st.write("3. Clean the speaker grille gently and run the water-ejection sound again.")
st.write("4. Test with music, a call on speakerphone, and a voice recording.")
st.write("5. If the problem continues, the speaker may need professional repair.")

st.header("How to Use the Free Tool")
st.write("1. Open the tool on your phone.")
st.write("2. Turn the volume to maximum.")
st.write("3. Play the speaker-cleaning sound.")
st.write("4. Repeat until the sound is clear.")

st.markdown(
    'Open the free tool: <a href="https://speakercleaner.net" target="_blank">Speaker Cleaner</a>',
    unsafe_allow_html=True,
)

st.caption("Demo app for Speaker Cleaner — a free online tool for water ejection, dust clearing, and audio troubleshooting.")
