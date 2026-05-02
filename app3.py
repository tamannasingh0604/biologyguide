import streamlit as st

st.set_page_config(page_title="Class 12 Bio: Premium Study Guide", layout="wide", page_icon="🌿", initial_sidebar_state="expanded")

# --- LIGHT HERBAL MULTI-COLOR CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, rgba(254, 240, 138, 0.4) 0%, rgba(187, 247, 208, 0.4) 50%, rgba(191, 219, 254, 0.4) 100%), 
                url('https://www.transparenttextures.com/patterns/leaves.png');
    background-color: #f8fafc;
}

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; color: #0f172a; }
h1, h2, h3 { font-family: 'Playfair Display', serif; font-weight: 800 !important; }

/* Splash Screen Button */
.splash-btn-container { display: flex; justify-content: center; margin-top: 50px; }
div.stButton > button:first-child {
    background: linear-gradient(90deg, #10b981, #059669); color: white;
    font-size: 1.5rem; font-weight: 800; padding: 15px 40px; border-radius: 50px;
    border: none; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4); transition: transform 0.2s;
}
div.stButton > button:first-child:hover { transform: scale(1.05); }

/* Glassmorphism Cards */
.bio-card {
    background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px);
    border-left: 8px solid #10b981; border-top: 1px solid rgba(255, 255, 255, 0.9);
    border-right: 1px solid rgba(255, 255, 255, 0.9); border-bottom: 1px solid rgba(255, 255, 255, 0.9);
    padding: 25px; border-radius: 15px; margin-bottom: 25px; color: #1e293b;
    box-shadow: 0 10px 30px rgba(16, 185, 129, 0.15); font-size: 1.1rem; line-height: 1.7; font-weight: 500;
}

