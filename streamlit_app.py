import streamlit as st

st.set_page_config(
    page_title="Molecular Decision Engine",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 Molecular Decision Engine")
st.write("Set your molecular priorities")

st.divider()

# -----------------------------
# USER PRIORITY SLIDERS
# -----------------------------

cell_penetration = st.slider(
    "Cell Penetration",
    0, 100, 70
)

reactivity = st.slider(
    "Reactivity",
    0, 100, 50
)

adaptability = st.slider(
    "Adaptability",
    0, 100, 80
)

target_specificity = st.slider(
    "Target Specificity",
    0, 100, 60
)

# -----------------------------
# MOLECULE DATABASE
# -----------------------------

molecules = {
    "Molecule A": {
        "Cell Penetration": 10,
        "Reactivity": 85,
        "Adaptability": 40,
        "Target Specificity": 70
    },

    "Molecule B": {
        "Cell Penetration": 30,
        "Reactivity": 25,
        "Adaptability": 90,
        "Target Specificity": 55
    },

    "Molecule C": {
        "Cell Penetration": 65,
        "Reactivity": 60,
        "Adaptability": 20,
        "Target Specificity": 95
    },

    "Molecule D": {
        "Cell Penetration": 90,
        "Reactivity": 40,
        "Adaptability": 65,
        "Target Specificity": 25
    }
}

# -----------------------------
# USER PRIORITIES
# -----------------------------

user_priorities = {
    "Cell Penetration": cell_penetration,
    "Reactivity": reactivity,
    "Adaptability": adaptability,
    "Target Specificity": target_specificity
}

# -----------------------------
# MATCHING ENGINE
# -----------------------------

scores = {}

for molecule, characteristics in molecules.items():

    total_difference = 0

    for characteristic in user_priorities:

        difference = abs(
            user_priorities[characteristic]
            - characteristics[characteristic]
        )

        total_difference += difference

    # Convert difference into a match percentage
    match_score = 100 - (total_difference / 4)

    scores[molecule] = match_score

# Find best molecule
best_molecule = max(scores, key=scores.get)
best_score = scores[best_molecule]

# -----------------------------
# SHOW RESULTS
# -----------------------------

st.divider()

st.subheader("Your selected priorities")

col1, col2 = st.columns(2)

with col1:
    st.metric("Cell Penetration", f"{cell_penetration}%")
    st.metric("Reactivity", f"{reactivity}%")

with col2:
    st.metric("Adaptability", f"{adaptability}%")
    st.metric("Target Specificity", f"{target_specificity}%")

st.divider()

st.subheader("🔎 Molecular Match")

st.success(
    f"Best molecular match: **{best_molecule}**"
)

st.metric(
    "Match Score",
    f"{best_score:.1f}%"
)

# -----------------------------
# SHOW ALL MOLECULES
# -----------------------------

st.write("### Comparison")

for molecule, score in sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
):

    st.write(
        f"**{molecule}** — {score:.1f}% match"
    )

st.divider()

st.caption(
    "The engine compares your priorities with the predefined "
    "characteristics of each molecule and selects the closest overall match."
)
