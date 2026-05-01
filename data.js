const termsDictionary = {
  "angiosperms": {
    title: "Angiosperms",
    content: "Angiosperms (flowering plants) are the most dominant group of land plants on Earth. They reproduce sexually via the formation of male and female gametes, pollination, fertilisation, and seed/fruit development. The seed is enclosed in a vessel (fruit)."
  },
  "microsporogenesis": {
    title: "Microsporogenesis",
    content: "The process of formation of microspores from a pollen mother cell (PMC) through meiosis is called microsporogenesis. The microspores are arranged in a cluster of four cells—the microspore tetrad."
  },
  "megasporogenesis": {
    title: "Megasporogenesis",
    content: "The process of formation of megaspores from the megaspore mother cell is called megasporogenesis. A single megaspore mother cell (MMC) differentiates in the micropylar region of the nucellus."
  },
  "double fertilisation": {
    title: "Double Fertilisation",
    content: "A unique event to angiosperms where two types of fusion occur: syngamy (fusion of male gamete with egg to form zygote) and triple fusion (fusion of male gamete with two polar nuclei to form Primary Endosperm Nucleus - PEN)."
  },
  "apomixis": {
    title: "Apomixis",
    content: "A form of asexual reproduction that mimics sexual reproduction, where seeds are produced without fertilisation. Seen in some species of Asteraceae and grasses."
  },
  "cleistogamy": {
    title: "Cleistogamy",
    content: "A condition where flowers do not open at all. These flowers are invariably autogamous as there is no chance of cross-pollen landing on the stigma. Examples include Viola, Oxalis, and Commelina."
  },
  "sporopollenin": {
    title: "Sporopollenin",
    content: "One of the most resistant organic materials known, which makes up the exine (outer layer) of pollen grains. It can withstand high temperatures and strong acids/alkalis. No enzyme that degrades sporopollenin is known so far."
  },
  "tapetum": {
    title: "Tapetum",
    content: "The innermost wall layer of the microsporangium. It nourishes the developing pollen grains. Cells of the tapetum possess dense cytoplasm and generally have more than one nucleus."
  }
};

