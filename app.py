import streamlit as st

st.set_page_config(page_title="Class 12 Bio: Reproduction in Flowering Plants", layout="wide", page_icon="🌿")

# Custom CSS for colorful presentation and typography
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #0d6e4a;
}

/* Custom Term Highlighting */
.term {
    color: #0d6e4a;
    font-weight: 700;
    border-bottom: 2px dotted #1ecc87;
    cursor: help;
}
.term:hover {
    background-color: #d0f5e5;
}

/* Custom Card */
.bio-card {
    background-color: #f0fdf4;
    border-left: 5px solid #1ecc87;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 15px;
    color: #0f1a0f;
}

/* Trivia Header */
.streamlit-expanderHeader {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%) !important;
    color: #92400e !important;
    font-weight: 800 !important;
    border-radius: 8px !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🌿 Sexual Reproduction in Flowering Plants")
st.markdown("**Complete NCERT Study Guide + Allen NEET Trivia (Class 12 Biology Ch. 1)**")

# Define Data
topics = [
    "Intro", "The Flower", "Stamen & Pollen", "Pistil & Ovule", 
    "Pollination", "Fertilisation", "Seed & Embryo", "Apomixis"
]

tabs = st.tabs(topics)

# --- TOPIC 1: INTRO ---
with tabs[0]:
    st.header("Introduction to Angiosperm Reproduction")
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Flowering plants that produce seeds enclosed within a fruit">Angiosperms</span> reproduce sexually via the flower. 
    The flower is a modified shoot functioning as a reproductive organ. It contains the essential and non-essential whorls.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Lifecycle Overview")
    st.markdown("Sporophyte (2n) ➡️ Flower ➡️ Gametes (n)")
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Angiosperms are the only group showing **double fertilisation** — first discovered by Nawaschin (1898).")
        st.write("- Term Angiosperm coined by Paul Hermann (1690).")
    
    st.video("https://www.youtube.com/watch?v=HLYPm2idSTE") # Placeholder for relevant 3D animation
    
    st.subheader("Practice Questions (PYQ)")
    q1 = st.radio("1. Double fertilisation is a unique feature of:", ["Gymnosperms", "Angiosperms", "Bryophytes", "Pteridophytes"], key="q1_1")
    if q1 == "Angiosperms":
        st.success("✓ Correct! Double fertilisation is unique to angiosperms.")
    elif q1:
        st.error("✗ Incorrect.")

