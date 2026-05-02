import streamlit as st

st.set_page_config(page_title="Class 12 Bio: Premium Study Guide", layout="wide", page_icon="🧬", initial_sidebar_state="expanded")

# --- PREMIUM DARK CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Outfit:wght@300;400;500;600;700&display=swap');

/* Main Background */
.stApp {
    background-color: #0b0f19;
}

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    color: #e2e8f0;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #34d399; /* Bright Emerald */
    text-shadow: 0 0 10px rgba(52, 211, 153, 0.2);
}

/* Glassmorphism Cards */
.bio-card {
    background: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(10px);
    border-left: 6px solid #10b981;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    color: #f8fafc;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    font-size: 1.05rem;
    line-height: 1.6;
}

/* Diagram Boxes */
.diagram-box {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
}

/* Term Highlighting */
.term {
    color: #6ee7b7;
    font-weight: 600;
    border-bottom: 2px dashed #10b981;
    cursor: help;
    transition: 0.3s;
}
.term:hover {
    background-color: rgba(16, 185, 129, 0.2);
    text-shadow: 0 0 8px #6ee7b7;
}

/* Expanders */
.streamlit-expanderHeader {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
    color: #fbbf24 !important;
    font-weight: 700 !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
}

/* YouTube Button */
a.yt-link {
    display: inline-block;
    background: linear-gradient(90deg, #be123c, #e11d48);
    color: white !important;
    padding: 12px 24px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    margin: 15px 0;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 15px rgba(225, 29, 72, 0.4);
}
a.yt-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(225, 29, 72, 0.6);
}

