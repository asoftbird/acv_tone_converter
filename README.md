# CSV to ACV converter

Mostly just a little tool made to convert dot gain compensation curves from https://cielab.xyz/dlp/ to ACV files that Photoshop (and printer RIP software) can read.
Currently, you'll need to edit the filename to import and export in main.py itself. 
It's very janky and hacked together to fit a specific use case, so you may not get any use out of it.

ACV file format spec: https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/#50577411_pgfId-1056330

Eventually I'll just make a command line version that supports this, but for now this suffices.
