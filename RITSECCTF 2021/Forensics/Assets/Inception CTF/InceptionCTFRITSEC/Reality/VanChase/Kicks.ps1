set-alias laylow "$env:ProgramFiles\7-Zip\7z.exe"
$7zf = "TheHotel.7z"
$7zp = "WaterUnderTheBridge" # <---- Enter Password inbetween the Double Qoutes
$7zo = "-aoa"
laylow x $7zf "-p$7zp" $7zo
Start-Sleep -s 3
New-Item -Path $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\ -Name TheHotel -ItemType "directory"
Start-Sleep -s 3
Move-Item -Path $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\ThePointMan.txt -Destination $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\TheHotel\ThePointMan.txt
Move-Item -Path $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\‎ -Destination $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\TheHotel\‎
Move-Item -Path $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\SnowFortress.7z -Destination $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\TheHotel\SnowFortress.7z
Start-Sleep -s 3
cd $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\TheHotel\ | cmd.exe --% /c type ‎ > ThePointMan.txt:‎
Remove-Item -Path $env:userprofile\Desktop\InceptionCTF\Reality\VanChase\TheHotel\‎
