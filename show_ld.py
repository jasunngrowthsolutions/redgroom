import re
with open('index.html') as f:
    content = f.read()
b = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL).group(1)
with open('ld_full.json','w') as out:
    out.write(b)
print('written', len(b))
