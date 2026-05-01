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
    The flower is fundamentally a <b>modified shoot</b>, meaning it is a specialized stem where leaves are modified into floral whorls (sepals, petals, stamens, and carpels). These structures facilitate the processes of pollination and fertilization, ensuring the continuity of the species. The life cycle exhibits <b>Alternation of Generations</b> between a dominant diploid sporophyte and a highly reduced haploid gametophyte.
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
    A flower is the reproductive unit in angiosperms. It is meant for sexual reproduction. A typical flower has four different kinds of whorls arranged successively on the swollen end of the stalk or pedicel, called the <b>thalamus or receptacle</b>.
    <br><br>
    <b>1. Accessory Whorls (Non-essential):</b><br>
    - <b>Calyx (Sepals):</b> Outermost whorl, usually green, protects the flower in the bud stage.<br>
    - <b>Corolla (Petals):</b> Brightly colored to attract insects for pollination.
    <br><br>
    <b>2. Essential Whorls (Reproductive):</b><br>
    - <b>Androecium (Stamens):</b> Male reproductive organ.<br>
    - <b>Gynoecium (Carpels/Pistil):</b> Female reproductive organ.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Epigynous flower**: Ovary is inferior. The thalamus encloses the ovary completely. Examples: Apple, Guava, Cucumber.")
        st.write("- **Perigynous flower**: Ovary is half-inferior. Examples: Rose, Plum, Peach.")
        st.write("- **Hypogynous flower**: Ovary is superior (most common). Examples: Mustard, China rose.")
        st.write("- Flowers lacking either stamens or carpels are termed **Unisexual** (e.g., Papaya).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=flower+anatomy+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Anatomy of a Flower</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t2_q1", "1. Which of the following plants is dioecious (bearing unisexual flowers on separate plants)?", ["Maize", "Coconut", "Papaya", "Castor"], 2, "Papaya and Date Palm are dioecious, meaning male and female flowers are on different plants.")
    render_quiz("t2_q2", "2. The essential whorls of a flower are:", ["Calyx and Corolla", "Androecium and Gynoecium", "Calyx and Androecium", "Corolla and Gynoecium"], 1, "Androecium and Gynoecium produce the gametes and are directly involved in reproduction.")
    render_quiz("t2_q3", "3. When both male and female flowers are present on the same plant, the plant is termed:", ["Dioecious", "Monoecious", "Hermaphrodite", "Polygamous"], 1, "Monoecious plants (like Maize and Castor) bear both male and female flowers on the same plant.")

