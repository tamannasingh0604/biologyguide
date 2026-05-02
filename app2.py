import streamlit as st

st.set_page_config(page_title="Class 12 Bio: Premium Study Guide", layout="wide", page_icon="🌿", initial_sidebar_state="expanded")

# --- LIGHT HERBAL MULTI-COLOR CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

/* Colorful Light Background with Leaf Pattern */
.stApp {
    background: linear-gradient(135deg, rgba(254, 240, 138, 0.4) 0%, rgba(187, 247, 208, 0.4) 50%, rgba(191, 219, 254, 0.4) 100%), 
                url('https://www.transparenttextures.com/patterns/leaves.png');
    background-color: #f8fafc;
}

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    color: #0f172a;
}

/* Base Headings */
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    font-weight: 800 !important;
}

/* Glassmorphism Cards */
.bio-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(12px);
    border-left: 8px solid #10b981;
    border-top: 1px solid rgba(255, 255, 255, 0.9);
    border-right: 1px solid rgba(255, 255, 255, 0.9);
    border-bottom: 1px solid rgba(255, 255, 255, 0.9);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
    color: #1e293b;
    box-shadow: 0 10px 30px rgba(16, 185, 129, 0.15);
    font-size: 1.1rem;
    line-height: 1.7;
    font-weight: 500;
}

/* Image Diagram Boxes */
.diagram-box {
    background: #ffffff;
    border: 3px dashed #10b981;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.diagram-box img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin-top: 10px;
}

