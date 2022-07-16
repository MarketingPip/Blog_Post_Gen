import codecs

import re as regex
## Menu Settings File

permalinks_file= "navlinks.md"
permalinks_file_contents = None

## Get each link in file & add to menu
menu=""
pattern = 'Link:(.*?) New_Window:(.*?) Title:(.*?) Position:(.*?)'
with open(permalinks_file) as f:
  file_contents = f.read()
  for (link, window, title, position) in regex.findall(pattern, file_contents, regex.DOTALL):
    if window == "True":
      Open_New_Window = "__target blank"
    else:
      Open_New_Window = "__target blank"
    if link == "null":
      link = ""
    else:
      link = link
    menu += f"""{position}<a href="{link}" {Open_New_Window}>{title}</a>"""  

# Open Index File Content
index_file_contents = ".github/index.md"
try:
    with open(index_file_contents, 'r') as f:
        index_file_contents = f.read()
        
        
except IOError:
    sys.exit('Input file does not exist, or has no content.  Exiting')

index_file_name = "pages/documentation.html"
    
# Write out index.html file    
try:
    with codecs.open(index_file_name, 'w', encoding='utf-8') as f:
        f.write(f"""
        <head>
         <meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Simply Docs Demo | Home</title>
<script src="/Blog_Post_Gen/assets/js/toc-generator.js"></script>   
<meta name="description" content="A showcase of Simply Docs by MarketingPipeline built using Simple.CSS">
<link rel="stylesheet" href="/Blog_Post_Gen//assets/style.css">
</head>
        
        <header>
   <nav>
  {menu}
</nav>
      <h1>Simply Docs</h1>
 
    </header>
<main>
      <fieldset>
        <!--
        Every fieldset must contain a legend. IE barfs if it's not there.
        It's no fun.
        -->
        <legend>Table Of Contents</legend>
        
      
<ul id="toc">

</ul>

 {index_file_contents}

        
        
      </fieldset>
<a href="https://github.com/MarketingPipeline/Simply-Docs/archive/refs/heads/main.zip"><button>Download This Template</button></a>
<footer>
      <p>Simply Docs was created by <a href="https://github.com/MarketingPipeline/">Marketing Pipeline</a> and is licensed under the MIT license.</p>
  <small>© 2014 Some company name</small>
      <address>email@email.com</address>
    </footer>
   
 <script src="https://cdn.jsdelivr.net/gh/MarketingPipeline/Markdown-Tag/markdown-tag.js"></script> 
        """)
except IOError:
    sys.exit('Input file does not exist, or has no content.  Exiting')  