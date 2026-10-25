const { chromium } = require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{
  // uso: RODAPE='Sintaxe · CEBRASPE' node render.js <pasta-saida> corpo1.html [corpo2.html ...]
  const b=await chromium.launch(); const dir=process.argv[2];
  const css=fs.readFileSync(path.join(__dirname,'base.css'),'utf8');
  for (const f of process.argv.slice(3)){
    const body=fs.readFileSync(f,'utf8');
    const html=`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`;
    const tmp=f.replace(/\.html$/,'.full.html'); fs.writeFileSync(tmp,html); const p=await b.newPage(); await p.goto('file://'+path.resolve(tmp),{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
    const out=path.join(dir,path.basename(f).replace(/\.html$/,'.pdf'));
    await p.pdf({path:out,format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
      footerTemplate:'<div style="font-family:DejaVu Sans,sans-serif;font-size:7.5pt;color:#8a90a2;width:100%;padding:0 15mm;display:flex;justify-content:space-between"><span>'+(process.env.RODAPE||'CEBRASPE — material direcionado')+'</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>',
      margin:{top:'16mm',bottom:'18mm',left:'15mm',right:'15mm'}});
    await p.close(); console.log(out, fs.statSync(out).size);
  }
  await b.close();
})();
