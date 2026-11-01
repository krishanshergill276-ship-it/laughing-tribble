import streamlit as st

st.title("Anki Flashcards")

if "cards" not in st.session_state:
    st.session_state.cards = []

st.header("Create a flashcard")
question = st.text_input("Question")
answer = st.text_input("Answer")

if st.button("Add flashcard"):
    if question.strip() and answer.strip():
        st.session_state.cards.append(
            {"question": question.strip(), "answer": answer.strip()}
        )
        st.success("Flashcard added!")
    else:
        st.warning("Enter both a question and an answer.")

st.header("Practice")

if not st.session_state.cards:
    st.write("Create a flashcard above to get started.")
else:
    card_number = st.selectbox(
        "Choose a flashcard",
        range(len(st.session_state.cards)),
        format_func=lambda number: st.session_state.cards[number]["question"],
    )
    card = st.session_state.cards[card_number]

    st.write("**Question:**", card["question"])

    if st.button("Show answer"):
        st.write("**Answer:**", card["answer"])
