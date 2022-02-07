# -*- mode: python

#from PyInstaller.utils.hooks import collect_submodules

#from PyInstaller.utils.hooks import collect_data_files

#import pkgutil

#hiddenimports = collect_submodules('sklearn')


block_cipher = None
datas = []
#datas+=collect_data_files("it_core_news_sm")

#datas += pkgutil.get_data('it_core_news_sm','it_core_news_sm-3.2.0\\ner\\model')


a = Analysis(['PugliaSostenibile_GUI.py'],
             pathex=["C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI"],
             binaries=[],
             datas=datas,
             hiddenimports=["sklearn.tree._utils", "sklearn.neighbors.quad_tree","sklearn.utils._typedefs", "sklearn.utils._cython_blas", "sklearn.neighbors.typedefs", "sklearn.neighbors._typedefs"],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)



a.datas += [
("SDGs\\SDGs_indicatori.json","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\SDGs\\SDGs_indicatori.json", "Data"),
("SDGs\\SDGs_json.json","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\SDGs\\SDGs_json.json", "Data"),
("VOCAB\\ngram\\vocabulary_1.xlsx","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\VOCAB\\ngram\\vocabulary_1.xlsx","Data"),
("VOCAB\\vocabulary.xlsx","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\VOCAB\\vocabulary.xlsx","Data"),
("LEMMAS\\lemma_sdgs.xlsx","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\LEMMAS\\lemma_sdgs.xlsx","Data"),
("LEMMAS\\lemma_targets.xlsx","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\LEMMAS\\lemma_targets.xlsx","Data"),
("utils\\images\\PugliaSostenibile2200x2239.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\PugliaSostenibile2200x2239.png","Data"),
("utils\\images\\COLORPugliaSostenibile175x161.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\COLORPugliaSostenibile175x161.png","Data"),
("utils\\images\\PugliaSostenibileICO.ico","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\PugliaSostenibileICO.ico","Data"),
("utils\\images\\COLORPugliaSostenibile200x184.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\COLORPugliaSostenibile200x184.png","Data"),
("utils\\images\\PugliaSostenibileICO_black.ico","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\PugliaSostenibileICO_black.ico","Data"),
("utils\\images\\sdgline108x2000.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\sdgline108x2000.png","Data"),
("utils\\images\\welcome_new.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\welcome_new.png","Data"),
("utils\\images\\COLORPugliaSostenibile450x415.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\COLORPugliaSostenibile450x415.png","Data"),
("utils\\images\\SDG\\SDG_Poster_#nonUN-IT500x290.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\SDG_Poster_#nonUN-IT500x290.png","Data"),
("utils\\images\\collab\\trio_collab500x162.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\collab\\trio_collab500x162.png","Data"),
("utils\\images\\COLORPugliaSostenibile300x276.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\COLORPugliaSostenibile300x276.png","Data"),
("Agenda2030\\Agenda-2030-Onu-italia.pdf","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\Agenda2030\\Agenda-2030-Onu-italia.pdf","Data"),
("utils\\images\\SDG\\goals\\1.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\1.png","Data"),
("utils\\images\\SDG\\goals\\2.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\2.png","Data"),
("utils\\images\\SDG\\goals\\3.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\3.png","Data"),
("utils\\images\\SDG\\goals\\4.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\4.png","Data"),
("utils\\images\\SDG\\goals\\5.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\5.png","Data"),
("utils\\images\\SDG\\goals\\6.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\6.png","Data"),
("utils\\images\\SDG\\goals\\7.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\7.png","Data"),
("utils\\images\\SDG\\goals\\8.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\8.png","Data"),
("utils\\images\\SDG\\goals\\9.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\9.png","Data"),
("utils\\images\\SDG\\goals\\10.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\10.png","Data"),
("utils\\images\\SDG\\goals\\11.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\11.png","Data"),
("utils\\images\\SDG\\goals\\12.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\12.png","Data"),
("utils\\images\\SDG\\goals\\13.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\13.png","Data"),
("utils\\images\\SDG\\goals\\14.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\14.png","Data"),
("utils\\images\\SDG\\goals\\15.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\15.png","Data"),
("utils\\images\\SDG\\goals\\16.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\16.png","Data"),
("utils\\images\\SDG\\goals\\17.png","C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\SDG\\goals\\17.png","Data")
]


for d in a.datas:
    if '_C.cp39-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break


		
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='PugliaSostenibile.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\PUGLIA_SOSTENIBILE_GUI\\PugliaSostenibileGUI\\utils\\images\\PugliaSostenibileICO_black.ico')