/* Multi-Color Gradient Text Classes */
.gradient-text-1 {
    background: linear-gradient(90deg, #db2777, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}
.gradient-text-2 {
    background: linear-gradient(90deg, #ea580c, #ca8a04);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}
.gradient-text-3 {
    background: linear-gradient(90deg, #059669, #0284c7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

/* Term Highlighting */
.term {
    color: #be123c;
    font-weight: 800;
    border-bottom: 3px dotted #f43f5e;
    cursor: help;
    transition: 0.3s;
}
.term:hover {
    background-color: #ffe4e6;
}

/* Expanders */
.streamlit-expanderHeader {
    background: linear-gradient(135deg, #fef08a 0%, #fde047 100%) !important;
    color: #9a3412 !important;
    font-weight: 800 !important;
    border: 2px solid #facc15 !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 10px rgba(250, 204, 21, 0.2);
}

/* YouTube Button */
a.yt-link {
    display: inline-block;
    background: linear-gradient(90deg, #be123c, #e11d48);
    color: white !important;
    padding: 12px 24px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 700;
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

st.markdown("<h1 class='gradient-text-1' style='font-size: 3rem;'>🌿 Sexual Reproduction in Flowering Plants</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='gradient-text-3'>Comprehensive NCERT Class 12 Biology & Allen NEET Notes</h3>", unsafe_allow_html=True)

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
    st.markdown("<h2 class='gradient-text-2'>1. Introduction & Life Cycle</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Highest evolved group of land plants">Angiosperms</span> represent the pinnacle of plant evolution. Unlike gymnosperms, their ovules are completely enclosed within an ovary, which later develops into a protective fruit. 
    <br><br>
    The defining characteristic of an angiosperm is the <b>flower</b>. A flower is a highly modified, determinant shoot specialized for sexual reproduction. The apical meristem changes into a floral meristem, and internodes do not elongate, causing the axis to condense.
    <br><br>
    The life cycle displays a distinct <b>Alternation of Generations</b>:
    <ul>
        <li><b>Sporophyte (2n):</b> The dominant, independent, photosynthetic plant body (the tree, shrub, or herb you see).</li>
        <li><b>Gametophyte (n):</b> Highly reduced, non-photosynthetic, and strictly parasitic on the sporophyte. It is represented only by the pollen grains (male) and the embryo sac (female).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h3 style="color:#059669; font-weight:800;">🖼️ NCERT Life Cycle Overview</h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Angiosperm_life_cycle_diagram.svg/800px-Angiosperm_life_cycle_diagram.svg.png" alt="Life Cycle of Angiosperm">
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Angiosperms uniquely exhibit **Double Fertilisation**, discovered by S.G. Nawaschin (1898) in *Fritillaria* and *Lilium*.")
        st.write("- **Smallest Angiosperm:** *Wolffia* (a rootless aquatic plant).")
        st.write("- **Largest Flower:** *Rafflesia arnoldii* (corpse flower, total root parasite).")
        st.write("- **Tallest Angiosperm:** *Eucalyptus* (up to 100 meters).")
    
    st.markdown('<a href="https://www.youtube.com/results?search_query=alternation+of+generations+angiosperms+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Animation: Life Cycle</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t1_q1", "1. What is the dominant phase in the life cycle of an angiosperm?", ["Haploid Gametophyte", "Diploid Sporophyte", "Triploid Endosperm", "None of the above"], 1, "The main plant body you see (tree, shrub, herb) is the diploid sporophyte.")
    render_quiz("t1_q2", "2. A flower is morphologically considered a modified:", ["Root", "Shoot", "Leaf", "Bud"], 1, "The thalamus is a condensed axis (stem) and the floral whorls are modified leaves, making it a modified shoot.")
    render_quiz("t1_q3", "3. Which unique event separates angiosperms from all other plant groups?", ["Seed formation", "Pollen tube formation", "Double fertilisation", "Vascular tissue presence"], 2, "While gymnosperms form seeds and pollen tubes, double fertilisation is strictly unique to angiosperms.")

# --- TOPIC 2: THE FLOWER ---
with tabs[1]:
    st.markdown("<h2 class='gradient-text-2'>2. Floral Anatomy & Whorls</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    The flower sits upon a condensed stalk end known as the <b>Thalamus (Receptacle)</b>. A typical angiosperm flower consists of four distinct whorls arranged successively:
    <br><br>
    <b>Accessory (Non-Essential) Whorls:</b><br>
    - <b>Calyx:</b> The outermost whorl, composed of sepals. It is usually green and protects the floral bud before it opens. Can be polysepalous (free) or gamosepalous (fused).<br>
    - <b>Corolla:</b> The second whorl, composed of petals. It is brightly colored and often fragrant to attract insects for pollination.
    <br><br>
    <b>Reproductive (Essential) Whorls:</b><br>
    - <b>Androecium:</b> The male whorl, composed of individual units called <b>stamens</b> (microsporophylls).<br>
    - <b>Gynoecium:</b> The central female whorl, composed of one or more <b>carpels/pistils</b> (megasporophylls).
    <br><br>
    If a flower has both Androecium and Gynoecium, it is <b>Bisexual</b>. If it has only one, it is <b>Unisexual</b> (staminate or pistillate).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h3 style="color:#059669; font-weight:800;">🖼️ NCERT Floral Anatomy</h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Mature_flower_diagram.svg/800px-Mature_flower_diagram.svg.png" alt="Anatomy of a Flower">
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Bracteate vs Ebracteate:** Bracts are reduced leaves at the base of the pedicel. Flowers with bracts are bracteate.")
        st.write("- **Actinomorphic (Radial Symmetry):** Flower can be divided into equal halves in any radial plane passing through the center (e.g., Mustard, Datura, Chilli).")
        st.write("- **Zygomorphic (Bilateral Symmetry):** Can be divided into equal halves in only ONE particular vertical plane (e.g., Pea, Gulmohur, Bean, Cassia).")
        st.write("- **Asymmetric (Irregular):** Cannot be divided into equal halves by any plane (e.g., Canna).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=flower+anatomy+3d+animation" target="_blank" class="yt-link">🎥 Watch 3D Flower Anatomy</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t2_q1", "1. Which plant bears unisexual flowers on completely separate male and female plants?", ["Maize", "Coconut", "Papaya", "Castor"], 2, "Papaya is strictly dioecious. Maize, coconut, and castor are monoecious (both sexes on one plant).")
    render_quiz("t2_q2", "2. A flower where the ovary is situated at the highest position, while other parts are situated below it, is called:", ["Epigynous", "Perigynous", "Hypogynous", "None of the above"], 2, "Hypogynous means 'below the gynoecium'. The ovary is superior (e.g., Mustard).")
    render_quiz("t2_q3", "3. What is the collective term for the calyx and corolla when they are indistinguishable in color and shape (e.g., Lily)?", ["Receptacle", "Perianth", "Involucre", "Tepals"], 1, "The entire whorl is called the perianth, and its individual distinct units are called tepals.")

# --- TOPIC 3: STAMEN & POLLEN ---
with tabs[2]:
    st.markdown("<h2 class='gradient-text-2'>3. Microsporogenesis & Male Gametophyte</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Anther Anatomy:</b> The anther is a tetrasporangiate structure consisting of four microsporangia located at its corners.
    <br><br>
    The microsporangium wall has 4 distinct layers:
    1. <b>Epidermis:</b> Outermost single layer, protective in function.
    2. <b>Endothecium:</b> Inner to epidermis. Cells develop fibrous thickenings of <span class="term" title="A hygroscopic carbohydrate">α-cellulose</span> which aid in the dehiscence (bursting) of the mature anther to release pollen.
    3. <b>Middle Layers:</b> 1-3 layers of ephemeral cells (they degenerate quickly and provide nourishment to tapetum).
    4. <b>Tapetum:</b> The innermost, highly active layer. Tapetal cells have dense cytoplasm, are generally multinucleated (due to endomitosis), and secrete immense nourishment for the developing pollen.
    <br><br>
    <b>Microsporogenesis:</b> The diploid Pollen Mother Cells (PMCs) in the center of the microsporangium undergo Meiosis to form 4 haploid microspores (a Microspore Tetrad). As the anther matures and dehydrates, they separate into individual pollen grains.
    <br><br>
    <b>The Pollen Grain:</b> Covered by a highly rugged, incredibly resistant outer layer called the <b>Exine</b> (made of sporopollenin) and a smooth inner <b>Intine</b> (made of cellulose and pectin). Inside, it divides into a large <b>Vegetative Cell</b> (stores food) and a small <b>Generative Cell</b> (divides to form 2 male gametes).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h3 style="color:#059669; font-weight:800;">🖼️ NCERT T.S. of Anther</h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Anther_wall.svg/800px-Anther_wall.svg.png" alt="Transverse Section of Anther">
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Sporopollenin** is formed by the oxidative polymerization of carotenoids. It is completely absent at the **germ pores** (the only place the pollen tube can exit).")
        st.write("- Tapetum produces **Ubisch bodies**, which are coated with sporopollenin and help in the thickening of the exine.")
        st.write("- Pollen grains can be preserved as fossils for millions of years purely because of the indestructible nature of sporopollenin.")
        st.write("- **Pollen Bank:** Pollen can be stored for years in **liquid nitrogen (-196°C)** for crop breeding programs.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=microsporogenesis+3d+animation" target="_blank" class="yt-link">🎥 Watch Microsporogenesis Animation</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t3_q1", "1. Which layer of the anther wall is directly responsible for providing nourishment to developing pollen?", ["Epidermis", "Endothecium", "Middle layers", "Tapetum"], 3, "The innermost Tapetum has dense cytoplasm and directly nourishes the microspores.")
    render_quiz("t3_q2", "2. A pollen grain is well preserved as a fossil because of the presence of:", ["Cellulose", "Pectin", "Sporopollenin", "Lignin"], 2, "Sporopollenin is the most resistant organic material known. No enzyme can degrade it.")
    render_quiz("t3_q3", "3. In a 2-celled pollen grain, the smaller spindle-shaped cell floating in the cytoplasm is called the:", ["Vegetative cell", "Generative cell", "Tube cell", "Synergid"], 1, "The generative cell is small and floats in the cytoplasm of the much larger vegetative cell.")

# --- TOPIC 4: PISTIL & OVULE ---
with tabs[3]:
    st.markdown("<h2 class='gradient-text-2'>4. Megasporangium (Ovule) & Embryo Sac</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Ovule Anatomy:</b> The ovule is attached to the placental cushion of the ovary by a tiny stalk called the <b>funicle</b>. The main body of the ovule fuses with the funicle at a junction called the <b>hilum</b>. 
    The protective coverings are called <b>integuments</b> (inner and outer). They encircle the central mass of cells (the <b>nucellus</b>) completely, except at the very tip, leaving a narrow opening called the <b>micropyle</b>. The basal end, directly opposite the micropyle, is the <b>chalaza</b>.
    <br><br>
    <b>Megasporogenesis & Embryo Sac Formation:</b> 
    A single prominent cell in the micropylar region of the nucellus differentiates into the Megaspore Mother Cell (MMC). The MMC undergoes meiosis to form a linear tetrad of 4 haploid megaspores. 
    <br><br>
    In most angiosperms, the 3 micropylar megaspores degenerate. Only the chalazal megaspore remains functional. This single functional megaspore undergoes exactly three rapid mitotic divisions to form an 8-nucleate, 7-celled structure known as the <b>Female Gametophyte</b> or <b>Embryo Sac</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h3 style="color:#059669; font-weight:800;">🖼️ NCERT Anatropous Ovule</h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Angiosperm_ovule.svg/500px-Angiosperm_ovule.svg.png" alt="Anatropous Ovule Anatomy">
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Development of the embryo sac from a single functional megaspore is strictly termed **monosporic development**.")
        st.write("- **Orthotropous Ovule:** The micropyle, chalaza, and funicle lie in one straight vertical line. It is considered the most primitive type (found in *Cycas*, *Piper*).")
        st.write("- **Anatropous Ovule:** The body of the ovule is completely inverted (180 degrees) so that the micropyle lies very close to the hilum. Found in 82% of all angiosperm families.")
        st.write("- The **Filiform apparatus** is a mass of finger-like cellular thickenings at the micropylar tip of the synergids. It secretes chemotropic substances to guide the pollen tube into the synergid.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=embryo+sac+development+animation" target="_blank" class="yt-link">🎥 Watch Embryo Sac Animation</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t4_q1", "1. A typical mature angiosperm embryo sac (Polygonum type) consists of:", ["8 cells, 7 nuclei", "7 cells, 8 nuclei", "8 cells, 8 nuclei", "7 cells, 7 nuclei"], 1, "It is 7-celled (3 antipodals, 2 synergids, 1 egg, 1 central cell) but 8-nucleate (the central cell has 2 polar nuclei).")
    render_quiz("t4_q2", "2. Which structure acts as a chemical beacon to guide the pollen tube into the synergid?", ["Integuments", "Antipodals", "Filiform apparatus", "Egg nucleus"], 2, "The filiform apparatus, located at the micropylar tip of synergids, chemically guides the tube.")
    render_quiz("t4_q3", "3. The functional megaspore is usually located at which end of the nucellus?", ["Micropylar end", "Chalazal end", "Equatorial region", "Hilum"], 1, "The 3 micropylar megaspores degenerate, leaving the single chalazal megaspore to become functional.")

# --- TOPIC 5: POLLINATION ---
with tabs[5]:
    st.markdown("<h2 class='gradient-text-2'>5. Pollination & Outbreeding Mechanisms</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    Since both male and female gametes are non-motile in angiosperms, they must be brought together. Pollination is the transfer of pollen grains from the anther to the stigma of a pistil.
    <br><br>
    <b>Types based on the Source of Pollen:</b><br>
    1. <b>Autogamy:</b> Same flower. Requires cleistogamy (closed flowers) or exact synchrony in anther dehiscence and stigma receptivity.<br>
    2. <b>Geitonogamy:</b> Different flower, same plant. It requires a pollinating agent but is genetically identical to autogamy since pollen comes from the same plant.<br>
    3. <b>Xenogamy:</b> Different plant. The <i>only</i> type of pollination that brings genetically different pollen grains to the stigma, ensuring genetic variation.
    <br><br>
    <b>Outbreeding Devices:</b> Continuous self-pollination results in a loss of vigor called <b>inbreeding depression</b>. To prevent this, plants evolved:<br>
    - <b>Dichogamy:</b> Anthers and stigmas mature at totally different times (Protandry = male first; Protogyny = female first).<br>
    - <b>Herkogamy:</b> A physical spatial barrier between the anther and stigma.<br>
    - <b>Self-incompatibility:</b> A powerful genetic mechanism where the stigma recognizes its own pollen (sharing the same S-alleles) and actively prevents pollen tube growth in the style.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h3 style="color:#059669; font-weight:800;">🖼️ NCERT Insect Pollination</h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Pollination.svg/600px-Pollination.svg.png" alt="Pollination Diagram">
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Entomophily (Insect):** The most common biotic agent. Flowers produce nectar, strong fragrances, and sticky pollen covered in Pollenkitt.")
        st.write("- **Anemophily (Wind):** Pollen is light, non-sticky, and produced in enormous quantities. Stigmas are large and feathery (e.g., corn cob tassels) to trap air-borne pollen. Flowers lack color/nectar.")
        st.write("- **Hydrophily (Water):** Quite rare. In *Vallisneria*, the female flower uncoils to reach the surface. In *Zostera* (sea grass), pollination occurs completely underwater with long, ribbon-like pollen that lacks sporopollenin.")
        st.write("- **Amorphophallus:** Tallest flower (6 feet). Provides a safe place for insects to lay eggs inside the flower in return for pollination.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=pollination+in+plants+3d+animation" target="_blank" class="yt-link">🎥 Watch Pollination Mechanisms</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t5_q1", "1. Which type of pollination brings genetically different types of pollen grains to the stigma?", ["Autogamy", "Geitonogamy", "Xenogamy", "Cleistogamy"], 2, "Xenogamy occurs between two completely different plants of the same species, ensuring genetic mixing.")
    render_quiz("t5_q2", "2. Cleistogamous flowers invariably exhibit:", ["Xenogamy", "Autogamy", "Geitonogamy", "All of the above"], 1, "Because they never open, cross-pollination is physically impossible. They are strictly obligate autogamous.")
    render_quiz("t5_q3", "3. What is the genetic mechanism that actively prevents self-pollen from fertilising ovules?", ["Apomixis", "Parthenocarpy", "Self-incompatibility", "Dichogamy"], 2, "Self-incompatibility is a genetic (S-allele) response that stops pollen tube growth if the pollen is from the same plant.")

# --- TOPIC 6: FERTILISATION ---
with tabs[6]:
    st.markdown("<h2 class='gradient-text-2'>6. Double Fertilisation</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Double Fertilisation</b> is the defining and most unique event of the angiosperm life cycle.
    <br><br>
    After entering the synergid via the filiform apparatus, the pollen tube ruptures, releasing two haploid male gametes into the cytoplasm of the synergid.
    <br><br>
    <b>1. Syngamy (Generative Fertilisation):</b><br>
    One male gamete (n) moves towards the egg cell (n) and fuses with its nucleus to form the diploid <b>Zygote (2n)</b>. This zygote will eventually develop into the embryo.
    <br><br>
    <b>2. Triple Fusion (Vegetative Fertilisation):</b><br>
    The second, highly active male gamete (n) travels to the massive central cell and fuses with the two polar nuclei (n+n) to form the triploid <b>Primary Endosperm Nucleus (PEN, 3n)</b>. Because this involves the fusion of three haploid nuclei, it is termed triple fusion.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="diagram-box">
        <h3 style="color:#059669; font-weight:800;">🖼️ NCERT Double Fertilisation</h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Double_Fertilization.svg/600px-Double_Fertilization.svg.png" alt="Double Fertilisation Process">
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- The central cell after triple fusion becomes the **Primary Endosperm Cell (PEC)** which divides aggressively to form the endosperm.")
        st.write("- **Chemoptropic movement:** The pollen tube grows through the solid style by secreting pectinases and is guided purely by chemical gradients of a Calcium-Boron-Inositol complex.")
        st.write("- **Entry into Ovule:** <br>1. **Porogamy:** Pollen tube enters through micropyle (most common).<br>2. **Chalazogamy:** Enters through chalaza (e.g., *Casuarina*).<br>3. **Mesogamy:** Enters through integuments/funicle (e.g., *Cucurbita*).")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=double+fertilisation+3d+animation" target="_blank" class="yt-link">🎥 Watch Double Fertilisation Animation</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t6_q1", "1. The exact ploidy level of the Primary Endosperm Nucleus (PEN) in a typical angiosperm is:", ["Haploid", "Diploid", "Triploid", "Tetraploid"], 2, "It results from the fusion of 1 male gamete (n) and 2 polar nuclei (n+n), making it strictly 3n (Triploid).")
    render_quiz("t6_q2", "2. Which two biological events constitute double fertilisation?", ["Syngamy and Plasmogamy", "Syngamy and Triple Fusion", "Triple fusion and Apomixis", "Karyogamy and Plasmogamy"], 1, "The fusion with the egg (syngamy) and the fusion with polar nuclei (triple fusion).")
    render_quiz("t6_q3", "3. What is the role of the filiform apparatus during this process?", ["To produce nectar", "To chemically guide the pollen tube", "To form the endosperm", "To protect the egg cell"], 1, "It is a specialized cellular thickening that secretes chemicals to guide the pollen tube exactly into the synergid.")

# --- TOPIC 7: SEED & EMBRYO ---
with tabs[7]:
    st.markdown("<h2 class='gradient-text-2'>7. Endosperm, Embryo & Seed Development</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Endosperm Development:</b> Strictly precedes embryo development because it must provide assured, massive nutrition to the developing embryo. In free-nuclear development (e.g., tender coconut water), the PEN undergoes successive nuclear divisions without forming cell walls. Wall formation occurs later from the periphery (the white coconut kernel).
    <br><br>
    <b>Embryogeny:</b> The zygote divides transversely to form a suspensor and a proembryo. This develops sequentially into the globular, heart-shaped, and finally the mature embryo. 
    - A <b>Dicot Embryo</b> consists of an embryonal axis and two cotyledons. The portion above the cotyledon attachment is the epicotyl (terminating in plumule). The portion below is the hypocotyl (terminating in radicle).
    - A <b>Monocot Embryo</b> has only one cotyledon (called the Scutellum in grasses).
    <br><br>
    <b>Seed & Fruit Formation:</b> Fertilised ovules mature into seeds. The ovary wall thickens to become the fruit wall (pericarp). True fruits develop strictly from the ovary. A <b>false fruit</b> develops when other floral parts, usually the fleshy thalamus, contribute to fruit formation (e.g., Apple, Cashew, Strawberry).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display:flex; justify-content: space-around;">
        <div class="diagram-box" style="width:48%;">
            <h3 style="color:#059669; font-weight:800; font-size:1.2rem;">🖼️ Dicot Embryo</h3>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Dicot_embryo.svg/500px-Dicot_embryo.svg.png" alt="Dicot Embryo">
        </div>
        <div class="diagram-box" style="width:48%;">
            <h3 style="color:#059669; font-weight:800; font-size:1.2rem;">🖼️ Monocot Embryo</h3>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Monocot_embryo.svg/500px-Monocot_embryo.svg.png" alt="Monocot Embryo">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- **Coleoptile & Coleorhiza:** In monocots, the delicate plumule is protected by a hollow foliar sheath called the coleoptile, and the radicle is protected by an undifferentiated root sheath called the coleorhiza.")
        st.write("- **Perisperm:** Persistent, leftover nucellus found in seeds of black pepper and beet.")
        st.write("- **Parthenocarpy:** Fruit development without fertilisation (e.g., seedless bananas). Can be artificially induced via growth hormones like Auxins and Gibberellins.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=embryo+development+in+plants+3d+animation" target="_blank" class="yt-link">🎥 Watch Embryo Development Animation</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t7_q1", "1. Tender coconut water (the liquid inside a young coconut) represents:", ["Free-nuclear endosperm", "Cellular endosperm", "Liquid mesocarp", "Perisperm"], 0, "The liquid part is thousands of free nuclei acting as a highly nutritious endosperm.")
    render_quiz("t7_q2", "2. A fruit that develops from parts of the flower other than the ovary (like the thalamus) is called a:", ["True fruit", "False fruit", "Parthenocarpic fruit", "Multiple fruit"], 1, "Apples and strawberries are false fruits because the massive, fleshy thalamus contributes to fruit formation.")
    render_quiz("t7_q3", "3. The single, shield-shaped cotyledon of a monocot (grass) embryo is specifically called:", ["Coleoptile", "Scutellum", "Epiblast", "Coleorhiza"], 1, "It is called the scutellum, situated to one side of the embryonal axis.")

# --- TOPIC 8: APOMIXIS ---
with tabs[7]:
    st.markdown("<h2 class='gradient-text-2'>8. Apomixis & Polyembryony</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Apomixis:</b> A highly specialized form of asexual reproduction that perfectly mimics sexual reproduction by producing seeds <b>without fertilisation</b>. 
    <br><br>
    Mechanism: Often, a diploid egg cell is formed without meiosis and develops directly into an embryo without syngamy. Seen frequently in the Asteraceae family and grasses.
    <br><br>
    <b>Polyembryony:</b> The presence of more than one embryo inside a single seed. In many *Citrus* and Mango varieties, nucellar cells surrounding the embryo sac start aggressively dividing and protrude into the sac, forming multiple embryos (Adventive Embryony).
    <br><br>
    <b>Agricultural Significance:</b> Cultivating hybrid seeds is expensive because new seeds must be produced every year to maintain hybrid vigour. If hybrids are made apomictic, the seeds will not undergo genetic segregation. Farmers can replant the seeds infinitely while retaining the exact hybrid vigour (heterosis).
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Because apomixis avoids both meiosis and syngamy, the progeny are exact genetic **clones** of the maternal plant.")
        st.write("- **Apospory:** Formation of a diploid embryo sac directly from a vegetative nucellar cell without spore formation.")
        st.write("- **Diplospory:** MMC skips meiosis and directly forms a diploid embryo sac.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=apomixis+and+polyembryony+class+12" target="_blank" class="yt-link">🎥 Watch Apomixis Explainer</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t8_q1", "1. Apomixis is functionally a form of:", ["Sexual reproduction", "Asexual reproduction", "Vegetative propagation", "Tissue culture"], 1, "Though it produces seeds, it involves no fusion of gametes, making it strictly asexual.")
    render_quiz("t8_q2", "2. Occurrence of more than one embryo in a seed is referred to as:", ["Apomixis", "Polyembryony", "Parthenocarpy", "Syngamy"], 1, "Commonly seen in Citrus fruits, caused by nucellar cells dividing into the embryo sac.")
    render_quiz("t8_q3", "3. What is the main advantage of apomictic seeds in agriculture?", ["They produce larger fruits", "They don't require water", "They maintain hybrid vigour across generations", "They grow faster"], 2, "Apomictic seeds don't undergo genetic segregation, so the superior hybrid traits are preserved perfectly forever.")

st.sidebar.markdown("### 🌿 Masterclass Settings")
st.sidebar.info("Experience the ultimate Class 12 Biology review. **Select a topic tab to begin.**")
st.sidebar.caption("© Antigravity AI Education")