</style>
""", unsafe_allow_html=True)

st.title("🧬 Masterclass: Sexual Reproduction in Flowering Plants")
st.markdown("<p style='color:#94a3b8; font-size:1.2rem; font-weight:300;'>Premium NCERT Presentation & Allen Module Trivia</p>", unsafe_allow_html=True)

# --- ONE TIME ANSWER QUIZ LOGIC ---
def render_quiz(q_id, question, options, answer_idx, explanation):
    answered_key = f"{q_id}_answered"
    val_key = f"{q_id}_val"
    
    if answered_key not in st.session_state:
        st.session_state[answered_key] = False

    selected = st.radio(
        question, 
        options, 
        key=val_key, 
        index=None, 
        disabled=st.session_state[answered_key]
    )
    
    if selected is not None and not st.session_state[answered_key]:
        st.session_state[answered_key] = True
        st.rerun()

    if st.session_state[answered_key]:
        if st.session_state[val_key] == options[answer_idx]:
            st.success(f"**✓ Brilliant!** {explanation}")
        else:
            st.error(f"**✗ Incorrect.** The right answer is **{options[answer_idx]}**. \n\n*Reasoning:* {explanation}")

tabs = st.tabs(["1. Intro", "2. Flower Anatomy", "3. Stamen & Pollen", "4. Pistil & Ovule", "5. Pollination", "6. Fertilisation", "7. Seed Dev", "8. Apomixis"])

# --- TOPIC 1: INTRO ---
with tabs[0]:
    st.header("1. Introduction & Life Cycle")
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Highest evolved group of land plants">Angiosperms</span> represent the pinnacle of plant evolution. Unlike gymnosperms, their ovules are completely enclosed within an ovary, which later develops into a protective fruit. 
    <br><br>
    The defining characteristic of an angiosperm is the <b>flower</b>. A flower is a highly modified, determinant shoot specialized for sexual reproduction. The life cycle displays a distinct <b>Alternation of Generations</b>:
    <ul>
        <li><b>Sporophyte (2n):</b> The dominant, independent, photosynthetic plant body.</li>
        <li><b>Gametophyte (n):</b> Highly reduced, parasitic on the sporophyte (represented by pollen grains and the embryo sac).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#34d399; margin-bottom:15px;">Alternation of Generations</h4>
        <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 600px;">
          <!-- Sporophyte -->
          <rect x="30" y="50" width="120" height="50" rx="10" fill="#10b981" />
          <text x="90" y="75" fill="#0f172a" font-weight="bold" font-size="14" text-anchor="middle">Sporophyte (2n)</text>
          <text x="90" y="90" fill="#0f172a" font-size="10" text-anchor="middle">Main Plant Body</text>
          
          <path d="M 150 75 L 210 75" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow1)"/>
          
          <!-- Meiosis -->
          <rect x="220" y="50" width="100" height="50" rx="25" fill="#3b82f6" />
          <text x="270" y="75" fill="#fff" font-weight="bold" font-size="14" text-anchor="middle">Meiosis</text>
          
          <path d="M 320 75 L 370 75" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow1)"/>
          
          <!-- Gametophyte -->
          <rect x="380" y="50" width="100" height="50" rx="10" fill="#f43f5e" />
          <text x="430" y="75" fill="#fff" font-weight="bold" font-size="14" text-anchor="middle">Gametophyte (n)</text>
          <text x="430" y="90" fill="#fff" font-size="10" text-anchor="middle">Pollen / Embryo Sac</text>
          
          <defs><marker id="arrow1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#fbbf24"/></marker></defs>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Angiosperms uniquely exhibit **Double Fertilisation**, discovered by Nawaschin (1898) in *Fritillaria* and *Lilium*.")
        st.write("- **Smallest Angiosperm:** *Wolffia* (rootless aquatic plant).")
        st.write("- **Largest Flower:** *Rafflesia arnoldii* (corpse flower, parasitic).")
    
    st.markdown('<a href="https://www.youtube.com/results?search_query=alternation+of+generations+angiosperms+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation: Life Cycle</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t1_q1", "1. What is the dominant phase in the life cycle of an angiosperm?", ["Haploid Gametophyte", "Diploid Sporophyte", "Triploid Endosperm", "None of the above"], 1, "The main plant body you see (tree, shrub, herb) is the diploid sporophyte.")
    render_quiz("t1_q2", "2. A flower is morphologically considered a modified:", ["Root", "Shoot", "Leaf", "Bud"], 1, "The thalamus is a condensed axis (stem) and the floral whorls are modified leaves, making it a modified shoot.")
    render_quiz("t1_q3", "3. Which unique event separates angiosperms from all other plant groups?", ["Seed formation", "Pollen tube formation", "Double fertilisation", "Vascular tissue presence"], 2, "While gymnosperms form seeds and pollen tubes, double fertilisation is strictly unique to angiosperms.")

# --- TOPIC 2: THE FLOWER ---
with tabs[1]:
    st.header("2. Floral Anatomy & Whorls")
    st.markdown("""
    <div class="bio-card">
    The flower sits upon a condensed stalk end known as the <b>Thalamus (Receptacle)</b>. The four whorls are classified based on their direct role in reproduction:
    <br><br>
    <b>Accessory (Non-Essential) Whorls:</b><br>
    - <b>Calyx:</b> Composed of sepals. Protects the floral bud. Can be polysepalous (free) or gamosepalous (fused).<br>
    - <b>Corolla:</b> Composed of petals. Brightly colored to attract pollinators.
    <br><br>
    <b>Reproductive (Essential) Whorls:</b><br>
    - <b>Androecium:</b> The male whorl, composed of individual units called <b>stamens</b> (microsporophylls).<br>
    - <b>Gynoecium:</b> The female whorl, composed of one or more <b>carpels/pistils</b> (megasporophylls).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#34d399; margin-bottom:15px;">Longitudinal Section of a Flower</h4>
        <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 400px;">
          <!-- Pedicel & Thalamus -->
          <path d="M 190 280 L 190 240 L 210 240 L 210 280 Z" fill="#22c55e" />
          <ellipse cx="200" cy="240" rx="40" ry="15" fill="#15803d" />
          <text x="260" y="250" fill="#cbd5e1" font-size="12">Thalamus</text>
          
          <!-- Sepals -->
          <path d="M 160 240 Q 120 200 150 180 Q 170 220 200 240 Z" fill="#4ade80" />
          <path d="M 240 240 Q 280 200 250 180 Q 230 220 200 240 Z" fill="#4ade80" />
          <text x="110" y="210" fill="#cbd5e1" font-size="12">Sepal (Calyx)</text>
          
          <!-- Petals -->
          <path d="M 170 230 C 50 150 100 50 180 180 C 185 190 200 230 200 240 Z" fill="#f472b6" opacity="0.8"/>
          <path d="M 230 230 C 350 150 300 50 220 180 C 215 190 200 230 200 240 Z" fill="#f472b6" opacity="0.8"/>
          <text x="310" y="140" fill="#fbcfe8" font-size="12">Petal (Corolla)</text>
          
          <!-- Pistil -->
          <path d="M 195 235 C 180 200 195 100 200 100 C 205 100 220 200 205 235 Z" fill="#c084fc" />
          <ellipse cx="200" cy="100" rx="12" ry="6" fill="#a855f7" /> <!-- Stigma -->
          <text x="140" y="105" fill="#e9d5ff" font-size="12">Stigma</text>
          <text x="160" y="160" fill="#e9d5ff" font-size="12">Style</text>
          
          <!-- Stamens -->
          <path d="M 180 235 Q 150 150 150 120" stroke="#fcd34d" stroke-width="3" fill="none" />
          <ellipse cx="150" cy="115" rx="8" ry="12" fill="#fbbf24" />
          <text x="90" y="120" fill="#fef3c7" font-size="12">Anther</text>
          
          <path d="M 220 235 Q 250 150 250 120" stroke="#fcd34d" stroke-width="3" fill="none" />
          <ellipse cx="250" cy="115" rx="8" ry="12" fill="#fbbf24" />
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Bracteate vs Ebracteate:** Bracts are reduced leaves at the base of the pedicel. Flowers with bracts are bracteate.")
        st.write("- **Actinomorphic (Radial):** Flower can be divided into equal halves in any radial plane (e.g., Mustard, Datura).")
        st.write("- **Zygomorphic (Bilateral):** Can be divided into equal halves in only ONE particular vertical plane (e.g., Pea, Gulmohur, Bean).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=flower+anatomy+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Flower Anatomy</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t2_q1", "1. Which plant bears unisexual flowers on completely separate male and female plants?", ["Maize", "Coconut", "Papaya", "Castor"], 2, "Papaya is strictly dioecious. Maize, coconut, and castor are monoecious (both sexes on one plant).")
    render_quiz("t2_q2", "2. A flower where the ovary is situated at the highest position, while other parts are situated below it, is called:", ["Epigynous", "Perigynous", "Hypogynous", "None of the above"], 2, "Hypogynous means 'below the gynoecium'. The ovary is superior.")
    render_quiz("t2_q3", "3. What is the collective term for the calyx and corolla when they are indistinguishable (e.g., Lily)?", ["Receptacle", "Perianth", "Involucre", "Tepals"], 1, "The whorl is called the perianth, and its individual units are called tepals.")

