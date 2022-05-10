'''list_doc_names.py

author: LG, Ludwig Geerman 2022 NL
tested: Adobe Photoshop Version: 23.3.1
os: win
'''

from win32com.client import Dispatch

ps = Dispatch("Photoshop.Application")
ps_docs = ps.Documents
ps_doc_names = (doc.Name for doc in ps_docs)
print(list(ps_doc_names))

