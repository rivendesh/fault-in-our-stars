```bash
(.env) (base) [main][~/Code/fault-in-our-stars/assets/test]$ python /Users/wayfinder/Code/fault-in-our-stars/test-code/create-list-curl-urls-kepler.py
Processing KIC 3863594...
Processing KIC 10417986...
Processing KIC 8912468...
Processing KIC 8758716...
Processing KIC 10855535...
Processing KIC 9472174...
Processing KIC 9612468...

Wrote download_kepler_lcs.sh
(.env) (base) *[main][~/Code/fault-in-our-stars/assets/test]$ awk '/^curl -O / {print $3}' ../../test-code/download_kepler_lightcurves.sh > test-kepler-urls.txt
awk: can't open file ../../test-code/download_kepler_lightcurves.sh
 source line number 1
(.env) (base) *[main][~/Code/fault-in-our-stars/assets/test]$ awk '/^curl -O / {print $3}' download_kepler_lcs.sh > test-kepler-urls.txt
(.env) (base) *[main][~/Code/fault-in-our-stars/assets/test]$ python /Users/wayfinder/Code/fault-in-our-stars/test-code/create-list-curl-urls-kepler.py
Processing KIC 3863594...
Processing KIC 10417986...
Processing KIC 8912468...
Processing KIC 8758716...
Processing KIC 10855535...
Processing KIC 9472174...
Processing KIC 9612468...

Wrote download_kepler_lcs.sh
(.env) (base) *[main][~/Code/fault-in-our-stars/assets/test]$ awk '/^curl -O / {print $3}' download_kepler_lcs.sh > test-kepler-urls.txt
(.env) (base) *[main][~/Code/fault-in-our-stars/assets/test]$ aria2c \
  -i test-kepler-urls.txt \
  -d . \
  -j 10 \
  -x 1 \
  -s 1 \
  -c \
  --max-tries=0 \
  --retry-wait=5 \
  --timeout=60 \
  --connect-timeout=60 \
  --check-integrity=true

04/13 05:03:27 [NOTICE] Downloading 119 item(s)

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2009166043257_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2010355172524_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2011177032512_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2012004120508_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2012088054726_llc.fits
[DL:6.1MiB][#031410 32KiB/75KiB(42%)][#3a9e19 320KiB/455KiB(70%)][#160a29 80KiB/455KiB(17%)][#dafc58 288KiB/458KiB(62%)][#9832c4 400KiB/480KiB(83%)](+5)
04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2009131105131_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2013131215648_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2010174085026_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2009259160929_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2013011073258_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2011073133259_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr010417986-2009166043257_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2012179063303_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2013098041711_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2010078095331_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr010417986-2009131105131_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr010417986-2011073133259_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr003863594-2009350155506_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr010417986-2010265121752_llc.fits

04/13 05:03:28 [NOTICE] Download complete: ./kplr010417986-2011177032512_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2013131215648_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2009259160929_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2009350155506_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2012179063303_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2009131105131_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2013098041711_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2011271113734_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2012088054726_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2010174085026_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2009166043257_llc.fits
[DL:8.0MiB][#87a48e 288KiB/458KiB(62%)][#de59de 288KiB/495KiB(58%)][#13acfc 240KiB/455KiB(52%)][#1e7633 320KiB/455KiB(70%)][#ceea57 304KiB/458KiB(66%)](+5)
04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2010078095331_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2009350155506_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2010174085026_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2009259160929_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2010265121752_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2011073133259_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2012277125453_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2012088054726_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr010417986-2010078095331_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2010355172524_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2012004120508_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008912468-2011271113734_llc.fits

04/13 05:03:29 [NOTICE] Download complete: ./kplr008758716-2009131105131_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008912468-2013131215648_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2009166043257_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008912468-2012277125453_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008912468-2011177032512_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008912468-2012179063303_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008912468-2013011073258_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2010078095331_llc.fits
[DL:7.9MiB][#da7a38 352KiB/438KiB(80%)][#ad72d1 240KiB/455KiB(52%)][#156162 336KiB/455KiB(73%)][#84b6f2 256KiB/480KiB(53%)][#eef889 192KiB/458KiB(41%)](+5)
04/13 05:03:30 [NOTICE] Download complete: ./kplr008912468-2013098041711_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2009350155506_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2010174085026_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2009259160929_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2011073133259_llc.fits

04/13 05:03:30 [NOTICE] Download complete: ./kplr008758716-2010355172524_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2012004120508_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2010265121752_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2012277125453_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2012179063303_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2011271113734_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2013131215648_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr010855535-2009166043257_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2013011073258_llc.fits
[DL:7.3MiB][#473562 464KiB/495KiB(93%)][#2996f2 384KiB/424KiB(90%)][#6cb731 192KiB/438KiB(43%)][#b5d94f 160KiB/455KiB(35%)][#af7e1b 96KiB/455KiB(21%)](+5)
04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2011177032512_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2012088054726_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr010855535-2009350155506_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr010855535-2010078095331_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr008758716-2013098041711_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr010855535-2009259160929_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr010855535-2011073133259_llc.fits

04/13 05:03:31 [NOTICE] Download complete: ./kplr010855535-2010355172524_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2010265121752_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2012004120508_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2012088054726_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr009472174-2009131105131_llc.fits
[DL:7.0MiB][#99b46b 464KiB/480KiB(96%)][#44abb2 336KiB/495KiB(67%)][#78cf2a 400KiB/475KiB(84%)][#20d057 320KiB/461KiB(69%)][#35b7a0 288KiB/495KiB(58%)](+5)
04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2010174085026_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2013098041711_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2011271113734_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2013131215648_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr009472174-2009166043257_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2013011073258_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2012179063303_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2011177032512_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr010855535-2012277125453_llc.fits

04/13 05:03:32 [NOTICE] Download complete: ./kplr009472174-2009259160929_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2011073133259_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2010078095331_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2010355172524_llc.fits
[DL:6.8MiB][#b5a590 320KiB/455KiB(70%)][#f5502e 416KiB/480KiB(86%)][#6223a4 400KiB/458KiB(87%)][#390929 480KiB/495KiB(96%)][#6bd961 320KiB/475KiB(67%)](+5)
04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2011177032512_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2010265121752_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2012088054726_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2010174085026_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2012004120508_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009612468-2009131105131_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2011271113734_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2012277125453_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2009350155506_llc.fits

04/13 05:03:33 [NOTICE] Download complete: ./kplr009472174-2012179063303_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009472174-2013011073258_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009472174-2013098041711_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2009166043257_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009472174-2013131215648_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2009350155506_llc.fits
[DL:6.5MiB][#ebfc3b 288KiB/455KiB(63%)][#99f6af 272KiB/458KiB(59%)][#ba3b6d 464KiB/480KiB(96%)][#aefa3c 224KiB/458KiB(48%)][#ff5fec 432KiB/455KiB(94%)](+5)
04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2010174085026_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2010355172524_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2011073133259_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2011177032512_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2010078095331_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2009259160929_llc.fits

04/13 05:03:34 [NOTICE] Download complete: ./kplr009612468-2010265121752_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2012179063303_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2011271113734_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2013131215648_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2013011073258_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2012004120508_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2012277125453_llc.fits

04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2012088054726_llc.fits
[#6d7c64 416KiB/438KiB(94%) CN:1 DL:585KiB]
04/13 05:03:35 [NOTICE] Download complete: ./kplr009612468-2013098041711_llc.fits

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
f89574|OK  |   654KiB/s|./kplr003863594-2009166043257_llc.fits
b0d6e4|OK  |   1.0MiB/s|./kplr003863594-2010355172524_llc.fits
b64245|OK  |   1.1MiB/s|./kplr003863594-2011177032512_llc.fits
665bf8|OK  |   1.0MiB/s|./kplr003863594-2012004120508_llc.fits
201059|OK  |   4.1MiB/s|./kplr003863594-2012088054726_llc.fits
031410|OK  |   452KiB/s|./kplr003863594-2009131105131_llc.fits
c5520a|OK  |    13MiB/s|./kplr003863594-2013131215648_llc.fits
9832c4|OK  |   704KiB/s|./kplr003863594-2010174085026_llc.fits
3a9e19|OK  |   646KiB/s|./kplr003863594-2009259160929_llc.fits
e01e7e|OK  |   2.3MiB/s|./kplr003863594-2013011073258_llc.fits
4f4aaa|OK  |   518KiB/s|./kplr003863594-2011073133259_llc.fits
24971c|OK  |    14MiB/s|./kplr010417986-2009166043257_llc.fits
f04f59|OK  |   2.0MiB/s|./kplr003863594-2012179063303_llc.fits
5fd48f|OK  |   1.9MiB/s|./kplr003863594-2013098041711_llc.fits
dafc58|OK  |   590KiB/s|./kplr003863594-2010078095331_llc.fits
d5e487|OK  |   1.1MiB/s|./kplr010417986-2009131105131_llc.fits
a8f997|OK  |   3.9MiB/s|./kplr010417986-2011073133259_llc.fits
160a29|OK  |   641KiB/s|./kplr003863594-2009350155506_llc.fits
c06259|OK  |   2.6MiB/s|./kplr010417986-2010265121752_llc.fits
f10c61|OK  |   3.2MiB/s|./kplr010417986-2011177032512_llc.fits
103969|OK  |    19MiB/s|./kplr010417986-2013131215648_llc.fits
741f0a|OK  |   0.9MiB/s|./kplr010417986-2009259160929_llc.fits
a04f43|OK  |   0.9MiB/s|./kplr010417986-2009350155506_llc.fits
efd42a|OK  |   1.8MiB/s|./kplr010417986-2012179063303_llc.fits
197a9d|OK  |    14MiB/s|./kplr008912468-2009131105131_llc.fits
5a0f3d|OK  |   1.9MiB/s|./kplr010417986-2013098041711_llc.fits
1ed6c6|OK  |   1.0MiB/s|./kplr010417986-2011271113734_llc.fits
2fa92a|OK  |   917KiB/s|./kplr010417986-2012088054726_llc.fits
a88a58|OK  |   905KiB/s|./kplr010417986-2010174085026_llc.fits
b6eb78|OK  |   1.2MiB/s|./kplr008912468-2009166043257_llc.fits
ceea57|OK  |   2.9MiB/s|./kplr008912468-2010078095331_llc.fits
1e7633|OK  |   2.7MiB/s|./kplr008912468-2009350155506_llc.fits
ef9d49|OK  |   3.1MiB/s|./kplr008912468-2010174085026_llc.fits
13acfc|OK  |   0.9MiB/s|./kplr008912468-2009259160929_llc.fits
960c93|OK  |   1.2MiB/s|./kplr008912468-2010265121752_llc.fits
77d2d7|OK  |   0.9MiB/s|./kplr008912468-2011073133259_llc.fits
de59de|OK  |   748KiB/s|./kplr010417986-2012277125453_llc.fits
2d871a|OK  |   2.4MiB/s|./kplr008912468-2012088054726_llc.fits
87a48e|OK  |   399KiB/s|./kplr010417986-2010078095331_llc.fits
31a389|OK  |   0.9MiB/s|./kplr008912468-2010355172524_llc.fits
9ca259|OK  |   1.8MiB/s|./kplr008912468-2012004120508_llc.fits
fc8cc4|OK  |   1.7MiB/s|./kplr008912468-2011271113734_llc.fits
0e2ef5|OK  |    24MiB/s|./kplr008758716-2009131105131_llc.fits
17425e|OK  |   2.5MiB/s|./kplr008912468-2013131215648_llc.fits
193af3|OK  |   2.4MiB/s|./kplr008758716-2009166043257_llc.fits
1eb0d9|OK  |   1.3MiB/s|./kplr008912468-2012277125453_llc.fits
25d49b|OK  |   634KiB/s|./kplr008912468-2011177032512_llc.fits
a1ce54|OK  |   823KiB/s|./kplr008912468-2012179063303_llc.fits
b79647|OK  |   0.9MiB/s|./kplr008912468-2013011073258_llc.fits
91778b|OK  |   1.2MiB/s|./kplr008758716-2010078095331_llc.fits
da7a38|OK  |   637KiB/s|./kplr008912468-2013098041711_llc.fits
156162|OK  |   858KiB/s|./kplr008758716-2009350155506_llc.fits
84b6f2|OK  |   1.1MiB/s|./kplr008758716-2010174085026_llc.fits
ad72d1|OK  |   700KiB/s|./kplr008758716-2009259160929_llc.fits
695a8b|OK  |   655KiB/s|./kplr008758716-2011073133259_llc.fits
7349c2|OK  |   764KiB/s|./kplr008758716-2010355172524_llc.fits
6959f1|OK  |   1.0MiB/s|./kplr008758716-2012004120508_llc.fits
eef889|OK  |   516KiB/s|./kplr008758716-2010265121752_llc.fits
2a302b|OK  |   1.1MiB/s|./kplr008758716-2012277125453_llc.fits
059ba7|OK  |   1.0MiB/s|./kplr008758716-2012179063303_llc.fits
5537eb|OK  |   640KiB/s|./kplr008758716-2011271113734_llc.fits
975cc6|OK  |   597KiB/s|./kplr008758716-2013131215648_llc.fits
f11f8c|OK  |   1.2MiB/s|./kplr010855535-2009166043257_llc.fits
b3980d|OK  |   900KiB/s|./kplr008758716-2013011073258_llc.fits
473562|OK  |   561KiB/s|./kplr008758716-2011177032512_llc.fits
2996f2|OK  |   573KiB/s|./kplr008758716-2012088054726_llc.fits
af7e1b|OK  |   1.5MiB/s|./kplr010855535-2009350155506_llc.fits
a4aec5|OK  |   1.1MiB/s|./kplr010855535-2010078095331_llc.fits
6cb731|OK  |   582KiB/s|./kplr008758716-2013098041711_llc.fits
b5d94f|OK  |   679KiB/s|./kplr010855535-2009259160929_llc.fits
3dc0a0|OK  |   830KiB/s|./kplr010855535-2011073133259_llc.fits
13ead8|OK  |   1.0MiB/s|./kplr010855535-2010355172524_llc.fits
f5ce74|OK  |   704KiB/s|./kplr010855535-2010265121752_llc.fits
29c27c|OK  |   1.2MiB/s|./kplr010855535-2012004120508_llc.fits
1dc71d|OK  |   0.9MiB/s|./kplr010855535-2012088054726_llc.fits
c4ae9a|OK  |    24MiB/s|./kplr009472174-2009131105131_llc.fits
99b46b|OK  |   479KiB/s|./kplr010855535-2010174085026_llc.fits
7a6e6f|OK  |   1.0MiB/s|./kplr010855535-2013098041711_llc.fits
78cf2a|OK  |   517KiB/s|./kplr010855535-2011271113734_llc.fits
006340|OK  |   812KiB/s|./kplr010855535-2013131215648_llc.fits
a82576|OK  |   1.3MiB/s|./kplr009472174-2009166043257_llc.fits
cfef14|OK  |   0.9MiB/s|./kplr010855535-2013011073258_llc.fits
20d057|OK  |   753KiB/s|./kplr010855535-2012179063303_llc.fits
44abb2|OK  |   468KiB/s|./kplr010855535-2011177032512_llc.fits
35b7a0|OK  |   798KiB/s|./kplr010855535-2012277125453_llc.fits
4ce5f9|OK  |   0.9MiB/s|./kplr009472174-2009259160929_llc.fits
71595c|OK  |   0.9MiB/s|./kplr009472174-2011073133259_llc.fits
ec24b4|OK  |   1.0MiB/s|./kplr009472174-2010078095331_llc.fits
949685|OK  |   872KiB/s|./kplr009472174-2010355172524_llc.fits
390929|OK  |   677KiB/s|./kplr009472174-2011177032512_llc.fits
6223a4|OK  |   508KiB/s|./kplr009472174-2010265121752_llc.fits
8e7700|OK  |   873KiB/s|./kplr009472174-2012088054726_llc.fits
f5502e|OK  |   492KiB/s|./kplr009472174-2010174085026_llc.fits
be360a|OK  |   649KiB/s|./kplr009472174-2012004120508_llc.fits
826803|OK  |   1.0MiB/s|./kplr009612468-2009131105131_llc.fits
6bd961|OK  |   544KiB/s|./kplr009472174-2011271113734_llc.fits
bc7b25|OK  |   0.9MiB/s|./kplr009472174-2012277125453_llc.fits
b5a590|OK  |   384KiB/s|./kplr009472174-2009350155506_llc.fits
b15a75|OK  |   783KiB/s|./kplr009472174-2012179063303_llc.fits
b75b6c|OK  |   741KiB/s|./kplr009472174-2013011073258_llc.fits
3f0ebd|OK  |   0.9MiB/s|./kplr009472174-2013098041711_llc.fits
835702|OK  |   466KiB/s|./kplr009612468-2009166043257_llc.fits
83778a|OK  |   379KiB/s|./kplr009472174-2013131215648_llc.fits
f3eb93|OK  |   1.0MiB/s|./kplr009612468-2009350155506_llc.fits
ba3b6d|OK  |   823KiB/s|./kplr009612468-2010174085026_llc.fits
ff5fec|OK  |   780KiB/s|./kplr009612468-2010355172524_llc.fits
88b53f|OK  |   809KiB/s|./kplr009612468-2011073133259_llc.fits
4900bc|OK  |   865KiB/s|./kplr009612468-2011177032512_llc.fits
99f6af|OK  |   553KiB/s|./kplr009612468-2010078095331_llc.fits
ebfc3b|OK  |   458KiB/s|./kplr009612468-2009259160929_llc.fits
aefa3c|OK  |   439KiB/s|./kplr009612468-2010265121752_llc.fits
a96b6e|OK  |   860KiB/s|./kplr009612468-2012179063303_llc.fits
81ed4f|OK  |   547KiB/s|./kplr009612468-2011271113734_llc.fits
69a44b|OK  |   402KiB/s|./kplr009612468-2013131215648_llc.fits
b6914d|OK  |   868KiB/s|./kplr009612468-2013011073258_llc.fits
ec35ba|OK  |   457KiB/s|./kplr009612468-2012004120508_llc.fits
b0e5bd|OK  |   691KiB/s|./kplr009612468-2012277125453_llc.fits
74581e|OK  |   455KiB/s|./kplr009612468-2012088054726_llc.fits
6d7c64|OK  |   616KiB/s|./kplr009612468-2013098041711_llc.fits

Status Legend:
(OK):download completed.
(.env) (base) [main][~/Code/fault-in-our-stars/assets/test]$
```
