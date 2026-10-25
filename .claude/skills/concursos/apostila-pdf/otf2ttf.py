# Converte as fontes Inter (OTF/CFF) para TTF com outro nome de família.
# Sem isso o Chromium embute a Inter como Type 3: PDF pesado e texto ruim de selecionar.
# uso: python3 -I otf2ttf.py Inter-Regular Inter-Italic ... (ver README.md)
import sys,os
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
def conv(src,dst,fam):
    f=TTFont(src); gs=f.getGlyphSet(); order=f.getGlyphOrder(); glyf={}
    for g in order:
        p=TTGlyphPen(gs); gs[g].draw(Cu2QuPen(p,1.0,reverse_direction=True)); glyf[g]=p.glyph()
    f['loca']=newTable('loca'); t=f['glyf']=newTable('glyf'); t.glyphOrder=order; t.glyphs=glyf
    del f['CFF ']
    if 'VORG' in f: del f['VORG']
    f['maxp']=newTable('maxp'); m=f['maxp']; m.tableVersion=0x00010000
    for k in ['maxZones','maxTwilightPoints','maxStorage','maxFunctionDefs','maxInstructionDefs','maxStackElements','maxSizeOfInstructions','maxComponentElements']: setattr(m,k,0)
    m.maxZones=1
    f['head'].glyphDataFormat=0; f.sfntVersion='\x00\x01\x00\x00'
    for r in f['name'].names:
        if r.nameID in (1,4,6,16):
            s=r.toUnicode().replace('Inter Display','InterTT Display').replace('InterDisplay','InterTTDisplay')
            if 'TT' not in s: s=s.replace('Inter','InterTT')
            r.string=s
    f.save(dst)
d='/usr/share/fonts/opentype/inter/'
for n in sys.argv[1:]:
    conv(d+n+'.otf',os.path.expanduser('~/.fonts/'+n.replace('Inter','InterTT')+'.ttf'),None)
