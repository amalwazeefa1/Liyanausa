
with open('assets/css/style.css', 'r') as f:
    content = f.read()

new_content = content.replace('@media (min-width: 1371px)', '@media (min-width: 768px)').replace('@media (max-width: 1370px)', '@media (max-width: 767.98px)')

if new_content != content:
    with open('assets/css/style.css', 'w') as f:
        f.write(new_content)
    print("Updated CSS to apply flex layout for dropdowns on tablets.")
else:
    print("Could not find the specified media queries to update.")
