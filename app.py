import streamlit as st
from optimism_score import PmB, PmG, PvB, PvG, PsB, PsG, TotalB, TotalG, GB

# Load the questions
with open("questions.txt", "r") as f:
    lines = f.readlines()

# Process the questions and options
questions = []
for i in range(0, len(lines), 4):
    q = lines[i].strip().split(". ")[1]
    t = lines[i+1].strip()
    o1 = lines[i+2].strip().split(". ")[1]
    s1 = int(lines[i+2].strip().split(". ")[2])
    o2 = lines[i+3].strip().split(". ")[1]
    s2 = int(lines[i+3].strip().split(". ")[2])
    questions.append((q, t, o1, s1, o2, s2))

# Initialize the app state
if 'index' not in st.session_state:
    st.session_state.index = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'PmB': 0,
        'PmG': 0,
        'PvB': 0,
        'PvG': 0,
        'PsB': 0,
        'PsG': 0,
    }

# Define a function to show the current question
def show_question():
    if st.session_state.index < len(questions):
        q, t, o1, s1, o2, s2 = questions[st.session_state.index]
        st.write(q)
        col1, col2 = st.columns(2)
        if col1.button(o1):
            st.session_state.scores[t] += s1
            st.session_state.index += 1
        if col2.button(o2):
            st.session_state.scores[t] += s2
            st.session_state.index += 1
    else:
        st.write(f"Results")
        # st.write(st.session_state.scores)

        pmB = st.session_state.scores['PmB']
        pvB = st.session_state.scores['PvB']
        psB = st.session_state.scores['PsB']
        pmG = st.session_state.scores['PmG']
        pvG = st.session_state.scores['PvG']
        psG = st.session_state.scores['PsG']

        st.write(f"PmB: {PmB(pmB)} ({pmB})")
        st.write(f"PvB: {PvB(pvB)} ({pvB})")
        st.write(f"PsB: {PsB(psB)} ({psB})")
        st.write(f"PmG: {PmG(pmG)} ({pmG})")
        st.write(f"PvG: {PvG(pvG)} ({pvG})")
        st.write(f"PsG: {PsG(psG)} ({psG})")

        B = pmB + pvB + psB
        G = pmG + pvG + psG

        st.write(f"Total B: {TotalB(B)} ({B})")
        st.write(f"Total G: {TotalG(G)} ({G})")
    
        st.write(f"G - B: {GB(G, B)} ({G-B})")        

# Define the main app
def main():
    st.title('Optimism Assessment')
    show_question()
    
    if st.session_state.index < len(questions):
        st.write(f"Question {st.session_state.index + 1} of {len(questions)}")

    if st.session_state.index > 0:
        if st.button('Back'):
            st.session_state.index -= 1
            st.session_state.scores[questions[st.session_state.index][1]] = 0

# Run the app
if __name__ == '__main__':
    main()
