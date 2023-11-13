mkdir text_files

curl https://www.gutenberg.org/cache/epub/84/pg84.txt > text_files/frankenstein.txt
curl https://www.gutenberg.org/cache/epub/64317/pg64317.txt > text_files/thegreatgatsby.txt
curl https://www.gutenberg.org/cache/epub/11/pg11.txt > text_files/aliceinwonderland.txt
curl https://www.gutenberg.org/cache/epub/345/pg345.txt > text_files/dracula.txt
curl https://www.gutenberg.org/cache/epub/174/pg174.txt > text_files/thepictureofdoriangray.txt
curl https://www.gutenberg.org/cache/epub/5200/pg5200.txt > text_files/metamorphosis.txt
curl https://www.gutenberg.org/cache/epub/1661/pg1661.txt > text_files/sherlockholmes.txt
curl https://www.gutenberg.org/cache/epub/43/pg43.txt > text_files/drjekyllandmrhyde.txt
curl https://www.gutenberg.org/cache/epub/1232/pg1232.txt > text_files/theprince.txt
curl https://www.gutenberg.org/cache/epub/1342/pg1342.txt > text_files/priceandprejudice.txt

sed -n '58,88p;89q' text_files/aliceinwonderland.txt > shingling_test.txt
