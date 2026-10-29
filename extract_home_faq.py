import re
with open('index.html') as f:
    content = f.read()
# Home section FAQ accordions
start = content.find('Quick Answers')
# find next major section after faq accordions
end = content.find('<!-- VIEW 2:', start)
section = content[start:end]
buttons = re.findall(r'<button[^>]*onclick="toggleAccordion\(this\)"[^>]*>\s*<span>(.*?)</span>', section, re.DOTALL)
answers = re.findall(r'<div class="accordion-inner px-6 pb-5 text-xs text-gray-300 leading-relaxed">(.*?)</div>', section, re.DOTALL)
print('Home Q:', len(buttons), 'A:', len(answers))
for i in range(min(len(buttons), len(answers))):
    q = re.sub(r'<.*?>', '', buttons[i]).strip()
    a = re.sub(r'<.*?>', '', answers[i]).strip()
    print(i+1, '|', q[:120])
    print('  ', a[:140].replace('\n',' '))
