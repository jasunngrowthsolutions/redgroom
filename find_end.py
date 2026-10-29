with open('index.html') as f:
    content = f.read()
start = content.find('<script type="application/ld+json">')
end = content.find('</script>', start)
print('end index', end)
snippet = content[end-30:end+30].replace('\n',' ')
print(snippet)
