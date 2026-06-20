import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Make navs sticky and glassmorphic
    content = re.sub(
        r'class="([^"]*?)border-b\s+bg-white([^"]*?)"',
        r'class="\1border-b bg-white/80 backdrop-blur-md sticky top-0 z-50\2"',
        content
    )
    content = re.sub(
        r'class="([^"]*?)border-b\s+bg-blue-50([^"]*?)"',
        r'class="\1border-b bg-blue-50/80 backdrop-blur-md sticky top-0 z-50\2"',
        content
    )

    # Logo styling
    content = re.sub(
        r'<a href="#" class="font-bold text-4xl">\s*<span class="text-green-500">zero</span> hunger\s*</a>',
        r'<a href="#" class="font-bold text-4xl tracking-tight text-slate-800">\n              <span class="bg-clip-text text-transparent bg-gradient-to-r from-emerald-500 to-teal-400">zero</span> hunger\n            </a>',
        content
    )

    # Donate buttons styling
    content = re.sub(
        r'<a\s+class="text-xl cursor-pointer font-semibold hover:text-green-600 donate-link"\s*>Donate ❤</a>',
        r'<a\n              class="text-lg cursor-pointer font-semibold bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-5 py-2 rounded-full shadow-md hover:shadow-lg hover:shadow-emerald-500/40 hover:-translate-y-0.5 transition-all duration-300 donate-link"\n              >Donate ❤</a>',
        content
    )
    # also the footer donate links which have hover:text-green-600 font-bold
    content = re.sub(
        r'<a\s+class="text-xl cursor-pointer hover:text-green-600 font-bold donate-link"\s*>Donate ❤</a>',
        r'<a\n              class="text-lg cursor-pointer font-bold bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-5 py-2 rounded-full shadow-md hover:shadow-lg hover:shadow-emerald-500/40 hover:-translate-y-0.5 transition-all duration-300 donate-link"\n              >Donate ❤</a>',
        content
    )

    # Availability cards hover effect
    content = re.sub(
        r'class="flex bg-white p-4 border-2 flex-col md:flex-row max-w-xl mx-auto gap-6 rounded-md my-10"',
        r'class="flex bg-white p-4 border flex-col md:flex-row max-w-xl mx-auto gap-6 rounded-xl my-10 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300"',
        content
    )

    # Inputs focus rings
    content = re.sub(
        r'outline-1 border-2 border-green-700 outline-green-700',
        r'border-2 border-slate-300 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200 outline-none transition-all',
        content
    )
    content = re.sub(
        r'border-2 border-green-700 outline-1 outline-green-800',
        r'border-2 border-slate-300 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200 outline-none transition-all',
        content
    )
    content = re.sub(
        r'border-2 border-green-700 outline-1 outline-green-700',
        r'border-2 border-slate-300 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200 outline-none transition-all',
        content
    )
    content = re.sub(
        r'border-2 border-green-700 px-4 py-2 outline-1 outline-green-700',
        r'border-2 border-slate-300 px-4 py-2 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200 outline-none transition-all',
        content
    )

    # Submit buttons
    content = re.sub(
        r'bg-green-900 bg-opacity-90 hover:bg-opacity-100',
        r'bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 shadow-lg hover:shadow-xl hover:-translate-y-0.5',
        content
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_html()
