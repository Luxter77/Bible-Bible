Clear-Host;

$out = "Bible-Bible-v1.zip";

$outpath = "C:\Users\Lucas\AppData\Roaming\.minecraft\saves\Test-Site\datapacks\";

.\biblier.minecraft.py;

Remove-Item ".\$out" -ErrorAction Ignore;

babel.py -c ".\$out";

".\$out";

Copy-Item -Force -Verbose ".\$out" "$outpath\$out";
