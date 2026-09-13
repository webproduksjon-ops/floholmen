document.addEventListener('DOMContentLoaded', () => {
  const current = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
  const aliases = {
    'cncmaskinering.html': 'cnc-maskinering.html',
    'mekanisk_verksted.html': 'mekanisk-verksted.html',
    'omoss.html': 'om-oss.html'
  };
  const normalized = aliases[current] || current;

  document.querySelectorAll('.navlinks a[href]').forEach((link) => {
    const target = link.getAttribute('href').split('#')[0].toLowerCase();
    if (target && target !== '#' && (target === normalized || aliases[target] === normalized)) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
});
