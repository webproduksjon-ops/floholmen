from pathlib import Path
root=Path('/tmp/floholmen')
# Make every primary navigation option visible on the homepage.
p=root/'index.html'; s=p.read_text(encoding='utf-8')
s=s.replace('<nav class="navlinks" aria-label="Hovedmeny"><a href="#tjenester">Tjenester</a><a href="om-oss.html">Om oss</a><a href="kontakt.html" class="cta">Ta kontakt ↗</a></nav>', '<nav class="navlinks" aria-label="Hovedmeny"><a href="tjenester.html">Tjenester</a><a href="om-oss.html">Om oss</a><a href="maskinpark.html">Maskinpark</a><a href="referanser.html">Referanser</a><a href="kontakt.html" class="cta">Ta kontakt ↗</a></nav>')
p.write_text(s, encoding='utf-8')
# Keep all navigation links available on small screens as a second, horizontally scrollable row.
p=root/'styles.css'; s=p.read_text(encoding='utf-8')
s=s.replace('.nav{height:72px}.navlinks{gap:12px}.navlinks a:not(.cta){display:none}', '.nav{height:auto;min-height:72px;padding:14px 0;align-items:flex-start;flex-wrap:wrap;gap:10px}.navlinks{width:100%;order:3;overflow-x:auto;justify-content:flex-start;gap:18px;padding-bottom:4px}.navlinks a{display:block!important;white-space:nowrap}')
p.write_text(s, encoding='utf-8')
# Replace generic captions with descriptions from the supplied machine-park screenshot.
machine_caps=[
'Platesaks max 3 150x6,3mm','Stansemaskin Schuler 50 tonn','Planslipemaskin 200x600mm.','Rundslipemaskin Johanson 24-C, utvendig sliping Ø230x1 500mm, innvendig sliping Ø200x350mm','Tannstikkemaskin FELLOWS 7125A, Ø250 MODUL 4,5.','Fresemaskin TOS FA4AU/CH, max kapasitet 1000x300 mm.','Boremaskin Roboma 12 UHI 1250','Revolverdreiebenk MAS R5, max kapasitet Ø310x750mm','CNC Maskineringssenter CINCINNATI','CNC Dreiebenk Okuma LC20, max kapasitet Ø300mm','Dossan Puma 400 LM – Dreiebenk. På cnc maskinering i form av dreiing, innehar vi alt fra små enkle cnc styrte dreiebenker til avanserte dreiesenter med verktøyveksler og 3 akser.','Bomar Sagemaskin']
p=root/'maskinpark.html'; s=p.read_text(encoding='utf-8')
for i,cap in enumerate(machine_caps,1):
    s=s.replace(f'<figcaption>Maskinpark · {i:02d}</figcaption>', f'<figcaption>{cap}</figcaption>')
p.write_text(s, encoding='utf-8')
# Replace generic captions with the reference descriptions from the supplied screenshot.
ref_files=[1,2,3,5,6,7,8,9,10,11]
ref_caps=['Heistrommel vaier for industri','Fjører for motor og girkasser','Akslinger/drivakslinger og tannhjul for girkasser','Kulelager – Trøstelager – Nålelager – Drivere','Kran / Reparasjon av kranmotorer til industri og båt','Reparasjon av kraner og heistromler','Reparasjon av kraner og heistromler','FF Launch simulation test systems','FF Launch simulation test systems','FF Launch simulation test systems']
p=root/'referanser.html'; s=p.read_text(encoding='utf-8')
for i,cap in zip(ref_files,ref_caps):
    s=s.replace(f'<figcaption>Leveranse fra Fløholmen</figcaption>', f'<figcaption>{cap}</figcaption>', 1)
p.write_text(s, encoding='utf-8')
