# make-sst-element

A Python program to make an SST Element repository

# Instructions

``` bash
$ pip3 install make-sst-element --user
$ make-sst-element /tmp/hello_element
What is your name? John Doe
What is your email address? johndoe1492@gmail.com
What is the element's name? HelloElement
 Name: John Doe
 Email: johndoe1492@gmail.com
 Element: HelloElement
Is this ok? [y/n] y
$ cd /tmp/hello_element
$ ls
autogen.sh  config  configure.ac  LICENSE  Makefile.am  NOTICE  README.md  src
$ ./autogen.sh
<LOTS OF OUTPUT>
$ ./configure --with-sst-core=$SST_CORE_HOME --prefix=$PWD/build
<LOTS OF OUTPUT>
$ make all && make install
<LOTS OF OUTPUT>
$ sst src/sst/helloelement/dummy.py -- 10 Stats.csv
<SST OUTPUT>
```