const topicsData = [
  {
    id: "intro",
    navTitle: "🌿 Intro",
    title: "Introduction to Angiosperm Reproduction",
    content: "Angiosperms reproduce sexually via the flower. The flower is a modified shoot functioning as a reproductive organ. It contains the essential and non-essential whorls.",
    diagramLabel: "NCERT: Life Cycle Overview",
    diagram: `<svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg">
      <rect x="50" y="50" width="100" height="40" rx="10" fill="#0d6e4a" />
      <text x="100" y="75" fill="#fff" text-anchor="middle">Sporophyte (2n)</text>
      <path d="M 160 70 L 220 70" stroke="#d97706" stroke-width="2" marker-end="url(#arrow)"/>
      <rect x="230" y="50" width="100" height="40" rx="10" fill="#16a06a" />
      <text x="280" y="75" fill="#fff" text-anchor="middle">Flower</text>
      <path d="M 340 70 L 400 70" stroke="#d97706" stroke-width="2" marker-end="url(#arrow)"/>
      <rect x="410" y="50" width="100" height="40" rx="10" fill="#1ecc87" />
      <text x="460" y="75" fill="#fff" text-anchor="middle">Gametes (n)</text>
      <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#d97706"/></marker></defs>
    </svg>`,
    youtube: { title: "Introduction to Sexual Reproduction in Plants (3D)", url: "https://www.youtube.com/results?search_query=sexual+reproduction+in+flowering+plants+class+12+animation" },
    trivia: [
      "Angiosperms are the only group showing double fertilisation — first discovered by Nawaschin (1898).",
      "Term Angiosperm coined by Paul Hermann (1690)."
    ],
    mcqs: [
      { question: "Double fertilisation is a unique feature of:", options: ["Gymnosperms", "Angiosperms", "Bryophytes", "Pteridophytes"], correctIdx: 1, explanation: "Double fertilisation is unique to angiosperms." },
      { question: "A flower is considered a modified:", options: ["Root", "Shoot", "Leaf", "Bud"], correctIdx: 1, explanation: "The flower is a modified shoot functioning as the reproductive unit." }
    ]
  },
  {
    id: "flower",
    navTitle: "🌸 The Flower",
    title: "Structure of a Typical Flower",
    content: "A typical flower consists of 4 whorls on a receptacle (thalamus): Calyx (sepals), Corolla (petals), Androecium (stamens), and Gynoecium (pistil).",
    diagramLabel: "Parts of a Flower",
    diagram: `<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
      <path d="M150,180 L150,150" stroke="green" stroke-width="5"/>
      <ellipse cx="150" cy="150" rx="20" ry="10" fill="green"/>
      <path d="M130,150 Q100,100 130,80 Q150,120 150,150" fill="pink"/>
      <path d="M170,150 Q200,100 170,80 Q150,120 150,150" fill="pink"/>
      <rect x="145" y="80" width="10" height="70" fill="#6d28d9"/>
      <ellipse cx="150" cy="75" rx="8" ry="5" fill="#6d28d9"/>
      <text x="150" y="195" text-anchor="middle" font-size="12">Thalamus & Whorls</text>
    </svg>`,
    youtube: { title: "Flower Structure 3D Anatomy", url: "https://www.youtube.com/results?search_query=flower+anatomy+3d+animation" },
    trivia: [
      "Epigynous flower: ovary inferior (apple, guava).",
      "Perigynous: ovary half-inferior (rose, plum)."
    ],
    mcqs: [
      { question: "Which of the following is dioecious?", options: ["Maize", "Coconut", "Papaya", "Castor"], correctIdx: 2, explanation: "Papaya has male and female flowers on different plants." },
      { question: "The essential whorls of a flower are:", options: ["Calyx and Corolla", "Androecium and Gynoecium", "Calyx and Androecium", "Corolla and Gynoecium"], correctIdx: 1, explanation: "Androecium and Gynoecium are directly involved in reproduction." }
    ]
  },
  {
    id: "stamen",
    navTitle: "🌾 Stamen",
    title: "Stamen, Microsporogenesis & Pollen Grain",
    content: "The stamen consists of the filament and the anther. The anther is bilobed and tetrasporangiate. Through microsporogenesis, diploid pollen mother cells undergo meiosis to form haploid microspores, which develop into pollen grains.",
    diagramLabel: "T.S of Anther",
    diagram: `<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="150" cy="75" rx="80" ry="50" fill="#e8f5ee" stroke="#0d6e4a" stroke-width="2"/>
      <circle cx="110" cy="75" r="15" fill="#fbbf24"/>
      <circle cx="190" cy="75" r="15" fill="#fbbf24"/>
      <circle cx="150" cy="45" r="15" fill="#fbbf24"/>
      <circle cx="150" cy="105" r="15" fill="#fbbf24"/>
      <text x="150" y="145" text-anchor="middle" font-size="12">Tetrasporangiate Anther</text>
    </svg>`,
    youtube: { title: "Microsporogenesis 3D Animation", url: "https://www.youtube.com/results?search_query=microsporogenesis+3d+animation" },
    trivia: [
      "Tapetum provides sporopollenin precursors and pollenkitt.",
      "Sporopollenin is absent at the germ pores.",
      "Pollen viability ranges from 30 mins (rice) to months (Rosaceae)."
    ],
    mcqs: [
      { question: "The innermost nutritive layer of the anther wall is:", options: ["Epidermis", "Endothecium", "Middle layers", "Tapetum"], correctIdx: 3, explanation: "Tapetum nourishes developing pollen grains." },
      { question: "Sporopollenin is a constituent of:", options: ["Exine of pollen", "Intine of pollen", "Pollen tube", "Seed coat"], correctIdx: 0, explanation: "Exine is made of sporopollenin, the most resistant organic material." }
    ]
  },
  {
    id: "pistil",
    navTitle: "🌼 Pistil",
    title: "Pistil, Ovule & Megasporogenesis",
    content: "The pistil comprises stigma, style, and ovary. The ovary contains ovules (megasporangia). The process of formation of megaspores from the MMC is megasporogenesis. The functional megaspore develops into the female gametophyte or embryo sac.",
    diagramLabel: "Anatropous Ovule",
    diagram: `<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="100" cy="100" rx="40" ry="60" fill="none" stroke="#16a06a" stroke-width="2"/>
      <ellipse cx="100" cy="100" rx="30" ry="50" fill="#d0f5e5" stroke="#0d6e4a" stroke-width="2"/>
      <ellipse cx="100" cy="90" rx="15" ry="25" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
      <text x="100" y="180" text-anchor="middle" font-size="12">Inverted Ovule (Micropyle near Funicle)</text>
    </svg>`,
    youtube: { title: "Megasporogenesis & Embryo Sac Animation", url: "https://www.youtube.com/results?search_query=megasporogenesis+3d+animation" },
    trivia: [
      "Embryo sac has 7 cells and 8 nuclei (Polygonum type).",
      "Synergids have filiform apparatus to guide pollen tubes.",
      "Most common ovule in angiosperms is Anatropous."
    ],
    mcqs: [
      { question: "The number of cells and nuclei in a mature embryo sac are:", options: ["7 cells, 8 nuclei", "8 cells, 8 nuclei", "7 cells, 7 nuclei", "6 cells, 8 nuclei"], correctIdx: 0, explanation: "It contains 3 antipodals, 2 synergids, 1 egg cell, and 1 central cell with 2 polar nuclei." },
      { question: "Filiform apparatus is characteristic of:", options: ["Antipodals", "Egg cell", "Synergids", "Central cell"], correctIdx: 2, explanation: "It is located at the micropylar end of synergids to guide the pollen tube." }
    ]
  },
  {
    id: "pollination",
    navTitle: "🐝 Pollination",
    title: "Pollination & Outbreeding Devices",
    content: "Pollination is the transfer of pollen from anther to stigma. It can be Autogamy (same flower), Geitonogamy (different flower, same plant), or Xenogamy (different plant). Outbreeding devices prevent self-pollination.",
    diagramLabel: "Agents of Pollination",
    diagram: `<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
      <rect x="20" y="20" width="80" height="40" fill="#bae6fd" rx="5"/>
      <text x="60" y="45" text-anchor="middle" font-size="12">Wind (Anemophily)</text>
      <rect x="110" y="20" width="80" height="40" fill="#fef9c3" rx="5"/>
      <text x="150" y="45" text-anchor="middle" font-size="12">Insects</text>
      <rect x="200" y="20" width="80" height="40" fill="#ccfbf1" rx="5"/>
      <text x="240" y="45" text-anchor="middle" font-size="12">Water</text>
    </svg>`,
    youtube: { title: "Pollination Mechanisms in Plants", url: "https://www.youtube.com/results?search_query=pollination+in+flowering+plants+animation" },
    trivia: [
      "Cleistogamy (flowers never open) ensures obligate autogamy.",
      "Zostera (sea grass) undergoes hypohydrophily (submerged pollination).",
      "Yucca plant and Pronuba moth have an obligate mutualistic relationship."
    ],
    mcqs: [
      { question: "Which flower shows cleistogamy?", options: ["Salvia", "Viola", "Vallisneria", "Maize"], correctIdx: 1, explanation: "Viola, Oxalis, and Commelina produce cleistogamous flowers." },
      { question: "In Zostera, pollination occurs by:", options: ["Wind", "Insects", "Submerged water", "Surface water"], correctIdx: 2, explanation: "Zostera uses hypohydrophily; pollen grains are long and ribbon-like." }
    ]
  },
  {
    id: "fertilisation",
    navTitle: "⚗️ Fertilisation",
    title: "Pollen-Pistil Interaction & Double Fertilisation",
    content: "After compatible pollination, the pollen tube grows through the style to the ovule. It enters the embryo sac via a synergid. Double fertilisation involves syngamy and triple fusion.",
    diagramLabel: "Double Fertilisation Process",
    diagram: `<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="150" cy="75" rx="50" ry="70" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
      <path d="M 50 130 L 120 130" stroke="green" stroke-width="3" stroke-dasharray="4"/>
      <text x="80" y="125" font-size="10">Pollen tube</text>
      <circle cx="150" cy="115" r="8" fill="red"/>
      <text x="170" y="120" font-size="10">Syngamy</text>
      <circle cx="150" cy="75" r="10" fill="blue"/>
      <text x="170" y="80" font-size="10">Triple Fusion</text>
    </svg>`,
    youtube: { title: "Double Fertilisation 3D Animation", url: "https://www.youtube.com/results?search_query=double+fertilisation+in+angiosperms+3d+animation" },
    trivia: [
      "Double fertilisation was discovered by Nawaschin (1898) in Lilium.",
      "Triple fusion yields the Primary Endosperm Nucleus (3n).",
      "Gymnosperms do not exhibit double fertilisation."
    ],
    mcqs: [
      { question: "The ploidy of endosperm in typical angiosperms is:", options: ["Haploid (n)", "Diploid (2n)", "Triploid (3n)", "Tetraploid (4n)"], correctIdx: 2, explanation: "It forms from the fusion of one male gamete and two polar nuclei." },
      { question: "Double fertilisation was first observed by Nawaschin in:", options: ["Lilium and Fritillaria", "Rosa and Hibiscus", "Triticum and Oryza", "Capsella"], correctIdx: 0, explanation: "Nawaschin observed this in Lilium and Fritillaria in 1898." }
    ]
  },
  {
    id: "seed",
    navTitle: "🌱 Seed",
    title: "Seed and Embryo Development",
    content: "Post-fertilisation, the zygote develops into the embryo and PEN into endosperm. The ovules mature into seeds and the ovary into a fruit. The endosperm may be completely consumed (ex-albuminous) or persist (albuminous).",
    diagramLabel: "Dicot vs Monocot Embryo",
    diagram: `<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
      <rect x="50" y="20" width="80" height="60" fill="#a3e635" rx="5"/>
      <text x="90" y="55" text-anchor="middle" font-size="12">Dicot (2 Cotyledons)</text>
      <rect x="170" y="20" width="80" height="60" fill="#fed7aa" rx="5"/>
      <text x="210" y="55" text-anchor="middle" font-size="12">Monocot (Scutellum)</text>
    </svg>`,
    youtube: { title: "Seed Germination and Embryo Development", url: "https://www.youtube.com/results?search_query=seed+development+class+12+animation" },
    trivia: [
      "Scutellum is the single shield-shaped cotyledon in monocots.",
      "Coconut water represents free-nuclear endosperm.",
      "Parthenocarpy is fruit formation without fertilisation (e.g., banana)."
    ],
    mcqs: [
      { question: "Coconut water represents which type of endosperm?", options: ["Free-nuclear", "Cellular", "Helobial", "Ruminate"], correctIdx: 0, explanation: "The liquid part is free-nuclear, while the white kernel is cellular endosperm." },
      { question: "In a monocot seed, the radicle is enclosed in:", options: ["Coleoptile", "Coleorhiza", "Scutellum", "Epiblast"], correctIdx: 1, explanation: "The radicle is covered by coleorhiza, while the plumule is covered by coleoptile." }
    ]
  },
  {
    id: "apomixis",
    navTitle: "🔬 Apomixis",
    title: "Apomixis and Polyembryony",
    content: "Apomixis is a form of asexual reproduction that mimics sexual reproduction, where seeds are formed without fertilisation. Polyembryony is the presence of more than one embryo in a seed.",
    diagramLabel: "Types of Apomixis",
    diagram: `<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
      <rect x="20" y="20" width="80" height="60" fill="#ede9fe" rx="5"/>
      <text x="60" y="55" text-anchor="middle" font-size="12">Diplospory</text>
      <rect x="110" y="20" width="80" height="60" fill="#fef3c7" rx="5"/>
      <text x="150" y="55" text-anchor="middle" font-size="12">Apospory</text>
      <rect x="200" y="20" width="80" height="60" fill="#fce7f3" rx="5"/>
      <text x="240" y="50" text-anchor="middle" font-size="10">Adventive</text>
      <text x="240" y="65" text-anchor="middle" font-size="10">Embryony</text>
    </svg>`,
    youtube: { title: "Apomixis & Polyembryony Explained", url: "https://www.youtube.com/results?search_query=apomixis+and+polyembryony+class+12" },
    trivia: [
      "Polyembryony in Citrus was discovered by Leeuwenhoek.",
      "Apomixis is agriculturally significant for maintaining hybrid vigour without buying new seeds.",
      "Orchid seeds are the smallest and most numerous seeds."
    ],
    mcqs: [
      { question: "Polyembryony through adventive embryony is most commonly seen in:", options: ["Wheat", "Orchids", "Citrus", "Pea"], correctIdx: 2, explanation: "Citrus seeds often contain multiple embryos originating from nucellar cells." },
      { question: "What is the agricultural significance of apomixis?", options: ["Increases genetic variation", "Maintains hybrid vigour", "Produces polyploid plants", "Promotes cross-pollination"], correctIdx: 1, explanation: "It helps fix hybrid characteristics across generations since it does not involve meiosis or fertilisation." }
    ]
  }
];
