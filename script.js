document.addEventListener('DOMContentLoaded', () => {
  renderNavigation();
  renderPages();
  // Show the first page by default
  showPage(topicsData[0].id);
});

function renderNavigation() {
  const nav = document.getElementById('nav-container');
  topicsData.forEach((topic, index) => {
    const btn = document.createElement('button');
    btn.className = 'topic-btn' + (index === 0 ? ' active' : '');
    btn.id = `nav-${topic.id}`;
    btn.textContent = topic.navTitle;
    btn.onclick = () => showPage(topic.id);
    nav.appendChild(btn);
  });
}

function renderPages() {
  const container = document.getElementById('content-container');
  topicsData.forEach((topic) => {
    const page = document.createElement('div');
    page.className = 'page';
    page.id = `page-${topic.id}`;
    
    // Header
    let html = `
      <div class="card">
        <h2 class="section-title">${topic.title}</h2>
        <p>${processClickableTerms(topic.content)}</p>
      </div>
    `;

    // Diagram (SVG String from data)
    if (topic.diagram) {
      html += `<div class="card" style="background:#f0fdf4; border-color:#16a06a; text-align:center;">
        <h4 style="color:#0d6e4a; margin-bottom:10px;">${topic.diagramLabel}</h4>
        ${topic.diagram}
      </div>`;
    }

    // YouTube Link
    if (topic.youtube) {
      html += `
        <a href="${topic.youtube.url}" target="_blank" class="yt-card">
          <div class="yt-icon">▶️</div>
          <div>
            <div style="font-size:0.8rem; color:#9f1239;">3D Animation Recommended</div>
            <div>${topic.youtube.title}</div>
          </div>
        </a>
      `;
    }

    // Trivia Bulb
    if (topic.trivia && topic.trivia.length > 0) {
      html += `
        <div class="bulb-trivia" id="trivia-${topic.id}">
          <div class="bulb-header" onclick="toggleTrivia('trivia-${topic.id}')">
            <span style="font-size:1.5rem">💡</span>
            <div class="bulb-label">NEET + Allen Trivia (Click to Expand)</div>
            <div class="bulb-arrow">▼</div>
          </div>
          <div class="bulb-body">
            <ul>
              ${topic.trivia.map(t => `<li>${processClickableTerms(t)}</li>`).join('')}
            </ul>
          </div>
        </div>
      `;
    }

    // MCQs
    if (topic.mcqs && topic.mcqs.length > 0) {
      html += `<div class="mcq-section"><h3 style="color:var(--violet); font-family:'Playfair Display'">Practice Questions (PYQ)</h3>`;
      topic.mcqs.forEach((mcq, qIdx) => {
        const itemId = `mcq-${topic.id}-${qIdx}`;
        html += `
          <div class="mcq-item" id="${itemId}">
            <p><strong>Q${qIdx + 1}:</strong> ${mcq.question}</p>
            <div class="mcq-options">
              ${mcq.options.map((opt, oIdx) => `
                <button class="mcq-opt" onclick="answerMCQ('${itemId}', this, ${oIdx === mcq.correctIdx})">${opt}</button>
              `).join('')}
            </div>
            <div class="mcq-ans">✓ ${mcq.explanation}</div>
          </div>
        `;
      });
      html += `</div>`;
    }

    page.innerHTML = html;
    container.appendChild(page);
  });
}

function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.topic-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(`page-${id}`).classList.add('active');
  document.getElementById(`nav-${id}`).classList.add('active');
  window.scrollTo(0,0);
}

function toggleTrivia(id) {
  const el = document.getElementById(id);
  el.classList.toggle('open');
}

function answerMCQ(itemId, btnEl, isCorrect) {
  const item = document.getElementById(itemId);
  // Disable all options in this question
  item.querySelectorAll('.mcq-opt').forEach(b => {
    b.disabled = true;
    b.style.cursor = 'default';
  });
  if (isCorrect) {
    btnEl.classList.add('correct');
  } else {
    btnEl.classList.add('wrong');
    // highlight correct one
    item.querySelectorAll('.mcq-opt').forEach((b, idx) => {
      // Find the correct button by triggering logic or we just show the explanation
    });
  }
  item.classList.add('revealed');
}

function processClickableTerms(text) {
  let processed = text;
  for (const term in termsDictionary) {
    const regex = new RegExp(`\\b${term}\\b`, 'gi');
    processed = processed.replace(regex, `<span class="term" onclick="openModal('${term}')">$&</span>`);
  }
  return processed;
}

function openModal(termKey) {
  const key = termKey.toLowerCase();
  const data = termsDictionary[key] || termsDictionary[Object.keys(termsDictionary).find(k => k.toLowerCase() === key)];
  if(data) {
    document.getElementById('modal-title').textContent = data.title;
    document.getElementById('modal-content').innerHTML = `<p>${data.content}</p>`;
    document.getElementById('term-modal').classList.add('open');
  }
}

function closeModal() {
  document.getElementById('term-modal').classList.remove('open');
}
