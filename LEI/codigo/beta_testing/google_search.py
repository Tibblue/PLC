
import os
os.chdir("/mnt/c/Users/raulv/OneDrive/Ambiente de Trabalho/Git/PLC/LEI/codigo/outros/Google-Search-API")
import google

num_page = 3
search_results = google.search("This is my query", num_page)
for result in search_results:
    print(result.description)