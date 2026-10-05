import streamlit as st
from PIL import Image
import re

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention

st.set_page_config(
    page_title="CaseFile AI",
    page_icon="🕵️"
)

st.title("🕵️ CaseFile AI")
st.caption("AI Based Mystery Evidence Analyzer")

st.write("📎 Upload an evidence image to start the investigation.")

file = st.file_uploader(
    "Upload Evidence",
    type=["jpg", "jpeg", "png"]
)


if file:
    image = Image.open(file)

    st.image(
        image,
        caption="Evidence Image",
        use_container_width=True
    )

    st.subheader("🔬 Forensic Scan")

    text = extract_text(image)

    if not text.strip():
        st.error("No readable text found.")
        st.stop()

    st.success("✅ Evidence text detected")

    words = re.findall(
        r"[A-Za-z]{3,}",
        text
    )

    words = list(dict.fromkeys(words))


    embeddings = create_embeddings(words)

    st.success("🧠 Evidence understood")

    scores = calculate_attention(embeddings)

    results = list(
        zip(words, scores)
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    st.divider()

    tab1, tab2, tab3 = st.tabs(
        ["📜 Evidence", "🔎 Clue Board", "🧠 AI Insight"]
    )

    with tab1:

        st.subheader("📜 Evidence Record")

        st.text_area(
            "Extracted Text",
            text,
            height=180
        )

        dates = re.findall(
            r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}",
            text
        )

        times = re.findall(
            r"\d{1,2}:\d{2}\s?(?:AM|PM)?",
            text,
            re.I
        )

        st.write("📅 Dates:", dates)
        st.write("⏰ Times:", times)

    with tab2:

        st.subheader("🔎 Clue Board")

        clue_words = [
            "missing", "suspect", "secret",
            "footprint", "phone", "message",
            "letter", "key", "door",
            "witness", "evidence",
            "unknown", "building"
        ]

        found = []

        for word in words:

            if word.lower() in clue_words:
                found.append(word)

        if found:

            for word in found[:5]:
                st.info("🔐 " + word)

        else:

            st.info("No special clue words found.")

    with tab3:

        st.subheader("🧠 AI Findings")

        for word, score in results[:5]:

            st.write(
                "🔎 **" + word + "**"
            )

        st.caption(
            "Higher attention means higher importance."
        )

    st.divider()

    st.subheader("🕵️ Investigation Result")

    st.success(
        "🔐 Strongest Clue: "
        + results[0][0]
    )

    st.success(
        "🎉 Coding Successfully Completed!"
    )

    st.caption(
        "OCR ✓  Embedding ✓  Attention ✓"
    )

else:

    st.info(
        "👆 Upload an evidence image to open the case."
    )