import re, json
with open('index.html') as f:
    content = f.read()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
print('Blocks:', len(blocks))
for i,b in enumerate(blocks):
    try:
        data = json.loads(b)
        print('Block', i, 'valid', data.get('@type') if isinstance(data, dict) else 'list')
    except Exception as e:
        print('Block', i, 'INVALID', str(e)[:200])
