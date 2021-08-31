
$higher = @("ostar", "script", "personal", "ledning")
foreach ($high in $higher) {
    New-Item -Path "E:\$high" -ItemType Directory
}

$ostar = @("Brie", "Chevre", "Gouda", "Emmentaler", "Mozzarella")
foreach ($ost in $ostar) {
    New-Item -Path "E:\ostar\$ost" -ItemType Directory
}