# --- TOPIC 3: STAMEN & POLLEN ---
with tabs[2]:
    st.header("3. Stamen, Microsporogenesis & Pollen Grain")
    st.markdown("""
    <div class="bio-card">
    <b>The Stamen:</b> Consists of a long, slender stalk called the <b>filament</b>, and a terminal, generally bilobed structure called the <b>anther</b>. A typical angiosperm anther is bilobed with each lobe having two theca (dithecous). Hence, it is a four-sided (tetragonal) structure consisting of four microsporangia.
    <br><br>
    <b>Structure of Microsporangium (Anther Wall):</b><br>
    1. Epidermis (outermost protective layer)<br>
    2. Endothecium (helps in anther dehiscence)<br>
    3. Middle layers (ephemeral)<br>
    4. <b>Tapetum:</b> Innermost layer. It provides nourishment to developing pollen grains.
    <br><br>
    <b>Microsporogenesis:</b> The process of formation of microspores from a Pollen Mother Cell (PMC) through meiosis. The microspores are arranged in a cluster of four (microspore tetrad). As the anther matures and dehydrates, the microspores dissociate and develop into <b>pollen grains (male gametophyte)</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Microsporogenesis Flowchart")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#d97706", fontcolor=white, fontname="Outfit"]
            "Sporogenous Tissue in Anther" -> "Pollen Mother Cell (PMC) [2n]"
            "Pollen Mother Cell (PMC) [2n]" -> "Meiosis I & II"
            "Meiosis I & II" -> "Microspore Tetrad (4 haploid cells)"
            "Microspore Tetrad (4 haploid cells)" -> "Dissociation & Maturation" -> "Pollen Grains (Male Gametophyte)"
            "Pollen Grains (Male Gametophyte)" -> "Vegetative Cell (Large)"
            "Pollen Grains (Male Gametophyte)" -> "Generative Cell (Small, divides into 2 male gametes)"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Tapetum** secretes enzymes, hormones, and pollenkitt (sticky substance in insect-pollinated flowers). It also secretes Ubisch bodies.")
        st.write("- <span class='term' title='Highly resistant organic compound in pollen exine'>Sporopollenin</span> forms the exine. It cannot be degraded by any known enzyme, acid, or high temperature. It is absent at the germ pores.", unsafe_allow_html=True)
        st.write("- Over 60% of angiosperms shed pollen at the **2-celled stage** (vegetative + generative cell). In the remaining, the generative cell divides to form 2 male gametes, shedding at the **3-celled stage**.")
        st.write("- Severe pollen allergies (asthma, bronchitis) are caused by *Parthenium* (carrot grass).")
        
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
    <b>The Pistil (Gynoecium):</b> Represents the female reproductive part. It consists of the stigma (landing platform for pollen), style (elongated tube), and ovary (basal swollen part containing ovules).
    <br><br>
    <b>The Ovule (Megasporangium):</b> Attached to the placenta via a stalk called the <b>funicle</b>. The body of the ovule fuses with the funicle at the <b>hilum</b>. It has protective envelopes called <b>integuments</b> which enclose the <b>nucellus</b> (mass of cells with abundant food reserve). The small opening at the tip is the <b>micropyle</b>, and the basal part is the <b>chalaza</b>.
    <br><br>
    <b>Megasporogenesis:</b> Formation of megaspores from the Megaspore Mother Cell (MMC). The MMC undergoes meiosis to form 4 megaspores. Usually, the upper 3 degenerate, and the lowermost functional megaspore develops into the female gametophyte (Embryo Sac). This method of embryo sac formation from a single megaspore is termed <b>monosporic development</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Embryo Sac Formation Flowchart")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#6d28d9", fontcolor=white, fontname="Outfit"]
            "Megaspore Mother Cell (2n) in Nucellus" -> "Meiosis"
            "Meiosis" -> "Linear Tetrad of 4 Megaspores (n)"
            "Linear Tetrad of 4 Megaspores (n)" -> "3 degenerate, 1 Functional Megaspore (Chalazal end)"
            "1 Functional Megaspore" -> "Mitosis 1 (2 Nuclei)" -> "Mitosis 2 (4 Nuclei)" -> "Mitosis 3 (8 Nuclei)"
            "8 Nucleate Stage" -> "Cell Wall Formation" -> "Mature Embryo Sac (7 cells, 8 nuclei)"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Mature Embryo Sac (Polygonum type):** Contains 7 cells and 8 nuclei.")
        st.write("- **Egg Apparatus:** 2 Synergids + 1 Egg cell (at micropylar end).")
        st.write("- **Antipodals:** 3 cells at the chalazal end.")
        st.write("- **Central Cell:** Largest cell, contains 2 polar nuclei.")
        st.write("- **Filiform apparatus** in synergids has finger-like cellular thickenings that chemically guide the pollen tube entry into the synergid.")
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
    <b>Pollination</b> is the mechanism to achieve the transfer of pollen grains to the stigma. 
    <br><br>
    <b>Types of Pollination:</b><br>
    1. <b>Autogamy:</b> Transfer of pollen to the stigma of the <i>same</i> flower. Requires synchrony in pollen release and stigma receptivity (e.g., Pea, Wheat).<br>
    2. <b>Geitonogamy:</b> Transfer of pollen to the stigma of <i>another flower of the same plant</i>. Functionally cross-pollination, but genetically similar to autogamy.<br>
    3. <b>Xenogamy:</b> Transfer of pollen to the stigma of a <i>different plant</i>. Only type that brings genetically different pollen grains (genetic variation).
    <br><br>
    <b>Outbreeding Devices:</b> Continuous self-pollination results in <b>inbreeding depression</b>. Plants developed mechanisms to discourage self-pollination, such as non-synchronization of pollen release and stigma receptivity (dichogamy), different positions of anther and stigma (herkogamy), self-incompatibility (genetic mechanism), and producing unisexual flowers.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Cleistogamous flowers:** Never open, ensuring obligate autogamy (e.g., *Viola*, *Oxalis*, *Commelina*). Advantage: Assured seed set even without pollinators.")
        st.write("- **Chasmogamous flowers:** Normal open flowers with exposed anthers and stigma.")
        st.write("- **Anemophily (Wind):** Pollen is light and non-sticky; stigma is large and feathery. Often have a single ovule per ovary (e.g., Grasses, Corn cob).")
        st.write("- **Hydrophily (Water):** Very rare (only ~30 genera, mostly monocots). In *Vallisneria* (surface pollination), female flower reaches surface. In *Zostera* (submerged pollination), pollen is long and ribbon-like without sporopollenin.")
        st.write("- **Entomophily (Insects):** Flowers are large, colorful, fragrant, and rich in nectar. Pollen is sticky (pollenkitt).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=pollination+in+flowering+plants+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation on Pollination Mechanisms</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t5_q1", "1. Which of the following flowers shows cleistogamy?", ["Salvia", "Viola", "Vallisneria", "Maize"], 1, "Viola (common pansy), Oxalis, and Commelina produce cleistogamous flowers which never open.")
    render_quiz("t5_q2", "2. In Zostera, pollination occurs via:", ["Wind", "Insects", "Submerged water", "Surface water"], 2, "Zostera uses hypohydrophily (submerged water pollination); pollen grains are long and ribbon-like.")
    render_quiz("t5_q3", "3. A genetic mechanism that prevents self-pollen from fertilizing the ovules is called:", ["Dichogamy", "Herkogamy", "Self-incompatibility", "Heterostyly"], 2, "Self-incompatibility is a genetically controlled mechanism that rejects self-pollen to prevent inbreeding.")

# --- TOPIC 6: FERTILISATION ---
with tabs[5]:
    st.header("6. Pollen-Pistil Interaction & Double Fertilisation")
    st.markdown("""
    <div class="bio-card">
    <b>Pollen-Pistil Interaction:</b> A dynamic process involving pollen recognition followed by promotion or inhibition of pollen. If compatible, the pollen grain germinates on the stigma to produce a pollen tube through one of the germ pores. The contents of the pollen grain move into the tube, which grows through the tissues of the stigma and style and reaches the ovary. It enters the ovule through the micropyle and then enters one of the synergids through the filiform apparatus.
    <br><br>
    <b>Double Fertilisation:</b> Once inside the synergid, the pollen tube releases two male gametes into the cytoplasm of the synergid.<br>
    1. <b>Syngamy:</b> One male gamete (n) moves towards the egg cell (n) and fuses with its nucleus. This completes syngamy, resulting in a diploid <b>Zygote (2n)</b>, which will develop into an embryo.<br>
    2. <b>Triple Fusion:</b> The other male gamete (n) moves towards the two polar nuclei (n+n) located in the central cell and fuses with them to produce a triploid <b>Primary Endosperm Nucleus (PEN, 3n)</b>. As this involves the fusion of three haploid nuclei, it is termed triple fusion.
    <br><br>
    Since two types of fusions (syngamy and triple fusion) take place in an embryo sac, the phenomenon is termed <b>Double Fertilisation</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Double Fertilisation Flowchart")
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#0369a1", fontcolor=white, fontname="Outfit"]
            "Pollen Tube enters Synergid" -> "Releases 2 Male Gametes (n)"
            "Releases 2 Male Gametes (n)" -> "Male Gamete 1"
            "Releases 2 Male Gametes (n)" -> "Male Gamete 2"
            
            "Male Gamete 1" -> "Fuses with Egg Cell (n) [Syngamy]"
            "Fuses with Egg Cell (n) [Syngamy]" -> "Zygote (2n)" -> "Embryo"
            
            "Male Gamete 2" -> "Fuses with 2 Polar Nuclei (n+n) [Triple Fusion]"
            "Fuses with 2 Polar Nuclei (n+n) [Triple Fusion]" -> "Primary Endosperm Nucleus (PEN, 3n)" -> "Endosperm"
        }
    ''')
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Porogamy:** Pollen tube enters through micropyle (most common).")
        st.write("- **Chalazogamy:** Pollen tube enters through chalaza (e.g., *Casuarina*).")
        st.write("- **Mesogamy:** Pollen tube enters through integuments (e.g., Cucurbita).")
        st.write("- Double fertilisation is unique to angiosperms. Gymnosperms do not exhibit this (their endosperm is haploid and pre-fertilisation).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=double+fertilisation+in+angiosperms+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation of Double Fertilisation</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t6_q1", "1. The ploidy of endosperm in typical angiosperms is:", ["Haploid (n)", "Diploid (2n)", "Triploid (3n)", "Tetraploid (4n)"], 2, "PEN is formed from the fusion of one male gamete (n) and two polar nuclei (n+n), making it 3n.")
    render_quiz("t6_q2", "2. Double fertilisation was first observed by Nawaschin in:", ["Lilium and Fritillaria", "Rosa and Hibiscus", "Triticum and Oryza", "Capsella"], 0, "S.G. Nawaschin discovered double fertilisation in Lilium and Fritillaria in 1898.")
    render_quiz("t6_q3", "3. Pollen tube entry into the ovule through the integuments is known as:", ["Porogamy", "Chalazogamy", "Mesogamy", "Syngamy"], 2, "Mesogamy is entry through the middle/integuments. Porogamy is through micropyle. Chalazogamy is through chalaza.")

# --- TOPIC 7: SEED & EMBRYO ---
with tabs[6]:
    st.header("7. Endosperm, Embryo Development & Seed")
    st.markdown("""
    <div class="bio-card">
    <b>Endosperm Development:</b> Precedes embryo development because it provides assured nutrition to the developing embryo. The PEN undergoes successive nuclear divisions to give rise to free nuclei (Free-nuclear endosperm, e.g., coconut water). Subsequently, cell wall formation occurs, making it a cellular endosperm (e.g., white coconut meat).
    <br><br>
    <b>Embryo Development (Embryogeny):</b> Develops at the micropylar end of the embryo sac where the zygote is situated. Zygote gives rise to the proembryo, followed by the globular, heart-shaped, and mature embryo.
    <br><br>
    <b>The Seed:</b> The final product of sexual reproduction. Fertilised ovules mature into seeds. A typical seed consists of seed coat(s), cotyledon(s), and an embryo axis. 
    - <b>Non-albuminous (ex-albuminous) seeds:</b> Have no residual endosperm as it is completely consumed during embryo development (e.g., pea, groundnut).
    - <b>Albuminous seeds:</b> Retain a part of the endosperm as it is not completely used up (e.g., wheat, maize, barley, castor).
    <br><br>
    The ovary develops into a <b>fruit</b>. A true fruit develops only from the ovary. A <b>false fruit</b> develops when the thalamus also contributes to fruit formation (e.g., Apple, Strawberry, Cashew).
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- **Perisperm:** In some seeds (like black pepper and beet), remnants of the nucellus are persistent. This is called perisperm.")
        st.write("- **Scutellum:** In monocots (like grass and maize), there is only one large, shield-shaped cotyledon called the scutellum.")
        st.write("- In monocot embryos, the plumule is covered by a hollow foliar structure called **Coleoptile**, and the radicle is covered by an undifferentiated sheath called **Coleorhiza**.")
        st.write("- **Parthenocarpy:** Fruit development without fertilisation (e.g., banana). These fruits are seedless and can be induced via growth hormones (Auxins).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=seed+development+and+germination+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation of Seed Development</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t7_q1", "1. Coconut water represents which type of endosperm?", ["Free-nuclear", "Cellular", "Helobial", "Ruminate"], 0, "The liquid part of a young coconut is thousands of free nuclei (free-nuclear endosperm).")
    render_quiz("t7_q2", "2. In a monocot seed, the radicle is enclosed in a protective sheath called:", ["Coleoptile", "Coleorhiza", "Scutellum", "Epiblast"], 1, "The radicle is covered by coleorhiza, while the plumule is covered by coleoptile.")
    render_quiz("t7_q3", "3. A fruit developed from a flower without fertilisation is called:", ["Parthenogenetic", "Parthenocarpic", "Apomictic", "Polyembryonic"], 1, "Parthenocarpic fruits (like bananas) develop without fertilisation and are naturally seedless.")

# --- TOPIC 8: APOMIXIS ---
with tabs[7]:
    st.header("8. Apomixis and Polyembryony")
    st.markdown("""
    <div class="bio-card">
    <b>Apomixis:</b> Although seeds are the products of fertilisation, a few flowering plants (such as some species of Asteraceae and grasses) have evolved a special mechanism to produce seeds <i>without fertilisation</i>. This is called apomixis. It is a form of asexual reproduction that mimics sexual reproduction.
    <br><br>
    <b>Polyembryony:</b> The occurrence of more than one embryo in a seed. In many Citrus and Mango varieties, some of the nucellar cells surrounding the embryo sac start dividing, protrude into the embryo sac, and develop into multiple embryos. 
    <br><br>
    <b>Agricultural Importance:</b> Hybrid seeds have to be produced every year, which is expensive. If hybrids are made into apomicts, there is no segregation of characters in the hybrid progeny. The farmers can keep using the harvested seeds year after year to raise new crops without losing the hybrid vigour (heterosis).
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 NEET + Allen Trivia"):
        st.write("- Apomixis avoids meiosis and syngamy, resulting in clones. The offspring are genetically identical to the parent plant.")
        st.write("- **Nucellar Polyembryony:** This is adventive embryony where sporophytic cells (nucellus or integuments) directly form embryos (seen in *Citrus*, *Opuntia*).")
        st.write("- Polyembryony in Citrus was first reported by Antonie van Leeuwenhoek (1719).")
        st.write("- The seeds of Orchids are incredibly small and numerous. A single orchid capsule may contain tens of thousands of dust-like seeds.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=apomixis+and+polyembryony+class+12" target="_blank" class="yt-link">🎥 Watch Explainer on Apomixis</a>', unsafe_allow_html=True)
    
    st.subheader("Practice Questions (Board PYQs)")
    render_quiz("t8_q1", "1. What is the main agricultural significance of apomixis?", ["Increases genetic variation", "Maintains hybrid vigour across generations", "Produces polyploid plants", "Promotes cross-pollination"], 1, "It helps fix hybrid characteristics across generations since it does not involve genetic segregation.")
    render_quiz("t8_q2", "2. Polyembryony through adventive embryony is most commonly seen in:", ["Wheat", "Orchids", "Citrus", "Pea"], 2, "Citrus seeds often contain multiple embryos originating from nucellar cells.")
    render_quiz("t8_q3", "3. Apomixis in plants is functionally a type of:", ["Sexual reproduction", "Asexual reproduction", "Vegetative propagation only", "Cross-pollination"], 1, "It mimics sexual reproduction (produces seeds) but is actually asexual because no fertilisation occurs.")

st.sidebar.markdown("### Guide Settings")
st.sidebar.info("Developed with Streamlit. Navigate through the detailed topics above.")
