import streamlit as st

st.set_page_config(page_title="Class 12 Bio: Reproduction in Flowering Plants", layout="wide", page_icon="🌿")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Outfit:wght@300;400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif; color: #0d6e4a; }
.term { color: #0d6e4a; font-weight: 700; border-bottom: 2px dotted #1ecc87; cursor: help; }
.term:hover { background-color: #d0f5e5; }
.bio-card { background-color: #f0fdf4; border-left: 5px solid #1ecc87; padding: 15px; border-radius: 8px; margin-bottom: 15px; color: #0f1a0f; }
.diagram-box { background-color: #ffffff; border: 2px dashed #16a06a; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 15px; }
.streamlit-expanderHeader { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%) !important; color: #92400e !important; font-weight: 800 !important; border-radius: 8px !important; }
a.yt-link { display: inline-block; background-color: #be123c; color: white !important; padding: 10px 15px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 10px 0; transition: 0.2s; }
a.yt-link:hover { background-color: #9f1239; }
</style>
""", unsafe_allow_html=True)

st.title("🌿 Sexual Reproduction in Flowering Plants")
st.markdown("**Complete NCERT Study Guide + Allen NEET Trivia (Class 12 Biology Ch. 1)**")

def render_quiz(q_id, question, options, answer_idx, explanation):
    q = st.radio(question, options, key=q_id, index=None)
    if q == options[answer_idx]:
        st.success(f"✓ Correct! {explanation}")
    elif q is not None:
        st.error("✗ Incorrect.")

tabs = st.tabs(["Intro", "The Flower", "Stamen & Pollen", "Pistil & Ovule", "Pollination", "Fertilisation", "Seed & Embryo", "Apomixis"])

# --- TOPIC 1: INTRO ---
with tabs[0]:
    st.header("1. Introduction to Angiosperm Reproduction")
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Plants producing seeds within a fruit">Angiosperms</span> (flowering plants) show immense diversity in morphological structures, but all of them share a common feature: they reproduce sexually through flowers. 
    <br><br>
    The flower is fundamentally a <b>modified shoot</b>. The life cycle exhibits <b>Alternation of Generations</b> between a dominant diploid sporophyte and a highly reduced haploid gametophyte.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">NCERT Diagram: Life Cycle Overview</h4>
        <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 500px;">
          <rect x="50" y="50" width="100" height="40" rx="10" fill="#0d6e4a" />
          <text x="100" y="75" fill="#fff" text-anchor="middle">Sporophyte (2n)</text>
          <path d="M 160 70 L 220 70" stroke="#d97706" stroke-width="2" marker-end="url(#arrow1)"/>
          <rect x="230" y="50" width="100" height="40" rx="10" fill="#16a06a" />
          <text x="280" y="75" fill="#fff" text-anchor="middle">Flower</text>
          <path d="M 340 70 L 400 70" stroke="#d97706" stroke-width="2" marker-end="url(#arrow1)"/>
          <rect x="410" y="50" width="100" height="40" rx="10" fill="#1ecc87" />
          <text x="460" y="75" fill="#fff" text-anchor="middle">Gametes (n)</text>
          <defs><marker id="arrow1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#d97706"/></marker></defs>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Lifecycle Overview (Flowchart)")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#0d6e4a", fontcolor=white, fontname="Outfit"]
            "Sporophyte Plant Body (2n)" -> "Flower (Reproductive Organ)"
            "Flower (Reproductive Organ)" -> "Stamen (Male)" 
            "Flower (Reproductive Organ)" -> "Pistil (Female)"
            "Stamen (Male)" -> "Pollen Grains (n)" [label="Meiosis"]
            "Pistil (Female)" -> "Embryo Sac (n)" [label="Meiosis"]
            "Pollen Grains (n)" -> "Fertilisation"
            "Embryo Sac (n)" -> "Fertilisation"
            "Fertilisation" -> "Zygote (2n)" -> "Embryo" -> "Seed" -> "Sporophyte Plant Body (2n)"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Angiosperms are the only group showing **double fertilisation** — first discovered by S.G. Nawaschin (1898) in *Lilium* and *Fritillaria*.")
        st.write("- Term Angiosperm was coined by Paul Hermann (1690).")
        st.write("- The largest flower in the world is *Rafflesia* and the smallest is *Wolffia*.")
    
    st.markdown('<a href="https://www.youtube.com/results?search_query=sexual+reproduction+in+flowering+plants+class+12+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation on Intro & Life Cycle</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t1_q1", "1. Double fertilisation is a unique feature of:", ["Gymnosperms", "Angiosperms", "Bryophytes", "Pteridophytes"], 1, "Double fertilisation is unique to angiosperms (flowering plants).")
    render_quiz("t1_q2", "2. A flower is considered a modified:", ["Root", "Shoot", "Leaf", "Bud"], 1, "The flower is a modified shoot functioning as the reproductive unit.")
    render_quiz("t1_q3", "3. Which of the following generations is dominant in the life cycle of an angiosperm?", ["Haploid Gametophyte", "Diploid Sporophyte", "Triploid Endosperm", "None of the above"], 1, "The main plant body of an angiosperm is the diploid sporophyte.")

# --- TOPIC 2: THE FLOWER ---
with tabs[1]:
    st.header("2. Structure of a Typical Flower")
    st.markdown("""
    <div class="bio-card">
    A typical flower consists of 4 whorls on a receptacle (thalamus): Calyx (sepals), Corolla (petals), Androecium (stamens), and Gynoecium (pistil).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">NCERT Diagram: Parts of a Flower</h4>
        <svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 400px;">
          <path d="M150,180 L150,150" stroke="green" stroke-width="5"/>
          <ellipse cx="150" cy="150" rx="20" ry="10" fill="green"/>
          <path d="M130,150 Q100,100 130,80 Q150,120 150,150" fill="pink"/>
          <path d="M170,150 Q200,100 170,80 Q150,120 150,150" fill="pink"/>
          <rect x="145" y="80" width="10" height="70" fill="#6d28d9"/>
          <ellipse cx="150" cy="75" rx="8" ry="5" fill="#6d28d9"/>
          <text x="150" y="195" text-anchor="middle" font-size="12">Thalamus (Base), Pistil (Purple), Petals (Pink)</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Epigynous flower**: Ovary is inferior. Examples: Apple, Guava, Cucumber.")
        st.write("- **Perigynous flower**: Ovary is half-inferior. Examples: Rose, Plum, Peach.")
        st.write("- **Hypogynous flower**: Ovary is superior (most common). Examples: Mustard, China rose.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=flower+anatomy+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Anatomy of a Flower</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t2_q1", "1. Which of the following plants is dioecious?", ["Maize", "Coconut", "Papaya", "Castor"], 2, "Papaya and Date Palm are dioecious, meaning male and female flowers are on different plants.")
    render_quiz("t2_q2", "2. The essential whorls of a flower are:", ["Calyx and Corolla", "Androecium and Gynoecium", "Calyx and Androecium", "Corolla and Gynoecium"], 1, "Androecium and Gynoecium produce the gametes and are directly involved in reproduction.")
    render_quiz("t2_q3", "3. When both male and female flowers are present on the same plant, the plant is termed:", ["Dioecious", "Monoecious", "Hermaphrodite", "Polygamous"], 1, "Monoecious plants (like Maize and Castor) bear both male and female flowers on the same plant.")

# --- TOPIC 3: STAMEN & POLLEN ---
with tabs[2]:
    st.header("3. Stamen, Microsporogenesis & Pollen Grain")
    st.markdown("""
    <div class="bio-card">
    <b>The Stamen:</b> Consists of a filament and an anther. The anther is bilobed and tetrasporangiate. Through <span class="term" title="Formation of microspores from PMC via meiosis">microsporogenesis</span>, diploid pollen mother cells undergo meiosis to form haploid microspores, which develop into pollen grains.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">Allen Diagram: T.S of Anther</h4>
        <svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 400px;">
          <ellipse cx="150" cy="75" rx="80" ry="50" fill="#e8f5ee" stroke="#0d6e4a" stroke-width="2"/>
          <circle cx="110" cy="75" r="15" fill="#fbbf24"/>
          <circle cx="190" cy="75" r="15" fill="#fbbf24"/>
          <circle cx="150" cy="45" r="15" fill="#fbbf24"/>
          <circle cx="150" cy="105" r="15" fill="#fbbf24"/>
          <text x="150" y="145" text-anchor="middle" font-size="12">Tetrasporangiate Anther (4 Microsporangia)</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Microsporogenesis Flowchart")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#d97706", fontcolor=white, fontname="Outfit"]
            "Sporogenous Tissue" -> "Pollen Mother Cell (PMC) [2n]" -> "Meiosis I & II" -> "Microspore Tetrad" -> "Pollen Grains"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Tapetum** secretes enzymes, hormones, and pollenkitt (sticky substance).")
        st.write("- <span class='term' title='Highly resistant organic compound in pollen exine'>Sporopollenin</span> forms the exine. It cannot be degraded by any known enzyme. It is absent at germ pores.", unsafe_allow_html=True)
        st.write("- Over 60% of angiosperms shed pollen at the **2-celled stage**.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=microsporogenesis+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation of Microsporogenesis</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t3_q1", "1. The innermost nutritive layer of the anther wall is:", ["Epidermis", "Endothecium", "Middle layers", "Tapetum"], 3, "The Tapetum nourishes the developing microspores/pollen grains.")
    render_quiz("t3_q2", "2. Sporopollenin is a constituent of:", ["Exine of pollen grain", "Intine of pollen grain", "Pollen tube", "Seed coat"], 0, "Exine is made of sporopollenin, the most resistant organic material known.")
    render_quiz("t3_q3", "3. A typical angiosperm anther is called tetrasporangiate because it contains:", ["2 microsporangia", "4 microsporangia", "4 microspores", "4 pollen grains"], 1, "It is bilobed, and each lobe contains two microsporangia, making four in total.")

# --- TOPIC 4: PISTIL & OVULE ---
with tabs[3]:
    st.header("4. Pistil, Megasporangium (Ovule) & Embryo Sac")
    st.markdown("""
    <div class="bio-card">
    <b>The Ovule:</b> Attached to the placenta via a stalk called the <b>funicle</b>. The body of the ovule fuses with the funicle at the <b>hilum</b>. 
    <b>Megasporogenesis:</b> Formation of megaspores from the Megaspore Mother Cell (MMC) to form the Embryo Sac.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">NCERT Diagram: Anatropous Ovule</h4>
        <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px;">
          <ellipse cx="100" cy="100" rx="40" ry="60" fill="none" stroke="#16a06a" stroke-width="2"/>
          <ellipse cx="100" cy="100" rx="30" ry="50" fill="#d0f5e5" stroke="#0d6e4a" stroke-width="2"/>
          <ellipse cx="100" cy="90" rx="15" ry="25" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
          <text x="100" y="180" text-anchor="middle" font-size="12">Inverted Ovule (Micropyle near Funicle)</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Embryo Sac Formation Flowchart")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#6d28d9", fontcolor=white, fontname="Outfit"]
            "MMC (2n)" -> "Linear Tetrad (4 Megaspores)" -> "3 degenerate, 1 Functional" -> "Mitosis x3" -> "Mature Embryo Sac (7 cells, 8 nuclei)"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Mature Embryo Sac (Polygonum type):** Contains 7 cells and 8 nuclei.")
        st.write("- **Egg Apparatus:** 2 Synergids + 1 Egg cell (at micropylar end).")
        st.write("- The most common type of ovule in angiosperms is the **Anatropous** ovule (inverted).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=megasporogenesis+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation of the Ovule & Embryo Sac</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t4_q1", "1. The number of cells and nuclei in a mature embryo sac are respectively:", ["7 cells, 8 nuclei", "8 cells, 8 nuclei", "7 cells, 7 nuclei", "6 cells, 8 nuclei"], 0, "It contains 3 antipodals, 2 synergids, 1 egg cell, and 1 central cell with 2 polar nuclei.")
    render_quiz("t4_q2", "2. Filiform apparatus is a characteristic feature of:", ["Antipodal cells", "Egg cell", "Synergids", "Central cell"], 2, "It is located at the micropylar end of synergids to guide the pollen tube chemically.")
    render_quiz("t4_q3", "3. The basal part of the ovule is known as:", ["Micropyle", "Hilum", "Chalaza", "Funicle"], 2, "The chalaza represents the basal part of the ovule, opposite to the micropylar end.")

# --- TOPIC 5: POLLINATION ---
with tabs[4]:
    st.header("5. Pollination & Outbreeding Devices")
    st.markdown("""
    <div class="bio-card">
    Pollination is the transfer of pollen grains to the stigma. Xenogamy is the only type that brings genetically different pollen grains. Outbreeding devices discourage self-pollination.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">Allen Diagram: Agents of Pollination</h4>
        <svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 500px;">
          <rect x="20" y="20" width="80" height="40" fill="#bae6fd" rx="5"/>
          <text x="60" y="45" text-anchor="middle" font-size="12">Wind (Anemophily)</text>
          <rect x="110" y="20" width="80" height="40" fill="#fef9c3" rx="5"/>
          <text x="150" y="45" text-anchor="middle" font-size="12">Insects (Entomophily)</text>
          <rect x="200" y="20" width="80" height="40" fill="#ccfbf1" rx="5"/>
          <text x="240" y="45" text-anchor="middle" font-size="12">Water (Hydrophily)</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Cleistogamous flowers:** Never open, ensuring obligate autogamy (e.g., *Viola*, *Oxalis*).")
        st.write("- **Hydrophily:** In *Zostera* (submerged pollination), pollen is long and ribbon-like without sporopollenin.")
        st.write("- **Entomophily:** Flowers are large, colorful, and rich in nectar. Pollen is sticky (pollenkitt).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=pollination+in+flowering+plants+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation on Pollination</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t5_q1", "1. Which of the following flowers shows cleistogamy?", ["Salvia", "Viola", "Vallisneria", "Maize"], 1, "Viola (common pansy), Oxalis, and Commelina produce cleistogamous flowers.")
    render_quiz("t5_q2", "2. In Zostera, pollination occurs via:", ["Wind", "Insects", "Submerged water", "Surface water"], 2, "Zostera uses hypohydrophily (submerged water pollination).")
    render_quiz("t5_q3", "3. A genetic mechanism that prevents self-pollen from fertilizing the ovules is:", ["Dichogamy", "Herkogamy", "Self-incompatibility", "Heterostyly"], 2, "Self-incompatibility prevents inbreeding.")

# --- TOPIC 6: FERTILISATION ---
with tabs[5]:
    st.header("6. Pollen-Pistil Interaction & Double Fertilisation")
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Syngamy + Triple fusion occurring in the same embryo sac">Double fertilisation</span> involves:
    1. <b>Syngamy:</b> Male gamete + Egg cell = Zygote (2n).
    2. <b>Triple Fusion:</b> Male gamete + 2 Polar nuclei = Primary Endosperm Nucleus (3n).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">NCERT Diagram: Double Fertilisation</h4>
        <svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 400px;">
          <ellipse cx="150" cy="75" rx="50" ry="70" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
          <path d="M 50 130 L 120 130" stroke="green" stroke-width="3" stroke-dasharray="4"/>
          <text x="80" y="125" font-size="10">Pollen tube</text>
          <circle cx="150" cy="115" r="8" fill="red"/>
          <text x="170" y="120" font-size="10">Syngamy (Zygote)</text>
          <circle cx="150" cy="75" r="10" fill="blue"/>
          <text x="170" y="80" font-size="10">Triple Fusion (PEN)</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Double Fertilisation Flowchart")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#0369a1", fontcolor=white, fontname="Outfit"]
            "Pollen Tube enters Synergid" -> "Releases 2 Male Gametes (n)"
            "Releases 2 Male Gametes (n)" -> "Fuses with Egg Cell [Syngamy]"
            "Releases 2 Male Gametes (n)" -> "Fuses with 2 Polar Nuclei [Triple Fusion]"
            "Fuses with Egg Cell [Syngamy]" -> "Zygote (2n)" -> "Embryo"
            "Fuses with 2 Polar Nuclei [Triple Fusion]" -> "PEN (3n)" -> "Endosperm"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Porogamy:** Pollen tube enters through micropyle (most common).")
        st.write("- **Chalazogamy:** Pollen tube enters through chalaza (e.g., *Casuarina*).")
        st.write("- Double fertilisation is unique to angiosperms.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=double+fertilisation+in+angiosperms+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation of Double Fertilisation</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t6_q1", "1. The ploidy of endosperm in typical angiosperms is:", ["Haploid (n)", "Diploid (2n)", "Triploid (3n)", "Tetraploid (4n)"], 2, "PEN is formed from the fusion of one male gamete (n) and two polar nuclei (n+n).")
    render_quiz("t6_q2", "2. Double fertilisation was first observed by Nawaschin in:", ["Lilium and Fritillaria", "Rosa and Hibiscus", "Triticum and Oryza", "Capsella"], 0, "S.G. Nawaschin discovered double fertilisation in Lilium and Fritillaria in 1898.")
    render_quiz("t6_q3", "3. Pollen tube entry into the ovule through the integuments is known as:", ["Porogamy", "Chalazogamy", "Mesogamy", "Syngamy"], 2, "Mesogamy is entry through the middle/integuments.")

# --- TOPIC 7: SEED & EMBRYO ---
with tabs[6]:
    st.header("7. Endosperm, Embryo Development & Seed")
    st.markdown("""
    <div class="bio-card">
    The zygote develops into the embryo and PEN into endosperm. The ovules mature into seeds and the ovary into a fruit. The endosperm may be completely consumed (ex-albuminous) or persist (albuminous).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">Allen Diagram: Dicot vs Monocot Embryo</h4>
        <svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 400px;">
          <rect x="50" y="20" width="80" height="60" fill="#a3e635" rx="5"/>
          <text x="90" y="55" text-anchor="middle" font-size="12">Dicot (2 Cotyledons)</text>
          <rect x="170" y="20" width="80" height="60" fill="#fed7aa" rx="5"/>
          <text x="210" y="55" text-anchor="middle" font-size="12">Monocot (Scutellum)</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Perisperm:** Remnants of the nucellus are persistent in black pepper and beet.")
        st.write("- **Scutellum:** Single shield-shaped cotyledon in monocots.")
        st.write("- **Parthenocarpy:** Fruit development without fertilisation (e.g., banana).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=seed+development+and+germination+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation of Seed Development</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t7_q1", "1. Coconut water represents which type of endosperm?", ["Free-nuclear", "Cellular", "Helobial", "Ruminate"], 0, "The liquid part of a young coconut is thousands of free nuclei.")
    render_quiz("t7_q2", "2. In a monocot seed, the radicle is enclosed in a protective sheath called:", ["Coleoptile", "Coleorhiza", "Scutellum", "Epiblast"], 1, "The radicle is covered by coleorhiza, while the plumule is covered by coleoptile.")
    render_quiz("t7_q3", "3. A fruit developed from a flower without fertilisation is called:", ["Parthenogenetic", "Parthenocarpic", "Apomictic", "Polyembryonic"], 1, "Parthenocarpic fruits (like bananas) develop without fertilisation and are naturally seedless.")

# --- TOPIC 8: APOMIXIS ---
with tabs[7]:
    st.header("8. Apomixis and Polyembryony")
    st.markdown("""
    <div class="bio-card">
    <b>Apomixis:</b> A form of asexual reproduction that mimics sexual reproduction, where seeds are formed without fertilisation. 
    <b>Polyembryony:</b> The occurrence of more than one embryo in a seed.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#0d6e4a;">Allen Diagram: Types of Apomixis</h4>
        <svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 500px;">
          <rect x="20" y="20" width="80" height="60" fill="#ede9fe" rx="5"/>
          <text x="60" y="55" text-anchor="middle" font-size="12">Diplospory</text>
          <rect x="110" y="20" width="80" height="60" fill="#fef3c7" rx="5"/>
          <text x="150" y="55" text-anchor="middle" font-size="12">Apospory</text>
          <rect x="200" y="20" width="80" height="60" fill="#fce7f3" rx="5"/>
          <text x="240" y="50" text-anchor="middle" font-size="10">Adventive</text>
          <text x="240" y="65" text-anchor="middle" font-size="10">Embryony</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Apomixis avoids meiosis and syngamy, resulting in clones.")
        st.write("- **Nucellar Polyembryony:** Adventive embryony where sporophytic cells (nucellus) directly form embryos (seen in *Citrus*, *Opuntia*).")
        st.write("- Polyembryony in Citrus was first reported by Antonie van Leeuwenhoek (1719).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=apomixis+and+polyembryony+class+12" target="_blank" class="yt-link">🎥 Watch Explainer on Apomixis</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t8_q1", "1. What is the main agricultural significance of apomixis?", ["Increases genetic variation", "Maintains hybrid vigour across generations", "Produces polyploid plants", "Promotes cross-pollination"], 1, "It helps fix hybrid characteristics across generations since it does not involve genetic segregation.")
    render_quiz("t8_q2", "2. Polyembryony through adventive embryony is most commonly seen in:", ["Wheat", "Orchids", "Citrus", "Pea"], 2, "Citrus seeds often contain multiple embryos originating from nucellar cells.")
    render_quiz("t8_q3", "3. Apomixis in plants is functionally a type of:", ["Sexual reproduction", "Asexual reproduction", "Vegetative propagation only", "Cross-pollination"], 1, "It mimics sexual reproduction (produces seeds) but is actually asexual because no fertilisation occurs.")

st.sidebar.markdown("### Guide Settings")
st.sidebar.info("Developed with Streamlit. Navigate through the detailed topics above.")