# --- TOPIC 3: STAMEN & POLLEN ---
with tabs[2]:
    st.header("3. Microsporogenesis & Male Gametophyte")
    st.markdown("""
    <div class="bio-card">
    <b>Anther Anatomy:</b> The anther is a four-sided (tetragonal) structure consisting of four microsporangia located at the corners. As the anther matures, these microsporangia develop into pollen sacs.
    <br><br>
    The microsporangium wall has 4 distinct layers:
    1. <b>Epidermis:</b> Single-layered, protective.
    2. <b>Endothecium:</b> Cells develop fibrous thickenings of <span class="term" title="A hygroscopic carbohydrate">α-cellulose</span> which aid in the dehiscence (bursting) of the anther to release pollen.
    3. <b>Middle Layers:</b> 1-3 layers, ephemeral (degenerate quickly).
    4. <b>Tapetum:</b> The innermost, highly active layer. Tapetal cells have dense cytoplasm, are generally multinucleated, and secrete nourishment and essential compounds (like sporopollenin precursors) for the developing pollen.
    <br><br>
    <b>The Pollen Grain:</b> Covered by a highly rugged, incredibly resistant outer layer called the <b>Exine</b> (made of sporopollenin) and a smooth inner <b>Intine</b> (made of cellulose and pectin).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#34d399; margin-bottom:15px;">T.S. of Mature Anther</h4>
        <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 500px;">
          <!-- Epidermis Outline -->
          <path d="M 200 40 C 350 10, 380 100, 300 160 C 250 200, 150 200, 100 160 C 20 100, 50 10, 200 40 Z" fill="#0f172a" stroke="#cbd5e1" stroke-width="3"/>
          <text x="200" y="25" fill="#cbd5e1" font-size="12" text-anchor="middle">Epidermis & Endothecium</text>
          
          <!-- 4 Microsporangia with Tapetum -->
          <circle cx="120" cy="80" r="30" fill="#1e293b" stroke="#fbbf24" stroke-width="4" stroke-dasharray="5,2"/>
          <text x="120" y="60" fill="#fbbf24" font-size="10" text-anchor="middle">Tapetum</text>
          
          <circle cx="280" cy="80" r="30" fill="#1e293b" stroke="#fbbf24" stroke-width="4" stroke-dasharray="5,2"/>
          
          <circle cx="140" cy="140" r="25" fill="#1e293b" stroke="#fbbf24" stroke-width="4" stroke-dasharray="5,2"/>
          
          <circle cx="260" cy="140" r="25" fill="#1e293b" stroke="#fbbf24" stroke-width="4" stroke-dasharray="5,2"/>
          
          <!-- Connective -->
          <circle cx="200" cy="100" r="15" fill="#334155" />
          <text x="200" y="104" fill="#94a3b8" font-size="10" text-anchor="middle">Connective</text>
          
          <!-- Pollen -->
          <circle cx="120" cy="80" r="3" fill="#fcd34d" />
          <circle cx="110" cy="75" r="3" fill="#fcd34d" />
          <circle cx="130" cy="85" r="3" fill="#fcd34d" />
          
          <circle cx="280" cy="80" r="3" fill="#fcd34d" />
          <circle cx="270" cy="85" r="3" fill="#fcd34d" />
          
          <text x="120" y="110" fill="#fcd34d" font-size="10" text-anchor="middle">Microspores</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Sporopollenin** is formed by the oxidative polymerization of carotenoids. It is completely absent at the **germ pores** (where the pollen tube will exit).")
        st.write("- Tapetum produces **Ubisch bodies**, which help in the formation of sporopollenin for the exine.")
        st.write("- Pollen grains can be stored for years in **liquid nitrogen (-196°C)** in pollen banks.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=microsporogenesis+3d+animation" target="_blank" class="yt-link">🎥 Watch Microsporogenesis Animation</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t3_q1", "1. Which layer of the anther wall is responsible for providing nourishment?", ["Epidermis", "Endothecium", "Middle layers", "Tapetum"], 3, "The innermost Tapetum has dense cytoplasm and nourishes the developing microspores.")
    render_quiz("t3_q2", "2. A pollen grain is well preserved as a fossil because of the presence of:", ["Cellulose", "Pectin", "Sporopollenin", "Lignin"], 2, "Sporopollenin is the most resistant organic material known and withstands degradation.")
    render_quiz("t3_q3", "3. In a 2-celled pollen grain, the smaller floating cell is called the:", ["Vegetative cell", "Generative cell", "Tube cell", "Synergid"], 1, "The generative cell is small and floats in the cytoplasm of the larger vegetative cell.")

# --- TOPIC 4: PISTIL & OVULE ---
with tabs[3]:
    st.header("4. Megasporangium (Ovule) & Embryo Sac")
    st.markdown("""
    <div class="bio-card">
    <b>Ovule Anatomy:</b> The ovule is attached to the placental cushion by the <b>funicle</b>. The protective coverings are called <b>integuments</b> (inner and outer). They encircle the entire ovule except at the tip, leaving a small opening called the <b>micropyle</b> (the gateway for the pollen tube). The basal end, directly opposite the micropyle, is the <b>chalaza</b>.
    <br><br>
    <b>Megasporogenesis & Embryo Sac:</b> 
    A single cell in the micropylar region of the nucellus differentiates into the Megaspore Mother Cell (MMC). The MMC undergoes meiosis to form a linear tetrad of 4 megaspores. 
    <br><br>
    In most angiosperms, only the chalazal megaspore remains functional, while the other three degenerate. This single functional megaspore undergoes three rapid mitotic divisions to form an 8-nucleate, 7-celled structure known as the <b>Female Gametophyte</b> or <b>Embryo Sac</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#34d399; margin-bottom:15px;">Mature Embryo Sac (Polygonum Type)</h4>
        <svg viewBox="0 0 300 350" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px;">
          <!-- Sac Outline -->
          <ellipse cx="150" cy="175" rx="80" ry="140" fill="#1e293b" stroke="#a855f7" stroke-width="4"/>
          
          <!-- Chalazal End (Top here for standard diagram) -->
          <text x="150" y="20" fill="#cbd5e1" font-size="12" text-anchor="middle">Chalazal End</text>
          
          <!-- Antipodals -->
          <ellipse cx="120" cy="60" rx="15" ry="10" fill="#c084fc" />
          <ellipse cx="150" cy="55" rx="15" ry="10" fill="#c084fc" />
          <ellipse cx="180" cy="60" rx="15" ry="10" fill="#c084fc" />
          <circle cx="120" cy="60" r="3" fill="#fff" />
          <circle cx="150" cy="55" r="3" fill="#fff" />
          <circle cx="180" cy="60" r="3" fill="#fff" />
          <text x="210" y="60" fill="#e9d5ff" font-size="10">Antipodals (3)</text>
          
          <!-- Central Cell & Polar Nuclei -->
          <circle cx="140" cy="170" r="6" fill="#fff" />
          <circle cx="160" cy="170" r="6" fill="#fff" />
          <text x="220" y="175" fill="#e9d5ff" font-size="10">Polar Nuclei (2)</text>
          <text x="150" y="140" fill="#a855f7" font-size="12" text-anchor="middle">Central Cell</text>
          
          <!-- Micropylar End (Bottom) -->
          <!-- Synergids -->
          <path d="M 120 280 C 100 240, 140 240, 140 280 Z" fill="#38bdf8" />
          <path d="M 180 280 C 200 240, 160 240, 160 280 Z" fill="#38bdf8" />
          <circle cx="125" cy="265" r="3" fill="#fff" />
          <circle cx="175" cy="265" r="3" fill="#fff" />
          <!-- Filiform Apparatus -->
          <path d="M 120 280 Q 130 270 140 280" stroke="#bae6fd" stroke-width="2" fill="none"/>
          <path d="M 160 280 Q 170 270 180 280" stroke="#bae6fd" stroke-width="2" fill="none"/>
          
          <!-- Egg Cell -->
          <ellipse cx="150" cy="245" rx="20" ry="25" fill="#f472b6" />
          <circle cx="150" cy="235" r="4" fill="#fff" />
          
          <text x="60" y="270" fill="#bae6fd" font-size="10">Synergids (2)</text>
          <text x="230" y="245" fill="#fbcfe8" font-size="10">Egg Cell (1)</text>
          <text x="150" y="305" fill="#bae6fd" font-size="10" text-anchor="middle">Filiform Apparatus</text>
          
          <text x="150" y="330" fill="#cbd5e1" font-size="12" text-anchor="middle">Micropylar End</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Development of embryo sac from a single megaspore is **monosporic development**.")
        st.write("- **Orthotropous Ovule:** Micropyle, chalaza, and funicle lie in one straight vertical line (primitive, found in *Cycas*, *Piper*).")
        st.write("- **Anatropous Ovule:** The body of the ovule is completely inverted so that the micropyle lies close to the hilum. Found in 82% of angiosperm families.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=embryo+sac+development+animation" target="_blank" class="yt-link">🎥 Watch Embryo Sac Animation</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t4_q1", "1. An angiosperm embryo sac usually consists of:", ["8 cells, 7 nuclei", "7 cells, 8 nuclei", "8 cells, 8 nuclei", "7 cells, 7 nuclei"], 1, "It is 7-celled and 8-nucleate. The central cell has two polar nuclei.")
    render_quiz("t4_q2", "2. Which structure guides the pollen tube into the synergid?", ["Integuments", "Antipodals", "Filiform apparatus", "Egg nucleus"], 2, "The filiform apparatus, located at the micropylar tip of synergids, chemically guides the tube.")
    render_quiz("t4_q3", "3. The functional megaspore is usually located at which end of the nucellus?", ["Micropylar end", "Chalazal end", "Equatorial region", "Hilum"], 1, "The 3 micropylar megaspores degenerate, leaving the chalazal one functional.")

# --- TOPIC 5: POLLINATION ---
with tabs[4]:
    st.header("5. Pollination & Outbreeding Mechanisms")
    st.markdown("""
    <div class="bio-card">
    Since both male and female gametes are non-motile in angiosperms, pollination is an absolute necessity. 
    <br><br>
    <b>Types based on Source of Pollen:</b><br>
    1. <b>Autogamy:</b> Same flower. Requires cleistogamy (closed flowers) or exact synchrony.<br>
    2. <b>Geitonogamy:</b> Different flower, same plant. It requires a pollinating agent but is genetically identical to autogamy.<br>
    3. <b>Xenogamy:</b> Different plant. The only type that provides genetic variation.
    <br><br>
    <b>Outbreeding Devices:</b> Hermaphrodite flowers can suffer from inbreeding depression. To prevent this, plants evolved:<br>
    - <b>Dichogamy:</b> Anthers and stigmas mature at different times (Protandry = male first; Protogyny = female first).<br>
    - <b>Herkogamy:</b> Physical barrier between anther and stigma.<br>
    - <b>Self-incompatibility:</b> A genetic mechanism where the stigma recognizes its own pollen and prevents pollen tube growth.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Entomophily (Insect):** Most common. Flowers produce nectar, fragrance, and sticky pollen.")
        st.write("- **Anemophily (Wind):** Stigma is large and feathery (e.g., corn cob tassels) to trap air-borne pollen. Flowers lack color/nectar.")
        st.write("- **Hydrophily (Water):** In *Vallisneria*, the female flower reaches the surface. In *Zostera*, pollination occurs completely underwater with ribbon-like pollen.")
        st.write("- **Amoorphophallus:** Tallest flower (6 feet). Gives a safe place for insects to lay eggs in return for pollination.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=pollination+in+plants+3d+animation" target="_blank" class="yt-link">🎥 Watch Pollination Mechanisms</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t5_q1", "1. Which type of pollination brings genetically different types of pollen grains?", ["Autogamy", "Geitonogamy", "Xenogamy", "Cleistogamy"], 2, "Xenogamy occurs between two completely different plants of the same species.")
    render_quiz("t5_q2", "2. Cleistogamous flowers invariably exhibit:", ["Xenogamy", "Autogamy", "Geitonogamy", "All of the above"], 1, "Because they never open, cross-pollination is impossible. They are obligate autogamous.")
    render_quiz("t5_q3", "3. What is the genetic mechanism that prevents self-pollen from fertilising ovules?", ["Apomixis", "Parthenocarpy", "Self-incompatibility", "Dichogamy"], 2, "Self-incompatibility is a genetic response that stops pollen tube growth if the pollen shares the same S-alleles.")

# --- TOPIC 6: FERTILISATION ---
with tabs[5]:
    st.header("6. Double Fertilisation")
    st.markdown("""
    <div class="bio-card">
    <b>Double Fertilisation</b> is the defining event of the angiosperm life cycle.
    <br><br>
    After entering the synergid via the filiform apparatus, the pollen tube ruptures, releasing two haploid male gametes.
    <br>
    1. <b>Syngamy (Generative Fertilisation):</b> One male gamete (n) fuses with the egg nucleus (n) to form the diploid <b>Zygote (2n)</b>.
    <br>
    2. <b>Triple Fusion (Vegetative Fertilisation):</b> The second male gamete (n) travels to the central cell and fuses with the two polar nuclei (n+n) to form the triploid <b>Primary Endosperm Nucleus (PEN, 3n)</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h4 style="color:#34d399; margin-bottom:15px;">Double Fertilisation Mechanism</h4>
        <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 500px;">
          <!-- Ovule -->
          <path d="M 200 180 C 100 180, 50 100, 100 40 C 150 100, 180 20, 200 20 C 220 20, 250 100, 300 40 C 350 100, 300 180, 200 180 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
          
          <!-- Embryo Sac -->
          <ellipse cx="200" cy="100" rx="60" ry="70" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
          
          <!-- Pollen Tube entering -->
          <path d="M 200 200 L 200 150 C 200 140, 180 140, 180 130" fill="none" stroke="#fcd34d" stroke-width="8" stroke-linecap="round"/>
          <text x="240" y="190" fill="#fcd34d" font-size="12">Pollen Tube</text>
          
          <!-- Egg and Syngamy -->
          <circle cx="180" cy="110" r="15" fill="#f472b6" />
          <circle cx="175" cy="130" r="4" fill="#ef4444" /> <!-- Male gamete 1 -->
          <path d="M 175 130 L 180 115" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow2)"/>
          <text x="100" y="115" fill="#f472b6" font-size="10">Syngamy (2n)</text>
          
          <!-- Central Cell and Triple Fusion -->
          <circle cx="200" cy="60" r="8" fill="#fff" />
          <circle cx="215" cy="60" r="8" fill="#fff" />
          <circle cx="220" cy="90" r="4" fill="#ef4444" /> <!-- Male gamete 2 -->
          <path d="M 220 90 L 210 70" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow2)"/>
          <text x="240" y="65" fill="#fff" font-size="10">Triple Fusion (3n)</text>
          
          <defs><marker id="arrow2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#ef4444"/></marker></defs>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- The central cell after triple fusion becomes the **Primary Endosperm Cell (PEC)** which divides to form endosperm.")
        st.write("- **Chemoptropic movement:** The pollen tube grows through the solid style by secreting pectinases and is guided purely by chemical gradients of calcium-boron-inositol.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=double+fertilisation+3d+animation" target="_blank" class="yt-link">🎥 Watch Double Fertilisation Animation</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t6_q1", "1. The ploidy level of the Primary Endosperm Nucleus (PEN) is:", ["Haploid", "Diploid", "Triploid", "Tetraploid"], 2, "It results from the fusion of 1 male gamete (n) and 2 polar nuclei (n+n).")
    render_quiz("t6_q2", "2. Which two events constitute double fertilisation?", ["Syngamy and Plasmogamy", "Syngamy and Triple Fusion", "Triple fusion and Apomixis", "Karyogamy and Plasmogamy"], 1, "The fusion with the egg (syngamy) and the fusion with polar nuclei (triple fusion).")
    render_quiz("t6_q3", "3. What is the role of the filiform apparatus?", ["To produce nectar", "To guide the pollen tube", "To form the endosperm", "To protect the egg cell"], 1, "It is a specialized cellular thickening that chemically guides the pollen tube into the synergid.")

# --- TOPIC 7: SEED & EMBRYO ---
with tabs[6]:
    st.header("7. Endosperm, Embryo & Seed Development")
    st.markdown("""
    <div class="bio-card">
    <b>Endosperm:</b> Provides massive nutritional support to the developing embryo. In free-nuclear development (like coconut water), the PEN undergoes successive nuclear divisions without cell walls. Wall formation occurs later (white coconut kernel).
    <br><br>
    <b>Embryogeny:</b> The zygote divides to form the proembryo, leading to the globular, heart-shaped, and mature embryo stages. 
    - A <b>Dicot Embryo</b> consists of an embryonal axis and two cotyledons. The portion above the cotyledon attachment is the epicotyl (terminating in plumule). The portion below is the hypocotyl (terminating in radicle).
    - A <b>Monocot Embryo</b> has only one cotyledon (Scutellum).
    <br><br>
    <b>Fruit Formation:</b> True fruits develop strictly from the ovary wall (pericarp). False fruits incorporate other parts, usually the thalamus (e.g., Apple, Cashew, Strawberry).
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Coleoptile & Coleorhiza:** In monocots, the plumule is protected by the coleoptile (hollow foliar structure) and the radicle is protected by the coleorhiza (undifferentiated sheath).")
        st.write("- **Perisperm:** Persistent, leftover nucellus found in black pepper and beet.")
        st.write("- **Parthenocarpy:** Fruit without fertilisation (seedless bananas). Induced via Auxins.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=embryo+development+in+plants+3d+animation" target="_blank" class="yt-link">🎥 Watch Embryo Development Animation</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t7_q1", "1. Tender coconut water represents:", ["Free-nuclear endosperm", "Cellular endosperm", "Liquid mesocarp", "Perisperm"], 0, "The liquid part is thousands of free nuclei acting as a nutritive endosperm.")
    render_quiz("t7_q2", "2. A fruit that develops from parts of the flower other than the ovary is called a:", ["True fruit", "False fruit", "Parthenocarpic fruit", "Multiple fruit"], 1, "Apples and strawberries are false fruits because the thalamus contributes to fruit formation.")
    render_quiz("t7_q3", "3. The single cotyledon of a monocot embryo is specifically called:", ["Coleoptile", "Scutellum", "Epiblast", "Coleorhiza"], 1, "It is a large, shield-shaped structure situated to one side of the embryonal axis.")

# --- TOPIC 8: APOMIXIS ---
with tabs[7]:
    st.header("8. Apomixis and Polyembryony")
    st.markdown("""
    <div class="bio-card">
    <b>Apomixis:</b> A highly specialized form of asexual reproduction that perfectly mimics sexual reproduction by producing seeds <b>without fertilisation</b>. 
    <br><br>
    Mechanism: Often, a diploid egg cell is formed without meiosis and develops directly into an embryo. Seen frequently in the Asteraceae family and grasses.
    <br><br>
    <b>Polyembryony:</b> The presence of more than one embryo inside a single seed. In many *Citrus* and Mango varieties, nucellar cells surrounding the embryo sac start aggressively dividing and protrude into the sac, forming multiple embryos (Adventive Embryony).
    <br><br>
    <b>Agricultural Significance:</b> Cultivating hybrid seeds is expensive because new seeds must be produced every year. If hybrids are made apomictic, the seeds will not undergo genetic segregation. Farmers can replant the seeds infinitely while retaining the exact hybrid vigour (heterosis).
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Because apomixis avoids both meiosis and syngamy, the progeny are exact genetic **clones** of the maternal plant.")
        st.write("- **Apospory:** Formation of a diploid embryo sac directly from a vegetative nucellar cell without spore formation.")
        st.write("- **Diplospory:** MMC skips meiosis and directly forms a diploid embryo sac.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=apomixis+and+polyembryony+class+12" target="_blank" class="yt-link">🎥 Watch Apomixis Explainer</a>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Board PYQ Challenge")
    render_quiz("t8_q1", "1. Apomixis is functionally a form of:", ["Sexual reproduction", "Asexual reproduction", "Vegetative propagation", "Tissue culture"], 1, "Though it produces seeds, it involves no fusion of gametes, making it strictly asexual.")
    render_quiz("t8_q2", "2. Occurrence of more than one embryo in a seed is referred to as:", ["Apomixis", "Polyembryony", "Parthenocarpy", "Syngamy"], 1, "Commonly seen in Citrus fruits, caused by nucellar cells dividing into the embryo sac.")
    render_quiz("t8_q3", "3. What is the main advantage of apomictic seeds in agriculture?", ["They produce larger fruits", "They don't require water", "They maintain hybrid vigour across generations", "They grow faster"], 2, "Apomictic seeds don't undergo genetic segregation, so the superior hybrid traits are preserved perfectly forever.")

st.sidebar.markdown("### 🧬 Masterclass Settings")
st.sidebar.info("Experience the ultimate Class 12 Biology review. **Select a topic tab to begin.**")
st.sidebar.caption("© Antigravity AI Education")
