import regex as re

xml_EN_PT = '''<xml>
  <body>
    <tu>
      <seg xml:lang="EN">The cat is sleeping</seg>
      <seg xml:lang="PT">O gato esta a dormir</seg>
    </tu>
    <tu>
      <seg xml:lang="EN">The cat is dead</seg>
      <seg xml:lang="PT">O gato esta a morto</seg>
    </tu>
  </body>
</xml>'''

xml_PT_ES = '''<xml>
  <body>
    <tu>
      <seg xml:lang="PT">O gato esta a dormir</seg>
      <seg xml:lang="ES">El gato esta dormindo</seg>
    </tu>
    <tu>
      <seg xml:lang="PT">O gato esta a morto</seg>
      <seg xml:lang="ES">El gato esta morrido</seg>
    </tu>
  </body>
</xml>'''

def join_tmx(texto12,texto23):
  split12 = texto12.split('<body>')
  split12 = split12[1].split('</body>')
  split12 = split12[0]
  print(split12)

  split23 = texto23.split('<body>')
  split23 = split23[1].split('</body>')
  split23 = split23[0]
  print(split23)

  tus12 = re.findall(r'<tu>\n*(.+)\n*(.+)',split12)
  tus23 = re.findall(r'<tu>\n*(.+)\n*(.+)',split23)
  print(tus12)
  print(tus23)



print(join_tmx(xml_EN_PT,xml_PT_ES))