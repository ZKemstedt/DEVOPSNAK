﻿# $ostar = @("Brie", "Chevre", "Gouda", "Emmentaler", "Mozzarella")
# foreach ($ost in $ostar) {
#     Remove-Item "E:\ostar\$ost"
# }

$higher = @("ostar", "personal", "ledning")
foreach ($high in $higher) {
    Remove-Item "E:\$high" -Recurse
}