# --- TOPIC 2: THE FLOWER ---
with tabs[1]:
    st.header("Structure of a Typical Flower")
    st.markdown("""
    <div class="bio-card">
    A typical flower consists of 4 whorls on a receptacle (thalamus): Calyx (sepals), Corolla (petals), Androecium (stamens), and Gynoecium (pistil).
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Epigynous flower**: ovary inferior (apple, guava).")
        st.write("- **Perigynous**: ovary half-inferior (rose, plum).")
        
    st.video("https://www.youtube.com/watch?v=SiFaB1MZ1Yw")
    
    st.subheader("Practice Questions (PYQ)")
    q2 = st.radio("1. Which of the following is dioecious?", ["Maize", "Coconut", "Papaya", "Castor"], key="q2_1")
    if q2 == "Papaya":
        st.success("✓ Correct! Papaya has male and female flowers on different plants.")
    elif q2:
        st.error("✗ Incorrect.")

# --- TOPIC 3: STAMEN & POLLEN ---
with tabs[2]:
    st.header("Stamen, Microsporogenesis & Pollen Grain")
    st.markdown("""
    <div class="bio-card">
    The stamen consists of the filament and the anther. The anther is bilobed and tetrasporangiate. Through <span class="term" title="Formation of microspores from PMC via meiosis">microsporogenesis</span>, diploid pollen mother cells undergo meiosis to form haploid microspores, which develop into pollen grains.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Tapetum** provides sporopollenin precursors and pollenkitt.")
        st.markdown('- <span class="term" title="Highly resistant organic compound in pollen exine">Sporopollenin</span> is absent at the germ pores.', unsafe_allow_html=True)
        st.write("- Pollen viability ranges from 30 mins (rice) to months (Rosaceae).")
        
    st.video("https://www.youtube.com/watch?v=B1B3h-L-l4M")
    
    st.subheader("Practice Questions (PYQ)")
    q3 = st.radio("1. The innermost nutritive layer of the anther wall is:", ["Epidermis", "Endothecium", "Middle layers", "Tapetum"], key="q3_1")
    if q3 == "Tapetum":
        st.success("✓ Correct! Tapetum nourishes developing pollen grains.")
    elif q3:
        st.error("✗ Incorrect.")

# --- TOPIC 4: PISTIL & OVULE ---
with tabs[3]:
    st.header("Pistil, Ovule & Megasporogenesis")
    st.markdown("""
    <div class="bio-card">
    The pistil comprises stigma, style, and ovary. The ovary contains ovules. The process of formation of megaspores from the MMC is <span class="term" title="Formation of megaspores from MMC via meiosis">megasporogenesis</span>.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Embryo sac has 7 cells and 8 nuclei (Polygonum type).")
        st.write("- Synergids have filiform apparatus to guide pollen tubes.")
        st.write("- Most common ovule in angiosperms is Anatropous.")
        
    st.subheader("Practice Questions (PYQ)")
    q4 = st.radio("1. Filiform apparatus is characteristic of:", ["Antipodals", "Egg cell", "Synergids", "Central cell"], key="q4_1")
    if q4 == "Synergids":
        st.success("✓ Correct! It is located at the micropylar end of synergids to guide the pollen tube.")
    elif q4:
        st.error("✗ Incorrect.")

# --- TOPIC 5: POLLINATION ---
with tabs[4]:
    st.header("Pollination & Outbreeding Devices")
    st.markdown("""
    <div class="bio-card">
    Pollination is the transfer of pollen from anther to stigma. Outbreeding devices prevent self-pollination.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Cleistogamy** (flowers never open) ensures obligate autogamy.")
        st.write("- **Zostera** (sea grass) undergoes hypohydrophily.")
        st.write("- Yucca plant and Pronuba moth have an obligate mutualistic relationship.")
        
    st.subheader("Practice Questions (PYQ)")
    q5 = st.radio("1. Which flower shows cleistogamy?", ["Salvia", "Viola", "Vallisneria", "Maize"], key="q5_1")
    if q5 == "Viola":
        st.success("✓ Correct! Viola, Oxalis, and Commelina produce cleistogamous flowers.")
    elif q5:
        st.error("✗ Incorrect.")

# --- TOPIC 6: FERTILISATION ---
with tabs[5]:
    st.header("Pollen-Pistil Interaction & Double Fertilisation")
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Syngamy + Triple fusion occurring in the same embryo sac">Double fertilisation</span> involves syngamy and triple fusion.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Triple fusion yields the Primary Endosperm Nucleus (3n).")
        st.write("- Gymnosperms do not exhibit double fertilisation.")
        
    st.subheader("Practice Questions (PYQ)")
    q6 = st.radio("1. The ploidy of endosperm in typical angiosperms is:", ["Haploid (n)", "Diploid (2n)", "Triploid (3n)", "Tetraploid (4n)"], key="q6_1")
    if q6 == "Triploid (3n)":
        st.success("✓ Correct! It forms from the fusion of one male gamete and two polar nuclei.")
    elif q6:
        st.error("✗ Incorrect.")

# --- TOPIC 7: SEED & EMBRYO ---
with tabs[6]:
    st.header("Seed and Embryo Development")
    st.markdown("""
    <div class="bio-card">
    Post-fertilisation, the zygote develops into the embryo and PEN into endosperm.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Scutellum** is the single shield-shaped cotyledon in monocots.")
        st.write("- Coconut water represents free-nuclear endosperm.")
        st.write("- Parthenocarpy is fruit formation without fertilisation.")
        
    st.subheader("Practice Questions (PYQ)")
    q7 = st.radio("1. Coconut water represents which type of endosperm?", ["Free-nuclear", "Cellular", "Helobial", "Ruminate"], key="q7_1")
    if q7 == "Free-nuclear":
        st.success("✓ Correct! The liquid part is free-nuclear.")
    elif q7:
        st.error("✗ Incorrect.")

# --- TOPIC 8: APOMIXIS ---
with tabs[7]:
    st.header("Apomixis and Polyembryony")
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Production of seeds without fertilisation">Apomixis</span> is a form of asexual reproduction that mimics sexual reproduction.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Polyembryony in Citrus was discovered by Leeuwenhoek.")
        st.write("- Apomixis is agriculturally significant for maintaining hybrid vigour without buying new seeds.")
        
    st.subheader("Practice Questions (PYQ)")
    q8 = st.radio("1. What is the agricultural significance of apomixis?", ["Increases genetic variation", "Maintains hybrid vigour", "Produces polyploid plants", "Promotes cross-pollination"], key="q8_1")
    if q8 == "Maintains hybrid vigour":
        st.success("✓ Correct! It helps fix hybrid characteristics across generations.")
    elif q8:
        st.error("✗ Incorrect.")

st.sidebar.markdown("### Guide Settings")
st.sidebar.info("Developed with Streamlit. Use the tabs above to navigate topics.")
