document.addEventListener('DOMContentLoaded', () => {
  const current = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
  const aliases = {
    'cncmaskinering.html': 'cnc-maskinering.html',
    'mekanisk_verksted.html': 'mekanisk-verksted.html',
    'omoss.html': 'om-oss.html'
  };
  const servicePages = new Set(['cnc-maskinering.html', 'cncmaskinering.html', 'elektromotorer.html', 'mekanisk-verksted.html', 'mekanisk_verksted.html']);
  const normalized = servicePages.has(current) ? 'index.html#tjenester' : (aliases[current] || current);

  document.querySelectorAll('.navlinks a[href]').forEach((link) => {
    const rawTarget = link.getAttribute('href').toLowerCase();
    const target = rawTarget.includes('#tjenester') ? 'index.html#tjenester' : rawTarget.split('#')[0];
    if (target && target !== '#' && (target === normalized || target === 'index.html#tjenester' && normalized === 'index.html#tjenester' || aliases[target] === normalized)) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
});