/* Gradients */
.gradient-text-1 { background: linear-gradient(90deg, #db2777, #7c3aed); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.gradient-text-2 { background: linear-gradient(90deg, #ea580c, #ca8a04); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.gradient-text-3 { background: linear-gradient(90deg, #059669, #0284c7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

.term { color: #be123c; font-weight: 800; border-bottom: 3px dotted #f43f5e; cursor: help; }
.term:hover { background-color: #ffe4e6; }
.streamlit-expanderHeader { background: linear-gradient(135deg, #fef08a 0%, #fde047 100%) !important; color: #9a3412 !important; font-weight: 800 !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# --- SPLASH SCREEN LOGIC ---
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; color: #0f172a;'>Are you ready for this race? 🚀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.5rem; color: #475569;'>The Ultimate NCERT Biology Revision is about to begin.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("Let's Get Started!", use_container_width=True):
            st.balloons()
            st.session_state.started = True
            st.rerun()
    st.stop()  # Stop rendering the rest of the app until started

# --- MAIN APP ---
st.markdown("<h1 class='gradient-text-1' style='font-size: 3rem;'>🌿 Sexual Reproduction in Flowering Plants</h1>", unsafe_allow_html=True)

def render_quiz(q_id, question, options, answer_idx, explanation):
    answered_key = f"{q_id}_answered"
    val_key = f"{q_id}_val"
    if answered_key not in st.session_state: st.session_state[answered_key] = False

    selected = st.radio(question, options, key=val_key, index=None, disabled=st.session_state[answered_key])
    
    if selected is not None and not st.session_state[answered_key]:
        st.session_state[answered_key] = True
        st.rerun()

    if st.session_state[answered_key]:
        if st.session_state[val_key] == options[answer_idx]:
            st.success(f"**✓ Brilliant!** {explanation}")
        else:
            st.error(f"**✗ Incorrect.** The right answer is **{options[answer_idx]}**. \n\n*Reasoning:* {explanation}")

tabs = st.tabs(["1. Intro", "2. Flower Anatomy", "3. Stamen", "4. Pistil", "5. Pollination", "6. Fertilisation", "7. Seed", "8. Apomixis", "9. Last Min Notes", "10. Trivia Time"])

# --- 1: INTRO ---
with tabs[0]:
    st.markdown("<h2 class='gradient-text-2'>1. Introduction & Life Cycle</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <span class="term" title="Highest evolved group of land plants">Angiosperms</span> exhibit an <b>Alternation of Generations</b>:
    <ul>
        <li><b>Sporophyte (2n):</b> The dominant, independent plant body.</li>
        <li><b>Gametophyte (n):</b> Highly reduced, non-photosynthetic, and parasitic on the sporophyte (pollen grains & embryo sac).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#059669", fontcolor=white, fontname="Outfit"]
            "Sporophyte (2n)" -> "Flower"
            "Flower" -> "Stamen (Male)" 
            "Flower" -> "Pistil (Female)"
            "Stamen (Male)" -> "Pollen Grains (n)" [label="Meiosis"]
            "Pistil (Female)" -> "Embryo Sac (n)" [label="Meiosis"]
            "Pollen Grains (n)" -> "Fertilisation"
            "Embryo Sac (n)" -> "Fertilisation"
            "Fertilisation" -> "Zygote (2n)" -> "Seed" -> "Sporophyte (2n)"
        }
    ''')

# --- 2: FLOWER ---
with tabs[1]:
    st.markdown("<h2 class='gradient-text-2'>2. Floral Anatomy</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Accessory Whorls:</b> Calyx (sepals) and Corolla (petals).<br>
    <b>Reproductive Whorls:</b> Androecium (stamens) and Gynoecium (pistils).
    </div>
    """, unsafe_allow_html=True)
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#db2777", fontcolor=white, fontname="Outfit"]
            "Flower Whorls" -> "Accessory (Non-Essential)"
            "Flower Whorls" -> "Reproductive (Essential)"
            "Accessory (Non-Essential)" -> "Calyx (Sepals)"
            "Accessory (Non-Essential)" -> "Corolla (Petals)"
            "Reproductive (Essential)" -> "Androecium (Male)" -> "Stamens"
            "Reproductive (Essential)" -> "Gynoecium (Female)" -> "Pistils/Carpels"
        }
    ''')

# --- 3: STAMEN ---
with tabs[2]:
    st.markdown("<h2 class='gradient-text-2'>3. Microsporogenesis & Pollen</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    Anther Wall Layers: Epidermis → Endothecium → Middle Layers → Tapetum.<br>
    <b>Tapetum</b> nourishes the developing pollen grains.<br>
    Pollen exine is made of highly resistant <b>Sporopollenin</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#ea580c", fontcolor=white, fontname="Outfit"]
            "Pollen Mother Cell [2n]" -> "Meiosis" -> "Microspore Tetrad (n)" -> "Pollen Grains"
        }
    ''')

# --- 4: PISTIL ---
with tabs[3]:
    st.markdown("<h2 class='gradient-text-2'>4. Megasporangium (Ovule)</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    Mature Embryo Sac (Polygonum type) is <b>7-celled and 8-nucleate</b>. The filiform apparatus guides the pollen tube into the synergid.
    </div>
    """, unsafe_allow_html=True)
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#7c3aed", fontcolor=white, fontname="Outfit"]
            "MMC (2n)" -> "Meiosis" -> "4 Megaspores" -> "3 Degenerate, 1 Functional" -> "3 Mitotic Divisions" -> "Mature Embryo Sac"
        }
    ''')

# --- 5: POLLINATION ---
with tabs[4]:
    st.markdown("<h2 class='gradient-text-2'>5. Pollination Mechanisms</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    <b>Xenogamy</b> brings genetically different pollen grains.<br>
    <b>Outbreeding Devices:</b> Dichogamy, Herkogamy, and Self-incompatibility (genetic mechanism to prevent selfing).
    </div>
    """, unsafe_allow_html=True)
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#ca8a04", fontcolor=white, fontname="Outfit"]
            "Types of Pollination" -> "Autogamy" [label="Same Flower"]
            "Types of Pollination" -> "Geitonogamy" [label="Same Plant"]
            "Types of Pollination" -> "Xenogamy" [label="Different Plant"]
            "Autogamy" -> "Genetically Identical"
            "Geitonogamy" -> "Genetically Identical"
            "Xenogamy" -> "Genetically Different"
        }
    ''')

# --- 6: FERTILISATION ---
with tabs[5]:
    st.markdown("<h2 class='gradient-text-2'>6. Double Fertilisation</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    1. <b>Syngamy:</b> Male Gamete (n) + Egg (n) = Zygote (2n).<br>
    2. <b>Triple Fusion:</b> Male Gamete (n) + 2 Polar Nuclei = PEN (3n).
    </div>
    """, unsafe_allow_html=True)
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#0284c7", fontcolor=white, fontname="Outfit"]
            "Pollen Tube Enters" -> "Releases 2 Male Gametes"
            "Releases 2 Male Gametes" -> "Syngamy -> Zygote (2n)"
            "Releases 2 Male Gametes" -> "Triple Fusion -> PEN (3n)"
        }
    ''')

# --- 7: SEED ---
with tabs[6]:
    st.markdown("<h2 class='gradient-text-2'>7. Seed & Embryo</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    True fruits develop from the ovary. False fruits involve the thalamus (e.g., Apple).<br>
    Monocot embryo has one cotyledon called the <b>Scutellum</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#10b981", fontcolor=white, fontname="Outfit"]
            "Post-Fertilisation Events" -> "Zygote becomes Embryo"
            "Post-Fertilisation Events" -> "PEN becomes Endosperm"
            "Post-Fertilisation Events" -> "Ovule becomes Seed"
            "Post-Fertilisation Events" -> "Ovary becomes Fruit"
        }
    ''')

# --- 8: APOMIXIS ---
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
    
    st.graphviz_chart('''
        digraph {
            node [shape=box, style="filled,rounded", color="#7c3aed", fontcolor=white, fontname="Outfit"]
            "Apomixis" -> "Asexual Reproduction"
            "Asexual Reproduction" -> "Mimics Sexual Reproduction"
            "Mimics Sexual Reproduction" -> "Seeds Without Fertilisation"
            "Seeds Without Fertilisation" -> "Maintains Hybrid Vigour"
        }
    ''')
    
    with st.expander("💡 High-Yield Allen NEET Trivia"):
        st.write("- Because apomixis avoids both meiosis and syngamy, the progeny are exact genetic **clones** of the maternal plant.")
        st.write("- **Apospory:** Formation of a diploid embryo sac directly from a vegetative nucellar cell without spore formation.")
        st.write("- **Diplospory:** MMC skips meiosis and directly forms a diploid embryo sac.")
        
    st.markdown('<a href="https://www.youtube.com/results?search_query=apomixis+and+polyembryony+class+12" target="_blank" class="yt-link">🎥 Watch Apomixis Explainer</a>', unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text-1'>📝 Board PYQ Challenge</h3>", unsafe_allow_html=True)
    render_quiz("t8_q1", "1. Apomixis is functionally a form of:", ["Sexual reproduction", "Asexual reproduction", "Vegetative propagation", "Tissue culture"], 1, "Though it produces seeds, it involves no fusion of gametes, making it strictly asexual.")
    render_quiz("t8_q2", "2. Occurrence of more than one embryo in a seed is referred to as:", ["Apomixis", "Polyembryony", "Parthenocarpy", "Syngamy"], 1, "Commonly seen in Citrus fruits, caused by nucellar cells dividing into the embryo sac.")
    render_quiz("t8_q3", "3. What is the main advantage of apomictic seeds in agriculture?", ["They produce larger fruits", "They don't require water", "They maintain hybrid vigour across generations", "They grow faster"], 2, "Apomictic seeds don't undergo genetic segregation, so the superior hybrid traits are preserved perfectly forever.")

# --- 9: LAST MIN NOTES ---
with tabs[8]:
    st.markdown("<h2 class='gradient-text-1'>9. Last Minute Rapid Revision</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card">
    🔥 <b>Essential One-Page Summary:</b>
    <ul>
        <li><b>Microsporogenesis:</b> Forms haploid microspores from diploid PMC via meiosis.</li>
        <li><b>Tapetum:</b> Innermost anther wall layer, provides nourishment to pollen.</li>
        <li><b>Exine:</b> Hard outer layer of pollen made of <b>sporopollenin</b> (most resistant organic material).</li>
        <li><b>Megasporogenesis:</b> Functional megaspore develops into the 7-celled, 8-nucleate embryo sac.</li>
        <li><b>Filiform apparatus:</b> In synergids, chemically guides pollen tube entry.</li>
        <li><b>Xenogamy:</b> Cross-pollination; brings genetic variation.</li>
        <li><b>Cleistogamous flowers:</b> Never open, strictly autogamous (e.g., Viola, Oxalis).</li>
        <li><b>Double Fertilisation:</b> Unique to angiosperms. Syngamy (zygote 2n) + Triple Fusion (PEN 3n).</li>
        <li><b>False Fruits:</b> Thalamus contributes to fruit formation (Apple, Strawberry).</li>
        <li><b>Apomixis:</b> Seed formation without fertilisation. Great for maintaining hybrid vigour.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 10: TRIVIA TIME (20 PYQs) ---
with tabs[9]:
    st.markdown("<h2 class='gradient-text-3'>10. Trivia Time (Board PYQs)</h2>", unsafe_allow_html=True)
    st.info("Test your knowledge with 20 real Board Previous Year Questions! Click to lock your answer.")
    
    render_quiz("pyq1", "1. [CBSE 2020] The innermost layer of anther is tapetum whose function is:", ["Protection", "Dehiscence", "Nourishment", "Mechanical support"], 2, "Tapetum has dense cytoplasm and nourishes the developing pollen grains.")
    render_quiz("pyq2", "2. [CBSE 2019] Even in absence of pollinating agents, seed-setting is assured in:", ["Commelina", "Zostera", "Salvia", "Fig"], 0, "Commelina produces cleistogamous (closed) flowers which are obligate autogamous.")
    render_quiz("pyq3", "3. [CBSE 2018] Double fertilization is:", ["Fusion of two male gametes with one egg", "Syngamy and triple fusion", "Fusion of one male gamete with two polar nuclei", "Fusion of two male gametes of pollen tube with two different eggs"], 1, "It comprises syngamy (forming zygote) and triple fusion (forming PEN).")
    render_quiz("pyq4", "4. [CBSE 2017] Flowers which have single ovule in the ovary and are packed into inflorescence are usually pollinated by:", ["Bee", "Wind", "Bat", "Water"], 1, "Wind pollinated flowers typically have a single ovule and are packed into an inflorescence (e.g., corn cob).")
    render_quiz("pyq5", "5. [CBSE 2016] Advantage of cleistogamy is:", ["Higher genetic variability", "More vigorous offspring", "No dependence on pollinators", "Vivipary"], 2, "Since flowers never open, pollinators are completely unnecessary for seed set.")
    render_quiz("pyq6", "6. [CBSE 2015] Filiform apparatus is characteristic feature of:", ["Aleurone cell", "Synergids", "Generative cell", "Nucellar embryo"], 1, "It is located at the micropylar tip of the synergids.")
    render_quiz("pyq7", "7. [CBSE 2014] Which one of the following fruits is parthenocarpic?", ["Apple", "Jackfruit", "Banana", "Brinjal"], 2, "Bananas develop without fertilization and are naturally seedless.")
    render_quiz("pyq8", "8. [CBSE 2013] Megasporangium is equivalent to:", ["Nucellus", "Ovule", "Embryo sac", "Fruit"], 1, "The ovule is structurally the integumented megasporangium.")
    render_quiz("pyq9", "9. [CBSE 2012] The advantage of seeds in angiosperms is:", ["They remain dormant", "Reproductive processes become independent of water", "They form fruits", "They attract animals"], 1, "Unlike lower plants, pollination and fertilization in seed plants do not require liquid water.")
    render_quiz("pyq10", "10. [CBSE 2011] Wind pollinated flowers are:", ["Small, brightly colored, producing large number of pollen grains", "Small, producing large number of dry pollen grains", "Large, producing abundant nectar", "Small, producing nectar and dry pollen"], 1, "They produce millions of dry, light pollen grains and do not waste energy on color or nectar.")
    render_quiz("pyq11", "11. [CBSE 2010] Endosperm is completely consumed by the developing embryo in the seed of:", ["Pea", "Castor", "Coconut", "Maize"], 0, "Pea is a non-endospermic (ex-albuminous) seed.")
    render_quiz("pyq12", "12. [CBSE 2009] Unisexuality of flowers prevents:", ["Geitonogamy but not xenogamy", "Autogamy and geitonogamy", "Autogamy but not geitonogamy", "Both autogamy and xenogamy"], 2, "If a plant is monoecious (unisexual flowers on same plant), it prevents autogamy but geitonogamy can still occur.")
    render_quiz("pyq13", "13. [CBSE 2019] Water hyacinth and water lily are pollinated by:", ["Water currents", "Insects or wind", "Birds", "Bats"], 1, "Though aquatic, their flowers emerge above water and are pollinated by insects or wind.")
    render_quiz("pyq14", "14. [CBSE 2018] Pollen grains can be stored for several years in:", ["Liquid nitrogen (-196°C)", "Liquid oxygen (-196°C)", "Liquid hydrogen (-196°C)", "Liquid argon (-196°C)"], 0, "Cryopreservation uses liquid nitrogen at -196°C.")
    render_quiz("pyq15", "15. [CBSE 2017] Attractants and rewards are required for:", ["Entomophily", "Hydrophily", "Cleistogamy", "Anemophily"], 0, "Insects require nectar (reward) and color/fragrance (attractant) to visit flowers.")
    render_quiz("pyq16", "16. [CBSE 2016] Proximal end of the filament of stamen is attached to the:", ["Placenta", "Thalamus or petal", "Anther", "Connective"], 1, "The base is attached to the thalamus or the petal (if epipetalous).")
    render_quiz("pyq17", "17. [CBSE 2015] In angiosperms, microsporogenesis and megasporogenesis:", ["Involve meiosis", "Occur in ovule", "Occur in anther", "Form gametes without further divisions"], 0, "Both processes involve meiosis of Mother Cells (MMC/PMC) to form haploid spores.")
    render_quiz("pyq18", "18. [CBSE 2014] Nucellar polyembryony is widely reported in species of:", ["Citrus", "Gossypium", "Triticum", "Brassica"], 0, "Citrus and Mango show adventive polyembryony from nucellar cells.")
    render_quiz("pyq19", "19. [CBSE 2013] Perisperm differs from endosperm in:", ["Being a diploid tissue", "Its formation by fusion", "Being a haploid tissue", "Having no reserve food"], 0, "Perisperm is the persistent remnant of the nucellus, which is sporophytic (2n), while endosperm is 3n.")
    render_quiz("pyq20", "20. [CBSE 2012] What is the function of germ pore?", ["Initiation of pollen tube", "Release of male gametes", "Emergence of radicle", "Absorption of water for seed germination"], 0, "Germ pores are places where sporopollenin is absent, allowing the pollen tube to emerge.")

st.sidebar.markdown("### 🌿 Masterclass Settings")
st.sidebar.info("Experience the ultimate Class 12 Biology review.")
st.sidebar.caption("© Antigravity AI Education")
