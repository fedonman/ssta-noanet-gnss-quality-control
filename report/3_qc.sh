for rnx in unzipped/*o; do
	teqc +qc $rnx
done
if [ ! -d reports];  then
	mkdir reports
fi
for report in unzipped/*S; do
	mv $report reports/
done
