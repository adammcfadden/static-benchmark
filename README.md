# HTTP Server Benchmarks

Testing using siege

Install latest version of siege

```
sudo apt-get install -y build-essential
wget http://download.joedog.org/siege/siege-latest.tar.gz
tar -zxvf siege-latest.tar.gz
cd siege-*/
./configure
make
sudo make install
mkdir ~/.siege
siege.config
```

Run your tests with

```
siege -f file_list.txt -c 24 -t60s
```

Change -t to reflect the desired concurrency.

## GO

```
GOMAXPROCS=1 go run go/src/static-benchmark/http/http.go
```