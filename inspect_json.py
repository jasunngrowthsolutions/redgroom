import re
with open('index.html') as f:
    content = f.read()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
print('Blocks:', len(blocks))
for i,b in enumerate(blocks):
    snippet = b[:700].replace('\n',' ')
    print('BLOCK', i, 'len', len(b), '|', snippet)
