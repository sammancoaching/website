// Style audit: loads each page in a hidden iframe and tallies the computed
// styles the browser actually renders (colours, fonts, borders, radii...).
// It also lists text whose contrast against its background is below WCAG AA.
//
// Run it with style_audit.py, or paste this file into the DevTools console
// on any page of the running site and call:  await styleAudit(['/', '/contact.html'])

async function styleAudit(pages) {
  const luminance = rgb => {
    const v = rgb.map(x => { x /= 255; return x <= 0.03928 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4; });
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
  };
  const contrast = (a, b) => {
    const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
    return (hi + 0.05) / (lo + 0.05);
  };
  const parse = c => (c.match(/[\d.]+/g) || []).map(Number);
  const isTransparent = c => c === 'rgba(0, 0, 0, 0)' || c === 'transparent';

  // Nearest ancestor background, blending translucent layers onto what is below.
  const backgroundOf = (el, win) => {
    const layers = [];
    for (let e = el; e; e = e.parentElement) {
      const cs = win.getComputedStyle(e);
      if (cs.backgroundImage !== 'none') return null; // can't know what's behind text on an image
      if (!isTransparent(cs.backgroundColor)) {
        const [r, g, b, a = 1] = parse(cs.backgroundColor);
        layers.push([r, g, b, a]);
        if (a === 1) break;
      }
    }
    let result = [255, 255, 255];
    for (const [r, g, b, a] of layers.reverse()) {
      result = [r * a + result[0] * (1 - a), g * a + result[1] * (1 - a), b * a + result[2] * (1 - a)];
    }
    return result.map(Math.round);
  };

  const tally = {};
  const add = (category, value, page) => {
    tally[category] ??= {};
    tally[category][value] ??= { count: 0, pages: new Set() };
    tally[category][value].count++;
    tally[category][value].pages.add(page);
  };
  const perPage = {};
  const lowContrast = {};

  for (const page of pages) {
    const frame = document.createElement('iframe');
    frame.style.cssText = 'width:1280px;height:900px;position:absolute;left:-5000px;top:0';
    document.body.appendChild(frame);
    await new Promise(resolve => { frame.onload = resolve; frame.src = page; });
    await new Promise(resolve => setTimeout(resolve, 300)); // let web fonts and scripts settle
    const doc = frame.contentDocument, win = frame.contentWindow;
    const visible = [...doc.body.querySelectorAll('*')].filter(e => e.getClientRects().length);

    perPage[page] = {
      title: doc.title,
      elements: visible.length,
      inlineStyles: doc.querySelectorAll('body [style]').length,
      styleTags: doc.querySelectorAll('body style').length,
    };

    for (const el of visible) {
      const cs = win.getComputedStyle(el);
      const hasText = [...el.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim())
        || (el.tagName === 'INPUT' && el.placeholder);
      if (hasText) {
        add('text colour', cs.color, page);
        add('font', `${cs.fontFamily.split(',')[0]} ${cs.fontSize} weight ${cs.fontWeight}`, page);
        add('font size', cs.fontSize, page);
        add('font family', cs.fontFamily.split(',')[0], page);

        const bg = backgroundOf(el, win);
        if (bg) {
          const ratio = contrast(parse(cs.color).slice(0, 3), bg);
          const large = parseFloat(cs.fontSize) >= 24 || (parseFloat(cs.fontSize) >= 18.66 && Number(cs.fontWeight) >= 700);
          if (ratio < (large ? 3 : 4.5)) {
            const key = `${ratio.toFixed(2)}:1  ${cs.color} on rgb(${bg.join(', ')})${large ? ' (large text)' : ''}`;
            lowContrast[key] ??= { count: 0, pages: new Set(), examples: new Set() };
            lowContrast[key].count++;
            lowContrast[key].pages.add(page);
            if (lowContrast[key].examples.size < 3) lowContrast[key].examples.add(`${el.tagName.toLowerCase()} "${el.textContent.trim().slice(0, 25)}"`);
          }
        }
      }
      if (!isTransparent(cs.backgroundColor)) add('background', cs.backgroundColor, page);
      if (cs.borderTopStyle !== 'none' && cs.borderTopWidth !== '0px') add('border', `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`, page);
      if (cs.borderTopLeftRadius !== '0px') add('radius', cs.borderTopLeftRadius, page);
      if (cs.boxShadow !== 'none') add('shadow', cs.boxShadow, page);
      if (/^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(el.tagName) && (!isTransparent(cs.backgroundColor) || cs.borderTopWidth !== '0px')) {
        add('control', `<${el.tagName.toLowerCase()} class="${el.className}">  bg ${cs.backgroundColor}  text ${cs.color}  border ${cs.borderTopWidth} ${cs.borderTopColor}  radius ${cs.borderTopLeftRadius}  ${cs.fontFamily.split(',')[0]} ${cs.fontSize}`, page);
      }
    }
    frame.remove();
  }

  const sorted = (map, extra = () => ({})) => Object.entries(map)
    .sort((a, b) => b[1].count - a[1].count)
    .map(([value, o]) => ({ value, count: o.count, pages: [...o.pages], ...extra(o) }));
  const categories = {};
  for (const [category, values] of Object.entries(tally)) categories[category] = sorted(values);
  return {
    perPage,
    categories,
    lowContrast: sorted(lowContrast, o => ({ examples: [...o.examples] })),
  };
}
