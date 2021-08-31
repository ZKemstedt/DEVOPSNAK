# Hand-in excersize 2

## pdftosite.sh
```sh
#!/bin/bash

# Generates the main index.html file
generateIndexHTML() {
	pagesHTML=""
	for ((i=1; i<=$pagecount; i++)); do
		pagesHTML="$pagesHTML<a href=\"page$i/index.html\">page$i</a><br/>"
	done
	
	cat <<HTML >> "$destination/index.html"
<!DOCTYPE html>
<html>
 <head>
  <meta charset="UTF-8">
  <title>$title</title>
 </head>
 <body>
  $pagesHTML	 
 </body>
HTML
}

# Generates an HTML file with the given
# "title", "text" and "images".
# The resulting file is written to "dest"
# The "images" argument contains a list of
# image files, assumed to sit next to the
# generated HTML file.
generatePageHTML() {
    local title=$1
    local text=$2
    local images=$3
    local dest=$4
    
    imageHTML=""
    
    for image in $images; do
        imageHTML="$imageHTML <img src=\"$(basename $image)\"/>"
    done
    
    cat <<HTML > "$dest"
<!DOCTYPE html>
<html>
 <head>
  <meta charset="UTF-8">
  <title>$title</title>
  <style>
   img {
    border: 1px solid black;
   }
  </style>
 </head>
 <body>
  <pre>
$text
  </pre>
  $imageHTML
 </body>
</html>
HTML
}

extractImages() {
	local dest="$destination/page$1"

	# extract and process images
	pdfimages -all -f $1 -l $1 "$pdf" "$dest/img"
	for img in $(ls "$dest"); do
		if [[ $img == *.jpg ]]; then
			jpegtopnm "$dest/$img" -quiet >> "$dest/$img.t"
		elif [[ $img == *.png ]]; then
			pngtopnm "$dest/$img" -quiet >> "$dest/$img.t"
		fi
	done
	for img in $(ls "$dest" | egrep *[.]t); do
 		pnmscale $dest/$img -width=600 | ppmtopgm | ppmtojpeg > "$dest/$img.jpeg"
	done

	# remove temporary files
	rm -f $dest/*.t
	rm -f $dest/*.png
	rm -f $dest/*.jpg

	# return the imagefiles
	ls $dest | egrep *[.]jpeg
}

exportPage() {
    # create target folder
	mkdir "$destination/page$1"
	local html="$destination/page$1/index.html"

    # call extractImages
	local images=$(extractImages $1)

    # use "pdftotext" to extract the text from a single page:
	local text="$(pdftotext -f "$1" -l "$1" "$pdf" -)"
	local title="$(echo "$text" | head -n 1)"

	# call generatePageHTML
	generatePageHTML "$title" "$text" "$images" "$html"
}

debug() {
	local msg=$1
	echo "(debug) $msg"
}

main() {
 	pdf=$1
    destination=$2

	if [ -z "$pdf" ] | [ -z "$destination" ]; then
		echo "Usage: pdftosite <pdf> <destination>"
		exit 1
	fi

	if [ -d "$destination" ]; then
		echo "The path '$destination' already exists!"
		exit 1
	else
		mkdir "$destination"
	fi
	
	pagecount=$(pdfinfo "$pdf" | grep "Pages:" | awk '{print $2}')
	if [ -z "$pagecount" ]; then
		echo "Invalid pdf!"
		exit 1
	fi
	
	title=$(basename "$pdf")
	title=${title%.pdf}

	# then run "exportPage" for each page
	for ((i=1; i<=$pagecount; i++)); do
		exportPage $i
	done

	# create main index
	generateIndexHTML 
}


main "$1" "$2"
```


## servepdf.sh
```sh
#/bin/bash

folder=~/.zeketempservepdf
pdf=$1
port=$2

# assert called correctly
if [ -z "$1" ] | [ -z "$2" ]; then
	echo "usage: ./servepdf <pdf> <port>"
	exit 1
elif [ "$2" -lt 1024 ] | [ "$2" -gt 65535 ]; then # also triggers for non-numeric $2
	echo "invalid port: $port"
	exit 1
elif [ ! -f "$pdf" ]; then
	echo "invalid pdf!"
	exit 1
fi

# remove data from last run if it exists
if [ -d $folder ]; then
	echo "$folder exists, removing..."
	rm -r $folder
fi

# create site
echo -n "creating site..."
# I tried to make pdftosite propogate errors and
# servepdf to handle those errors but I couldn't
# make it work in time (writing this at april 7 23:35)
ret=$(./pdftosite.sh "$pdf" "$folder")
if [ ! $? ]; then
	echo "$ret"
	exit 1
else
	echo "done"
fi

# serve site
echo "serving $pdf to port $port" 
cd $folder # lul :)
python3 -mhttp.server $port > $folder/server.log 2>&1
```