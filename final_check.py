with open('index.html') as f:
    content = f.read()
print('tailwind.config occurrences:', content.count('tailwind.config'))
print('FAQPage present:', 'FAQPage' in content)
print('luxury shadow in config:', "'luxury'" in content)
print('shadow-gold-glow in config:', "'gold-glow'" in content)
