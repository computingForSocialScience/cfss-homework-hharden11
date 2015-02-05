wc -l permits.csv
head -1 permits.csv > permits_hydepark.csv
grep "Hyde Park" permits.csv >> permits_hydepark.csv