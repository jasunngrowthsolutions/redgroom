import re
with open('index.html') as f:
    content = f.read()
start = content.find('id="view-faq"')
end = content.find('<!-- JASUNN Footer -->', start)
section = content[start:end]
buttons = re.findall(r'<button[^>]*onclick="toggleAccordion\(this\)"[^>]*>\s*<span>(.*?)</span>', section, re.DOTALL)
answers = re.findall(r'<div class="accordion-inner px-6 pb-6 text-sm text-gray-600 leading-relaxed">(.*?)</div>', section, re.DOTALL)
print('Q:', len(buttons), 'A:', len(answers))
for i in range(min(len(buttons), len(answers))):
    q = re.sub(r'<.*?>', '', buttons[i]).strip()
    a = re.sub(r'<.*?>', '', answers[i]).strip()
    print(i+1, '|', q[:120])
    print('  ', a[:140].replace('\n',' '))
