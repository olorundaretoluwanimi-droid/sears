#!/bin/sh
# Archive material for "What Happened to Sears?" — public domain, CC0 or CC BY only (licences logged in SOURCES.jsonl).
cd "$(dirname "$0")/.." || exit 1
PY=${PY:-python -I}
F="$PY tools/footage.py fetch"
big() {   # name, commons file title, credit, licence, width
  ls raw/$1.* >/dev/null 2>&1 && return 0
  enc=$($PY -c "import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1].replace(' ','_')))" "$2")
  $F "https://commons.wikimedia.org/wiki/Special:FilePath/$enc?width=${5:-2600}" --name "$1" \
    --page "https://commons.wikimedia.org/wiki/File:$enc" --license "$4" --credit "$3"; sleep 2
}
PD="Public domain"
big sears_portrait "Richard Warren Sears.jpg" "Richard W. Sears, c. 1890–1910" "$PD" 1966
big sears_young "Richardsears-young.jpeg" "Richard W. Sears as a young man" "$PD" 216
big roebuck "AlvahRoebuck.jpg" "Alvah C. Roebuck, c. 1890–1910" "$PD" 548
big rosenwald1919 "Julius Rosenwald, Pres. of Sears Roebuck LCCN2016827305.jpg" "National Photo Company, 1919 (Library of Congress)" "$PD" 2600
big trio1895 "R.W. Sears, president - A.E. Nusbaum, treas. and gen'l. manager - J. Rosenwald, vice president LCCN2015645507.jpg" "1895 (Library of Congress)" "$PD" 3600
big ad1888 "RW Sears Watch Advertisement 1888.jpg" "Winchester Journal, Indiana, 5 Jan 1888" "$PD" 569
R="Sears, Roebuck and Co., 1906 booklet; scan Richard from USA (CC BY 2.0)"
big p1906_desk "Mr Sears - President of Sears Roebuck at his desk 1906 (6043566777).jpg" "$R" "CC BY 2.0" 2076
big p1906_trainshed "Train Shed and Shipping Rooms - Sears Roebuck Chicago ILL 1906 (6043968718).jpg" "$R" "CC BY 2.0" 2076
big p1906_yards "Railroad Yards - Sears Roebuck Chicago ILL 1906 (6044034910).jpg" "$R" "CC BY 2.0" 2076
big p1906_general "General View - Sears Roebuck Chicago ILL 1906 (6043576301).jpg" "$R" "CC BY 2.0" 2076
big p1906_merch "Merchandise Building - Sears Roebuck Chicago ILL 1906 (6043596175).jpg" "$R" "CC BY 2.0" 2076
big p1906_noon "On the Street at Noon - Sears Roebuck Chicago ILL 1906 (6043313379).jpg" "$R" "CC BY 2.0" 2076
big p1906_cafe "Girls Cafeteria - Sears Roebuck Chicago ILL 1906 (6042645881).jpg" "$R" "CC BY 2.0" 2076
H="Historic American Buildings Survey (Library of Congress)"
big habs_conveyors "THIRD FLOOR, SHIPPING COURT, VIEW OF CONVEYORS FROM SUPERVISOR'S PLATFORM - Sears Roebuck and Company Mail Order Plant, Merchandise Building, 924 South Homan Avenue, Chicago, HABS ILL,16-CHIG,110A-65.tif" "$H" "$PD" 3600
big habs_tower "TOWER, VIEW TO SOUTHWEST - Sears Roebuck and Company Mail Order Plant, Merchandise Building, 924 South Homan Avenue, Chicago, Cook County, IL HABS ILL,16-CHIG,110A-4.tif" "$H" "$PD" 3000
big habs_packer "SECOND FLOOR, SECTION A, PACKER'S STATION - Sears Roebuck and Company Mail Order Plant, Merchandise Building, 924 South Homan Avenue, Chicago, Cook County, IL HABS ILL,16-CHIG,110A-68.tif" "$H" "$PD" 3000
big truck1909 "Electric truck owned by Sears Roebuck. Two of them were in use around 1908.jpg" "Walter W. Macfarren, 1909" "$PD" 1322
big rfd_wagon "Rural Free Delivery Carrier and Wagon (2550432375).jpg" "Smithsonian National Postal Museum" "No known copyright restrictions (Smithsonian, Flickr Commons)" 3600
big rfd_laceyville "R(ural) F(ree) D(elivery), Laceyville, Pa. LCCN2005686635.jpg" "1907 (Library of Congress)" "$PD" 1536
big rfd_1914a "POST OFFICE DEPARTMENT. PARCEL POST. RURAL FREE DELIVERY LCCN2016865323.jpg" "Harris & Ewing, 1914 (Library of Congress)" "$PD" 3600
big rfd_1914b "POST OFFICE DEPARTMENT. PARCEL POST. RURAL FREE DELIVERY LCCN2016865324.jpg" "Harris & Ewing, 1914 (Library of Congress)" "$PD" 3600
big parcel1913 "Opening up Parcel Post, 1913; P.M.G. Hitchcock LCCN2016852637.jpg" "National Photo Company, 1913 (Library of Congress)" "$PD" 3000
big parcel_wagons "Parcel Post delivery wagons 1913.JPG" "Parcel Post wagons, 1913" "$PD" 932
big rfd_auto "Rural carrier in automobile at mailboxes, c.1910.jpg" "Smithsonian National Postal Museum" "No known copyright restrictions (Smithsonian, Flickr Commons)" 3600
big mh1918_cover "1918 Sears Modern Homes Catalog.jpg" "Sears, Roebuck and Co., 1918" "$PD" 697
big lumber_stamp "Photo of stamped lumber found in a Sears catalog house.jpg" "Rosemary Thornton, 2013 (released into the public domain)" "$PD" 2816
big store1926_seattle "Sears, Roebuck & Company's Western Branch, ca 1926 (MOHAI 5790).jpg" "Webster & Stevens, c. 1926 (MOHAI)" "$PD" 700
big store1929_allentown "1929 - Sears Roebuck Building - 129-133 North Seventh Street - Allentown PA.jpg" "Allentown, Pa., 1929" "$PD" 1400
big tower_river "Sears Tower from the Chicago River, Chicago, IL.jpg" "w_lemay, 2015 (CC0)" "CC0" 2446
big tower1974 "NEW AMTRAK TURBOLINER WHICH NOW MAKES THE PASSENGER RUN BETWEEN CHICAGO AND ST. LOUIS, MISSOURI, CONTRASTS WITH THE... - NARA - 556076~2.jpg" "Documerica, U.S. EPA, 1974 (National Archives)" "$PD" 1813
big closing_hialeah "Sears Store Closing Sale Westland Mall Hialeah (49525992311).jpg" "Phillip Pessar, 2020 (CC BY 2.0)" "CC BY 2.0" 3600
big closed_brooklyn "Sears - Closed Retail Store in Brooklyn Center, Minnesota (48826141373).jpg" "Tony Webster, 2019 (CC BY 2.0)" "CC BY 2.0" 3600
big closed_vero "Former Sears, Indian River Mall, Vero Beach, Florida.jpg" "Pokemonprime, 2024 (CC BY 4.0)" "CC BY 4.0" 3600
big craftsman_westland "Sears Westland Mall - Craftsman Tools.jpg" "Phillip Pessar, 2019 (CC BY 2.0)" "CC BY 2.0" 3600
big kenmore "Kenmore Washing Machine and Dryer.JPG" "Stilfehler, 2007 (public domain)" "$PD" 1944
big carl_station "Carlinville Amtrak station, 2020.jpg" "TheCatalyst31, 2020 (CC0)" "CC0" 3600
big carl_courthouse "McCoupan County Courthouse, East 1st Street, Carlinville, Illinois LCCN2017706052.tif" "John Margolies, 1991 (Library of Congress)" "$PD" 2600
big carl_ed1940 "1940 Census Enumeration District Maps - Illinois - Macoupin County - Carlinville - ED 59-20, ED 59-21, ED 59-22, ED 59-23, ED 59-24 - NARA - 5831612.jpg" "U.S. Census Bureau, 1940 (National Archives)" "$PD" 4296
big carl_1873 "Birds eye view of Carlinville, Macoupin County Ill. (2674657848).jpg" "J. J. Stoner, 1873 (Norman B. Leventhal Map Center, Boston Public Library, CC BY 2.0)" "CC BY 2.0" 2000
ia() {   # name, identifier, leaf, credit
  ls raw/$1.* >/dev/null 2>&1 && return 0
  $F "https://archive.org/download/$2/page/n$3_w2400.jpg" --name "$1" --page "https://archive.org/details/$2/page/n$3" --license "Public domain (published before 1931)" --credit "$4"; sleep 2
}
ia hb1921_sell HonorBiltModernHomes 7 "Sears, Roebuck and Co., Honor Bilt Modern Homes, 1921, p. 4 (Internet Archive)"
ia hb1921_quantity HonorBiltModernHomes 8 "Sears, Roebuck and Co., Honor Bilt Modern Homes, 1921, p. 5 (Internet Archive)"
C97="Sears, Roebuck and Co., Consumers Guide, Catalogue No. 104, Spring 1897 (Internet Archive)"
for n in 0 1 29 55 171 369 370; do ia c1897_n$n sears-roebuck-catalog-104-spring-1897 $n "$C97"; done
C28="Sears, Roebuck and Co., Catalog No. 157, Fall 1928 (Internet Archive)"
for n in 0 460 476 477; do ia c1928_n$n sears-roebuck-catalog-157-fall-1928 $n "$C28"; done
M18="Sears, Roebuck and Co., Honor Bilt Modern Homes, 1918 (Internet Archive)"
for n in 0 12 52 55 66; do ia mh1918_n$n SearsRobuckHomesCCA98234 $n "$M18"; done
ia mh1911_n0 modernhomes00sear 0 "Sears, Roebuck and Co., Modern Homes, 1911 (Internet Archive)"
ia c1918_n0 catalog1918sear_201901 0 "Sears, Roebuck and Co., Catalog, 1918 (Internet Archive)"
ia c1902_n0 sears-roebuck-catalogue-111 0 "Sears, Roebuck and Co., Catalogue No. 111, Spring 1902 (Internet Archive)"
ia c1912_n0 sears-roebuck-catalog-124-spring-1912 0 "Sears, Roebuck and Co., Catalog No. 124, Spring 1912 (Internet Archive)"
for n in 2 4 54 372 376 380; do ia c1897_n$n sears-roebuck-catalog-104-spring-1897 $n "$C97"; done
for n in 162 993 995; do ia c1928_n$n sears-roebuck-catalog-157-fall-1928 $n "$C28"; done
